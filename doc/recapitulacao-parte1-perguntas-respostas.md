# Recapitulação — Parte I (Capítulos 1 a 8)
### Fundamentals of Software Architecture — Perguntas de discussão respondidas

---

## Capítulo 1: Introdução

**Quais são as quatro dimensões que definem a arquitetura de software?**
As quatro dimensões centrais são: 
(1) **estrutura/estilo arquitetural** — o tipo de estilo em que o sistema é implementado (microsserviços, camadas, monolito etc.); 
(2) **características arquiteturais** — os critérios de sucesso do sistema, geralmente ortogonais à funcionalidade de domínio (escalabilidade, disponibilidade, segurança...); (3) **decisões arquiteturais** — as regras que definem como o sistema deve ser construído; e 
(4) **componentes lógicos** — os blocos que organizam a lógica de negócio. Nos resumos deste material, estrutura e estilo às vezes aparecem desmembrados em dois itens, totalizando cinco pilares, mas a essência é a mesma.

**Qual é a diferença entre uma decisão arquitetural e um princípio de design?**
Uma decisão arquitetural é uma **regra obrigatória** — algo que o sistema deve ou não deve fazer (ex.: "somente a camada de serviços pode acessar o banco de dados"). Um princípio de design é uma **diretriz orientativa**, uma boa prática recomendada, mas não uma regra rígida de cumprimento obrigatório.

**Liste as oito expectativas básicas de um arquiteto de software.**
1. Definir as decisões arquiteturais e os princípios de design que vão guiar a equipe, o departamento ou a empresa.
2. Analisar continuamente o estado da arquitetura e do ambiente tecnológico, propondo melhorias.
3. Manter-se atualizado com as tendências e tecnologias do mercado.
4. Garantir que as decisões e princípios definidos sejam de fato seguidos.
5. Ter vivência prática com um leque amplo e variado de tecnologias, frameworks e plataformas.
6. Possuir certo grau de conhecimento sobre o domínio de negócio em que atua.
7. Desenvolver fortes habilidades interpessoais — trabalho em equipe, facilitação e liderança.
8. Compreender o "clima político" da empresa e saber transitar bem por ele.

**Qual é a Primeira Lei da Arquitetura de Software?**
"Tudo em arquitetura de software é uma questão de trade-off." Quase nenhuma decisão arquitetural traz apenas vantagens — ganhar em uma característica costuma custar em outra.

---

## Capítulo 2: Pensamento arquitetural

**Nomeie três critérios para determinar se uma decisão está mais relacionada com a arquitetura ou design.**
1. Qual o nível de raciocínio e planejamento envolvido na decisão?
2. Quantas pessoas ou equipes são afetadas por ela?
3. A decisão aponta para uma visão estratégica de futuro, ou para uma ação tática e imediata?

**Liste os três níveis do triângulo do conhecimento e forneça um exemplo de cada um.**
1. **O que você sabe** — tecnologias e ferramentas usadas no dia a dia (ex.: a linguagem de programação principal do arquiteto).
2. **O que você sabe que não sabe** — assuntos que você já ouviu falar ou conhece superficialmente, mas sem domínio prático (ex.: saber que existe Kubernetes, sem nunca ter operado um cluster).
3. **O que você não sabe que não sabe** — tecnologias ou soluções que resolveriam perfeitamente um problema, mas cuja existência o profissional nem imagina (ex.: desconhecer completamente uma ferramenta de nicho que seria ideal para o caso).

**Por que é mais importante o arquiteto se concentrar na amplitude técnica em vez de na profundidade técnica?**
Porque o valor do arquiteto está em conectar problemas específicos às soluções tecnológicas mais adequadas dentre um leque amplo de opções — e não em dominar cada tecnologia em profundidade de implementação. Aprofundar-se é papel natural do desenvolvedor especialista; o arquiteto precisa reconhecer boas soluções mesmo sem ser o maior especialista em cada uma delas.

**Quais são algumas maneiras de manter sua profundidade técnica e permanecer prático como arquiteto?**
Reservar tempo regular para escrever código de produção (mesmo em provas de conceito, que costumam virar referência); assumir histórias técnicas ou dívidas técnicas, liberando a equipe para o trabalho funcional; criar pequenas ferramentas de linha de comando para apoiar o time; participar de revisões de código; e reservar blocos curtos de tempo (como os ~20 minutos sugeridos no capítulo) para explorar tecnologias fora da zona de conforto.

---

## Capítulo 3: Modularidade

**Descreva a diferença entre modularidade e granularidade e forneça um exemplo de cada um.**
Modularidade é o **agrupamento lógico** de código relacionado — como organizar classes ou funções em módulos coerentes (ex.: separar um módulo de "Pedidos" e outro de "Pagamentos"). Granularidade é o **tamanho** que cada uma dessas partes deve assumir (ex.: decidir se "Pagamentos" deve virar um único microsserviço grande ou ser dividido em serviços menores, como "Cobrança" e "Estorno").

**Qual é a diferença entre acoplamento e coesão?**
Coesão mede o quanto os elementos **dentro de um mesmo módulo** estão relacionados entre si — quanto mais relacionados, mais coeso. Acoplamento mede o grau de dependência **entre módulos diferentes** — quanto mais um módulo depende de outro, mais acoplados eles estão.

**O que significa o termo conascência?**
É um framework de análise (não apenas uma métrica) que permite descrever com mais precisão os diferentes tipos de acoplamento existentes entre elementos de software, indo além de contar apenas conexões de entrada/saída.

**Qual é a diferença entre conascência estática e dinâmica?**
A estática diz respeito ao acoplamento observável diretamente no código-fonte (em tempo de compilação/design). A dinâmica só pode ser percebida a partir das chamadas realizadas em tempo de execução.

**Qual é a forma mais forte de conascência?**
A conascência de identidade (dinâmica), que ocorre quando múltiplos componentes precisam referenciar exatamente a mesma instância de um elemento — é a mais difícil de gerenciar e a que gera maior risco de mudanças em cascata.

**Qual é a forma mais fraca de conascência?**
A conascência de nome (estática), que ocorre simplesmente quando múltiplos componentes precisam concordar com o nome de um elemento (ex.: nome de um método ou classe).

**O que é preferível dentro de um codebase: conascência estática ou dinâmica?**
A estática é preferível, pois é visível diretamente no código-fonte e pode ser detectada por ferramentas de análise estática. A dinâmica só se manifesta em tempo de execução, sendo mais difícil de identificar e controlar.

---

## Capítulo 4: Definição das características arquiteturais

**Quais são os três critérios a que um atributo deve atender para ser considerado uma característica arquitetural?**
1. Especifica uma consideração de design que **não pertence** ao domínio de negócio.
2. Influencia algum aspecto da **estrutura** do sistema.
3. É **crítica ou importante** para o sucesso da aplicação.

**Qual é a diferença entre uma característica implícita e uma explícita? Forneça um exemplo de cada um.**
Implícita é aquela esperada por padrão, mesmo sem estar formalmente documentada (ex.: segurança básica de acesso). Explícita é aquela descrita conscientemente em documentos de requisitos pelas partes interessadas (ex.: "o sistema deve suportar 5.000 usuários simultâneos").

**Forneça um exemplo de uma característica operacional.**
Disponibilidade, desempenho, escalabilidade ou recuperabilidade.

**Forneça um exemplo de uma característica estrutural.**
Manutenibilidade, extensibilidade, implantabilidade ou portabilidade.

**Forneça um exemplo de uma característica transversal (cross-cutting).**
Segurança, usabilidade, acessibilidade ou conformidade legal.

**Por que é impossível criar uma lista padrão de características arquiteturais para toda a indústria?**
Porque cada projeto nasce de um contexto único — negócio, stakeholders, restrições técnicas e culturais — e pode inclusive originar características próprias, inventadas especificamente para aquele cenário. Isso reforça a ideia central do Capítulo 1: arquitetura depende de circunstância, não existe "certo" em abstrato.

---

## Capítulo 5: Identificando características arquiteturais

**Forneça uma razão que torne boa prática limitar o número de características ("capacidades") que uma arquitetura deve suportar.**
Cada característica adotada tem um custo real: exige esforço de design do arquiteto, esforço de implementação e manutenção da equipe, e eventualmente suporte estrutural adicional. Manter a lista curta favorece um design mais simples, elegante e focado no que realmente importa para o sucesso do sistema.

**Verdadeiro ou falso? A maioria das características arquiteturais vem dos requisitos de negócio e das histórias de usuário.**
**Falso.** Segundo o capítulo, as características são reveladas por três fontes: as preocupações do próprio domínio de negócio, os requisitos explícitos do projeto e o conhecimento implícito que o arquiteto acumula sobre o domínio — sendo que boa parte delas não está formalizada em requisitos ou histórias de usuário.

**Se um stakeholder do negócio declarar que o tempo de lançamento no mercado é a preocupação mais importante, quais características arquiteturais a arquitetura terá de suportar?**
"Tempo de lançamento no mercado" é um objetivo de negócio tipicamente **composto**: costuma se decompor em várias características simultâneas, como testabilidade, implantabilidade (deployability), modularidade/baixo acoplamento e, em muitos casos, escalabilidade — capacidades que juntas permitem entregar mudanças com rapidez e segurança.

**Qual é a diferença entre escalabilidade e elasticidade?**
Escalabilidade é a capacidade de suportar um **crescimento gradual e sustentado** de carga ou usuários sem degradação. Elasticidade é a capacidade de responder rapidamente a **picos súbitos e temporários** de carga, escalando (e desescalando) de forma ágil conforme a demanda muda.

**Qual é a diferença de uma característica arquitetural composta? Forneça um exemplo.**
É quando um objetivo de negócio, ao ser enunciado, na verdade mistura várias características diferentes em uma única frase, em vez de representar uma capacidade isolada. Exemplo: "agilidade de negócio" pode envolver, ao mesmo tempo, testabilidade, implantabilidade, modularidade e escalabilidade — cabe ao arquiteto decompor esse objetivo composto em características simples e mensuráveis.

---

## Capítulo 6: Medindo e controlando as características arquiteturais

**Por que a complexidade ciclomática é uma métrica tão importante para a análise na arquitetura?**
Porque ela transforma um conceito antes abstrato (a complexidade/manutenibilidade de um trecho de código) em um **indicador objetivo e mensurável**, calculado a partir do número de caminhos independentes possíveis no fluxo de execução — ilustrando a ideia central do capítulo de que características arquiteturais devem ser acompanhadas por dados, não apenas intuição.

**O que são funções de aptidão de arquitetura? Como podem ser usadas para analisar uma arquitetura?**
São funções-objetivo usadas para fornecer uma avaliação objetiva de quão íntegra está uma característica arquitetural específica (ou uma combinação delas). Na prática, transformam princípios arquiteturais muitas vezes vagos em verificações automatizáveis, que podem rodar continuamente (por exemplo, em pipelines de CI/CD) para garantir que a arquitetura continue respeitando o que foi definido.

**Forneça um exemplo de uma função de aptidão para a medição de escalabilidade de uma arquitetura.**
Um teste automatizado de carga, executado periodicamente, que simula um número crescente de usuários simultâneos e falha caso o tempo de resposta ou a taxa de erro ultrapasse um limite pré-definido.

**Qual é o critério mais importante para uma característica arquitetural permitir que arquitetos e desenvolvedores criem funções de aptidão?**
A característica precisa ser **mensurável objetivamente** — ou seja, é necessário existir um indicador quantificável associado a ela. Sem um indicador claro, não é possível construir uma verificação automatizada confiável.

---

## Capítulo 7: O escopo das características arquiteturais

**O que é um quantum arquitetural e por que é importante para a arquitetura?**
É a menor unidade do sistema capaz de ser executada de forma independente, incluindo seus próprios dados e as dependências necessárias para operar sozinha. É importante porque muda a pergunta do arquiteto de "quais características o sistema inteiro precisa?" para "quais características cada quantum precisa?", evitando o erro de tratar todo o sistema como um bloco único com as mesmas exigências.

**Imagine um sistema composto de uma única interface de usuário com quatro serviços implantados independentemente, cada um com o próprio banco de dados. Esse sistema teria um único quantum ou quatro quanta? Por quê?**
Depende do grau de acoplamento entre eles. Se a UI depende de chamadas **síncronas** a esses quatro serviços para completar suas operações de negócio, eles ficam atrelados em termos de disponibilidade e desempenho — nesse caso, formam, na prática, **um único quantum**, mesmo tendo bancos de dados separados. Só formariam **quatro quanta** de fato independentes se cada serviço conseguisse operar, falhar e evoluir sem que isso comprometesse a operação dos demais — ou seja, sem dependência síncrona direta entre eles.

**Qual é a diferença entre acoplamento estático e dinâmico? Forneça exemplo de cada um.**
O acoplamento estático refere-se a como os serviços estão conectados por contrato/design (ex.: um serviço que depende diretamente da API de outro para funcionar). O dinâmico refere-se ao comportamento de comunicação em tempo de execução entre eles (ex.: a sequência real de chamadas realizadas para completar uma transação de negócio, incluindo latência e ordem das chamadas).

**Por que a comunicação síncrona tem um impacto potencial maior nas características arquiteturais operacionais do que as assíncronas?**
Porque na comunicação síncrona o serviço chamador fica bloqueado esperando a resposta — a disponibilidade e o desempenho dele ficam diretamente atrelados à disponibilidade e ao desempenho do serviço chamado. Se este falhar ou ficar lento, o efeito se propaga imediatamente. Na comunicação assíncrona, os serviços ficam desacoplados no tempo, permitindo que um continue operando mesmo que o outro esteja indisponível ou lento.

---

## Capítulo 8: Pensamento baseado em componentes

**Como normalmente os componentes se manifestam dentro de uma aplicação ou serviço?**
Geralmente como pacotes, namespaces, diretórios de código-fonte, módulos ou bibliotecas — agrupamentos físicos de classes ou arquivos-fonte relacionados que implementam uma função de negócio específica.

**Qual é a diferença entre particionamento técnico e particionamento por domínio? Forneça um exemplo de cada um.**
O particionamento técnico organiza os componentes por **camadas técnicas** (ex.: apresentação, lógica de negócio, acesso a dados). O particionamento por domínio organiza os componentes em torno de **áreas de negócio** (ex.: "Pedidos", "Pagamentos", "Clientes"), como propõe o Domain-Driven Design.

**Qual é a vantagem do particionamento por domínio?**
Facilita a evolução para arquiteturas distribuídas, já que cada domínio pode se tornar um serviço independente com fronteiras bem definidas; melhora o alinhamento entre a estrutura técnica e a estrutura de negócio; e tende a reduzir o acoplamento entre áreas de negócio distintas.

**Em que circunstâncias o particionamento técnico seria uma escolha melhor do que o particionamento por domínio?**
Em sistemas menores, monolíticos, com fronteiras de domínio ainda pouco claras, ou quando a simplicidade e a velocidade inicial de desenvolvimento são prioridade sobre uma futura decomposição em serviços independentes — por exemplo, sistemas essencialmente CRUD, que sequer justificariam uma arquitetura elaborada.

**O que é a Armadilha da Entidade? Por que não é uma boa abordagem para a identificação de componentes?**
É o antipadrão em que o arquiteto deriva os componentes diretamente das entidades de domínio do sistema. O resultado costuma ser componentes com nomes ambíguos, que se tornam depósitos genéricos "faz-tudo" de funcionalidades relacionadas à entidade — perdendo granularidade adequada e finalidade clara, prejudicando a coesão.

**Quando podemos escolher a abordagem do Fluxo de Trabalho em vez da abordagem do Ator/Ação para identificar componentes básicos?**
Quando o sistema é fortemente orientado a **processos e sequências de etapas de negócio** (ex.: um fluxo de aprovação ou um pipeline de processamento de pedidos), nos quais entender a sequência de passos revela melhor os componentes do que mapear ações isoladas do usuário. A abordagem Ator/Ação tende a funcionar melhor quando o sistema é mais orientado a interações discretas do usuário, sem uma sequência rígida de processo.

---

Arquitetura de Software
│
├── Cap.1 → O que é Arquitetura
│
├── Cap.2 → Como pensa um Arquiteto
│
├── Cap.3 → Como organizar o software
│
├── Cap.4 → Quais características importam
│
├── Cap.5 → Como descobri-las
│
├── Cap.6 → Como medi-las
│
├── Cap.7 → Onde elas se aplicam
│
└── Cap.8 → Como transformar tudo isso em componentes
