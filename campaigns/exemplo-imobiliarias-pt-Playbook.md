# Playbook — Imobiliárias Internacionais em Portugal

Documento mestre da campanha. Guia conteúdo, ads e outbound como uma única máquina — nenhuma subpasta (`Conteudo/`, `Ads/`, `Outbound/`, `Signals/`, `Scripts/`) deve divergir do que está aqui.

## ICP

Imobiliárias em Portugal que atendem comprador estrangeiro — sinal técnico: site multi-idioma (hreflang em 3+ línguas: en, fr, de, es, nl, it, sv, zh), listagem ativa de imóveis, geralmente segmento médio-alto/luxo (Algarve, Lisboa, Porto, Quinta do Lago). Fonte de verdade: `Signals/lote_835/resultados.csv` (753 domínios scrapeados) + `Signals/resultados.csv` (11 contas priorizadas/qualificadas manualmente).

Dor comum identificada no scraping (coluna "Ângulo de abordagem" do CSV): consultores sobrecarregados com triagem manual de lead internacional, tempo de resposta lento pra quem está em fuso diferente, equipe pequena vs. volume de imóveis listados.

## Oferta

Não é serviço genérico de geração de demanda. É um **artefato 1:1**: uma landing page personalizada para cada imobiliária, com um agente de IA embutido treinado no próprio catálogo/site dela (dados já extraídos no scraping), capaz de qualificar e responder o comprador internacional 24/7 em múltiplos idiomas.

O artefato é a prova, mas construído sob demanda — não em massa. A copy de outbound anuncia que já foi criado um artefato específico pra empresa (claim como quebra-gelo), mas o build de fato só acontece **quando o lead responde**: nesse momento entregamos uma prévia, e o artefato completo (com treinamento do time e handoff) é apresentado ao vivo na reunião. Isso substitui o material rico genérico (ebook/quiz) desse CLAUDE.md pra essa campanha específica: aqui o material rico é personalizado por conta e construído just-in-time, não distribuído em massa.

Escopo completo da entrega (o que é vendido na call de 20min): montar a estrutura completa (site + agente), **treinar o time interno** da imobiliária pra operar/manter, e entregar pronto na mão deles — não é um serviço gerenciado recorrente, é handoff. Por isso todo lead qualificado precisa ser avaliado quanto a ter um **champion interno** capaz de absorver as demandas de "vibe coding" e ser treinado — sem esse champion, o handoff não se sustenta pós-entrega.

## Dados e Filtros da Base

Log do processo de filtragem que parte da base bruta de scraping (`Signals/lote_835/resultados.csv`, 753 domínios) até a lista final de prospects trabalhada em outbound. Cada passo documentado aqui pra manter rastreável por que um domínio/contato entrou ou saiu da lista.

**Passo 1 — priorização de domínios + remoção de redes grandes**
- Partiu dos 753 domínios da base bruta → selecionados **500 domínios**, priorizando os marcados como internacional (`Internacional = Sim`) e com imóveis listados (`Imoveis listados = Sim`).
- Removidos domínios/membros de grandes redes internacionais — **Engel & Völkers, Corcoran Group e The Agency RE** — porque cada uma tinha volume excessivo de membros no LinkedIn, poluindo a lista de prospects (não é o perfil de agência pequena/média que a oferta 1:1 serve bem, e distorcia a proporção da amostra).
- Resultado: **594 prospects** (contatos de LinkedIn, não domínios — o número sobe em relação aos 500 domínios porque cada domínio pode ter múltiplos membros elegíveis).
- Arquivo: `Imobiliárias PT - Leads 1 - raw.csv`

**Passo 2 — filtro geográfico + enriquecimento de perfil via Apify**
- Filtro: mantidos leads com País na região Europa (ISO) + Brasil (exceção explícita por afinidade cultural, não geográfica) — Turquia e Cazaquistão tratados como fora (transcontinentais, maioria do território na Ásia). Critério validado com o usuário em 2026-07-08.
- Resultado do filtro: **594 → 524 prospects** mantidos (70 removidos — principais países fora: EUA, África do Sul, Turquia, EAU, Canadá, China, Índia, Cazaquistão, Paquistão, Catar, Uruguai, Angola, Argentina, Austrália).
- Enriquecimento: actor Apify `dev_fusion/linkedin-profile-scraper` rodado sobre os 524 (`linkedin_identifier` como input). Escolhido em vez de um actor alternativo mais barato que não retorna email/domínio de empresa — decisão de manter o atual porque o domínio da empresa (`companyWebsite`) é a chave de cruzamento confiável com `Empresa > Domínio` da base original; o alternativo só teria nome/slug de empresa (fuzzy match), enfraquecendo o cruzamento e o flag de desalinhamento.
- Campos adicionados por lead: `cargo_apify`, `headline_apify`, `empresa_atual_apify`, `sobre_apify`, `localizacao_apify`, `skills_apify`, `email_apify`, `telefone_apify`, `possivel_desalinhado`, `motivo_desalinhado`.
- **Sem posts/atividade recente do LinkedIn** — esse actor só faz enriquecimento de perfil, não de atividade. Decisão: seguir sem posts (não seria usado como "quebra-gelo" nessa campanha — ver `## Os 3 Pilares` acima, o quebra-gelo é o claim do artefato, não o post curtido).
- `possivel_desalinhado`: flag automático quando a indústria/empresa atual do lead no LinkedIn não bate com a empresa/setor original da base — sinaliza troca de emprego ou vínculo pessoa↔empresa errado na base bruta. Não remove ninguém, só marca pra revisão manual antes do outbound.

**Resultados do Passo 2 (rodado em 2026-07-08):**

| Métrica | Resultado |
|---|---|
| Base após Passo 1 | 524 leads |
| Enriquecidos via Apify | 499/524 (95%) |
| Sem retorno (perfil privado/inválido) | 25 |
| Com email descoberto | 282/499 (57%) |
| Marcados `possivel_desalinhado` | 38/499 (8%) — revisar `motivo_desalinhado` antes de entrar na cadência |

- Arquivo final: `Imobiliárias PT - Leads 1 - treated.csv`
- Script: `Scripts/enrich_leads.py` (venv isolado em `Scripts/.venv`, key em `Scripts/.env` — nunca no venv, ver padrão em `Scripts/`)

**Passo 3 — geração de copy personalizada 1:1 (rodado em 2026-07-08)**
- 10 leads-modelo validados manualmente pelo usuário (6 iterações) → regras consolidadas em `Outbound/copys-modelo-10-leads.md`: convite sem CTA (networking + afinidade + âncora local), FUP1 com claim do artefato + prova social ("cases de até 40% de conversão"), FUP2 com mecânica completa (qualifica, tira dúvidas, indica imóveis se `tem_listing=Sim`, agenda visita; site + WhatsApp + LinkedIn).
- Afinidade por área do lead (vendas/marketing/fundador/dados, ver `brand/background.md`) e âncora local (ex: mesma cidade, mesma ex-empresa, mesmo evento).
- Geração em escala: 12 subagentes por track de língua (9 PT, 2 EN, 1 ES) + QA determinístico (limite 300 chars, claim exato, regra de listing, termos proibidos). 451 leads gerados, 100% aprovados no QA.
- Estilos aplicados: #1 direto/vendas (235), #5 fundador-pra-fundador (158), #8 McKinsey/corporativo (58).
- Arquivo final: `Imobiliárias PT - Leads 1 - treated-final.csv` (524 linhas: 451 geradas + 10 modelos validados + 63 sem mensagem, marcadas com o motivo em `status_geracao`).

Passos seguintes serão adicionados aqui conforme o processo avança.

## Objetivo (60-90 dias)

Agendar reuniões/demos com decisores das imobiliárias. Não é campanha de awareness nem de fechamento imediato — é ABM de geração de pipeline via prova viva.

## Os 3 Pilares Aplicados a Essa Campanha

### 1. Sinal (Signals/) — já em andamento

Scraping identifica: idiomas do site, se é internacional, imóveis listados, breve descrição, ângulo de abordagem sugerido por IA. Próximo passo: **scoring/priorização** do lote de 753 contra os critérios abaixo antes de qualquer outbound.

Critérios de priorização (aplicar sobre `resultados.csv`):
- 4+ idiomas no site (sinal forte de operação internacional já madura)
- Catálogo de imóveis ativo e crawleável (senão não dá pra construir o agente rápido)
- Segmento médio-alto/luxo (ticket do imóvel correlaciona com orçamento pra ferramenta)
- Sem chatbot/IA visível no site atual (gap claro pra preencher)

### 2. Outbound (Outbound/) — canal primário

Motion:
1. Selecionar conta priorizada → disparar sequência de convite (LinkedIn) + email dizendo que visitamos o site e criamos um artefato que pode aumentar a conversão deles em até 30% (mais vendas). Nesse ponto o artefato **ainda não existe de fato** — a copy usa o claim como quebra-gelo, não como entrega.
2. Cadência máxima: **3 mensagens LinkedIn + 3 emails**. Sem resposta após isso, a conta cai pro pilar de conteúdo/ads como reforço passivo (sem downsell de evento nessa campanha — ver `#### Fluxo de Cadência`).
3. **Só quando o lead responde** é que o artefato é de fato construído (usando dados já extraídos em `Signals/lote_835/homes_html/`) e enviamos uma **prévia**, com a mensagem de que o artefato completo será apresentado na reunião.
4. CTA único: agendar 20min. A oferta da call é clara — vamos montar essa estrutura completa pra eles, treinar o time interno e entregar pronta na mão deles.
5. Antes de avançar pra call/proposta, checar se existe **champion interno** na imobiliária capaz de absorver as demandas de "vibe coding" e ser treinado — sem isso o handoff não se sustenta.

Scripts de outreach e sequência de follow-up vivem em `Scripts/` (a criar).

#### Ficha Operacional da Campanha

Campos padrão de toda campanha de outbound do usuário (preencher antes do primeiro disparo):

| Campo | Definição pra Imobiliárias-PT |
|---|---|
| **Tipo de campanha** | Cold Outbound personalizado por artefato — não é frio puro: o "sinal" que substitui curtida/comentário é o próprio site scrapeado da imobiliária (fit técnico + dor inferida), então cada lead já chega com research feito antes do D0. |
| **Canal** | Ambos — LinkedIn (conexão + FUP) e Email (paralelo a partir do D+2) |
| **Target e base de leads** | ICP: imobiliárias PT com site multi-idioma (ver `## ICP` acima). Base: `Signals/lote_835/resultados.csv` (753 domínios), priorizada em `Signals/resultados.csv`. Decisor-alvo: sócio/diretor comercial ou responsável por marketing/digital da imobiliária — **a mapear por conta** (o scraping pega a empresa, não o contato — enriquecimento de contato é etapa própria, ver abaixo). |
| **Ideia da campanha** | O quebra-gelo não é um post curtido — é o claim de que já visitamos o site e criamos um artefato específico pra eles, capaz de aumentar a conversão em até 30% (mais vendas). O artefato só é de fato construído quando o lead responde: entregamos uma prévia e reservamos o completo (+ treinamento do time + handoff) pra reunião. |
| **Data de início** | A definir |
| **Duração do ciclo** | Campanha encerra X dias após o primeiro disparo pro lead — mesma lógica do modelo padrão. Definir X após rodar o primeiro lote piloto. |
| **Data de fim** | A definir |
| **Bot conectado à campanha** | A definir (ferramenta de automação LinkedIn+Email a escolher) |

#### Pontos de Atenção

- Leads dessa campanha SEMPRE têm personalização de copy — a base inteira já vem com research (idiomas, imóveis, descrição, ângulo sugerido no CSV), não existe versão genérica sem personalização.
- Checar se variável **empresa** está carregando corretamente antes de disparar.
- Checar se variável **first name** está carregando corretamente em todos os canais — histórico de bug conhecido em outras campanhas: carrega na mensagem de FUP1 via ferramenta de email mas falha na mensagem de LinkedIn. Testar os dois canais separadamente antes do disparo em massa.
- O claim "criamos esse artefato pra vocês" na copy de outbound precisa ter processo de build-sob-resposta rápido o suficiente pra não furar a promessa — se o lead responde e a prévia demora demais, a tese da campanha quebra. Definir SLA interno de tempo entre resposta e envio da prévia.
- Não construir o artefato completo antes da resposta — desperdiça esforço em contas que nunca respondem. Prévia só depois do "sim".

#### Fluxo de Cadência

Máximo 3 mensagens LinkedIn + 3 emails — sem os toques extras (FUP3/Email4) do modelo padrão, porque aqui a resposta muda o fluxo (dispara o build do artefato) em vez de só continuar a cadência:

| Toque | Ação |
|---|---|
| D0 | Solicita conexão no LinkedIn com nota personalizada (claim do artefato + estimativa de +30% conversão) |
| D+2 | LinkedIn msg 1 + Email 1 |
| D+2 | LinkedIn msg 2 + Email 2 |
| D+4 | LinkedIn msg 3 + Email 3 (último toque do ciclo) |
| Ao responder | Build do artefato (prévia) → envio da prévia → CTA de 20min com promessa de artefato completo + treinamento do time + handoff |
| — | Sem resposta após os 3 toques: conta cai pro pilar de conteúdo/ads como reforço passivo (sem downsell de evento nessa campanha) |

#### Definições sobre Tratamento da Base

Etapas ANTES do enriquecimento (curadoria):
- Rodar scoring/priorização sobre os 753 domínios (ver critérios em `## Sinal` acima) — já mapeado como pendência.
- Filtrar apenas leads em empresas dentro do ICP (site multi-idioma + catálogo ativo).
- Eliminar empresas de eventual lista de negativação (clientes atuais, concorrentes diretos, parceiros) — **a definir se existe lista**.

#### Definições sobre Enriquecimento e Personalização

Base já vem parcialmente enriquecida pelo scraping (`resultados.csv`): idiomas do site, imóveis listados, descrição extraída, ângulo de abordagem sugerido por IA. Falta enriquecer por conta antes do disparo:
- Nome e cargo do decisor/contato (o scraping mapeia a empresa, não a pessoa)
- Headline e summary do LinkedIn do decisor
- Dor específica inferida para o cargo do contato (ex: se for sócio vs. gestor de marketing, a dor muda)
- Sinal de existência de champion interno pra vibe coding (checar no perfil/empresa antes da call — cargo técnico, marketing digital, ou alguém já mexendo em automação)
- Case relevante (assim que o primeiro cliente fechar)

Link do artefato **não** entra no enriquecimento pré-disparo — só é gerado reativamente após resposta do lead (ver `#### Fluxo de Cadência`).

#### Resultados e Debriefing

A preencher após o primeiro ciclo — taxa de resposta, reuniões agendadas, aprendizados sobre qual variação de copy/ângulo performou melhor por segmento de imobiliária (luxo vs. médio padrão, Algarve vs. Lisboa/Porto).

### 3. Conteúdo + Ads (Conteudo/ e Ads/Creative) — reforço, não canal isolado

Conteúdo dessa campanha roda em paralelo ao outbound, mesmo público-alvo, pra aquecer antes do contato e dar contexto depois:
- Análises sobre o mercado imobiliário internacional em Portugal (Golden Visa, D7, fluxo de comprador estrangeiro, tempo médio de resposta a lead como métrica que dói).
- Cases/prints do agente rodando (com autorização) uma vez que os primeiros clientes fecharem.
- Ads amplificam esse mesmo conteúdo pro público de decisores de imobiliária (lookalike a partir da lista de 753 contas, não interesse genérico).

Voz segue [brand/voice.md](../00%20Brand/voice.md) — arquétipo Engenheiro-Prático-Estoico: mostrar o agente funcionando > falar sobre IA de forma abstrata.

## Fluxo Ponta a Ponta

```
Signals (scraping) → Score/Priorização → Outbound (claim do artefato, 3 LI + 3 email)
        → Lead responde → Build do artefato (prévia) → CTA 20min
        → Reunião: artefato completo + treinamento do time + handoff → Meeting booked / Deal
        ↘ Sem resposta → Conteúdo/Ads rodando em paralelo pro mesmo público (reforço passivo)
```

## KPIs (60-90 dias)

- Taxa de resposta à cadência de 3+3 toques (valida se o claim do artefato + estimativa de +30% conversão funciona como quebra-gelo)
- Tempo entre resposta do lead e envio da prévia do artefato (SLA interno — não pode furar a promessa da copy)
- % de leads respondentes com champion interno identificado (valida se o handoff é viável)
- Reuniões/demos agendadas (métrica norte)
- Contas priorizadas trabalhadas do lote de 753

## Pendente / Próximos Passos

- [ ] Rodar scoring sobre os 753 domínios de `lote_835/resultados.csv` e gerar shortlist priorizada (pasta `Signals/`)
- [ ] Definir processo/tooling de build **rápido** do artefato personalizado (site + agente embutido) — precisa rodar sob demanda logo após resposta do lead, não em lote antecipado — documentar em `Scripts/`
- [ ] Definir SLA interno entre resposta do lead e envio da prévia do artefato
- [ ] Escrever as 3 mensagens LinkedIn + 3 emails da cadência (claim do artefato + estimativa de +30% conversão) — `Scripts/` e `Outbound/`
- [ ] Escrever a mensagem de prévia (pós-resposta) e o roteiro da call de 20min (artefato completo + treinamento + handoff) — `Scripts/`
- [ ] Definir critério pra identificar champion interno na conta (cargo, sinais no LinkedIn/site) antes de avançar pra reunião
- [ ] Primeiro post de conteúdo ancorando a dor (tempo de resposta a lead internacional) — `Conteudo/`
- [ ] Definir data de início e duração do ciclo (X dias pós-primeiro disparo)
- [ ] Escolher bot/ferramenta de automação LinkedIn+Email
- [ ] Confirmar se existe lista de negativação (clientes atuais, concorrentes, parceiros)
- [ ] Mapear processo de enriquecimento de contato (nome/cargo/headline do decisor por empresa) — o scraping hoje só cobre a empresa
