# Fundamentos da Arquitetura de Software - Uma Abordagem Moderna de Engenharia

## Capítulo 1: Introdução

> "Todas as arquiteturas são produtos de seu contexto - lembre-se disso ao ler este livro"

> "A arquitetura é composta da estrutura do sistema, combinada com as caracteristicas de arquitetura (capacidades), os compomentes lógicos, os estilos de arquitetura e as decisões."

> "Tudo na arquitetura de software é um trade-off."

> "Por que é mais importante do que como."

> "A maioria das decisões de arquitetura não é binária; em vez disso, existe em um espectro entre extremos."

> "Espera-se que um arquiteto defina as decisões e arquitetura e os principios de design usados para guiar as decisões e tecnologia dentro da equipe, do departamento ou em toda a empresa."

> "Espera-se que um arquiteto analise continuamente a arquitetura e o ambiente tecnológico atual e recomende soluções para melhoria."

> "Espera-se que o arquiteto mantenha-se atualizado com as últimas tecnologias e tendências da indústria."

> "Espera-se que o arquiteto garanta a conformidade com as decisões de arquiteturas e os princípios de design."

> "Espera-se que o arquiteto tenha experiência com uma quantidade grande e variada de tecnologias, frameworks, plataforma e ambientes."

> "Espera-se que o arquiteto tenha certo nível de expertise no domínio dos negócios."

> "Espera-se que o arquiteto tenha habilidades interpessoais excepcionais, incluindo trabalho em equipe, facilitação e liderança."

> "Espera-se que o arquiteto entenda o clima político da empresa e seja capaz de lidar com a política."

[Resumo do capítulo](doc/capitulo1/resumo.md)

## Parte 1: Fundamentos

### Capitulo 2 - Pensamento arquitetural

> "Pensamento arquitetural: entender com uma alteração específica pode impactar a escalabilidade geral, como diferentes partes de um sistema interagem, saber quais bibliotecas e frameworks de terceiros seriam mais apropriados."

> "Pensar como arquiteto: entender o que é arquitetura de software, as difenças entre arquitetura de design, compreender a importancia dos impulsionadores de negócio, entender, analisar e conciliar trade-offs."

> "Arquitetura de software: sua estrutura."

> "Design: sua aparência."

> "Estratégica: decisões de longo prazo."

> "Tática: são de curto prazo."

> "Qual é o nível de raciocínio e planejamento envolvido na decisão?"

> "Quantas pessoas estão envolvidas na decisão?"

> "A decisão tem relação com uma visão de longo prazo ou com uma ação de curto prazo?"

> "Valor de um arquiteto é ter um amplo conhecimento da tecnologia e de como a usar para resolver problemas específicos."

> "Os desenvolvedores passam suas carreiras inteiras aprimorando a expertise."

> "Equilibrar a profundidade e amplitude de seu portfólio de conhecimento é algo que todo desenvolvedor deve considerar ao longo da carreira."

> "Aproveite seus 20 minutos enquanto sua mente está fresca e antes que as distrações tomem conta."

> "Aumentará sua amplitude técnica e o ajudará a desenvolver e manter o conhecimento que o tornará um arquiteto de software eficaz."

> "Radar pessoal fornecerá um bom arcabouço para a expansão de seu portfólio tecnológico."

> "Tarefa difíceis que um arquiteto enfrenta é como equilibrar a codificação prática com a arquitetura de software."

[Resumo do capítulo](doc/capitulo2/resumo.md)

### Capitulo 3 - Modularidade

> "A modularidade é um princípio organizador."

> "... codebase sustentáveis exigem a ordem e a consistência que isso proporcina."

> "A modularidade trata da divisão de sistemas em partes menores, como na transição de um estilo de arquitetura monolítica (como a tradicional arquitetura em camadas N-tier) para um estilo de arquitetura altamente distribuída, como nos microsserviços."

> "A granularidade, está relacionada com o tamanho dessas partes - que tamanho uma parte específica do sistema (ou serviço) deve ter."

> "Modularidade: um agrupamento lógico de código relacionado, que pode ser um grupo de classes em uma linguagem orientada a objetos ou um grupo de funções em uma linguagem estruturada ou funcional."

> "A coesão mede a extensão até a qual as partes de um módulo devem estar contidas dentro do mesmo módulo."

> "Métrica LCOM: a soma dos conjuntos de métodos não compartilhados por meio de campos compartilhados."

> "Segunda Lei da Arquitetura de Software: por que é mais importante de que como."

> "O acoplamento aferente mede o número de conexões de entrada de um artefato de código (compomente, classe, função e assim por diante). O acoplamento eferente mede as conexões de saída de outros artefatos de código."

> "Abstração é a proporção existente entre artefatos abstratos (classes abstratas, interfaces e assim por diante) e artefatos concretos (implementações)."

> "Os arquitetos calculam a abstração determinando a razão entre a soma dos artefatos abstratos e a soma dos artefatos concretos e abstratos."

> "métricas holísticas, estrutura arquitetural é a distância da sequência principal."

> "A conascência não é uma métrica de acoplamento como os acoplamentos aferente e eferente - em vez disso, representa uma linguagem que ajuda os arquitetos a descreverem os diferentes tipos de acoplamento com mais precisão."

> "A conascência estática é o acoplamento no nível do código-fonte."

> "A conascência dinâmica, que analisa as chamadas no tempo de execução. "

> "A conascência é uma estrutura de análise."

> "Regra de grau: converta formas fortes em formas mais fracas de conascência"

> "Regra de localidade: à medida que a distância entre os elementos de software aumentar, use formas mais fracas de conascência."

[Resumo do capítulo](doc/capitulo3/resumo.md)