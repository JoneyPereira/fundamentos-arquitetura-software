# Fundamentos da Arquitetura de Software - Uma Abordagem Moderna de Engenharia

## Skills

Este repositório também reúne skills práticas para agentes de IA, derivadas dos
conceitos estudados em cada capítulo. Cada skill fica em `skills/<nome>/SKILL.md`
e pode ser usada diretamente em agentes como Claude Code, Cursor, etc.

---

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

---

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

---

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

**Skill relacionada:** [`lcom96-repository-analysis`](doc/skills/lcom96-repository-analysis/SKILL.md)
> Analisa a coesão de classes de um repositório real calculando LCOM96 por classe,
> gerando ranking de baixa coesão e apontando indícios de violação de SRP.

---

### Capitulo 4 - Definição das características arquiteturais

> "Design estrutual: análise de características arquiteturais, design de componentes lógicos."

> "definir, descobrir e analisar todas as coisas que o software deve fazer que não estão diretamente relacionadas à funcionalidade do domínio: características arquiteturais"

> "característica arquitetural: especificar uma consideração de design que não seja do domínio, influenciar algum aspecto do design e ser crítico ou importante para o sucesso da aplicação."

> "critérios operacionais e de design para o sucesso do projeto"

> "identificar considerações importante de design"

> "se esforçar para escolher o menor número possível de características arquiteturais em vez de o maior."

> "características arquiteturais implícitas: disponibilidade, confiabilidade e segurança."

> "características arquiteturais explícitas: aparecem em documentos de requisitos."

> "um projeto de software pode inventar características arquiteturais com base em fatores únicos."

> "Cada característica suportada exigirá esforço de design do arquiteto, esforço dos desenvolvedores para implementá-la e mantê-la e, talvez, suporte estrutural."

> "Nunca tente obter a melhor arquitetura, vise obter a arquitetura menos pior."

> "Esforce-se para projetar uma arquitetura que seja o mais interativa posível."

> "mais importante do desenvolvimento de software ágil é o valor da iteração."

[Resumo do capítulo](doc/capitulo4/resumo.md)

---

### Capitulo 5 - Identificando características arquiteturais

> "identificar as características arquiteturais ('capacidades') corretas para determinado problema ou aplicação exige não só o conhecimento do problema do domínio, mas também a colaboração das partes interessadas para determinar o que é realmente importante do ponto de vista do domínio."

> "podemos descobrir características arquiteturais: as preocupações do domínio, os requisitos do projeto e nosso conhecimento implicíto do domínio."

> "arquitetos e os stakeholders do domínio falam idiomas diferentes."

> "'tradizir' as preocupações do domínio para a linguagem das características arquiteturais."

> "Conhecer os principais objetivos do domínio permite que o arquiteto traduza essas preocupações para as 'capacidades', o que forma a base para decisões arquiteturais e justificáveis."

> "uma armadilha comum é a criação de equivalências falsas, como equiparar agilidade somente com tempo de lançamento no mercado."

> "objetivos de negócio começam como características arquiteturais compostas."

> "Decompô-las e dar às caracteríticas resultantes definições objetivas faz parte do trabalho dos arquitetos."

> "Não existem respostas erradas na arquitetura, apenas respostas caras. - Uma das famosas frases de Mark."

> "identificar corretamente elementos estruturais importantes talvez facilite criar um desifn mais simples ou elegante."

> "esforce-se para manter a lista final o mais curta possível."

> "colaboração entre o arquiteto e os stakeholders d negócio é crucial durante a análise das características arquiteturais."

[Resumo do capítulo](doc/capitulo5/resumo.md)

[Facilitador de características arquiteturais (ferramenta interativa)](doc/capitulo5/facilitador-caracteristicas.html)

---

### Capitulo 6 - Medindo e controlando as características arquiteturais

> "É benéfico para os arquitetos saber como medir e controlar as características arquiteturais."

> "Equipes de alto nível baseiam suas definições em análises estatísticas."

> "Um aspecto mensurável de código é a complexidade, definida pela métrica Complexidade Ciclomática."

> "o processo de desenvolvimento de software, pode influenciar a estrutura da arquitetura."

> "governança é uma responsabilidade importante do papel do arquiteto."

> "seu escopo abrange qualquer aspecto do processo de desenvolvimento de software que os arquitetos queiram influenciar."

> "função de aptidão: uma função objeto usada para avaliar se o resultado chegou próximo de atingir seu objetivo."

> "função de aptidão arquitetural: qualquer mecanismo que forneça uma avaliação objetiva da integridade de alguma característica araquitetural ou combinação de características arquiteturais."

> "Os arquitetos devem assegurar que os desenvolvedores entendam a finalidade de uma função de aptidão antes de impô-la a eles."

>"problema que pode ocorrer com qualquer métrica ou medição: a possibilidade de os desenvolvedores tentarem manipular o sistema."

> "A engenharia do caos oferece uma nova e interessante perspectiva para a arquitetura: não é uma questão de se algo acabará sobrebdo danos, e sim quando."

> "funções de aptidão - não são um mecanismo de governanção pesado, e sim uma forma de os arquitetos expressarem e cerificarem automaticamente principios arquiteturais importantes."

[Resumo do capítulo](doc/capitulo6/resumo.md)

[Calcula a Complexidade Ciclomática (CC)](doc/capitulo6/cyclomatic_complexity.py)

---

### Capitulo 7 - Escopo das características arquiteturais

> "pensamento dos arquitetos de software deve evoluir com o ecossistema."

> "isso é mais evidente na definição do escopo das características arquiteturais."

> "uma falha fatal: assumir um único conjunto de características arquiteturais para todo o sistema."

> "quantum arquitetural é a 'menor parte do sistema que é executada independetemente'."

> "um serviço pode ser executado independentemente dentro da arquitetura, incluindo seus dados e outras dependências."

> "DDD é uma tecnica de modelagem que permite que os arquitetos decompanham domínios de problema complexos de maneira organizada."

> "Acoplamentos mais altos são permitidos para escopos mais restritos; quanto mais amplo o escopo, mais fraco deve ser o acoplamento."

> "conceito de quantum arquitetural oferece uma nova forma de pensar sobre o escopo."

> "Determinar os limites do quantum do domínio do problema ajuda na escolha de um estilo arquitetural: uma arquitetura monolítica ou uma aquitetura distribuída."

> "considerar pelo menos dois cenários ao usar recursos baseados em nuvem: para hospedar contêiners e recursos do provedor de nuvem como compomentes do sistema."

[Resumo do capítulo](doc/capitulo7/resumo.md)

---

### Capitulo 8 - Pensamento baseado em componentes

> "componentes lógicos - os blocos de construção de um sistema."

> "Pensar com base em componentes é ver a estrutura de um sistema como um conjunto de componentes lógicos, todos interagindo para executar certas funções do negócio."

> "as principais funções que um sistema executa representam os compomentes deste sistema."

> "arquitetura lógica é composta dos compomentes lógicos (blocos de construção) de um sistema e de como interagem uns com outros."

> "arquitetura física, inclui artefatos físicos como serviços, interfaces de usuário, bancos de dados e assim por diante."

> "numa arquitetura lógica, o mais importante é o que o sistema faz, como essa funcionalidade é demarcada e como as partes funcionais do sistema interagem."

> "arquitetura lógica envolve identificar e reestruturar componentes lógicos continuamente"

> "O desafio é deterinar quais devem ser os compomentes iniciais básicos."

> "interar pelos compomentes lógicos à medida que aprendemos mais sobre o sistema."

> "Uma abordagem comum para identificar os compoementes iniciais básicos de uma arquitetura lógica é a do Fluxo de Trabalho (Workflow)"

> "concentre-se nos fluxos de trabalho principais."

> "Outra maneira de os arquitetos identificarem os compomentes iniciais básicos é com as abordagem do Ator/Ação."

> "identifica as principais ações que um usuário pode realizar no sistema."

> "tentador para um arquiteto começar a identificar compomentes se concentrando nas entidades envolvidas no sistema e derivando compomentes dessas entidades."

> "os nomes do compomentes lógicos são ambíguos e não descrevem o papel do compomente."

> "antipadrão Armadilha da Entidade."

> "os componentes se tornam depósitos para funcionalidades relacionadas ao domínio."

> "ele passa a ser semelhantes às classes utilitárias 'faz-tudo' que todo desenvolvedor já escreveu pelo menos uma vez na carreira."

> "os compomentes passam a ter baixa granularidade, fazem coisas demais e perdem a finalidade."

> "Se um arquiteto estiver construindo um sistema, operações CRUD, o sistema não precisará de uma arquitetura, e sim de um framework, ferramentea ou ambiente nocode/low-code baseado em CRUD."

> "próxima etapa da criação de uma arquitetura lógica é atribuir histórias de usuário ou requisitos aos compoemntes lógicos."

> "próxima etapa do refinamento dos compomentes lógicos é analisar os papéis e responsabilidades de cada compomente."

> "coesão: como e quanto as operações de um compomente estão inter-relacionadas."

> "etapa de análise final é considerar as característics arquiteturais que o sistema exigirá."

> "uma visão puramente funcional do design de compomentes poderia levar um arquiteto a atribuir um único compomente para manipular a interação do usuário, analisar os compomentes em termos de características arquiteturais leva a uma subdivisão."

> "determinação de quais características arquiteturais são as mais importamtes para o sistema."

> "arquitetos devem iterar continuamente nos seus designs de compomentes em colaboração com os desenvolvedores."

> "reestruturar os compomentes frequentemente ao longo do ciclo de vida de um sistema ou produto."

> "mais acoplados estiverem os componentes de um sistema, mas difícil será mantê-lo e testá-lo"

> "O acoplamento estático ocorre quando os compomentes se comunicam uns com os outros de forma sincrona."

> "Acoplamento aferente é o grau em que os outros compomentes dependem de um compomente-alvo."

> "Acoplamento eferente é o grau em que um compomente-alvo depende de outros compomentes."

> "Acoplamento temporal descreve dependências não estáticas, geralmente baseadas em tempo ou transações."

> "buscar o fraco acoplamento no design do sistema."

> "técnica para a criação de sistemas fracamente acoplados se chama Lei de Demeter."

> "um componente ou serviço deve ter conhecimento limitado de outros compomentes ou serviços."

> "A ideia existente por trás da Lei de Demeter é a limitação do conhecimento que cada compomente tem sobre o restante do sistema."

> "Aplicar a Lei de Demeter não reduz necessamente o nível de acoplamento em todo o sistema; em vez disso, geralmente ela redistribui esse acoplamento para diferentes partes do sistema."

[Resumo do capítulo](doc/capitulo8/resumo.md)