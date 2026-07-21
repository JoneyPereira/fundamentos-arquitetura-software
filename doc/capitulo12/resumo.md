# Capítulo 12 - Estilo Arquitetural de Pipeline

## Resumo

O décimo segundo capítulo apresenta um estilo fundamental e bastante difundido: a **arquitetura de pipeline**, também conhecida como arquitetura de pipes e filtros. Trata-se de um padrão familiar a muitos desenvolvedores, já que é o princípio subjacente às linguagens de shell de terminal em sistemas Unix — a ideia de encadear pequenas operações, cada uma processando a saída da anterior.

A estrutura do estilo se baseia em dois elementos complementares: os **filtros**, que contêm a funcionalidade do sistema e executam funções de negócio específicas, e os **pipes**, canais unidirecionais que transportam os dados de um filtro para o próximo na cadeia. Em sua forma mais simples, a arquitetura de pipeline constitui uma única unidade de implantação, com toda a funcionalidade organizada em filtros conectados por esses pipes. No entanto, o estilo também admite uma variação distribuída: é possível implantar cada filtro (ou um conjunto deles) como um serviço independente, transformando o pipeline em uma arquitetura distribuída, com comunicação remota síncrona ou assíncrona entre os componentes.

Os autores classificam os filtros em quatro tipos, de acordo com seu papel no fluxo:

- **Produtor** — ponto de partida do processo; é um filtro exclusivamente de saída, sem receber entrada.
- **Transformador** — recebe uma entrada, opcionalmente aplica alguma transformação sobre parte ou a totalidade dos dados, e encaminha o resultado adiante pelo pipe de saída.
- **Testador** — recebe uma entrada, avalia-a segundo um ou mais critérios e, opcionalmente, produz uma saída baseada nesse teste.
- **Consumidor** — ponto de término do fluxo; costuma persistir o resultado final em um banco de dados ou exibi-lo em uma interface de usuário.

Quanto à topologia de dados, o capítulo observa que ela pode variar bastante nesse estilo, indo desde um único banco de dados compartilhado até um banco de dados dedicado a cada filtro, dependendo do grau de independência que se deseja entre as etapas do processamento.

Em relação à nuvem, o estilo de pipeline se adapta bem a implantações baseadas em nuvem, justamente por seu alto grau de modularidade e pela separação clara entre os diferentes tipos de filtro. As opções de implantação são flexíveis: os filtros podem ser publicados como funções serverless, como funções conteinerizadas independentes ou reunidos em um único serviço monolítico que contenha todos os quatro tipos de componente.

O capítulo também aponta riscos recorrentes na adoção desse estilo. Um deles é sobrecarregar os filtros com responsabilidades demais, o que compromete sua granularidade e sua finalidade original. Outro risco comum é a introdução de comunicação bidirecional entre filtros, o que rompe a lógica unidirecional que caracteriza o estilo. Há também dificuldades ligadas ao tratamento de erros — quando uma falha ocorre no meio do pipeline, não é trivial determinar como sair corretamente do fluxo e se recuperar de forma consistente — e ao gerenciamento dos contratos entre filtros, área que exige atenção contínua dos arquitetos. Para efeitos de governança, os autores recomendam justamente usar o papel e a responsabilidade de cada filtro como referência.

Do ponto de vista das características arquiteturais, o pipeline é descrito como um estilo independente da topologia de equipes, funcionando de forma razoável com praticamente qualquer configuração organizacional. Estruturalmente, é classificado como uma arquitetura **particionada tecnicamente**, já que sua lógica de aplicação é separada de acordo com os tipos de filtro, e não por domínios de negócio. Uma vantagem estrutural relevante é a possibilidade de modificar ou substituir qualquer filtro isoladamente, sem afetar os demais — o que favorece a manutenibilidade. O capítulo também sugere um caminho de evolução: transformar o pipeline em uma arquitetura distribuída com comunicação assíncrona, na qual cada filtro se torna uma unidade de implantação separada e os pipes passam a ser chamadas remotas.

Por fim, os autores delimitam o campo de aplicação ideal do estilo: ele é adequado a sistemas de qualquer nível de complexidade, desde que as etapas de processamento sejam distintas, ordenadas, determinísticas e unidirecionais. Quando o fluxo de trabalho é não determinístico, a arquitetura orientada a eventos tende a ser mais adequada. Na prática, o pipeline aparece com frequência em tarefas que envolvem processamento simples e unidirecional de dados.

## Principais aprendizados

- A arquitetura de pipeline organiza o sistema em filtros (que executam funções de negócio) conectados por pipes unidirecionais (que transportam dados) — o mesmo princípio das linguagens de shell Unix.
- Existem quatro tipos de filtro: produtor (só saída), transformador (transforma dados), testador (avalia critérios) e consumidor (encerra o fluxo, geralmente persistindo ou exibindo o resultado).
- O estilo pode ser implantado como unidade monolítica única ou de forma distribuída, com cada filtro virando um serviço independente e comunicação síncrona ou assíncrona entre eles.
- A topologia de dados é flexível, podendo variar de um banco único a um banco por filtro.
- Riscos recorrentes incluem sobrecarregar filtros com responsabilidades demais, introduzir comunicação bidirecional indevida, dificuldade de recuperação em caso de erro no meio do fluxo e complexidade na gestão dos contratos entre filtros.
- É um estilo particionado tecnicamente, independente da topologia de equipes, e permite substituir ou modificar filtros isoladamente sem impactar os demais.
- É mais indicado para fluxos de processamento determinísticos, ordenados e unidirecionais; fluxos não determinísticos favorecem a arquitetura orientada a eventos.
