# Capítulo 9 - Fundamentos (Parte 2: Estilos de Arquitetura)

## Resumo

O capítulo 9 abre a Parte II do livro, dedicada aos estilos de arquitetura, e deixa claro desde o início que compreender esses estilos demanda tempo e esforço — mas é um investimento necessário, já que conhecer os diversos estilos e os trade-offs associados a cada um é o que permite ao arquiteto tomar decisões eficazes. O capítulo funciona como uma base conceitual, apresentando os elementos que compõem um estilo arquitetural antes de mergulhar nos estilos específicos nos capítulos seguintes.

Um estilo de arquitetura é descrito por um conjunto de fatores que se combinam: a topologia dos componentes, a arquitetura física, a forma de implantação, o estilo de comunicação entre as partes e a topologia dos dados. Nomear um estilo (como "microsserviços" ou "monólito em camadas") oferece uma forma concisa de resumir esse conjunto complexo de fatores, facilitando a comunicação entre arquitetos.

O capítulo contrapõe essa ideia ao antipadrão da **Grande Bola de Lama** — um sistema sem estrutura interna real, com código espaguete, disperso, desleixado e cheio de correções acumuladas, no qual manipuladores de eventos se conectam diretamente a chamadas de banco de dados sem nenhuma camada de organização.

A partir daí, o capítulo percorre a evolução histórica do particionamento de sistemas:

- **Arquitetura de duas camadas (cliente/servidor)** — separa a funcionalidade técnica entre front-end e back-end.
- **Arquitetura de três camadas** — acrescenta um servidor de aplicação entre o front-end e um servidor de banco de dados de nível industrial.
- A quantidade e a forma dessas camadas variam conforme as necessidades da aplicação e as capacidades da plataforma disponível — não existe um número "certo" de camadas.

Um ponto de atenção recorrente é que nunca foi fácil enxergar as implicações de longo prazo de uma decisão de design, o que reforça a recomendação de **preferir designs simples**.

O capítulo destaca que a forma como os componentes de alto nível são organizados — o **particionamento de alto nível** — tem um impacto enorme na arquitetura, e apresenta duas abordagens centrais:

- **Monólito em camadas** — organiza a arquitetura com base em capacidades técnicas (apresentação, regras de negócio, serviços, persistência etc.), seguindo o padrão MVC (Model-View-Controller) como exemplo típico dessa organização.
- **Monólito modular** — mantém uma única unidade de implantação e um único banco de dados, mas particiona internamente o código com base em domínios, inspirando-se nas ideias de Domain-Driven Design (Eric Evans). É essa mesma filosofia de domínios e fluxos de trabalho independentes e desacoplados que fundamenta, mais adiante, a arquitetura de microsserviços.

Essa distinção leva à separação entre dois tipos de particionamento:

- **Particionamento técnico** — separa componentes de alto nível com base em capacidades técnicas.
- **Particionamento por domínio** — separa componentes de alto nível por fluxo de trabalho e/ou domínio de negócio.

O capítulo também recorre à **Lei de Conway**, segundo a qual empresas que projetam sistemas tendem a produzir designs que são cópias das suas próprias estruturas de comunicação — reforçando que a arquitetura de um sistema costuma espelhar a organização de quem a constrói.

Na sequência, o capítulo separa os estilos arquiteturais em dois grandes grupos: **monolíticos** (uma única unidade de implantação para todo o código) e **distribuídos** (várias unidades de implantação conectadas por protocolos de acesso remoto). Para os estilos distribuídos, os autores revisitam as clássicas **falácias da computação distribuída**, alertando sobre suposições perigosas que arquitetos costumam fazer:

1. **A rede é confiável** — não é; por isso existem mecanismos como tempos limite (timeouts) e circuit breakers entre serviços.
2. **A latência é zero** — nunca é; conhecer a latência média (e especialmente a dos percentis 95–99) é crucial em produção.
3. **A largura de banda é infinita** — a comunicação entre serviços consome banda de forma significativa; o acoplamento de carimbo (stamp coupling) pode ser mitigado com endpoints privados, seletores de campo, GraphQL, contratos orientados ao consumidor ou endpoints internos de mensagens, sempre transmitindo apenas os dados necessários.
4. **A topologia nunca muda** — exige comunicação constante com as equipes de operações e rede sobre mudanças planejadas, para evitar surpresas.
5. **Existe apenas um administrador** — arquiteturas distribuídas costumam exigir coordenação com múltiplos administradores, o que aumenta a complexidade de coordenação geral.
6. **O custo de transporte é zero** — arquiteturas distribuídas custam significativamente mais que monolíticas, por conta de hardware, servidores, gateways, firewalls, sub-redes e proxies adicionais; é preciso analisar a topologia atual quanto a capacidade, largura de banda, latência e zonas de segurança.
7. **A rede é homogênea** — pacotes de rede se perdem, o que afeta suposições sobre confiabilidade, latência e largura de banda.
8. **É fácil criar versões** — versionar a comunicação entre serviços é sensato, mas traz trade-offs que precisam ser antecipados.
9. **As atualizações compensatórias sempre funcionam** — ao projetar fluxos de trabalho transacionais em microsserviços, é preciso prever não só o fluxo de compensação "normal", mas também como se recuperar caso a atualização (ou a própria compensação) falhe.

Por fim, o capítulo conecta a discussão de estilos arquiteturais à obra **Team Topologies**, apresentando quatro tipos de equipe relevantes para a forma como sistemas são construídos e mantidos:

- **Equipes alinhadas ao fluxo** — focadas estritamente em uma única linha de trabalho, como um produto, serviço ou conjunto específico de funcionalidades.
- **Equipes de facilitação** — preenchem lacunas de capacidade, oferecendo espaço para pesquisa, aprendizado e tarefas importantes, porém não urgentes.
- **Equipes de subsistemas complicados** — dominam totalmente um subsistema ou domínio complexo e apoiam equipes alinhadas ao fluxo na sua aplicação, reduzindo a carga cognitiva dessas equipes.
- **Equipes de plataforma** — fornecem serviços internos e blocos de construção reutilizáveis, apoiando as demais equipes, removendo atritos desnecessários e garantindo governança em relação a qualidade e segurança.

## Principais aprendizados

- Um estilo arquitetural é definido pela combinação de topologia de componentes, arquitetura física, forma de implantação, estilo de comunicação e topologia de dados.
- A Grande Bola de Lama é o antipadrão que representa a ausência total de estrutura arquitetural.
- A evolução de arquiteturas de duas e três camadas mostra que o número e a forma das camadas dependem do contexto da aplicação e da plataforma.
- O particionamento de alto nível pode ser técnico (por capacidades técnicas, como no monólito em camadas e no MVC) ou por domínio (como no monólito modular e nos microsserviços, inspirados em DDD).
- A Lei de Conway lembra que a estrutura de comunicação de uma organização tende a se refletir na estrutura dos sistemas que ela constrói.
- As falácias da computação distribuída são suposições perigosas e recorrentes que todo arquiteto de sistemas distribuídos precisa conhecer e mitigar ativamente.
- Os quatro tipos de equipe de Team Topologies (alinhada ao fluxo, de facilitação, de subsistemas complicados e de plataforma) ajudam a pensar a arquitetura também sob a ótica organizacional, não apenas técnica.
