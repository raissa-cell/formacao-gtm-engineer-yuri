---
name: company-lookalike
description: Gera lista lookalike de empresas a partir de um grupo-semente (clientes, melhores contas, ICP). Enriquece as sementes, clusteriza em perfis, monta filtros firmográficos por cluster (Brasil via CNPJ e global), busca na Nuvia, pontua critérios qualitativos (idade, familiar vs. profissionalizada, fundo, alinhamento cultural) e entrega a lista na Nuvia ou como pacote de filtros/CSV para Clay, Apollo etc. Gatilhos - "lookalike", "empresas parecidas com", "clonar meu ICP", "achar mais clientes como esses", "expandir lista a partir dessas empresas", "clusterizar minhas contas".
---

# Company Lookalike

Entrada: grupo de empresas-semente (CNPJ, domínio ou nome). Saída: lista de empresas parecidas, por cluster, com score, na Nuvia ou exportável.

Regras do repo valem aqui: carregar `nuvia-crm` e `playbook/nuvia-mcp-boas-praticas.md` antes de qualquer escrita na Nuvia; confirmar com o aluno antes de criar lista; buscar é gratuito, `enrich_list` é o único que gasta crédito; todo lead passa pela triagem de ICP (`automations/leads/triagem_icp.py`); PII e CSVs ficam fora do git.

## Fluxo

### 0. Entrada e escopo
Pergunte, se faltar: mercado (Brasil, global ou ambos), tipo de entrada, destino (Nuvia, CSV/pacote de filtros), tamanho desejado da lista (padrão: 200 a 500, curadoria acima de volume). Mínimo recomendado de sementes: 5. Abaixo de 5, avise que o cluster será frágil.

### 1. Resolver as sementes
- **CNPJ**: `search_brazil_companies` com `filters.cnpjs`. Para nome: `nome_empresa` (fuzzy) e confirme o match com o aluno.
- **Domínio**: `filters.dominio` (BR) ou `search_businesses` com `company_name`; use `link_brazil_to_global` / `link_global_to_brazil` para cruzar as duas bases.
- Sementes não resolvidas: liste e pergunte; não invente dados.

### 2. Enriquecer cada semente (matriz de atributos)
Monte uma tabela semente x atributo. Campo vazio fica vazio.

| Atributo | Fonte |
|---|---|
| CNAE principal e secundários, setor | CNPJ |
| Porte, capital social | CNPJ |
| Funcionários (faixa), receita (faixa) | `search_businesses` (só global) |
| Ano de início, idade | CNPJ `inicio_atividade` / `company_age` |
| UF, município, região | CNPJ |
| Natureza jurídica, matriz/filial, nº de locais | CNPJ / global |
| Stack tecnológico | `company_tech_stack_*` (global) |
| Palavras-chave do site | `website_keywords` (global) ou Firecrawl |
| Quadro societário (nº sócios, sobrenomes, idades, sócio PJ) | CNPJ |

Para BR sem faixa de funcionários/receita: usar `porte` e `capital_social` como proxy e avisar o limite.

### 3. Clusterizar
- Agrupe por similaridade nos atributos de maior peso: indústria > tamanho/porte > idade > geografia > estrutura.
- Cada cluster precisa de no mínimo 3 sementes; sementes soltas viram "outliers" e ficam de fora (mostre quais).
- Nomeie cada cluster de forma descritiva ("LTDA familiar, 15+ anos, SP, varejo") e mostre: sementes, moda e faixa de cada atributo, % de coesão.
- Mostre os clusters ao aluno e espere OK antes de buscar. Ele pode juntar, dividir ou descartar.

### 4. Montar filtros por cluster
Por cluster, gere dois níveis:
- **Estrito** (moda do grupo): resultado enxuto, alta precisão.
- **Expandido** (moda ± vizinhança): faixa de tamanho adjacente, janela de idade ±N anos, CNAEs vizinhos, região em vez de município.

Higiene sempre ligada: BR `situacao_cadastral=Ativa`, `identificador=Matriz`, `tem_dominio=true` (e `tem_linkedin` quando o canal for LinkedIn); global `has_website=true`. Exclua as próprias sementes (`exclude.business_id`, ou filtrando por CNPJ/domínio no pós-processamento).

Pesos padrão do score firmográfico: indústria 30, tamanho 20, idade 15, geografia 15, estrutura jurídica 10, stack/keywords 10. Ajuste se o aluno disser que algo é inegociável (vira filtro duro, não peso).

Resolva valores de catálogo ANTES de buscar: `lookup_brazil_filter_values` (CNAE, cidade, natureza) e `lookup_filter_values` (global). Lookup vazio = termo errado, reformule 1 a 2 vezes.

### 5. Buscar
`search_brazil_companies` / `search_businesses`, `page_size` 20, comece pelo estrito. Se `total_results` ficar abaixo do alvo, passe ao expandido. Se vier milhares, adicione filtros antes de paginar. Mostre `total_results` por cluster e por nível antes de trazer a lista.

### 6. Score qualitativo (só nos finalistas, ~top 100 por cluster)
Qualitativo é caro; nunca rode na lista inteira. Marque cada sinal como `confirmado`, `provável` ou `desconhecido`; não preencha por palpite.

| Sinal | Como inferir |
|---|---|
| Anos de mercado | `inicio_atividade`; buckets <3, 3-7, 8-15, 15+ |
| Familiar | sobrenome repetido entre sócios, poucos sócios, sócio-administrador mais velho. Heurística: rotule "provável" |
| Investida por fundo | sócio PJ (FIP, holding, gestora) no quadro; confirme com busca web (notícias, Crunchbase) |
| Fase de crescimento | nº de filiais, vagas abertas, mudança de porte |
| Alinhamento cultural | site e LinkedIn lidos via Firecrawl/Apify, classificados contra o perfil das sementes (tom, posicionamento, maturidade digital) |

Score final = firmográfico (0-100) x 0,7 + qualitativo (0-100) x 0,3. Mostre as colunas separadas, não só o total.

### 7. Entrega
Mostre amostra (10 por cluster) + totais e espere OK. Depois:
- **Nuvia**: confirmar antes; rodar `whoami`; criar lista com nome `lookalike-<publico>-<AAAA-MM>`; popular só via `add_records` (skill `nuvia-crm`); deduplicar por CNPJ/domínio, nunca por nome; guardar cluster, score e sinais em colunas. Enriquecer contato (e-mail 1 crédito, telefone 10) só após confirmar custo.
- **Outra ferramenta**: gerar `campaigns/<publico>/outbound/lookalike-<AAAA-MM>.md` com o pacote de filtros por cluster em linguagem de cada ferramenta (Clay, Apollo, Sales Navigator) + CSV em pasta ignorada pelo git.
- Registrar a metodologia (sementes, clusters, filtros, data) no mesmo `.md`, para repetir e comparar depois.

## Limitações (diga ao aluno)
- Brasil não tem filtro de funcionários nem receita.
- `country_code` global filtra pela sede registrada, não pelo país de operação.
- Familiar e fundo são inferências sobre o quadro societário, não fatos.
- Lookalike com poucas sementes gera clusters instáveis.

## Formato da resposta
Tabelas markdown enxutas: sementes resolvidas, clusters, filtros por cluster, contagens, amostra. Sem travessão. Pergunte só o que bloqueia.
