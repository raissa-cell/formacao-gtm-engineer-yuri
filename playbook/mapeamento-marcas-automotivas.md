# Mapeamento de marcas automotivas

Referência para descobrir grupos e unidades de concessionárias autorizadas no Brasil. O arquivo operacional está em [`../automations/leads/config/marcas-automotivas-br.json`](../automations/leads/config/marcas-automotivas-br.json) e o formato de saída em [`../automations/leads/schemas/concessionaria-web.schema.json`](../automations/leads/schemas/concessionaria-web.schema.json).

## Objetivo

Começar pela rede oficial de cada montadora, identificar concessionárias e depois agrupar unidades que pertencem ao mesmo grupo econômico. A pesquisa deve responder:

1. A unidade é autorizada pela montadora?
2. É ponto de vendas ou apenas oficina/peças?
3. Qual grupo controla a unidade?
4. Quantas unidades comerciais ativas o grupo possui?
5. Existem sinais públicos de WhatsApp, ofertas, test drive, formulários e Ads?
6. Onde procurar decisores e champions?

## Marcas mapeadas

### Prioridade 1 — começar por aqui

| Marca | Localizador oficial | Observação de captura |
|---|---|---|
| Fiat | [Rede Fiat](https://www.fiat.com.br/concessionarias.html) | Cidade, filtros, site e WhatsApp da concessionária |
| Chevrolet | [Rede Chevrolet](https://www.chevrolet.com.br/localizar-concessionaria) | Separar pontos de venda de serviços/peças |
| Volkswagen | [Rede Volkswagen](https://www.vw.com.br/pt/busca-de-concessionarias.html) | Buscar ponto oficial de vendas e serviços |
| Toyota | [Rede Toyota](https://www.toyota.com.br/contato/localize-uma-concessionaria) | Confirmar concessionária versus posto de serviço |
| Honda Automóveis | [Rede Honda](https://www.honda.com.br/automoveis/concessionarias/busca) | Não misturar com a rede de motocicletas |
| Hyundai | [Rede Hyundai](https://www.hyundai.com.br/concessionarias.html) | Nome, CEP/localização e formulários comerciais |
| Ford | [Rede Ford](https://www.ford.com.br/dealer-locator/) | Usar filtro “Vendas”; não contar apenas peças/serviços |
| Renault | [Rede Renault](https://www.renault.com.br/encontre-uma-concessionaria.html) | Endereço/localização e lista completa |
| Nissan | [Rede Nissan](https://www.nissan.com.br/encontre-uma-concessionaria.html) | Cidade/CEP e localização atual |
| Jeep | [Rede Jeep](https://www.jeep.com.br/concessionarias.html) | Cidade, ofertas e vendas diretas |
| BYD | [Rede BYD](https://www.byd.com/br/find-store) | CEP/endereço/cidade; rede em expansão rápida |
| GWM | [Rede GWM](https://www.gwmmotors.com.br/pt/concessionarias) | Busca por CEP; Haval, Ora, Tank, Poer e Wey são aliases |
| CAOA Chery | [Site CAOA Chery](https://caoachery.com.br/) | Localizador dinâmico; aplicar fallback por Google quando necessário |

### Prioridade 2 — expansão e premium

| Marca | Localizador/rede oficial | Observação de captura |
|---|---|---|
| Ram | [Rede Ram](https://www.ram.com.br/concessionarias.html) | O localizador expõe WhatsApp por concessionária |
| Peugeot | [Rede Peugeot](https://carros.peugeot.com.br/servicos-e-manutencao/assistencia-e-garantia/peugeot-professional-center.html) | Cidade/nome/CEP e filtro por serviço |
| Citroën | [Rede Citroën](https://www.citroen.com.br/concessionarias.html) | Cidade e localização; observar proposta/reserva online |
| Mitsubishi | [Rede Mitsubishi](https://www.mitsubishimotors.com.br/concessionarias) | Rede oficial, ofertas e test drive |
| Kia | [Rede Kia](https://www.kia.com.br/concessionarias) | Lista por estado; distinguir showroom de assistência |
| Audi | [Rede Audi](https://www.audi.com.br/pt/informacoes-ao-consumidor/rede-concessionaria/) | Buscar também por “Audi Center + cidade” |
| Volvo Cars | [Rede Volvo](https://www.volvocars.com/br/dealers/concessionarios/) | Mapa/lista e filtros de vendas/serviço |
| Geely | [Unidades Geely](https://www.geelybrasil.com.br/contato) | O formulário oficial lista unidades e canais de contato |
| GAC | [GAC Brasil](https://www.gacgroup.com/pt-br) | Usar o menu “Concessionário” e fallback por Google |
| JAC Motors | [Rede JAC](https://www.jacmotors.com.br/rede-credenciada/) | Distinguir concessionária de rede autorizada apenas para serviço |

## Schema de busca por marca

Para cada marca, o mapa guarda:

| Campo | Uso |
|---|---|
| `id`, `name`, `aliases` | Normalização; evita tratar Haval/GWM ou GM/Chevrolet como marcas diferentes |
| `priority` | Ordem de pesquisa |
| `official_site` e `official_domain` | Restringir busca à fonte primária |
| `locator_url` | Fonte oficial para autorização e unidades |
| `locator_mode` | Tipo de navegação esperado |
| `locator_verified` | Se o endereço foi conferido nesta revisão |
| `commercial_clues` | Textos e elementos que indicam jornada comercial pública |

## Schema de extração dos sites

Cada unidade encontrada deve gerar um registro contendo:

- fonte, URL e data da observação;
- marca normalizada e alias encontrado;
- nome do grupo controlador, quando identificável;
- nome, cidade, UF, endereço e tipo da unidade;
- status de autorização;
- indicação se conta como unidade comercial;
- site, telefone e Google Maps;
- WhatsApp público e contexto em que aparece;
- ofertas, formulário, test drive e landing pages;
- URLs para descobrir personas no LinkedIn, Instagram, site e imprensa;
- evidência por critério, com confiança.

## Regras de contagem e deduplicação

1. Contar somente `sales`, `sales_and_service` e showrooms com venda confirmada.
2. Não contar oficina, peças ou centro técnico isolado como unidade comercial.
3. Seminovos no mesmo endereço não cria automaticamente outra unidade.
4. Deduplicar por `marca + grupo + cidade + endereço normalizado`.
5. Google Maps serve para descoberta. Autorização deve ser confirmada no localizador da montadora ou site oficial.
6. Se a informação não aparecer, registrar `nao_verificado`; nunca converter ausência de resultado em `nao`.

## Ordem de pesquisa

1. Abrir o localizador oficial da marca.
2. Coletar unidades por estado/cidade e filtrar pontos de venda.
3. Abrir o site de cada concessionária para identificar o grupo e as demais unidades.
4. Buscar o grupo no Google e Google Maps para complementar endereços.
5. Conferir WhatsApp, ofertas, test drive, formulários e páginas de campanha.
6. Procurar decisores e champions no LinkedIn, Instagram, site e imprensa.
7. Salvar uma URL de evidência para cada critério utilizado no ICP.

## Manutenção

Redes de concessionárias e URLs mudam. Revisar o mapa trimestralmente e sempre que um localizador retornar erro. A data de verificação fica no campo `verified_at` do JSON.
