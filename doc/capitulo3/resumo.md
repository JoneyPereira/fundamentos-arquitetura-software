# Capítulo 3 - Modularidade

## Resumo

O terceiro capítulo trata da modularidade como princípio organizador do código, essencial para manter codebases sustentáveis ao longo do tempo, já que sistemas bem organizados dependem da ordem e da consistência que a modularidade proporciona. Modularidade, nesse contexto, é definida como o agrupamento lógico de código relacionado — um conjunto de classes, em linguagens orientadas a objetos, ou um conjunto de funções, em linguagens estruturadas ou funcionais.

A ideia central é a divisão de sistemas grandes em partes menores, o que fica evidente na transição de estilos arquiteturais monolíticos (como a arquitetura em camadas N-tier) para estilos altamente distribuídos, como microsserviços. Ligada a essa divisão está a noção de **granularidade**: o tamanho que cada parte do sistema (ou serviço) deve assumir.

Para avaliar a qualidade da modularização, os autores apresentam um conjunto de métricas:

- **Coesão** — mede o quanto as partes de um módulo devem permanecer contidas dentro dele mesmo, sendo aferida pela métrica LCOM (a soma dos conjuntos de métodos que não compartilham campos entre si).
- **Acoplamento aferente e eferente** — o acoplamento aferente conta as conexões de entrada que um artefato de código recebe (componente, classe, função etc.), enquanto o acoplamento eferente conta as conexões de saída que esse artefato gera em direção a outros.
- **Abstração** — representa a proporção entre artefatos abstratos (classes abstratas, interfaces) e artefatos concretos (implementações), calculada pela razão entre a soma dos artefatos abstratos e o total de artefatos abstratos e concretos.
- **Distância da sequência principal** — uma métrica holística que combina abstração e instabilidade para avaliar o equilíbrio estrutural da arquitetura.

Um dos princípios mais citados do capítulo é a chamada **Segunda Lei da Arquitetura de Software**, segundo a qual o motivo por trás de uma decisão é mais importante do que a forma como ela é implementada — reforçando um tema já apresentado no Capítulo 1.

O capítulo dedica uma seção especial ao conceito de **conascência**, apresentado não como mais uma métrica de acoplamento, mas como uma linguagem — um framework de análise — que permite aos arquitetos descrever com mais precisão os diferentes tipos de acoplamento existentes entre elementos de software. Dois tipos são destacados:

- **Conascência estática**, que diz respeito ao acoplamento observável no nível do código-fonte.
- **Conascência dinâmica**, que analisa o acoplamento a partir das chamadas realizadas em tempo de execução.

A partir desse framework, os autores propõem duas regras práticas para lidar com conascência:

1. **Regra de grau** — sempre que possível, converter formas fortes de conascência em formas mais fracas, reduzindo o risco de mudanças em cascata.
2. **Regra de localidade** — à medida que a distância entre os elementos de software aumenta, é recomendável utilizar formas mais fracas de conascência entre eles.

## Principais aprendizados

- Modularidade é o princípio que organiza o código em agrupamentos lógicos e sustenta a manutenibilidade de sistemas complexos.
- Granularidade — o tamanho ideal de cada módulo ou serviço — é uma decisão central ao aplicar modularidade.
- Métricas como coesão (LCOM), acoplamento aferente/eferente e abstração ajudam a quantificar a qualidade estrutural de um sistema.
- A conascência oferece um vocabulário mais rico do que as métricas tradicionais de acoplamento, permitindo decisões mais precisas sobre como reduzir dependências entre módulos.
- Duas regras práticas orientam o uso da conascência: preferir formas fracas a formas fortes (regra de grau) e enfraquecer o acoplamento à medida que a distância entre elementos aumenta (regra de localidade).
