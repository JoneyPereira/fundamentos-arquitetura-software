# Capítulo 4 - Definição das Características Arquiteturais

## Resumo

O quarto capítulo trata do design estrutural sob outro ângulo: a análise das características arquiteturais e o design dos componentes lógicos. O foco passa a ser identificar, descobrir e analisar tudo aquilo que o software precisa fazer que não está diretamente ligado à funcionalidade de domínio — é justamente esse conjunto de exigências que os autores chamam de **características arquiteturais**.

Uma característica arquitetural é definida por três condições que precisam se combinar: especifica uma consideração de design que não pertence ao domínio de negócio, influencia algum aspecto da estrutura do sistema e é crítica ou importante para o sucesso da aplicação. Em outras palavras, são os **critérios operacionais e de design** que determinam se o projeto vai (ou não) atender bem às suas necessidades — e o trabalho do arquiteto começa por identificar quais dessas considerações realmente importam para o contexto em questão.

O capítulo distingue dois tipos de origem para essas características:

- **Implícitas** — não aparecem formalmente em nenhum documento, mas são esperadas por padrão em praticamente qualquer sistema, como disponibilidade, confiabilidade e segurança.
- **Explícitas** — são aquelas que aparecem descritas em documentos de requisitos, definidas de forma consciente pelas partes interessadas.

Além dessas duas categorias, os autores observam que cada projeto de software pode **inventar** características arquiteturais próprias, motivadas por fatores únicos do seu contexto — o que reforça, uma vez mais, a ideia (já vista no Capítulo 1) de que arquitetura depende de circunstância.

Um alerta importante do capítulo é sobre o custo de sustentar essas características: cada uma que o sistema suporta exige esforço de design do arquiteto, esforço de implementação e manutenção por parte dos desenvolvedores e, eventualmente, suporte estrutural adicional. Por isso, a recomendação prática é clara — **buscar o menor número possível de características arquiteturais**, e não o maior, evitando sobrecarregar o projeto com exigências não essenciais.

Essa contenção se conecta a outra ideia central do capítulo: a de que não existe a arquitetura perfeita. Os autores defendem que o objetivo realista do arquiteto não é alcançar a "melhor" arquitetura, e sim a **arquitetura menos pior** possível dentro das restrições dadas — uma forma de reconhecer, na prática, que toda decisão envolve trade-offs (tema já trabalhado nos capítulos anteriores).

Por fim, o capítulo reforça a importância da **iteratividade** no processo de design: o arquiteto deve se esforçar para tornar a arquitetura o mais iterativa possível, já que, tanto quanto no desenvolvimento ágil, o verdadeiro valor está no processo de iterar — refinar, testar e ajustar as decisões arquiteturais ao longo do tempo, em vez de tentar acertar tudo de uma vez só.

## Principais aprendizados

- Características arquiteturais são os requisitos não funcionais e considerações de design que não pertencem ao domínio, mas que são críticos para o sucesso do sistema.
- Elas podem ser implícitas (esperadas por padrão, como segurança e disponibilidade), explícitas (formalizadas em requisitos) ou específicas de cada projeto.
- Cada característica adotada tem um custo real de design, implementação e manutenção — por isso o ideal é minimizar, não maximizar, a lista de características suportadas.
- Não existe arquitetura perfeita: o objetivo prático é buscar a arquitetura menos pior possível diante das restrições do contexto.
- A iteratividade é tão valiosa na arquitetura quanto no desenvolvimento ágil — o valor está no processo de refinar continuamente as decisões.
