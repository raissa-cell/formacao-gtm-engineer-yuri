# Filtros públicos — concessionárias automotivas

Versão operacional do ICP da Patagon AI para sourcing. A definição canônica permanece em [`../../playbook/icp-patagon-ai.md`](../../playbook/icp-patagon-ai.md).

## Regra de evidência

Usar apenas três estados antes da abordagem:

- `sim`: há evidência pública e a URL foi registrada;
- `nao`: há evidência pública que nega o critério;
- `nao_verificado`: a informação não foi localizada.

`nao_verificado` não significa `nao`. Volume de leads, investimento em mídia, processo, equipe e dor real pertencem à discovery.

## Gates da empresa

| Prioridade | Critério | Campo | Regra binária ou numérica | Evidência mínima | Ação quando falha |
|---|---|---|---|---|---|
| Gate | Concessionária autorizada | `concessionaria_autorizada` | `sim/nao/nao_verificado` | Localizador da montadora ou site oficial com bandeira identificada | `nao` = não priorizar; `nao_verificado` = enriquecer |
| Gate | Operação por bandeira | `operacao_por_bandeira` | `sim/nao/nao_verificado` | Página própria da marca/unidade, domínio ou comunicação institucional separada | `nao` = não priorizar; `nao_verificado` = enriquecer |
| Gate | Quatro ou mais unidades comerciais | `unidades_comerciais_ativas` | inteiro ou `nao_verificado`; gate `>=4` | Quatro endereços comerciais distintos confirmados; não contar oficina, peças, seminovos no mesmo endereço ou duplicidade | `<4` = não priorizar; desconhecido = enriquecer |

Um grupo pode representar várias montadoras e continuar no ICP quando opera concessionárias autorizadas separadas por bandeira.

## Sinais públicos de prioridade

| Critério | Campo | Regra pública | O que a evidência comprova | O que não comprova |
|---|---|---|---|---|
| Ads detectados | `ads_ativos_detectados` | `sim/nao_verificado` | Há anúncio ou landing page pública ativa; contar na Meta com Apify `apify/facebook-ads-scraper` (`onlyTotal: true`) | Investimento mensal, volume ou ROAS |
| WhatsApp comercial visível | `whatsapp_comercial_publico` | `sim/nao_verificado` | Existe canal em contexto de venda, oferta, test-drive ou contato comercial | Volume, SLA ou uso real para novos leads |
| Estrutura comercial encontrada | `estrutura_comercial_publica` | `sim/nao_verificado` | Há área/cargo ligado a vendas, marketing, CRM, BDC, performance ou operações | Tamanho, capacidade ou processo do time |
| Persona prioritária encontrada | `persona_prioritaria_encontrada` | `sim/nao_verificado` | Existe decisor ou champion atual com cargo confirmado | Autoridade final, dor ou intenção de compra |

## Enriquecimento cadastral e porte

Estes campos apoiam deduplicação, dimensionamento e priorização, mas não substituem os três gates da empresa.

| Critério | Campo | Fonte | Regra |
|---|---|---|---|
| Domínio oficial | `dominio_oficial` | Site oficial | Chave para cruzar Data Stone e Apollo |
| Colaboradores estimados | `colaboradores_estimados` | Apollo | Inteiro estimado; sempre guardar a data da consulta |
| CNPJ raiz | `cnpj_raiz` | Data Stone | Matriz associada ao domínio oficial |
| CNPJs ativos | `cnpjs_ativos_total` | Data Stone | Contar somente situação cadastral ativa |
| Sócios | `socios_total` | Data Stone | Contar pessoas/empresas únicas do quadro societário, documentando duplicidades |
| Filiais comerciais | `filiais_comerciais_confirmadas` | Data Stone + site/localizador/Maps | CNPJ ativo sozinho não comprova unidade comercial; confirmar endereço e operação |

### Priorização da conta

- **P1:** os três gates estão confirmados e os quatro sinais públicos foram encontrados.
- **P2:** os três gates estão confirmados, mas falta um ou mais sinais públicos.
- **P3:** aderência aparente, porém um ou mais gates ainda precisam de confirmação.
- **Não priorizar:** um gate estrutural falhou com evidência pública.

## Filtros da pessoa

| Critério | Campo | Valores permitidos | Regra de qualificação |
|---|---|---|---|
| Vínculo atual | `vinculo_atual_confirmado` | `sim/nao/nao_verificado` | Cargo e empresa precisam aparecer em fonte atual ou em duas fontes coerentes |
| Área aderente | `area` | `executiva`, `comercial`, `marketing`, `operacoes`, `crm_bdc`, `vendas_digitais`, `performance`, `outra` | `outra` exige justificativa para continuar |
| Papel estimado | `papel_compra_estimado` | `decisor`, `champion`, `usuario_influenciador`, `nao_prioritario`, `nao_verificado` | É hipótese de pesquisa, não autoridade confirmada |
| Confiança | `confianca_papel_compra` | `alta`, `media`, `baixa` | Alta exige cargo atual e escopo coerente; Instagram isolado não gera confiança alta |

### Cargos prioritários

1. Proprietário, sócio, presidente, CEO, diretor executivo, comercial, marketing, operações ou negócios/digital.
2. Head ou gerente comercial, marketing/growth, CRM/BDC, vendas digitais, performance, relacionamento ou central de leads.
3. Coordenador das mesmas áreas como champion potencial.

Pessoa inadequada não elimina a empresa: procurar outro contato.

## Campos que só podem ser confirmados na discovery

```text
whatsapp_novos_leads_confirmado
leads_novos_whatsapp_mes
investimento_ads_mes_confirmado
tempo_primeira_resposta
processo_qualificacao_followup
equipe_assumir_oportunidades
crm_e_integracoes
dor_patagon_confirmada
prioridade_e_orcamento
```

## Registro obrigatório por evidência

Para cada campo público preenchido, guardar:

```text
valor
url_fonte
tipo_fonte
data_verificacao
observacao
```

O mapa de fontes, ferramentas e esforço está em [`fontes.md`](fontes.md). O mapa de marcas e localizadores está em [`../../playbook/mapeamento-marcas-automotivas.md`](../../playbook/mapeamento-marcas-automotivas.md).
