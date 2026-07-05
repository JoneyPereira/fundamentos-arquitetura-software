#!/usr/bin/env python3
"""
cyclomatic_complexity.py

Calcula a Complexidade Ciclomática (CC) real de funções e métodos Python,
usando a AST (Abstract Syntax Tree) da própria linguagem — não regex/heurística.

Fórmula clássica: CC = E - N + 2P
Na prática, para um único grafo de fluxo por função (P = 1), isso equivale a:
    CC = 1 + (número de pontos de decisão)

Pontos de decisão contados:
- if / elif
- for / async for
- while
- except (cada cláusula except conta como um desvio)
- and / or (cada operando extra em uma expressão booleana)
- expressão condicional (ternário: `x if cond else y`)
- comprehensions (list/set/dict/generator) — cada `if` dentro do comprehension
- match/case (cada `case`, exceto o wildcard `case _` sem guard)
- assert
- with vários "context managers" NÃO conta (não é decisão de fluxo)

Uso:
    python cyclomatic_complexity.py caminho/arquivo.py
    python cyclomatic_complexity.py caminho/pasta/ --threshold 10
    python cyclomatic_complexity.py caminho/pasta/ --json relatorio.json
    python cyclomatic_complexity.py caminho/pasta/ --threshold 10 --fail-on-exceed

Uso como "função de aptidão" (fitness function) em CI:
    python cyclomatic_complexity.py src/ --threshold 10 --fail-on-exceed
    # retorna exit code 1 se alguma função exceder o limiar -> quebra o pipeline
"""

import argparse
import ast
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FunctionComplexity:
    name: str
    qualified_name: str
    file: str
    lineno: int
    complexity: int


class ComplexityVisitor(ast.NodeVisitor):
    """
    Percorre a AST de um módulo e calcula a CC de cada função/método,
    incluindo funções aninhadas (cada uma recebe sua própria contagem).
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.results: list[FunctionComplexity] = []
        self._scope_stack: list[str] = []

    # ---- entradas de função ----

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._handle_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._handle_function(node)

    def _handle_function(self, node):
        qualified = ".".join(self._scope_stack + [node.name])
        complexity = 1 + self._count_decision_points(node)
        self.results.append(
            FunctionComplexity(
                name=node.name,
                qualified_name=qualified,
                file=self.filename,
                lineno=node.lineno,
                complexity=complexity,
            )
        )
        # entra no escopo para nomear corretamente funções/métodos aninhados
        self._scope_stack.append(node.name)
        self.generic_visit(node)
        self._scope_stack.pop()

    # ---- contagem de pontos de decisão dentro de UMA função ----

    def _count_decision_points(self, func_node) -> int:
        count = 0

        def walk(node):
            nonlocal count
            for child in ast.iter_child_nodes(node):
                # não descer para dentro de funções aninhadas: elas são
                # contadas separadamente por sua própria chamada de
                # visit_FunctionDef/visit_AsyncFunctionDef
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue

                if isinstance(child, (ast.If, ast.IfExp)):
                    count += 1
                elif isinstance(child, (ast.For, ast.AsyncFor, ast.While)):
                    count += 1
                elif isinstance(child, ast.ExceptHandler):
                    count += 1
                elif isinstance(child, ast.Assert):
                    count += 1
                elif isinstance(child, ast.BoolOp):
                    # `a and b and c` -> 2 pontos extras (n operandos - 1)
                    count += len(child.values) - 1
                elif isinstance(child, ast.comprehension):
                    count += len(child.ifs)
                elif isinstance(child, getattr(ast, "Match", ())):
                    for case in child.cases:
                        is_wildcard = (
                            isinstance(case.pattern, ast.MatchAs)
                            and case.pattern.pattern is None
                            and case.guard is None
                        )
                        if not is_wildcard:
                            count += 1

                walk(child)

        walk(func_node)
        return count


def analyze_file(path: Path) -> list[FunctionComplexity]:
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"[aviso] não foi possível analisar {path}: {e}", file=sys.stderr)
        return []
    visitor = ComplexityVisitor(str(path))
    visitor.visit(tree)
    return visitor.results


def collect_python_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(p for p in target.rglob("*.py") if "__pycache__" not in p.parts)


def classify(cc: int, threshold: int) -> str:
    if cc > threshold:
        return "ACIMA DO LIMIAR"
    if cc >= max(1, threshold - 3):
        return "atenção"
    return "ok"


def main():
    parser = argparse.ArgumentParser(
        description="Calcula a Complexidade Ciclomática real (via AST) de funções Python."
    )
    parser.add_argument("path", type=Path, help="Arquivo .py ou diretório a analisar")
    parser.add_argument(
        "--threshold", type=int, default=10,
        help="Limiar de CC considerado aceitável (padrão: 10, referência comum na literatura)"
    )
    parser.add_argument("--json", type=Path, default=None, help="Salvar relatório completo em JSON")
    parser.add_argument(
        "--fail-on-exceed", action="store_true",
        help="Retorna exit code 1 se alguma função exceder o limiar (uso em CI, como função de aptidão)"
    )
    parser.add_argument(
        "--top", type=int, default=None,
        help="Mostrar apenas as N funções de maior complexidade"
    )
    args = parser.parse_args()

    if not args.path.exists():
        print(f"Caminho não encontrado: {args.path}", file=sys.stderr)
        sys.exit(2)

    files = collect_python_files(args.path)
    if not files:
        print("Nenhum arquivo .py encontrado.", file=sys.stderr)
        sys.exit(2)

    all_results: list[FunctionComplexity] = []
    for f in files:
        all_results.extend(analyze_file(f))

    all_results.sort(key=lambda r: r.complexity, reverse=True)
    display = all_results[: args.top] if args.top else all_results

    print(f"\nComplexidade Ciclomática — {len(files)} arquivo(s), {len(all_results)} função(ões)")
    print(f"Limiar configurado: {args.threshold}\n")
    print(f"{'CC':>4}  {'STATUS':<16}  {'FUNÇÃO':<40}  ARQUIVO:LINHA")
    print("-" * 100)
    exceeded = []
    for r in display:
        status = classify(r.complexity, args.threshold)
        if status == "ACIMA DO LIMIAR":
            exceeded.append(r)
        print(f"{r.complexity:>4}  {status:<16}  {r.qualified_name:<40}  {r.file}:{r.lineno}")

    if all_results:
        avg = sum(r.complexity for r in all_results) / len(all_results)
        print(f"\nMédia de CC: {avg:.1f}  |  Máxima: {all_results[0].complexity} ({all_results[0].qualified_name})")

    if exceeded:
        print(f"\n{len(exceeded)} função(ões) acima do limiar de {args.threshold}:")
        for r in exceeded:
            print(f"  - {r.qualified_name}  (CC={r.complexity})  em {r.file}:{r.lineno}")

    if args.json:
        payload = {
            "threshold": args.threshold,
            "total_functions": len(all_results),
            "exceeded_count": len(exceeded),
            "results": [
                {
                    "function": r.qualified_name,
                    "file": r.file,
                    "line": r.lineno,
                    "complexity": r.complexity,
                    "status": classify(r.complexity, args.threshold),
                }
                for r in all_results
            ],
        }
        args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nRelatório salvo em: {args.json}")

    if args.fail_on_exceed and exceeded:
        sys.exit(1)


if __name__ == "__main__":
    main()
