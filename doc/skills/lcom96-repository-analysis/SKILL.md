---
name: lcom96-repository-analysis
description: Analise LCOM96 por classe a partir de um link de repositorio
version: 1.0.0
last-updated: 2026-06-29
language: pt-BR
---

# ANALISE LCOM96 POR REPOSITORIO - v1.0.0

Versao em portugues.

Baseado em:
- `agente.txt`
- LCOM96
- Analise de coesao de classes
- Single Responsibility Principle

==================================================
1. VISAO GERAL
==================================================

Este prompt orienta a analise de coesao de classes em um repositorio.

Objetivo:
- Acessar repositorio informado pelo usuario.
- Identificar classes do codigo-fonte de producao.
- Calcular LCOM96 para cada classe valida.
- Gerar ranking por maior falta de coesao.
- Apontar indicios de violacao de SRP.
- Sugerir extracoes de classes quando houver baixa coesao.

Principios:
- Verificar antes de assumir.
- Separar fatos de inferencias.
- Declarar regras adotadas.
- Nao analisar codigo gerado.
- Nao tratar LCOM como prova absoluta de design ruim.

==================================================
2. ENTRADA OBRIGATORIA
==================================================

O usuario deve fornecer:

```text
Repositorio:
<cole aqui o link do repositorio>
```

Entrada opcional:

```text
Branch: <nome da branch>
Escopo: <modulo, pacote ou pasta>
Linguagem: <linguagem principal>
```

Se o link nao estiver acessivel:
- Informe o problema.
- Peca codigo-fonte.
- Aceite arquivo compactado.
- Aceite trecho de codigo como fallback.

==================================================
3. ESCOPO DA ANALISE
==================================================

Analise somente:
- Codigo-fonte de producao.
- Classes declaradas no proprio repositorio.
- Modulos, pacotes ou pastas relevantes.

Ignore:
- Testes.
- Mocks.
- Fixtures.
- Dependencias.
- Arquivos gerados.
- Build outputs.
- Exemplos.
- Codigo de terceiros.

Se houver multiplas linguagens:
- Identifique a linguagem principal.
- Declare linguagem analisada.
- Explique exclusoes relevantes.

==================================================
4. DEFINICOES DA METRICA
==================================================

Use estas definicoes:

```text
m = quantidade de metodos validos da classe
a = quantidade de atributos validos da classe
mu(Aj) = quantidade de metodos validos que acessam diretamente o atributo Aj
```

Onde:
- `Aj` representa um atributo valido da classe.
- `mu(Aj)` deve ser calculado atributo por atributo.
- Cada metodo conta no maximo uma vez por atributo.

==================================================
5. ATRIBUTOS VALIDOS
==================================================

Conte como atributo valido:
- Atributo de instancia.
- Declarado diretamente na classe.
- Pertencente ao estado interno da classe.

Ignore:
- Constantes.
- Atributos estaticos.
- Atributos herdados.
- Atributos gerados automaticamente.
- Campos de framework sem uso direto pela classe.

Exemplos que normalmente contam:

```text
this.total
self.total
@total
private BigDecimal total
```

Exemplos que normalmente nao contam:

```text
static final int MAX_SIZE
public static String VERSION
serialVersionUID
```

==================================================
6. METODOS VALIDOS
==================================================

Conte como metodo valido:
- Metodo de instancia.
- Declarado diretamente na classe.
- Com comportamento proprio.

Ignore:
- Construtores.
- Destrutores.
- Metodos estaticos.
- Metodos herdados.
- Metodos gerados automaticamente.
- Getters triviais.
- Setters triviais.
- `equals`.
- `hashCode`.
- `toString`.
- Metodos equivalentes triviais da linguagem.

Se um getter ou setter tiver regra de negocio:
- Declare a decisao.
- Conte somente se houver comportamento nao trivial.

==================================================
7. ACESSO DIRETO A ATRIBUTO
==================================================

Conte acesso direto quando o corpo do metodo referencia o atributo diretamente.

Exemplos:

```text
this.campo
self.campo
campo
@campo
```

Nao conte acesso indireto por:
- Getter.
- Setter.
- Chamada de outro metodo.
- Reflexao.
- Serializacao automatica.
- Binding de framework.

Regra:
- Se houver duvida, marque como nao contado.
- Explique a ambiguidade.

==================================================
8. FORMULA LCOM96
==================================================

Use exatamente esta formula:

```text
LCOM96 = (1 / a) * SUM((m - mu(Aj)) / m)
```

Passos:
1. Calcule `m`.
2. Calcule `a`.
3. Liste cada atributo `Aj`.
4. Calcule `mu(Aj)` para cada atributo.
5. Some todos os termos `(m - mu(Aj)) / m`.
6. Divida por `a`.
7. Arredonde o resultado final para 4 casas decimais.

==================================================
9. CASOS ESPECIAIS
==================================================

Se `a = 0`:
- Marque LCOM96 como `N/A`.
- Explique que nao ha atributos validos.

Se `m = 0`:
- Marque LCOM96 como `N/A`.
- Explique que nao ha metodos validos.

Se `a = 0` e `m = 0`:
- Marque LCOM96 como `N/A`.
- Explique ambos os motivos.

Ranking:
- Nao inclua classes com LCOM96 `N/A` no ranking numerico.
- Liste classes `N/A` em secao separada.

==================================================
10. FLUXO DE EXECUCAO
==================================================

Execute nesta ordem:

1. Acesse o repositorio.
2. Identifique linguagem principal.
3. Identifique estrutura de diretorios.
4. Defina escopo analisado.
5. Encontre classes de producao.
6. Remova arquivos ignorados.
7. Para cada classe, identifique atributos validos.
8. Para cada classe, identifique metodos validos.
9. Monte matriz metodo x atributo.
10. Calcule LCOM96.
11. Classifique coesao.
12. Monte ranking final.
13. Aponte indicios de SRP.
14. Sugira extracoes quando fizer sentido.

==================================================
11. SAIDA POR CLASSE
==================================================

Para cada classe, produza:

```text
Classe: <nome>
Arquivo: <caminho>

Atributos validos:
- <atributo>

Metodos validos:
- <metodo>

Matriz metodo x atributo:
| Metodo | atributo1 | atributo2 |
|--------|-----------|-----------|
| metodoA | X | - |
| metodoB | - | X |

mu(Aj):
- atributo1: <valor>
- atributo2: <valor>

Calculo:
LCOM96 = (1 / a) * SUM((m - mu(Aj)) / m)
LCOM96 = ...

Resultado:
- m: <valor>
- a: <valor>
- LCOM96: <valor>
- Coesao: <classificacao>
```

Use `X` para acesso direto.
Use `-` para ausencia de acesso direto.

==================================================
12. CLASSIFICACAO DA COESAO
==================================================

Use estes intervalos:

| Faixa | Classificacao |
|-------|---------------|
| 0 <= LCOM96 <= 0.2 | Excelente |
| 0.2 < LCOM96 <= 0.4 | Boa |
| 0.4 < LCOM96 <= 0.6 | Media |
| 0.6 < LCOM96 <= 0.8 | Ruim |
| 0.8 < LCOM96 <= 1.0 | Muito Ruim |

Observacao:
- Valores maiores indicam menor coesao.
- Valores menores indicam maior coesao.

==================================================
13. RANKING FINAL
==================================================

Ao final, crie ranking ordenado por maior LCOM96.

Formato:

```text
Ranking de baixa coesao:
| Posicao | Classe | Arquivo | LCOM96 | Coesao |
|---------|--------|---------|--------|--------|
| 1 | ClasseA | src/... | 0.8750 | Muito Ruim |
```

Depois, liste classes sem calculo:

```text
Classes com LCOM96 N/A:
| Classe | Arquivo | Motivo |
|--------|---------|--------|
| ClasseB | src/... | Sem atributos validos |
```

==================================================
14. ANALISE DE SRP
==================================================

LCOM96 alto pode indicar baixa coesao.
Nao trate como prova isolada de violacao de SRP.

Ao apontar SRP:
- Use linguagem de indicio.
- Cite evidencias objetivas.
- Cite metodos e atributos envolvidos.
- Explique responsabilidades possivelmente misturadas.

Formato:

```text
Indicios de SRP:
- Classe: <nome>
- Evidencia objetiva: <metodos usam grupos distintos de atributos>
- Inferencia de design: <responsabilidades possivelmente separadas>
- Confianca: baixa | media | alta
```

==================================================
15. SUGESTOES DE EXTRACAO
==================================================

Sugira extracao quando:
- LCOM96 for `Ruim` ou `Muito Ruim`.
- Matriz mostrar grupos independentes de atributos.
- Metodos formarem responsabilidades separadas.

Nao sugira extracao quando:
- Classe for pequena e clara.
- Baixa coesao vier de DTO, entidade anemica ou estrutura de framework.
- Evidencia for fraca.

Formato:

```text
Sugestao:
- Extrair: <nome sugerido>
- Origem: <classe atual>
- Atributos: <lista>
- Metodos: <lista>
- Motivo: <resumo>
```

==================================================
16. RELATORIO ESPERADO
==================================================

Estruture a resposta final assim:

```text
Analise LCOM96 - Conclusao

Repositorio:
- URL: <url>
- Branch: <branch ou padrao>
- Linguagem principal: <linguagem>
- Escopo analisado: <pastas>

Resumo:
- Classes analisadas: <qtd>
- Classes com LCOM96 calculado: <qtd>
- Classes N/A: <qtd>
- Maior LCOM96: <classe> (<valor>)

Detalhamento por classe:
<uma secao por classe>

Ranking:
<ranking final>

SRP:
<indicios>

Extracoes sugeridas:
<sugestoes>

Limitacoes:
<ambiguidades, arquivos ignorados, acesso ao repositorio>
```

==================================================
17. PROMPT RAPIDO
==================================================

Use este texto para executar a analise:

```text
Analise o repositorio abaixo e calcule LCOM96 para cada classe.

Repositorio:
<cole aqui o link do repositorio>

Siga o arquivo `lcom96-repository-analysis.prompt.md`.
Analise apenas codigo-fonte de producao.
Ignore testes, mocks, dependencias, arquivos gerados e exemplos.
Mostre atributos, metodos, matriz metodo x atributo, mu(Aj), calculo detalhado,
LCOM96 final, classificacao, ranking, indicios de SRP e sugestoes de extracao.
```

==================================================
18. CHECKLIST DE CONCLUSAO
==================================================

Antes de finalizar, confirme:

- [ ] Repositorio acessado ou indisponibilidade explicada.
- [ ] Linguagem principal identificada.
- [ ] Escopo analisado informado.
- [ ] Arquivos ignorados explicados.
- [ ] Classes de producao identificadas.
- [ ] Atributos validos listados.
- [ ] Metodos validos listados.
- [ ] Matriz metodo x atributo criada.
- [ ] `mu(Aj)` calculado por atributo.
- [ ] Formula detalhada por classe.
- [ ] LCOM96 arredondado para 4 casas.
- [ ] Coesao classificada.
- [ ] Ranking final criado.
- [ ] Classes `N/A` separadas.
- [ ] Indicios de SRP diferenciados de fatos.
- [ ] Extracoes sugeridas com justificativa.

==================================================
19. TROUBLESHOOTING
==================================================

Problema: repositorio privado.
Solucao: peca acesso, arquivo compactado ou trecho relevante.

Problema: repositorio grande.
Solucao: peca escopo ou analise modulo principal primeiro.

Problema: linguagem dinamica dificulta atributos.
Solucao: declare regra adotada e use apenas atributos evidentes.

Problema: framework gera metodos.
Solucao: ignore codigo gerado e declare exclusao.

Problema: classe sem atributos validos.
Solucao: marque LCOM96 como `N/A`.

Problema: classe sem metodos validos.
Solucao: marque LCOM96 como `N/A`.

Problema: getter ou setter contem regra.
Solucao: declare decisao antes de contar.

==================================================
FIM DA ANALISE LCOM96 POR REPOSITORIO
==================================================

Este e ponto de partida.
Ajuste conforme linguagem, framework e escopo do repositorio.