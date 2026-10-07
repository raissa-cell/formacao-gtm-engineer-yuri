# Mapa de fontes e concorrentes

Consultado em 07/10/2026. Este arquivo operacionaliza os critérios de [`filtros.md`](filtros.md) sem transformar ausência de evidência em desqualificação.

## Cinco fontes priorizadas

| Prioridade | Fonte pública | O que entrega | Como extrair | Esforço | Confiabilidade e limite |
|---|---|---|---|---|---|
| 1 | **Site oficial do grupo e das unidades**, partindo dos [localizadores das montadoras](../../playbook/mapeamento-marcas-automotivas.md) | Bandeiras, unidades, cidades, WhatsApp, ofertas, landing pages e sinais de estrutura | Firecrawl `map` para localizar páginas; `scrape`/`crawl` para conteúdo e links; revisão manual de contagem | Baixo a médio | Melhor combinação de critérios e fonte oficial; sites com JavaScript ou franquias em domínios separados exigem conferência |
| 2 | **Google Search e Google Maps** | Descoberta de grupos/unidades, endereços, site, telefone/WhatsApp, avaliações e nomes ligados à empresa | Apify Google Maps Scraper para escala; Google Search e revisão manual para deduplicar | Baixo | Alta cobertura, mas Maps não comprova autorização nem deve contar oficina/peças/seminovos automaticamente |
| 3 | **Meta Ad Library e Google Ads Transparency** | Anúncios, criativos, ofertas, destinos e atividade recente de mídia | Apify `apify/facebook-ads-scraper` com `onlyTotal: true` para contagem; revisão na [Meta Ad Library](https://www.facebook.com/ads/library/) e no [Google Ads Transparency Center](https://adstransparency.google.com/) | Baixo a médio | Prova anúncio localizado, não orçamento; ausência na página consultada fica `nao_verificado` |
| 4 | **LinkedIn da empresa e das pessoas**, incluindo vagas | Estrutura comercial, cargos, vínculo, senioridade, atividade e temas públicos | Apify para company/employees/posts; busca e revisão manual para confirmar o perfil correto | Médio | Forte para diretorias e áreas corporativas; papel de compra continua sendo estimativa |
| 5 | **Instagram oficial do grupo/unidade e de lideranças** | Ofertas, inaugurações, eventos, marcações, WhatsApp e pessoas visíveis na operação | Apify Instagram Scraper para posts públicos; revisão manual de bio, marcações e data | Médio | Muito útil no automotivo; cargo/vínculo de pessoa exige bio profissional, publicação institucional ou segunda fonte |

### Resposta do exercício

**A fonte que entrega mais critérios com menos esforço é o site oficial do grupo/unidade, iniciado pelo localizador da montadora.** Em uma única coleta é comum obter bandeira, unidades, cidades, canais comerciais, ofertas e links de campanha. O Google Maps entra antes como descoberta em escala, mas não deve ser a confirmação final dos gates.

Primeira raspagem recomendada: sites oficiais das concessionárias encontradas nos localizadores das 13 marcas prioritárias, usando Firecrawl e o schema [`concessionaria-web.schema.json`](../../automations/leads/schemas/concessionaria-web.schema.json).

## Melhores fontes por critério

As fontes aparecem em ordem de preferência. “Manual” significa que o resultado precisa de leitura humana mesmo quando a descoberta foi automatizada.

| Critério | 1ª fonte | 2ª fonte | 3ª fonte | 4ª fonte | 5ª fonte |
|---|---|---|---|---|---|
| `concessionaria_autorizada` | Localizador da montadora | Site da bandeira/unidade | Site do grupo | Google Search | Instagram oficial |
| `operacao_por_bandeira` | Site da bandeira/unidade | Localizador da montadora | Site do grupo | Instagram oficial | Google Maps |
| `unidades_comerciais_ativas` | Site/“lojas” do grupo | Localizadores das montadoras | Google Maps | Google Search | Instagram por unidade |
| `ads_ativos_detectados` | Meta Ad Library | Google Ads Transparency | Landing pages do site | Instagram/Facebook oficial | Resultados patrocinados no Google |
| `whatsapp_comercial_publico` | Site/landing page | Google Business/Maps | Instagram oficial | Anúncio ativo | Link de oferta/test-drive |
| `estrutura_comercial_publica` | LinkedIn empresa/funcionários | Vagas públicas | Site/imprensa oficial | Instagram institucional | Eventos/associações do setor |
| `persona_prioritaria_encontrada` | LinkedIn | Site/imprensa oficial | Instagram | Google Search | Eventos, montadoras e associações |
| Cargo e vínculo da pessoa | LinkedIn atual | Publicação institucional | Site/imprensa | Instagram com evidência profissional | Evento/associação com data |

## Ordem de extração

1. Descobrir empresas e unidades por localizador de marca, Google Search e Google Maps.
2. Rastrear o domínio oficial no Firecrawl e extrair páginas de lojas, marcas, ofertas e contato.
3. Deduplicar unidades por endereço e confirmar autorização/bandeira.
4. Contar anúncios ativos com o Actor oficial do Apify e revisar as páginas/bandeiras na biblioteca de anúncios.
5. Encontrar decisor e champion no LinkedIn; complementar com Instagram, site e imprensa.
6. Salvar valor, URL, fonte e data para cada campo.
7. Classificar conta em P1/P2/P3 e pessoa em T1/T2/T3.

## Contagem piloto de anúncios ativos

Coleta executada em 07/10/2026 com o Actor oficial [`apify/facebook-ads-scraper`](https://apify.com/apify/facebook-ads-scraper), usando `onlyTotal: true` e `activeStatus: active`.

| Conta | Página consultada | Anúncios ativos retornados | Classificação do sinal | Observação |
|---|---|---:|---|---|
| Grupo Saga | [Grupo Saga no Facebook](https://www.facebook.com/gruposagaoficial/) | 18 | `ads_ativos_detectados = sim` | Contagem da página oficial consultada; campanhas de bandeiras/unidades podem existir separadamente |
| Grupo Navesa | [Ford Navesa no Facebook](https://www.facebook.com/CurtaNavesa/) | 16 | `ads_ativos_detectados = sim` | Resultado da página Ford Navesa, não soma automaticamente GWM, GAC ou outras bandeiras do grupo |
| Grupo Líder | [Grupo Líder no Facebook](https://www.facebook.com/grupoliderof/) | 0 | `ads_ativos_detectados = nao_verificado` | Zero na página corporativa não prova ausência de Ads nas páginas das concessionárias, marcas ou regiões |

- Execução Apify: `NAmgmJT4dAnmInSNb`.
- Dataset: `7uq7t0mkduHE2um5w`.
- A contagem é uma fotografia da consulta e pode mudar a qualquer momento.
- Para qualificar o grupo completo, repetir a coleta nas páginas de cada bandeira/unidade localizada no site oficial.

## Concorrentes monitorados

O recorte abaixo inclui concorrentes funcionais, não necessariamente idênticos à Patagon AI. Os três oferecem automação ou agentes conversacionais com WhatsApp e jornadas de vendas/atendimento; a Patagon está sendo posicionada de forma mais específica em novos leads, qualificação, acompanhamento e handoff para o time comercial.

| Concorrente | Sobreposição relevante | Página oficial de clientes/cases | Página social usada | Post de maior engajamento no recorte | Como extrair |
|---|---|---|---|---|---|
| **Blip** | Inteligência conversacional e IA em WhatsApp ao longo de marketing, vendas e atendimento | [Cases Blip](https://www.blip.ai/cases/) | [LinkedIn](https://www.linkedin.com/company/blipbr/) | [Blip id 2026 no ar](https://www.linkedin.com/posts/blipbr_blipid-blipid2026-conversasinteligentes-activity-7501290764522614784-VITH) — 130 reações, 1 comentário e 13 compartilhamentos; score 144 | Firecrawl na página de cases; Apify LinkedIn Company Posts nos posts |
| **Zenvia** | Customer Cloud, IA e jornadas de venda/atendimento via canais conversacionais, incluindo WhatsApp | [Casos de sucesso](https://zenvia.com/casos-de-sucesso/) | [LinkedIn](https://www.linkedin.com/company/zenvia-inc/) | [Operação de Black Friday](https://www.linkedin.com/posts/zenvia-inc_como-bater-recordes-de-vendas-na-black-friday-activity-7512909136393744385-UQhf) — 82 reações, 17 comentários e 27 compartilhamentos; score 126 | Firecrawl na página de cases; Apify LinkedIn Company Posts nos posts |
| **Botmaker** | Agentes de IA, bots e live chat para vendas, atendimento e processos no WhatsApp e outros canais | [Clientes e casos](https://botmaker.com/pt/nossos-clientes/todos-os-clientes/) | [LinkedIn](https://www.linkedin.com/company/botmaker/) | [Vagas em IA e operações](https://www.linkedin.com/posts/botmaker_la-ia-est%C3%A1-cambiando-la-forma-en-que-las-activity-7483514789260976128-GwjH) — 94 reações, 8 comentários e 8 compartilhamentos; score 110 | Firecrawl na página de clientes; Apify LinkedIn Company Posts nos posts |

### Evidências extraídas com Firecrawl

As três páginas oficiais foram raspadas ao vivo em 07/10/2026 com `firecrawl_scrape`, `maxAge: 0` e saída estruturada em JSON. As informações abaixo vieram do conteúdo das páginas, não de snippets de busca.

| Concorrente | Casos extraídos da página oficial | Evidência de WhatsApp, vendas ou leads | Status da coleta |
|---|---|---|---|
| **Blip** | Stellantis, Banco Arbi, Claro Chile, Energisa e Leroy Merlin, entre outros | Stellantis usa WhatsApp em suporte técnico; Banco Arbi escalou venda de consignado no canal; Claro Chile aparece com venda remota e acompanhamento via WhatsApp | `HTTP 200`; scrape `01a11893-e5ac-702b-a097-b004951a8a2e` |
| **Zenvia** | Agro Amazônia, Le Creuset, Light, Smart Fluency, Mamba Digital e Cartão de TODOS, entre outros | Smart Fluency aparece com faturamento dobrado usando WhatsApp e chatbot; Cartão de TODOS com aumento de 26% na conversão via chamadas de voz no WhatsApp | `HTTP 200`; scrape `01a11893-e6b1-73c3-9c7c-1f006d250338` |
| **Botmaker** | Payless, Alicerce, Tenda, Ford, Boti e Viacerta, entre outros | Tenda aparece com aumento de 13% nas vendas mensais; 70% dos leads da Ford são atendidos pelo bot sem intervenção humana | `HTTP 200`; scrape `01a11893-e6ab-72c9-8070-172ed77b575f` |

Essas evidências ajudam a comparar linguagem, prova e caso de uso. Não demonstram que a solução, implantação ou ICP de cada concorrente seja igual ao da Patagon AI.

### Método do ranking de posts

- Coleta: Apify `harvestapi/linkedin-company-posts` em 07/10/2026.
- Amostra: até 30 posts por página, limitados aos últimos seis meses.
- Itens retornados: 81.
- Execução Apify: `beQc3ua6q8fIxc2XG`; dataset: `vTelji4UXE78vSshg`.
- Para evitar que um repost de terceiro ganhasse como se fosse conteúdo próprio, o ranking considerou apenas posts cujo autor era a própria empresa.
- Score comparável do exercício: `reações + comentários + compartilhamentos`.
- As métricas são uma fotografia da data de consulta e podem crescer depois.

Não chamar esses resultados de “maior post de todos os tempos”. O resultado correto é **maior engajamento observado no recorte definido**.

## O que observar nos concorrentes

| Dimensão | Pergunta de análise |
|---|---|
| ICP comunicado | Falam com enterprise genérico, automotivo ou times comerciais com novos leads? |
| Momento da jornada | Aquisição, primeiro atendimento, qualificação, venda, suporte ou pós-venda? |
| Promessa | Receita, redução de custo, velocidade, disponibilidade ou experiência? |
| Handoff humano | Como descrevem a passagem da IA para o time? |
| Prova | Quais métricas e segmentos aparecem nos cases? |
| Conteúdo | Quais formatos e temas concentram engajamento? |
| Diferenciação Patagon | Onde uma proposta focada em lead novo + WhatsApp + qualificação + follow-up é mais clara e específica? |

## Fontes históricas dos três leads da aula

Estas fontes permanecem como memória do exercício anterior. Os leads precisam ser requalificados contra [`filtros.md`](filtros.md) antes de qualquer disparo.

### Grupo Líder

- Site institucional: <https://grupolider.com.br/>
- Marcas e unidades: <https://grupolider.com.br/concessionarias>
- Experiência do cliente e canais digitais: <https://blog.grupolider.com.br/experiencia-do-cliente-como-o-grupo-lider-esta-reinventando-o-atendimento/>

### Grupo Saga

- Site institucional: <https://www.gruposaga.com.br/>
- Saga Geely: <https://www.geelybrasil.com.br/sagageely/quem-somos>
- Lojas e canais de atendimento: <https://www.gruposaga.com.br/index.php/lojas>

### Grupo Navesa

- Site institucional: <https://www.navesa.com.br/index.html>

### Perfis dos leads

- Fabio Calligari: <https://www.linkedin.com/in/fabio-calligari-2b836491/>
- Lindomar Oliveira: <https://www.linkedin.com/in/lindomar-oliveira-29074315a/>
- Sandro Toledo: <https://www.linkedin.com/in/sandro-toledo-gyn2/>

Os perfis foram lidos na sessão autenticada da Raissa. Nenhum dado de contato privado foi coletado.
