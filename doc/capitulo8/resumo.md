# Capítulo 8 - Pensamento Baseado em Componentes

## Resumo

O oitavo capítulo encerra a Parte I do livro voltando-se para os **componentes lógicos**, definidos como os blocos de construção fundamentais de um sistema. Pensar com base em componentes significa enxergar a estrutura de um sistema como um conjunto de componentes lógicos que interagem entre si para executar funções de negócio — sendo que as principais funções desempenhadas pelo sistema são justamente o que definem esses componentes.

Os autores distinguem dois níveis de arquitetura: a **arquitetura lógica**, formada pelos componentes lógicos e pela forma como eles interagem — na qual o que mais importa é o que o sistema faz, como essa funcionalidade é demarcada e como as partes funcionais se relacionam —, e a **arquitetura física**, que engloba os artefatos concretos, como serviços, interfaces de usuário e bancos de dados. Definir a arquitetura lógica é um processo contínuo: envolve identificar e reestruturar componentes à medida que o entendimento sobre o sistema evolui, e não uma tarefa que se encerra em uma única etapa inicial.

O grande desafio inicial é determinar quais devem ser os componentes básicos de partida. O capítulo apresenta duas abordagens práticas para essa identificação:

- **Abordagem por Fluxo de Trabalho (Workflow)** — concentra-se nos principais fluxos de trabalho do sistema como ponto de partida para definir os componentes.
- **Abordagem por Ator/Ação** — parte da identificação das principais ações que um usuário pode realizar no sistema.

Em contraste, os autores alertam para um antipadrão comum: a **Armadilha da Entidade**, que ocorre quando o arquiteto se concentra nas entidades de domínio do sistema e deriva componentes diretamente delas. O resultado costuma ser nomes de componentes ambíguos, que não descrevem de fato seu papel, e componentes que se tornam depósitos genéricos de funcionalidades relacionadas ao domínio — semelhantes às classes utilitárias "faz-tudo" que todo desenvolvedor já escreveu em algum momento da carreira. Esse tipo de componente acaba tendo baixa granularidade, faz coisas demais e perde a finalidade original. O capítulo também observa que, se um sistema se resume a operações CRUD, ele provavelmente não precisa de uma arquitetura elaborada, e sim de um framework ou ferramenta no-code/low-code voltada para CRUD.

Depois de definidos os componentes iniciais, o processo segue com a **atribuição de histórias de usuário ou requisitos** a cada componente lógico. Na sequência, entra a etapa de refinamento, que consiste em analisar os papéis e responsabilidades de cada componente — sendo a **coesão** um critério central nessa análise, entendida como o quanto as operações de um componente estão inter-relacionadas entre si.

A etapa final de análise volta a conectar o capítulo aos temas anteriores do livro: considerar as **características arquiteturais** que o sistema exigirá. Uma visão puramente funcional do design de componentes poderia levar, por exemplo, à atribuição de um único componente para lidar com toda a interação do usuário; ao analisar os componentes também sob a ótica das características arquiteturais, no entanto, o arquiteto é levado a subdividir esse componente — reforçando que determinar quais características são mais importantes para o sistema influencia diretamente o desenho dos componentes lógicos. Assim como já apontado em capítulos anteriores, o design de componentes não é um evento único: os arquitetos devem iterar continuamente sobre ele, em colaboração com os desenvolvedores, reestruturando os componentes com frequência ao longo do ciclo de vida do sistema ou produto.

O capítulo fecha tratando do **acoplamento** entre componentes, reforçando uma ideia simples, porém central: quanto mais acoplados estiverem os componentes de um sistema, mais difícil será mantê-lo e testá-lo. São apresentados diferentes tipos de acoplamento:

- **Acoplamento estático** — ocorre quando os componentes se comunicam entre si de forma síncrona.
- **Acoplamento aferente** — o grau em que outros componentes dependem de um componente-alvo.
- **Acoplamento eferente** — o grau em que um componente-alvo depende de outros componentes.
- **Acoplamento temporal** — descreve dependências não estáticas, geralmente baseadas em tempo ou em transações.

Diante disso, os autores recomendam buscar sempre o fraco acoplamento no design do sistema, e apresentam a **Lei de Demeter** como técnica para viabilizar isso: um componente ou serviço deve ter conhecimento limitado sobre os demais componentes ou serviços do sistema, restringindo o quanto cada parte "sabe" sobre o restante da arquitetura. Por fim, fica um alerta importante: aplicar a Lei de Demeter não necessariamente reduz o acoplamento total do sistema — na prática, ela costuma apenas redistribuir esse acoplamento para outras partes do sistema.

## Principais aprendizados

- Componentes lógicos são os blocos de construção de um sistema; pensar com base em componentes significa enxergar o sistema como um conjunto de partes que interagem para cumprir funções de negócio.
- Arquitetura lógica (componentes e suas interações) e arquitetura física (artefatos concretos como serviços, UIs e bancos de dados) são níveis complementares, mas distintos, de análise.
- As abordagens de Fluxo de Trabalho e de Ator/Ação são formas práticas de identificar os componentes iniciais de um sistema.
- A Armadilha da Entidade é um antipadrão recorrente: derivar componentes diretamente das entidades de domínio tende a gerar componentes ambíguos, "faz-tudo" e de baixa granularidade.
- O design de componentes segue um fluxo: identificar componentes iniciais, atribuir histórias/requisitos, analisar papéis e coesão, e por fim considerar as características arquiteturais exigidas — um processo iterativo, não único.
- Existem diferentes tipos de acoplamento entre componentes (estático, aferente, eferente e temporal), e buscar o fraco acoplamento é uma meta central do design.
- A Lei de Demeter ajuda a limitar o conhecimento que um componente tem sobre os demais, mas não elimina o acoplamento do sistema — apenas o redistribui para outras partes.
