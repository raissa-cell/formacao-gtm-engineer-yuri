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
| `whatsapp_comercial_publico` | Site/landing page com Firecrawl | Google Business/Maps | Instagram oficial | Anúncio ativo | Link de oferta/test-drive |
| `estrutura_comercial_publica` | LinkedIn empresa/funcionários | Vagas públicas | Site/imprensa oficial | Instagram institucional | Eventos/associações do setor |
| `persona_prioritaria_encontrada` | LinkedIn | Site/imprensa oficial | Instagram | Google Search | Eventos, montadoras e associações |
| Cargo e vínculo da pessoa | LinkedIn atual | Publicação institucional | Site/imprensa | Instagram com evidência profissional | Evento/associação com data |

## Links, widgets e schema de WhatsApp no site

No Firecrawl, procurar primeiro páginas de contato, lojas, ofertas, test-drive e vendas; coletar links e HTML para encontrar CTAs renderizados e links presentes em scripts/widgets. Detectar ao menos estes formatos:

| Padrão | Interpretação |
|---|---|
| `https://wa.me/<numero>` ou `https://wa.me/message/<codigo>` | Link curto do WhatsApp / link curto de negócio |
| `https://api.whatsapp.com/send?phone=<numero>` | Link click-to-chat via `api.whatsapp.com` |
| `https://www.whatsapp.com/send?phone=<numero>` | Link click-to-chat via domínio principal |
| `https://web.whatsapp.com/send?phone=<numero>` | Abertura do chat pela versão web |
| `whatsapp://send?phone=<numero>` | Deep link para abrir o app |
| `tel:`, botão/ícone com evento JavaScript ou widget de terceiro | Canal telefônico ou CTA cuja URL final precisa ser inspecionada |

O Schema.org não tem um tipo/campo exclusivo chamado “WhatsApp”. Inspecionar `Organization` ou `AutomotiveBusiness`, especialmente `contactPoint`, `telephone`, `url` e `sameAs`; em paralelo, procurar os links nos elementos `<a>`, botões, atributos `data-*` e scripts/widgets. `telephone` sozinho não prova que o número recebe WhatsApp. Endpoints de backend da WhatsApp Business Platform (por exemplo, Graph API) são infraestrutura de servidor e não devem ser classificados como CTA público.

### Varredura piloto com Firecrawl

Em 07/10/2026, Firecrawl coletou links, HTML e JSON-LD das páginas abaixo. A busca cobriu links `wa.me`, `api.whatsapp.com`, `whatsapp.com/send`, `web.whatsapp.com/send` e variações. Nenhuma dessas três páginas expôs um link direto de WhatsApp no HTML/links coletados; isso não prova ausência no site inteiro, pois widgets podem carregar depois e concessionárias usam domínios próprios.

| Empresa | Página inspecionada | Tipos JSON-LD detectados | Link direto de WhatsApp nessa página |
|---|---|---|---|
| Grupo Saga | <https://www.gruposaga.com.br/saga-distrito-federal/contato> | `AutomotiveBusiness` | Não localizado |
| Grupo Navesa | <https://www.navesa.com.br/> | Nenhum detectado | Não localizado |
| Grupo Líder | <https://grupolider.com.br/fale-conosco/contato> | `Organization` | Não localizado |

Na Navesa e no Grupo Líder, o mapa também revelou domínios próprios por bandeira/unidade. A próxima coleta deve testar essas páginas de vendas/oferta, além do site do grupo, para localizar os links realmente usados na entrada de leads.

## Tráfego do site — Similarweb

Usar o [Similarweb](https://www.similarweb.com/) para estimar o volume de visitas do domínio oficial e identificar tendência, canais e páginas mais acessadas quando esses dados estiverem disponíveis. Esse dado ajuda a priorizar contas com maior alcance digital e possível entrada de demanda no site.

O tráfego estimado **não é quantidade de leads** e não confirma conversões nem volume de conversas no WhatsApp. Registrar domínio consultado, período, visitas estimadas, fonte e data; tratar resultado ausente ou indisponível como `nao_verificado`. Para confirmar leads e origem, usar dados internos da empresa durante discovery ou analytics compartilhado pelo prospect.

| Campo sugerido | Fonte | Interpretação |
|---|---|---|
| `visitas_site_estimadas_mes` | Similarweb | Estimativa mensal de visitas ao domínio; guardar período e data da consulta |
| `tendencia_trafego_site` | Similarweb | Tendência de crescimento/queda na janela disponível; sinal de alcance digital |
| `canais_aquisicao_site` | Similarweb | Mix estimado de canais, quando disponível; pode indicar dependência de mídia paga ou busca |

Esse sinal complementa Ads detectados e WhatsApp comercial público. Não substitui a confirmação de investimento em Ads, leads novos, conversão ou fluxo para WhatsApp.

## Ordem de extração

1. Descobrir empresas e unidades por localizador de marca, Google Search e Google Maps.
2. Rastrear o domínio oficial no Firecrawl; coletar páginas de lojas, marcas, ofertas e contato; extrair links de WhatsApp e tipos/campos de JSON-LD.
3. Usar o domínio oficial no Data Stone para localizar a empresa raiz, contar CNPJs ativos e sócios; validar filiais pela situação cadastral, sem presumir que todo CNPJ seja uma unidade comercial.
4. Enriquecer o mesmo domínio no Apollo para estimar colaboradores e localizar a página corporativa correta no LinkedIn.
5. Deduplicar unidades por endereço e confirmar autorização/bandeira.
6. Contar anúncios ativos com o Actor oficial do Apify e revisar as páginas/bandeiras na biblioteca de anúncios.
7. Consultar no Similarweb o domínio oficial para estimar tráfego mensal, tendência e canais de aquisição, quando houver cobertura.
8. Encontrar decisor e champion no LinkedIn; complementar com Instagram, site e imprensa.
9. Salvar valor, URL, período, fonte e data para cada campo.
10. Classificar conta em P1/P2/P3 e pessoa em T1/T2/T3.

## Camada cadastral e de porte — Data Stone + Apollo

O domínio oficial é a chave de entrada comum. No Data Stone, o fluxo esperado é **domínio → empresa raiz → CNPJs vinculados → somente situação cadastral ativa**. No Apollo, o domínio retorna o porte estimado da organização. As fontes não são intercambiáveis: Apollo estima colaboradores; Data Stone/Receita sustenta CNPJ, filiais e quadro societário.

| Campo | Fonte principal | Regra de preenchimento |
|---|---|---|
| `dominio_oficial` | Site oficial | Domínio canônico, sem caminho e sem parâmetros |
| `colaboradores_estimados` | Apollo | Registrar o número e marcar como estimativa, com data da consulta |
| `cnpj_raiz` | Data Stone | CNPJ da matriz/empresa raiz localizada pelo domínio |
| `cnpjs_ativos_total` | Data Stone | Contar apenas registros cuja situação cadastral esteja ativa |
| `socios_total` | Data Stone | Contar sócios únicos vinculados ao CNPJ raiz; registrar a regra usada quando houver duplicidade |
| `filiais_comerciais_confirmadas` | Data Stone + site/localizador/Maps | Um CNPJ ativo é candidato a filial; só vira unidade comercial após confirmação de endereço e operação |

### Enriquecimento piloto por domínio

Consulta executada no Apollo em 07/10/2026. O enriquecimento canônico consumiu um crédito por empresa encontrada. A consulta no Data Stone está pendente porque a sessão abriu na tela de login e o conector não está disponível neste ambiente; os campos correspondentes permanecem `nao_verificado` até a autenticação.

| Empresa | Domínio | Colaboradores estimados (Apollo) | Total de sócios (Data Stone) | CNPJs ativos (Data Stone) |
|---|---|---:|---:|---:|
| Grupo Saga | `gruposaga.com.br` | 8.000 | `nao_verificado` | `nao_verificado` |
| Grupo Navesa | `navesa.com.br` | 310 | `nao_verificado` | `nao_verificado` |
| Grupo Líder | `grupolider.com.br` | 850 | `nao_verificado` | `nao_verificado` |

Os números do Apollo representam porte estimado da organização no domínio, não folha de pagamento nem soma oficial de vínculos trabalhistas.

## Dealerbook e alternativa aberta para marcas

O Dealerbook foi avaliado, mas não é uma base aberta para extração: exige cadastro e limita recursos por plano; o “mapa com lojas” aparece nos planos de negócio. Para coleta reproduzível, priorizar os localizadores oficiais das montadoras. Testes com as páginas da Toyota e da CAOA Chery retornaram concessionária, cidade, UF, endereço e site, mantendo a marca conhecida pela fonte de origem.

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
