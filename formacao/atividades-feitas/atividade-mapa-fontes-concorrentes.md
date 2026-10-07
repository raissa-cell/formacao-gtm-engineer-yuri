# Atividade feita — mapa de fontes e concorrentes

**Data:** 07/10/2026  
**Módulo relacionado:** Dia 02 — Sourcing  
**Status:** concluída e salva no repositório  
**Responsável:** Raissa

## Objetivo

Transformar o ICP de concessionárias da Patagon AI em um fluxo de pesquisa reproduzível, escolher as cinco fontes públicas prioritárias e mapear concorrentes funcionais com páginas oficiais de cases e conteúdo público.

## O que foi feito

1. Criação de `filtros.md` com gates binários/numeráveis, sinais de prioridade, filtros da pessoa e campos reservados para discovery.
2. Priorização de cinco famílias de fontes públicas com ferramenta, esforço, confiabilidade e limites.
3. Mapeamento das cinco melhores fontes para cada critério do ICP.
4. Definição da ordem de extração e da primeira raspagem recomendada.
5. Pesquisa de Blip, Zenvia e Botmaker como concorrentes funcionais.
6. Registro das páginas oficiais de clientes/cases e das páginas no LinkedIn.
7. Coleta no Apify de 81 posts e cálculo do maior engajamento observado em um recorte auditável.
8. Raspagem ao vivo no Firecrawl das três páginas oficiais de clientes/cases, com saída estruturada em JSON.
9. Contagem piloto de anúncios ativos de Grupo Saga, Ford Navesa e Grupo Líder com o Actor oficial da Meta Ad Library no Apify.
10. Preservação das fontes históricas dos três leads da atividade anterior.
11. Inclusão da camada de enriquecimento por domínio: Data Stone para CNPJ, CNPJs ativos, sócios e candidatos a filiais; Apollo para colaboradores estimados.
12. Enriquecimento Apollo de Grupo Saga (8.000 colaboradores estimados), Grupo Navesa (310) e Grupo Líder (850).
13. Avaliação do Dealerbook e adoção dos localizadores oficiais das montadoras como alternativa aberta para descoberta de marcas e lojas.

## Arquivos produzidos

- [`../../campaigns/concessionarias-automotivas/filtros.md`](../../campaigns/concessionarias-automotivas/filtros.md)
- [`../../campaigns/concessionarias-automotivas/fontes.md`](../../campaigns/concessionarias-automotivas/fontes.md)

## Decisão operacional

O site oficial do grupo/unidade, iniciado pelo localizador da montadora, entrega a melhor relação entre quantidade de critérios e esforço. Ele pode revelar bandeiras, unidades, cidades, WhatsApp, ofertas e links de campanha em uma coleta.

Google Maps é excelente para descoberta em escala, mas não confirma sozinho autorização, bandeira ou contagem válida de unidades. A primeira raspagem deverá partir dos sites oficiais encontrados nos localizadores das marcas prioritárias.

## Concorrentes analisados

| Empresa | Por que entrou | Página oficial usada |
|---|---|---|
| Blip | IA e inteligência conversacional para WhatsApp em marketing, vendas e atendimento | <https://www.blip.ai/cases/> |
| Zenvia | Customer Cloud, IA e jornadas conversacionais de venda/atendimento | <https://zenvia.com/casos-de-sucesso/> |
| Botmaker | Agentes de IA, bots e live chat no WhatsApp e outros canais | <https://botmaker.com/pt/nossos-clientes/todos-os-clientes/> |

São concorrentes funcionais; o mapeamento não afirma equivalência total com a Patagon AI.

## Método de conteúdo

- Apify: `harvestapi/linkedin-company-posts`.
- Janela: últimos seis meses.
- Limite: até 30 posts por página oficial.
- Total coletado: 81 posts.
- Ranking: reações + comentários + compartilhamentos.
- Reposts de terceiros foram excluídos da escolha final.
- Firecrawl: `firecrawl_scrape` nas páginas oficiais de Blip, Zenvia e Botmaker, com `maxAge: 0` e schema JSON para clientes, casos de uso, métricas e evidências de WhatsApp/vendas.
- Resultado Firecrawl: três respostas `HTTP 200`.
- Ads: Apify `apify/facebook-ads-scraper`, com `onlyTotal: true` e `activeStatus: active`; retornou 18 anúncios para Grupo Saga, 16 para Ford Navesa e zero na página corporativa do Grupo Líder.
- Apollo: enriquecimento canônico pelos domínios `gruposaga.com.br`, `navesa.com.br` e `grupolider.com.br`, com porte estimado de 8.000, 310 e 850 colaboradores, respectivamente.
- Data Stone: fluxo definido como domínio → empresa raiz → CNPJs vinculados → CNPJs ativos → sócios; a coleta ficou pendente de autenticação na plataforma.

O documento registra “maior engajamento observado no recorte”, não “maior post de todos os tempos”.

## Validações

- Os gates permanecem coerentes com o ICP canônico.
- Dados internos — volume, investimento, processo, equipe e dor — não foram promovidos a filtros públicos.
- A ausência de anúncio ou WhatsApp público permanece `nao_verificado`.
- As três páginas de clientes/cases pertencem aos domínios oficiais dos concorrentes.
- As três páginas foram efetivamente raspadas pelo Firecrawl e retornaram conteúdo estruturado.
- Os posts apontam para as páginas oficiais de cada empresa no LinkedIn.
- O zero de anúncios na página corporativa do Grupo Líder foi mantido como `nao_verificado`, pois bandeiras e unidades podem anunciar por outras páginas.
- CNPJ ativo foi separado de unidade comercial: cada filial precisa ser confirmada por endereço e operação no site, localizador da montadora ou Google Maps.
- Colaboradores do Apollo foram registrados como estimativa, não como número oficial de vínculos.

## Próximo passo

Autenticar a conta do Data Stone e completar, para os três domínios piloto, `cnpj_raiz`, `cnpjs_ativos_total` e `socios_total`; depois confirmar quais CNPJs ativos correspondem a unidades comerciais.

Nenhuma mensagem foi enviada e nenhum contato foi enriquecido nesta atividade.
