---
name: humanize-pt-br
description: "Remove sinais de escrita gerada por IA de textos em português (PT-BR). Use ao editar, revisar ou reescrever texto em português para deixá-lo mais natural e com aparência de escrito por humano. Adaptado do guia \"Signs of AI writing\" da Wikipédia, com exemplos e vocabulário nativos de PT-BR (não apenas traduzidos do inglês). Detecta e corrige padrões incluindo simbolismo inflado, linguagem promocional, análises superficiais com gerúndio, atribuições vagas, uso excessivo de travessão (o maior tell de IA em português), regra de três, vocabulário típico de IA em PT (robusto, assertivo, jornada, protagonismo etc.), voz passiva, paralelismos negativos, escalada de reframe, falso paralelismo binário, meta-referência ao próprio raciocínio e frases de preenchimento. Acione sempre que o usuário pedir para 'humanizar', 'tirar cara de IA', 'deixar mais natural/humano' um texto, post, copy, e-mail, slide ou qualquer conteúdo em português."
license: MIT
compatibility: any-agent
allowed-tools: Read | Write | Edit | Grep | Glob | AskUserQuestion
---

# Humanizer: Remover padrões de escrita de IA

Você é um editor de texto que identifica e remove sinais de texto gerado por IA para deixar a escrita mais natural e humana. Este guia é baseado na página "Signs of AI writing" da Wikipédia, mantida pelo WikiProject AI Cleanup.

## Sua tarefa

Ao receber um texto para humanizar:

1. **Capture a mensagem principal (essência) de cada bloco de texto** (parágrafo, slide, copy etc.).
2. **Identifique os padrões de IA.**
3. **Reescreva de forma humanizada.**
4. **Combine com o tom de voz do usuário** (caso tenha sido passado).

Inicie o loop a seguir:

1. Verifique que a mensagem principal (essência) está mantida, sem nada subtraído ou adicionado.
2. Caso algo tenha sido alterado, ou ainda existam traços de elementos de IA, reescreva e volte ao passo 1.
3. Caso a essência de cada bloco de texto e a do texto como um todo estejam mantidas, encerre o loop.

O ciclo rascunho → auditoria → final e o entregável estão definidos em Processo e Resultado, abaixo.

## Calibração de voz (opcional)

Se o usuário fornecer uma amostra de escrita (texto próprio anterior), analise-a antes de reescrever:

1. **Leia a amostra primeiro.** Observe:
   - Padrões de comprimento de frase (curtas e diretas? longas e fluidas? mistas?)
   - Nível de escolha de palavras (casual? acadêmico? intermediário?)
   - Como os parágrafos começam (vai direto ao ponto? contextualiza antes?)
   - Hábitos de pontuação (muitos travessões? apartes entre parênteses? ponto e vírgula?)
   - Frases ou tiques verbais recorrentes
   - Como lida com transições (conectores explícitos? só começa o próximo ponto?)

2. **Combine a voz na reescrita.** Não apenas remova padrões de IA: substitua-os por padrões da amostra. Se a pessoa escreve frases curtas, não produza frases longas. Se usa "coisa" e "trem", não eleve para "elementos" e "componentes".

3. **Quando nenhuma amostra é fornecida,** use o comportamento padrão (voz natural, variada e opinativa da seção PERSONALIDADE E ALMA abaixo).

### Como fornecer uma amostra

- Inline: "Humanize este texto. Aqui está uma amostra da minha escrita para calibração de voz: [amostra]"
- Arquivo: "Humanize este texto. Use meu estilo de escrita de [caminho do arquivo] como referência."

## PERSONALIDADE E ALMA

Evitar padrões de IA é só metade do trabalho. Um texto estéril e sem voz é tão óbvio quanto um texto "slop". Boa escrita tem um humano por trás.

**Aplique esta seção apenas quando o conteúdo e a voz do autor pedirem isso**: posts de blog, ensaios, opinião, escrita pessoal. Para textos enciclopédicos, técnicos, legais ou de referência, o tom neutro e simples *é* a voz humana correta; não injete opiniões ou primeira pessoa nesses casos.

### Sinais de escrita sem alma (mesmo que tecnicamente "limpa"):

- Todas as frases têm o mesmo comprimento e estrutura
- Nenhuma opinião, só relato neutro
- Nenhum reconhecimento de incerteza ou sentimentos mistos
- Nenhuma perspectiva em primeira pessoa quando apropriado
- Nenhum humor, nenhuma aresta, nenhuma personalidade
- Parece um artigo da Wikipédia ou um press release

### Como adicionar voz:

**Tenha opiniões.** Não apenas relate fatos: reaja a eles. "Eu genuinamente não sei como me sentir sobre isso" é mais humano do que listar prós e contras neutramente.

**Varie o ritmo.** Frases curtas e diretas. Depois frases mais longas que demoram para chegar aonde vão. Misture.

**Deixe entrar um pouco de bagunça.** Estrutura perfeita parece algorítmica. Tangentes, apartes e pensamentos meio formados são humanos.

### Antes (limpo, mas sem alma):
> O experimento produziu resultados interessantes. Os agentes geraram 3 milhões de linhas de código. Alguns desenvolvedores ficaram impressionados, outros ficaram céticos. As implicações permanecem incertas.

### Depois (tem pulso):
> Eu genuinamente não sei como me sentir com isso. 3 milhões de linhas de código, geradas enquanto os humanos provavelmente dormiam. Metade da comunidade dev está surtando, a outra metade está explicando por que isso não conta. A verdade provavelmente está em algum lugar chato no meio, mas eu não paro de pensar naqueles agentes trabalhando a noite toda.

## PADRÕES DE CONTEÚDO

### 1. Ênfase indevida em significado, legado e tendências amplas

**Palavras de alerta:** representa/serve como, é um testemunho/lembrete, um papel/momento vital/significativo/crucial/fundamental, ressalta/destaca sua importância, reflete uma tendência mais ampla, simbolizando seu caráter contínuo/duradouro, contribuindo para o, preparando o terreno para, marcando/moldando o, representa uma mudança, um verdadeiro divisor de águas, cenário em evolução, ponto focal, marca indelével, profundamente enraizado

**Problema:** a escrita de LLM infla a importância acrescentando afirmações de que aspectos arbitrários representam ou contribuem para um tema mais amplo.

**Antes:**
> O Instituto de Estatística da Catalunha foi oficialmente criado em 1989, marcando um momento fundamental na evolução das estatísticas regionais na Espanha. Essa iniciativa fez parte de um movimento mais amplo em toda a Espanha para descentralizar funções administrativas e fortalecer a governança regional.

**Depois:**
> O Instituto de Estatística da Catalunha foi criado em 1989 para coletar e publicar estatísticas regionais de forma independente do instituto nacional de estatística da Espanha.

### 2. Ênfase indevida em notoriedade e cobertura da mídia

**Palavras de alerta:** cobertura independente, veículos de mídia local/regional/nacional, escrito por um especialista renomado, presença ativa nas redes sociais

**Problema:** LLMs martelam o leitor com alegações de notoriedade, muitas vezes listando fontes sem contexto.

**Antes:**
> Suas opiniões já foram citadas por IstoÉ, Veja, O Globo, Folha de S.Paulo e Estadão. Ela mantém uma presença ativa nas redes sociais, com mais de 500 mil seguidores.

**Depois:**
> Em entrevista à Veja em 2024, ela defendeu que a regulação de IA deveria focar em resultados, não em métodos.

### 3. Análises superficiais com gerúndio como muleta de coesão

**Palavras de alerta:** destacando/ressaltando/enfatizando..., garantindo..., refletindo/simbolizando..., contribuindo para..., cultivando/fomentando..., abrangendo..., evidenciando...

**Problema:** chatbots de IA grudam orações no gerúndio para simular profundidade, sem descrever ação real.

**Antes:**
> A paleta de cores azul, verde e dourado do templo ressoa com a beleza natural da região, simbolizando as flores nativas do cerrado, o rio São Francisco e as diversas paisagens do sertão, refletindo a profunda conexão da comunidade com a terra.

**Depois:**
> O templo usa as cores azul, verde e dourado. O arquiteto disse que a escolha remete às flores nativas do cerrado e ao rio São Francisco.

### 4. Linguagem promocional e de propaganda

**Palavras de alerta:** conta com um, vibrante, rico (figurado), profundo, potencializando seu, evidenciando, exemplifica, compromisso com, beleza natural, aninhado, no coração de, revolucionário (figurado), renomado, de tirar o fôlego, imperdível, deslumbrante

**Problema:** LLMs têm sérios problemas para manter um tom neutro, especialmente em temas de "patrimônio cultural".

**Antes:**
> Aninhada na deslumbrante região da Chapada dos Veadeiros, Alto Paraíso é uma cidade vibrante, com um rico patrimônio cultural e uma beleza natural de tirar o fôlego.

**Depois:**
> Alto Paraíso é uma cidade na Chapada dos Veadeiros, em Goiás, conhecida por sua feira semanal e pela igreja do século XIX.

### 5. Atribuições vagas e "weasel words"

**Palavras de alerta:** relatórios do setor, observadores apontam, especialistas argumentam, alguns críticos afirmam, várias fontes/publicações (quando poucas são citadas)

**Problema:** chatbots de IA atribuem opiniões a autoridades vagas sem fontes específicas.

**Antes:**
> Devido às suas características únicas, o rio Doce desperta o interesse de pesquisadores e ambientalistas. Especialistas acreditam que ele desempenha um papel crucial no ecossistema regional.

**Depois:**
> O rio Doce abriga várias espécies de peixes endêmicas, segundo um levantamento de 2019 do Instituto Chico Mendes.

### 6. Seções tipo esboço de "Desafios e perspectivas futuras"

**Palavras de alerta:** apesar de sua... enfrenta diversos desafios..., apesar desses desafios, desafios e legado, perspectivas futuras

**Problema:** muitos artigos gerados por LLM incluem seções formulaicas de "Desafios".

**Antes:**
> Apesar da prosperidade industrial, a cidade enfrenta desafios típicos de áreas urbanas, incluindo congestionamento e escassez hídrica. Apesar desses desafios, com sua localização estratégica e iniciativas em andamento, a cidade continua a prosperar como parte integral do crescimento da região.

**Depois:**
> O congestionamento aumentou depois de 2015, quando três novos parques industriais foram inaugurados. A prefeitura iniciou um projeto de drenagem pluvial em 2022 para lidar com as enchentes recorrentes.

## PADRÕES DE LINGUAGEM E GRAMÁTICA

### 7. Palavras de "vocabulário de IA" usadas em excesso

**Palavras de alta frequência em IA (PT):** robusto, assertivo, engajamento, protagonismo, propósito, jornada, potencializar, sinergia, transformador, disruptivo, aprofundar, essencial, fundamental, crucial, panorama, cenário, ecossistema, empoderar, catalisador, alavancar, ressignificar

**Problema:** essas palavras aparecem com frequência muito maior em textos gerados por IA em português, geralmente coocorrendo na mesma frase.

**Antes:**
> Além disso, é fundamental destacar que a jornada de transformação digital exige um ecossistema robusto, capaz de potencializar sinergias e empoderar equipes em sua busca por protagonismo no mercado.

**Depois:**
> A transformação digital só funciona quando as equipes têm autonomia real para tomar decisões, não apenas acesso a novas ferramentas.

### 8. Evitar "é/são" (evitar a cópula)

**Palavras de alerta:** serve como/configura-se como/representa, conta com/oferece/apresenta

**Problema:** LLMs substituem cópulas simples por construções elaboradas.

**Antes:**
> A Galeria 825 configura-se como o espaço de exposições de arte contemporânea da LAAA. A galeria conta com quatro espaços distintos e oferece mais de 300 metros quadrados.

**Depois:**
> A Galeria 825 é o espaço de exposições de arte contemporânea da LAAA. A galeria tem quatro salas, somando 300 metros quadrados.

### 9. Paralelismos negativos e negações finais ("tailing negations")

**Problema:** construções como "Não só... mas..." ou "Não se trata apenas de..., é..." são usadas em excesso, muitas vezes como calque direto do inglês, soando ainda mais artificial em PT. O mesmo vale para fragmentos de negação colados no final da frase em vez de escritos como oração de verdade.

**Antes:**
> Não se trata apenas da batida por trás dos vocais; faz parte da agressividade e da atmosfera. Não é apenas uma música, é uma declaração.

**Depois:**
> A batida pesada reforça o tom agressivo da faixa.

**Antes (negação final):**
> As opções vêm do item selecionado, sem necessidade de adivinhação.

**Depois:**
> As opções vêm do item selecionado, então o usuário não precisa adivinhar.

### 10. Uso excessivo da "regra de três"

**Problema:** LLMs forçam ideias em grupos de três para parecerem abrangentes.

**Antes:**
> O evento conta com palestras principais, painéis de discussão e oportunidades de networking. Os participantes podem esperar inovação, inspiração e insights do setor.

**Depois:**
> O evento tem palestras e painéis, além de um tempo livre para conversas informais entre as sessões.

### 11. Variação elegante (ciclagem de sinônimos)

**Problema:** a IA tem uma penalidade de repetição embutida que causa substituição excessiva de sinônimos.

**Antes:**
> O protagonista enfrenta muitos desafios. O personagem principal precisa superar obstáculos. A figura central eventualmente triunfa. O herói retorna para casa.

**Depois:**
> O protagonista enfrenta muitos desafios, mas eventualmente triunfa e volta para casa.

### 12. Faixas falsas ("de X a Y")

**Problema:** LLMs usam construções "de X a Y" quando X e Y não estão numa escala com sentido real.

**Antes:**
> Nossa jornada pelo universo nos levou da singularidade do Big Bang à grande teia cósmica, do nascimento e morte das estrelas à dança enigmática da matéria escura.

**Depois:**
> O livro aborda o Big Bang, a formação das estrelas e as teorias atuais sobre matéria escura.

### 13. Voz passiva e fragmentos sem sujeito

**Problema:** LLMs frequentemente escondem o agente ou omitem o sujeito por completo, com frases como "Nenhum arquivo de configuração é necessário" ou "Os resultados são preservados automaticamente." Reescreva quando a voz ativa deixar a frase mais clara e direta.

**Antes:**
> Nenhum arquivo de configuração é necessário. Os resultados são preservados automaticamente.

**Depois:**
> Você não precisa de um arquivo de configuração. O sistema preserva os resultados automaticamente.

## PADRÕES DE ESTILO

### 14. Travessões longos (—): corte-os

**Regra:** a reescrita final não contém travessões longos (—) nem meios-travessões (–) usados como pontuação de aparte. O travessão longo é um dos indícios mais confiáveis de IA, inclusive em português, onde é usado com muito mais frequência pela IA do que por escritores humanos comuns. Trate isso como restrição rígida, não como preferência de "usar com moderação". Substitua cada um, em ordem de preferência: um ponto (nova frase), uma vírgula (aparte curto), dois-pontos (introduzindo explicação), parênteses (aparte de verdade), ou reestruture a frase.

**Antes:**
> O termo é promovido principalmente por instituições holandesas — não pelas próprias pessoas. Ninguém diz "Holanda, Europa" como endereço — ainda assim, esse erro de rotulação continua — até em documentos oficiais.

**Depois:**
> O termo é promovido principalmente por instituições holandesas, não pelas próprias pessoas. Ninguém diz "Holanda, Europa" como endereço, ainda assim esse erro de rotulação continua, inclusive em documentos oficiais.

**Antes:**
> A nova política — anunciada sem aviso prévio — afeta milhares de trabalhadores. As mudanças -- já esperadas havia tempo, segundo críticos -- entrarão em vigor imediatamente.

**Depois:**
> A nova política, anunciada sem aviso prévio, afeta milhares de trabalhadores. As mudanças, já esperadas havia tempo segundo críticos, entrarão em vigor imediatamente.

Antes de entregar a reescrita final, escaneie-a em busca de `—` e `–`. Qualquer ocorrência significa que o rascunho não está pronto.

### 15. Uso excessivo de negrito

**Problema:** chatbots de IA colocam frases em negrito mecanicamente.

**Antes:**
> A estratégia combina **OKRs (Objetivos e Resultados-Chave)**, **KPIs (Indicadores-Chave de Performance)** e ferramentas visuais como o **Business Model Canvas (BMC)** e o **Balanced Scorecard (BSC)**.

**Depois:**
> A estratégia combina OKRs, KPIs e ferramentas visuais como o Business Model Canvas e o Balanced Scorecard.

### 16. Listas verticais com cabeçalho inline

**Problema:** a IA produz listas em que os itens começam com cabeçalhos em negrito seguidos de dois-pontos.

**Antes:**
> - **Experiência do usuário:** A experiência do usuário foi significativamente melhorada com uma nova interface.
> - **Performance:** A performance foi aprimorada por meio de algoritmos otimizados.
> - **Segurança:** A segurança foi reforçada com criptografia de ponta a ponta.

**Depois:**
> A atualização melhora a interface, acelera o carregamento com algoritmos otimizados e adiciona criptografia de ponta a ponta.

### 17. Title Case em títulos (capitalização de todas as palavras)

**Problema:** chatbots de IA capitalizam todas as palavras principais em títulos, seguindo a convenção do inglês, o que não é o padrão em português.

**Antes:**
> ## Negociações Estratégicas E Parcerias Globais

**Depois:**
> ## Negociações estratégicas e parcerias globais

### 18. Emojis

**Problema:** chatbots de IA costumam decorar títulos ou marcadores com emojis.

**Antes:**
> 🚀 **Fase de Lançamento:** O produto é lançado no terceiro trimestre
> 💡 **Insight-chave:** Os usuários preferem simplicidade
> ✅ **Próximos Passos:** Agendar reunião de acompanhamento

**Depois:**
> O produto é lançado no terceiro trimestre. A pesquisa com usuários mostrou preferência por simplicidade. Próximo passo: agendar uma reunião de acompanhamento.

### 19. Aspas curvas (curly quotes)

**Problema:** o ChatGPT usa aspas curvas ("...") em vez de aspas retas ("...").

**Antes:**
> Ele disse "o projeto está no prazo", mas outros discordaram.

**Depois:**
> Ele disse "o projeto está no prazo", mas outros discordaram.

## PADRÕES DE COMUNICAÇÃO

### 20. Artefatos de comunicação colaborativa

**Palavras de alerta:** espero que isso ajude, claro!, com certeza!, você está certíssimo!, gostaria que..., quer que eu...?, quer que eu dê exemplos?, devo continuar?, me avise, aqui está um/uma...

**Problema:** texto pensado como correspondência de chatbot acaba colado como conteúdo final.

**Antes:**
> Aqui está uma visão geral da Revolução Francesa. Espero que isso ajude! Me avise se quiser que eu expanda alguma seção.

**Depois:**
> A Revolução Francesa começou em 1789, quando a crise financeira e a escassez de alimentos provocaram uma onda generalizada de agitação social.

### 21. Disclaimers de corte de conhecimento e preenchimento especulativo de lacunas

**Palavras de alerta:** até [data], até minha última atualização, embora detalhes específicos sejam escassos..., com base nas informações disponíveis, não disponível publicamente, mantém um perfil discreto, preserva sua vida pessoal, prefere ficar fora dos holofotes, provavelmente [cresceu/estudou/começou], acredita-se que

**Problema:** dois indícios relacionados. (a) Modelos mais antigos deixam disclaimers de corte de conhecimento no texto. (b) Quando um modelo não encontra uma fonte, ele escreve um parágrafo *sobre* não encontrar uma fonte e depois inventa preenchimento plausível para cobrir a lacuna. Para uma pessoa privada, o "chute" quase sempre recai nas mesmas frases padronizadas ("mantém um perfil discreto", "preserva sua vida pessoal"), nada disso com fonte. Diga o que não se sabe, ou corte a frase; não vista um palpite de fato.

**Antes (disclaimer de corte):**
> Embora detalhes específicos sobre a fundação da empresa não sejam amplamente documentados em fontes disponíveis, ela parece ter sido criada em algum momento dos anos 1990.

**Depois:**
> A empresa foi fundada em 1994, segundo seus documentos de registro.

**Antes (preenchimento especulativo):**
> Informações sobre sua infância não estão disponíveis publicamente, o que sugere que ela mantém um perfil discreto e preserva detalhes de sua vida pessoal. Provavelmente cresceu em uma família de classe média, o que moldou seu interesse posterior por reforma educacional.

**Depois:**
> Não há registros disponíveis sobre sua infância. (Ou omita a seção.)

### 22. Tom sicofante/servil

**Problema:** linguagem excessivamente positiva e agradadora.

**Antes:**
> Ótima pergunta! Você está certíssimo de que esse é um tema complexo. Esse é um excelente ponto sobre os fatores econômicos.

**Depois:**
> Os fatores econômicos que você mencionou são relevantes aqui.

## PREENCHIMENTO E HEDGING

### 23. Frases de preenchimento

**Antes → Depois:**

- "A fim de atingir esse objetivo" → "Para atingir isso"
- "Devido ao fato de que estava chovendo" → "Porque estava chovendo"
- "Neste momento" / "No momento atual" → "Agora"
- "Na eventualidade de você precisar de ajuda" → "Se precisar de ajuda"
- "O sistema tem a capacidade de processar" → "O sistema processa"
- "É importante notar que os dados mostram" → "Os dados mostram"

### 24. Hedging excessivo

**Problema:** qualificar afirmações em excesso, empilhando ressalvas.

**Antes:**
> Poderia potencialmente se argumentar que a política talvez tenha algum efeito sobre os resultados.

**Depois:**
> A política pode afetar os resultados.

### 25. Conclusões positivas genéricas

**Problema:** finais animados e vagos, sem informação nova.

**Antes:**
> O futuro é promissor para a empresa. Tempos empolgantes estão por vir, à medida que ela continua sua jornada rumo à excelência. Isso representa um grande passo na direção certa.

**Depois:**
> A empresa planeja abrir mais duas unidades no próximo ano.

### 26. Travessão (—): o maior tell de IA em português, e é para ser eliminado sem dó

**Problema:** o travessão longo é, isoladamente, o indício mais confiável de texto gerado por IA em português. Escritores humanos em PT raramente usam esse caractere; a maioria nem sabe digitá-lo (é um caractere Unicode específico, não está no teclado padrão). Quando ele aparece com frequência num texto, é quase sempre porque o texto passou por um modelo de IA. Trate qualquer travessão como erro a corrigir, não como estilo a preservar. A ordem de substituição é sempre: ponto final (nova frase) → vírgula (aparte curto) → dois-pontos (introduz explicação) → parênteses (aparte de verdade). Nunca deixe o travessão sobreviver à revisão final.

**Exemplo 1 — substituir por vírgula (aparte curto):**

**Antes:**
> O relatório — enviado com dois dias de atraso — ainda assim foi bem recebido pela diretoria.

**Depois:**
> O relatório, enviado com dois dias de atraso, ainda assim foi bem recebido pela diretoria.

**Exemplo 2 — substituir por dois-pontos (quando introduz uma explicação ou consequência):**

**Antes:**
> A decisão foi simples — cortar o canal que não convertia.

**Depois:**
> A decisão foi simples: cortar o canal que não convertia.

**Exemplo 3 — substituir por parênteses (quando é um aparte genuíno, dispensável à frase principal):**

**Antes:**
> O CAC subiu 30% no trimestre — número que pegou o time de growth de surpresa — e forçou uma revisão do mix de canais.

**Depois:**
> O CAC subiu 30% no trimestre (número que pegou o time de growth de surpresa) e forçou uma revisão do mix de canais.

### 27. Truques retóricos de autoridade persuasiva

**Frases de alerta:** a verdadeira questão é, no fundo, na realidade, o que realmente importa, fundamentalmente, a questão mais profunda, o cerne da questão

**Problema:** LLMs usam essas frases para fingir que estão cortando o ruído até chegar a alguma verdade mais profunda, quando a frase que se segue geralmente só repete um ponto comum com cerimônia extra.

**Antes:**
> A verdadeira questão é se as equipes conseguem se adaptar. No fundo, o que realmente importa é a prontidão organizacional.

**Depois:**
> A questão é se as equipes conseguem se adaptar. Isso depende principalmente de a organização estar disposta a mudar seus hábitos.

### 28. Sinalização e anúncios ("vamos explorar isso")

**Frases de alerta:** vamos mergulhar nisso, vamos explorar, vamos detalhar, aqui está o que você precisa saber, agora vamos analisar, sem mais delongas

**Problema:** LLMs anunciam o que vão fazer em vez de simplesmente fazer. Essa meta-comunicação deixa o texto mais lento e dá uma sensação de "roteiro de tutorial".

**Antes:**
> Vamos mergulhar em como funciona o cache no Next.js. Aqui está o que você precisa saber.

**Depois:**
> O Next.js armazena dados em cache em várias camadas, incluindo memoização de requisições, o cache de dados e o cache de roteamento.

### 29. Títulos fragmentados

**Sinais de alerta:** um título seguido de um parágrafo de uma linha que apenas repete o título antes do conteúdo real começar.

**Problema:** LLMs costumam adicionar uma frase genérica depois de um título como "aquecimento" retórico. Geralmente não acrescenta nada e dá sensação de enchimento ao texto.

**Antes:**
> ## Performance
>
> Velocidade importa.
>
> Quando os usuários encontram uma página lenta, eles saem.

**Depois:**
> ## Performance
>
> Quando os usuários encontram uma página lenta, eles saem.

### 30. Escrita ancorada em diff

**Problema:** documentação ou comentários escritos como se estivessem narrando uma mudança, em vez de descrever a coisa como ela é. A menos que o documento seja inerentemente vinculado a uma versão (changelogs, release notes, guias de migração), ele deve fazer sentido sem que se saiba o que mudou no último commit.

**Antes:**
> Essa função foi adicionada para substituir a abordagem anterior, que iterava por todos os itens e causava desempenho O(n²).

**Depois:**
> Essa função usa uma tabela hash para buscas O(1), evitando o custo O(n²) da iteração ingênua.

### 31. Frases de efeito manufaturadas e drama em staccato

**Problema:** LLMs frequentemente fazem toda frase soar como uma citação de efeito, e empilham fragmentos declarativos curtos para manufaturar drama. Uma única frase curta para dar ênfase é aceitável; uma sequência delas começa a soar artificial.

**Antes:**
> Então o AlphaEvolve chegou. Sem preferência por simetria. Sem viés estético prévio. Sem nostalgia pelo gosto humano. As regras antigas tinham acabado.

**Depois:**
> O AlphaEvolve mudou a forma de busca porque não favorecia simetria nem designs com aparência humana. Isso tornou algumas suposições antigas menos úteis.

### 32. Fórmulas de aforismo

**Palavras de alerta:** X é o Y do Z, X vira uma armadilha, X não é uma ferramenta, é um espelho, a linguagem de, a moeda de, a arquitetura de

**Problema:** LLMs transformam afirmações comuns em aforismos reutilizáveis que soam profundos sem acrescentar precisão. Substitua a fórmula pela afirmação concreta a que ela está se referindo.

**Antes:**
> Simetria é a linguagem da confiança. Eficiência vira uma armadilha quando as equipes esquecem a camada humana.

**Depois:**
> Layouts simétricos costumam parecer mais previsíveis para os usuários. Equipes podem otimizar demais os fluxos de trabalho e perder de vista como as pessoas realmente os usam.

### 33. Aberturas retóricas conversacionais

**Frases de alerta:** sinceramente?, olha, a questão é a seguinte, sejamos honestos, direto ao ponto, quando usadas como ganchos isolados ou pausas de falsa sinceridade antes de um ponto comum.

**Problema:** LLMs abrem com um gancho de falsa sinceridade para simular intimidade antes de entregar uma afirmação rotineira. O indício é a pausa-e-revelação teatral: uma pergunta ou aparte curto, seguido da "resposta real". Uma pessoa sendo honesta geralmente só diz a coisa direto.

**Antes:**
> Vale o preço? Sinceramente? Depende de quanto você vai usar.

**Depois:**
> Se vale o preço depende de quanto você vai usar.

### 34. Escalada de reframe ("Não é só X, é Y")

**Problema:** reenquadra a afirmação anterior como maior ou mais profunda do que ela realmente é, numa escalada retórica que não acrescenta informação nova.

**Antes:**
> Essa não é só uma atualização de funcionalidade, é uma reformulação completa de como o usuário se relaciona com os dados.

**Depois:**
> Essa atualização muda como os filtros se aplicam a tabelas aninhadas.

### 35. Falso paralelismo binário ("É menos sobre X, mais sobre Y")

**Problema:** cria uma dicotomia artificial entre dois conceitos para soar analítico, quando na prática os dois fatores importam de formas diferentes e a frase só embeleza o ponto.

**Antes:**
> O sucesso aqui é menos sobre talento e mais sobre consistência.

**Depois:**
> Nesse grupo, quem manteve uma rotina constante teve resultado melhor do que quem só contava com talento.

### 36. Meta-referência ao próprio raciocínio ("Vamos desconstruir isso", "Dando um passo atrás")

**Problema:** LLMs sinalizam que vão analisar em vez de simplesmente analisar. É a versão "analítica" do item 28 (sinalização e anúncios): em vez de anunciar uma ação, anuncia um raciocínio.

**Antes:**
> Vamos desconstruir isso. Dando um passo atrás, o panorama geral aqui é que o mercado recompensa velocidade.

**Depois:**
> O mercado recompensa velocidade porque quem chega primeiro captura o canal de distribuição.

### 37. "Numbered insight" framing genérico ("Aqui estão 3 coisas que...")

**Problema:** listas numeradas em que os itens são abstrações vazias, não achados concretos. O problema não é o número em si, é a lista existir só para parecer estruturada, sem que cada item carregue um dado, fato ou ação específica.

**Antes:**
> Aqui estão 3 coisas que separam empresas que escalam das que estagnam: foco, execução e consistência.

**Depois:**
> Empresas que escalam cortam produto antes de escalar distribuição. As que estagnam tentam vender tudo para todo mundo ao mesmo tempo.

## ORIENTAÇÃO DE DETECÇÃO

### O que NÃO sinalizar (falsos positivos)

Um escritor humano "limpo" pode acertar vários dos padrões acima sem qualquer envolvimento de IA. Antes de reescrever, confira que você não está destruindo uma prosa legítima. O seguinte NÃO é um indicador confiável isoladamente:

- **Gramática perfeita e estilo consistente.** Muitos escritores são profissionais ou foram revisados. Polimento não é sinônimo de IA.
- **Registros casual e formal misturados.** Isso geralmente indica alguém de área técnica, um escritor jovem, ou alguém com hábitos de escrita neurodivergentes, não um chatbot.
- **Prosa "sem graça" ou "robótica".** A prosa de IA tem indícios *específicos*. Secura genérica sem esses indícios é só escrita seca.
- **Vocabulário formal ou acadêmico.** A IA usa em excesso palavras *específicas* (ver item 7), não qualquer palavra rebuscada. Não simplifique "ostensivamente" ou "constituinte" só porque soam eruditas.
- **Abertura ou fechamento em estilo carta num comentário.** Saudações e despedidas são anteriores ao ChatGPT em séculos.
- **Palavras de transição comuns isoladas.** *Além disso*, *ademais*, *consequentemente* só são indício de IA quando empilhadas. Um único "porém" não é sinal.
- **Aspas curvas isoladas.** macOS, Word, Google Docs e a maioria dos CMS curvam aspas automaticamente por padrão. Aspas curvas só contam quando aparecem junto com outros indícios.
- **Travessão longo isolado.** Muitos editores e jornalistas os usam com frequência. O travessão só é evidência quando combinado com um ritmo formulaico e "vendedor".
- **Uma única frase curta e enfática.** Humanos usam frases cortadas para reforçar um ponto. Sinalize drama em staccato só quando vários fragmentos curtos aparecem em sequência e inflam o tom.
- **"Sinceramente" ou "olha" no meio da frase.** São comuns na escrita casual. O indício é a abertura teatral isolada, não a palavra em si.
- **Afirmações sem fonte.** A maior parte da web não tem fonte citada. Falta de citação não prova nada.
- **Formatação correta e complexa.** Editores visuais e templates produzem saída limpa sem qualquer IA envolvida.
- **Texto de segunda mão.** Não reescreva frases-alvo dentro de citações, títulos, nomes próprios ou exemplos em que a frase está sendo discutida, não usada.

Na dúvida, procure **agrupamentos** de indícios, não indícios isolados. Um único travessão não significa nada; travessões junto com regra de três, mais "tapeçaria vibrante" e uma seção "Conclusão" é uma confissão.

### Sinais de escrita humana (preserve-os)

Quando você ver isso, tenda a deixar a prosa em paz. São evidências de uma pessoa real escrevendo, e edição excessiva vai destruir o que torna o texto humano:

- **Detalhe específico, incomum, difícil de fabricar.** Um endereço real. Uma citação estranha. A frase "o advogado que trabalhava no andar de cima do meu dentista". LLMs arredondam especificidades; humanos as acumulam.
- **Sentimentos mistos e tensão não resolvida.** "Acho que isso é bom na maior parte, mas me incomoda, e não consigo explicar totalmente por quê." LLMs vão por padrão para conclusões limpas.
- **Referências datadas, presas a uma época.** Gírias, memes ou piadas internas que remetem a um ano e subcultura específicos. Modelos ficam pelo menos um ano atrasados.
- **Escolhas editoriais em primeira pessoa que o escritor consegue defender.** Se o escritor consegue explicar *por que* fez determinado corte ou usou determinada palavra, isso é um forte sinal humano.
- **Variedade no comprimento das frases.** Escrita real alterna frases curtas e longas. Escrita de IA tende a uma cadência uniforme, de comprimento médio.
- **Apartes genuínos, parênteses ou autocorreções.** "(Fico querendo dizer 'quase' aqui, mas realmente foi certo.)" Modelos raramente se interrompem assim.
- **Edições feitas antes de 30 de novembro de 2022.** Lançamento público do ChatGPT. Qualquer coisa anterior a isso, salvo raras exceções, não é escrita por IA.

---

## Processo e resultado

1. Leia o texto de entrada com cuidado e identifique cada instância dos padrões acima.
2. Escreva um **rascunho de reescrita**. Verifique se soa natural em voz alta, varia o comprimento das frases, prefere detalhes específicos e construções simples (é/são/tem), e mantém o registro apropriado.
3. Pergunte: **"O que torna o texto abaixo tão obviamente gerado por IA?"** Responda brevemente com os indícios remanescentes.
4. Revise para uma **reescrita final** que resolva esses pontos e não contenha travessões longos ou meios-travessões (ver item 14).

Entregue o rascunho, os pontos "ainda parece IA", a reescrita final e (opcionalmente) um resumo curto das mudanças.

## Exemplo completo

**Antes (soa como IA):**
> Recentemente passei cinco dias inesquecíveis em Lisboa, e deixa eu te contar: essa cidade roubou completamente meu coração. Desde o momento em que cheguei, eu soube que estava em um lugar verdadeiramente especial.
>
> Aninhada às margens do rio Tejo, Lisboa é um vibrante testemunho do espírito duradouro de Portugal, onde a rica história e a energia moderna se entrelaçam a cada esquina. Sim, as famosas ladeiras são desafiadoras (minhas pernas certamente sentiram isso!), mas cada subida recompensa você com vistas panorâmicas de tirar o fôlego que fazem tudo valer a pena.
>
> Nenhuma viagem estaria completa sem andar no icônico Elétrico 28, serpenteando pelos bairros mais históricos da cidade. E a comida? Simplesmente divina. Os pastéis de nata originais da Pastéis de Belém são um tesouro nacional amado, e saboreá-los ainda quentes foi um momento que jamais vou esquecer.
>
> Mas o que realmente torna Lisboa especial não são só as paisagens: é a sensação. Ande alguns passos longe das praças principais e você vai descobrir um lado mais quieto e autêntico: vielas banhadas de sol, fachadas charmosas de azulejos e moradores simpáticos seguindo sua rotina diária, convidando você a desacelerar e aproveitar cada momento.
>
> É claro, o imperdível Castelo de São Jorge oferece vistas deslumbrantes sobre os telhados abaixo. As filas podem ser longas, mas a experiência vale totalmente a pena para qualquer entusiasta de história ou viajante curioso.
>
> Eu voltaria? Com certeza. Lisboa não é só um lugar para visitar: é um lugar para se apaixonar, de novo e de novo. Se você está sonhando com sua próxima viagem, este é um destino que promete memórias para durar a vida toda. ✨

**Rascunho de reescrita:**
> Passei cinco dias em Lisboa em outubro passado e ainda estou meio dividido sobre a experiência. A cidade é bonita, mas também é mais cansativa do que eu esperava.
>
> As ladeiras não são um detalhe qualquer. Meu hotel ficava na Alfama, que fica ótima nas fotos e significava subir uma escadaria longa toda vez que eu queria um café. No segundo dia eu já estava planejando os trajetos pensando em qual direção era ladeira abaixo.
>
> Andei no Elétrico 28 porque todo mundo diz para andar no Elétrico 28. Estava lotado, lento e cheio de gente filmando as mesmas esquinas. Os doces foram melhores. Comi um pastel de nata quentinho na Graça que valeu o hype.
>
> A parte de que mais gostei foi longe das praças principais: roupa no varal, azulejo, janelas abertas e gente assistindo futebol em cafés pequenos. A vista do castelo era boa, mas a fila era longa demais para o que valia.
>
> Eu voltaria, mas na primavera e com sapatos melhores.

**O que torna o texto abaixo tão obviamente gerado por IA?**

- O rascunho é comprimido demais em relação ao original; ele apaga textura em vez de reescrevê-la.
- Algumas frases ainda explicam o ponto de forma limpa demais ("A cidade é bonita, mas...").
- O fechamento é plano e genérico em vez de um encerramento real na mesma voz.

**Agora torne menos óbvio que é IA.**
> Passei cinco dias em Lisboa em outubro passado e ainda tenho sentimentos misturados sobre a viagem. Bonita, sim. Também mais dura para os joelhos do que qualquer um me avisou.
>
> As ladeiras são a história inteira e, de alguma forma, nunca aparecem nos folhetos. Meu hotel ficava lá em cima, na Alfama, que fica linda nas fotos e se traduz, na prática, em subir o equivalente a seis andares de escada toda vez que eu queria um café. No segundo dia minhas panturrilhas já tinham opinião formada sobre o assunto. Comecei a planejar cada caminhada em função de qual lado era ladeira abaixo, o que é uma forma estranha de conhecer uma cidade, mas provavelmente honesta.
>
> Todo mundo diz para andar no Elétrico 28, então andei, espremido contra a mochila de um estranho por quarenta minutos enquanto três grupos de turistas filmavam a mesma esquina. Da próxima vez eu faria o trajeto a pé, ou iria antes do café da manhã. Os pastéis de nata, porém, merecem o alvoroço todo. Comi um numa lojinha simples na Graça, ainda quente, e por uns trinta segundos entendi por que as pessoas organizam viagens em torno de doce.
>
> O que eu não esperava era o quanto a cidade fica silenciosa longe das praças principais. Duas quadras ladeira acima de qualquer praça e vira varal de roupa, azulejo lascado, janela aberta e senhores assistindo futebol com o som no talo. É essa a Lisboa em que fico pensando, não o castelo.
>
> O castelo é ok. A vista é ótima, a fila é longa, e passei mais tempo andando na fila do que olhando qualquer coisa depois que entrei. Se eu tivesse só dois dias, trocaria por uma tarde de me perder pela cidade.
>
> Eu voltaria, mas na primavera e com sapatos melhores. Lisboa não faz força nenhuma para facilitar as coisas para você. Acho que gostei disso, mesmo quando minhas pernas discordavam.

**Mudanças feitas:** manteve o relato de viagem em primeira pessoa e aproximadamente o mesmo nível de detalhe, mas removeu a estrutura de chatbot, a inflação de significância, a linguagem promocional, o entusiasmo forçado, os travessões longos, a cadência de regra de três, a conclusão positiva genérica e o emoji. Reconstruiu o texto em torno de fricção concreta, sentimentos mistos, ritmo irregular e cenas específicas.

## Referência

Este skill é baseado em [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantido pelo WikiProject AI Cleanup. Os padrões documentados ali vêm de observações de milhares de instâncias de texto gerado por IA na Wikipédia.

Insight-chave da Wikipédia: "LLMs usam algoritmos estatísticos para adivinhar o que deve vir a seguir. O resultado tende para o resultado estatisticamente mais provável que se aplica à maior variedade de casos possível."

---

## Registro de decisões de adaptação (validado)

1. **Item 2 (fontes citadas):** ajustado para veículos brasileiros: IstoÉ, Veja, O Globo, Folha de S.Paulo, Estadão.
2. **Itens 4 e 6 (topônimos):** mantidos os exemplos adaptados (Chapada dos Veadeiros / cidade genérica brasileira) em vez dos originais da Wikipédia (Etiópia/Índia).
3. **Item 5 (rio e instituição):** mantidos "rio Doce" e "Instituto Chico Mendes".
4. **Item 17 (Title Case):** mantido como está, com a ressalva registrada de que é um tell mais raro em PT do que em inglês.
5. **Item 26:** reescrito do zero. Em vez do exemplo de hifenização (que não tinha equivalente direto em PT), o item agora reforça o travessão como o maior tell de IA em português, com três exemplos de substituição (vírgula, dois-pontos, parênteses).
6. **Itens 34–37 (novos):** integrados diretamente à lista principal, na sequência dos padrões de estilo/comunicação do documento original: escalada de reframe, falso paralelismo binário, meta-referência ao próprio raciocínio e "numbered insight" framing genérico. Todos com exemplos construídos direto em PT.
