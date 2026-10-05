# PAT — Programa de Alimentação do Trabalhador (MTE)

Dados públicos do MTE com a relação de pessoas jurídicas e nutricionistas inscritos no PAT. Snapshots semestrais/anuais publicados em SharePoint pelo Ministério do Trabalho. Cobre **4 listas distintas**: empresas beneficiárias (empregadoras inscritas), empresas facilitadoras (operadoras de vale-refeição/alimentação), empresas fornecedoras (cozinhas industriais/restaurantes coletivos) e nutricionistas responsáveis técnicos.

> **Doc operacional**: [`docs/pat/00-visao-geral.md`](../../../docs/pat/00-visao-geral.md) (bronze) + [`docs/pat/silver-pipeline.md`](../../../docs/pat/silver-pipeline.md) (silver) + [`docs/pat/gold-pipeline.md`](../../../docs/pat/gold-pipeline.md) (**gold — usar por padrão**) + [`docs/pat/queries-cookbook.md`](../../../docs/pat/queries-cookbook.md) (boas práticas + receitas).

---

## 1. Contexto crítico — não pule

### O que é o PAT

Programa criado pela **Lei 6.321/1976**, regulamentado pelo Decreto 10.854/2021. Permite que a empresa empregadora ofereça vale-refeição / vale-alimentação / refeição na empresa para os trabalhadores e **deduza até 4% do IRPJ devido** (limitado a 1 SM por trabalhador/mês).

### Quem é obrigado a estar no PAT?

**Ninguém. A adesão é voluntária.** Não há obrigatoriedade legal de empresa estar inscrita.

A motivação real é fiscal — **dedução de IRPJ**. Por isso a base é fortemente enviesada:

| Quem **costuma** estar no PAT | Quem **costuma** NÃO estar |
|---|---|
| Médias e grandes empresas (Lucro Real ou Presumido) que pagam IRPJ | **MEI** (Microempreendedor Individual) — não paga IRPJ, sem benefício |
| Indústria, varejo de grande porte, bancos, telecom | **Simples Nacional** — IRPJ unificado no DAS, não dedutível por PAT |
| Setor público em alguns casos (Correios, BB, Caixa, secretarias) | Profissionais liberais sem CNPJ |
| Empresas que oferecem benefícios formais a colaboradores | PMEs informais |

### Implicação para análise

- **Cobertura ≠ universo de empresas**: o PAT não representa o mercado total de empregadores brasileiro.
- **PMEs/MEI sub-representados**: mesmo bronze_cnpj cobre 100% das empresas formais; já o PAT só cobre os ~345k grupos que aderiram.
- **Análises de "vidas cobertas" ≠ trabalhadores totais do Brasil**: em 2025 o PAT cobria ~22M trabalhadores ativos, contra ~57M assalariados formais (CAGED) — cobertura de ~38%.
- **Filtros importantes** quando o usuário perguntar "essa empresa está no PAT?" → resposta de "não cadastrada" não é exceção, é o normal pra muitos perfis.

### Diferença Facilitadora × Fornecedora

| Papel | O que faz | CNAE típico | Exemplos |
|---|---|---|---|
| **Beneficiária** | Empresa empregadora inscrita no PAT (oferece benefício aos trabalhadores) | qualquer setor | Bradesco, Correios, Petrobras, Ambev |
| **Facilitadora** | Operadora de vale-refeição/alimentação (cartão/voucher) | "Emissão de vales-alimentação" (8299-7-04), "Administração de cartões de crédito" | Alelo, Ticket, Sodexo, Vólus, COVABRA |
| **Fornecedora** | Produz refeições prontas (cozinha industrial, marmitex, restaurante coletivo) | "Restaurantes" (5611-2-01), "Fornecimento de alimentos preparados preponderantemente para empresas" (5620-1-01) | Sapore, GRSA, GR, Verdes Vales |

**78 CNPJs aparecem em ambas as listas** (facilitadora + fornecedora) — supermercados que operam vale e fornecem (Bompreço, GPA, Mateus, Muffato), e operadoras de vale que viram parceiros fornecedores (Ticket, Alelo).

**Não há FK pública entre beneficiária × facilitadora/fornecedora.** Quem é cliente de quem é informação privada do contrato comercial. "Quantas vidas atende a Sodexo" não é derivável dessa fonte.

---

## 2. Tabelas e granularidade

### `bronze_pat` (4 tabelas — granularidade fonte)

| Tabela | Linhas | Granularidade | Notas |
|---|---:|---|---|
| `empresas_beneficiarias` | 532.088 | 1 linha por unidade PAT (CNPJ 14 dígitos) | Sheets `Beneficiárias-ATIVO` (483k) + `Beneficiárias-INATIVO` (49k); única lista com `total_trabalhadores` e faixas salariais |
| `empresas_facilitadoras` | 645 | 1 linha por unidade | `Facilitadoras-ATIVO` (589) + `_INATIVO` (56) |
| `empresas_fornecedoras` | 27.349 | 1 linha por unidade | `Fornecedoras-ATIVO` (19.612) + `_INATIVO` (7.737) |
| `nutricionistas` | 37.676 | 1 linha por nutricionista | Schema diferente — tem CRN e Num Registro PAT, **sem CNPJ** — não cruza diretamente com bronze_cnpj |

Schema bronze (todas STRING + 4 metadados `_sheet_origem, _arquivo_origem, _data_carga, _periodo`):

- `cnpj` (14 dígitos, só números)
- `razao_social`, `matriz_ou_filial`, `municipio` (declarado no PAT), `uf` (declarado no PAT)
- `no_registro` (Nº Registro PAT, chave do programa)
- `data_cadastro` (formato `DD-MM-YYYY`)
- `situacao` (`Ativo` / `Inativo`)
- Beneficiárias só: `total_trabalhadores`, `ate_5_salarios_minimos`, `acima_de_5_salarios_minimos`

### `silver_pat` (3 tabelas — uso analítico, com auditoria/divergência)

| Tabela | Linhas | Granularidade | Quando usar |
|---|---:|---|---|
| `empresas_beneficiarias_grupo` | 345.726 | 1 linha por **CNPJ_BASICO** (inclui zumbis) | Investigação histórica, comparação grupo vs ativos |
| `empresas_beneficiarias` | 521.245 | 1 linha por CNPJ unidade (inclui inativas) | Auditoria, análise pat_rfb_divergente |
| `empresas_servicos_alimentacao` | 27.916 | 1 linha por CNPJ único | Mercado completo (inclui inativas) |

Silver_pat **não tem** tabela pra nutricionistas (descartado por baixa utilidade).

### `gold_pat` (3 tabelas + 1 view — DEFAULT pra consumo direto) ⭐

Camada limpa: filtros aplicados upstream, município/UF/razão sempre RFB (UPPERCASE), folha pré-calculada.

| Tabela | Linhas | Granularidade | Quando usar |
|---|---:|---|---|
| `gold_pat.empresas` | 288.376 | 1 linha por CNPJ_BASICO ATIVO + `unidades ARRAY<STRUCT>` top 50 | Ranking, "X tem N filiais e Y trabalhadores", queries inline sem JOIN |
| `gold_pat.empresas_unidades` | 407.226 | 1 linha por CNPJ unidade ativa+consistente | Análise por cidade, mapas, dashboards (Looker Studio etc.) |
| `gold_pat.servicos_alimentacao` | 20.149 | 1 linha por CNPJ unificado (papel ativo) | Mercado de operadores PAT (com endereço RFB completo) |
| **`gold_pat.empresas_outliers_suspeitos`** (VIEW) | 1.362 | cadastros PAT estatisticamente improváveis | Filtrar de rankings ou listar pra revisar |

**Filtros embutidos no gold:**
- `total_trabalhadores_ativos > 0` (sem 26.809 zumbis)
- `situacao_pat = 'Ativo'` AND `NOT pat_rfb_divergente` (sem 64.887 unidades baixadas na RFB)
- `municipio_rfb IS NOT NULL` (sem unidades sem endereço)
- `razao_social` RFB-first com fallback PAT normalizado (UPPER + NFKD strip)
- **`folha_mensal_estimada_brl`** pré-calculada (NUMERIC) — heurística 3SM/8SM com SM=R$1.518

> **Use gold por padrão.** Silver só pra investigação/auditoria de divergências. Bronze só pra debug do source.

---

## 3. Princípios não-negociáveis — leia antes de escrever query

### P0. Default = `gold_pat` ⭐

Para perguntas analíticas (consumo, ranking, mapas, "X tá no PAT?", folha estimada), **vá direto pra `gold_pat`**. Os filtros já estão aplicados (sem zumbis, sem divergentes), o município já é RFB (UPPERCASE), a folha já tem valor numérico. Use silver/bronze só pra:

- **Auditoria** (`pat_rfb_divergente=true`, comparação PAT × RFB) → silver
- **Investigação histórica** (incluindo zumbis) → silver
- **Schema bruto da fonte** → bronze

### P0.1 (CRÍTICO) Nunca inferir localização da razão social

**Antes de afirmar UF/cidade de qualquer empresa, SEMPRE consulte `municipio_rfb` e `uf_rfb` (gold) ou `municipio` decodificado de `bronze_cnpj.estabelecimentos`.**

Razão social pode mencionar uma cidade que **não é** a real:
- Filiais/franquias com nome regional mas operação em outra UF
- Denominações genéricas ("Padaria Carioca" pode estar em SP)
- Nomes de família que coincidem com cidades

Caso real (2026-05-02): "F. TAVARES DA COSTA VEIGA ME" foi assumido como sendo do RJ pela razão social mas é de Cuiabá/MT (Estação do Café, Pães e Doces, Av. Brasil, CPA II). Confirmado via gold + WebSearch.

**Anti-padrão**: dizer "essa padaria do Rio…" antes de rodar `SELECT uf, municipio FROM gold_pat.empresas_unidades WHERE cnpj_basico = X`.

### P1. Geografia: use `municipio_rfb`, **não** `municipio_pat`

O cadastro PAT é **centralizado pela matriz**. A Ambev tem 77 unidades, mas declara só **1 município no PAT** ("Rio de Janeiro" — sede); na verdade tem filiais em **65 municípios diferentes** (verdade RFB).

```sql
-- ❌ ERRADO — todas as unidades da Ambev colapsam em 1 cidade
SELECT municipio_pat, SUM(total_trabalhadores_unid) FROM `silver_pat.empresas_beneficiarias` ...

-- ✅ CERTO — endereço real RFB de cada filial
SELECT municipio_rfb, uf_rfb, SUM(total_trabalhadores_unid) FROM `silver_pat.empresas_beneficiarias` ...
```

### P2. Análise comercial: use `total_trabalhadores_ativos`, **não** `total_trabalhadores_grupo`

13,8% do total no PAT (~3,5M trabalhadores) está em **unidades inativas** (empresas em recuperação, fechadas, fundidas). 26.352 grupos são "zumbi" (zero ativos). `total_trabalhadores_grupo` inclui esses; `total_trabalhadores_ativos` não.

| Coluna | Quando usar |
|---|---|
| `total_trabalhadores_grupo` | Histórico, "quanto já passou pelo PAT" |
| `total_trabalhadores_ativos` | **Análise comercial — vidas cobertas hoje** ⭐ |
| `total_trabalhadores_inativos` | Detectar grupos zumbi |

### P3. Grupo econômico = `cnpj_basico` (8 dígitos)

Filiais compartilham raiz. `COUNT(DISTINCT cnpj_basico)` pra contar grupos únicos. Bradesco (60746948) tem 3.521 unidades PAT que são 1 grupo só.

### P4. Cuidado com `pat_rfb_divergente=true`

64.887 unidades têm `situacao_pat='Ativo'` mas estão **baixadas na RFB** (`situacao_cadastral_rfb='08'`) — Lojas Americanas (1.717), HSBC (944), Itaú (871). Se a análise depende de "operação real hoje", filtre `pat_rfb_divergente = false`.

### P5. Tabela unificada de serviços tem 3 papéis

Na `empresas_servicos_alimentacao`, `papel ∈ {AMBOS, FACILITADORA, FORNECEDORA}`. **Não filtre** `papel='FACILITADORA'` se quer todas as facilitadoras (perderia as 78 em AMBOS). Use `WHERE eh_facilitadora` (que cobre AMBOS + FACILITADORA puro).

### P6. PAT cobre pequena parcela do universo de empresas

Quando o usuário perguntar "essa empresa pequena/MEI tá no PAT?" — provavelmente não. Não é exceção. Sempre que uma empresa não aparecer, dizer **"não cadastrada no PAT (adesão é voluntária; MEI/Simples geralmente não aderem)"**, não "empresa não existe".

### P7. Sem FK entre beneficiárias × facilitadoras/fornecedoras

Não tente cruzar "quem é cliente da Sodexo" — esse vínculo é privado. Pode mostrar **mercado** de facilitadoras (645 empresas), não **clientela** delas.

### P8. Nutricionistas sem CNPJ

`bronze_pat.nutricionistas` tem CRN + Nº Registro PAT, **não tem CNPJ**. Não cruza com bronze_cnpj diretamente. Vínculo só via `num_registro_pat ↔ no_registro` das beneficiárias/facilitadoras/fornecedoras.

### P8.1 Cadastros PAT podem ter outliers — sempre questione anomalias

A fonte PAT (auto-declarada pelo empregador) tem **erros de digitação**. Empresas micro/pequenas declarando milhares de funcionários é o erro mais comum.

**Sinal de alerta**:
- `total_trabalhadores > 100` AND `porte = 'MICRO EMPRESA'`
- `total_trabalhadores * 4554 > capital_social * 50` (folha estimada / capital > 50)
- `total_trabalhadores > 200` AND `capital_social < 100000`
- Email é `gmail.com`/`hotmail.com` (provedor pessoal — empresa real teria domínio próprio)
- Sem sócios em `silver_cnpj.socios`

**Caso real**: F. TAVARES DA COSTA VEIGA ME (CNPJ 09150946) declarou 2.412 trabalhadores em 1 unidade (12 ≤5SM + 2.400 >5SM!). Capital R$ 30k, ME, gmail genérico, padaria de bairro em Cuiabá (confirmado por Instagram + CNN Brasil V&G). Erro de cadastro do declarante.

**Quando detectar outlier**: avise o usuário, sugira filtrar em rankings, ofereça WebSearch para validar (ver `09-artifacts-e-visuais.md` + `10-enriquecimento-web.md`).

**Use a view pronta**: `gold_pat.empresas_outliers_suspeitos` lista os 1.362 cadastros suspeitos com `razao_suspeita` e `score_suspeita` (1-3). Pra filtrar de rankings:

```sql
SELECT e.* FROM `gold_pat.empresas` e
LEFT JOIN `gold_pat.empresas_outliers_suspeitos` o USING (cnpj_basico)
WHERE o.cnpj_basico IS NULL  -- só não-suspeitos
ORDER BY e.total_trabalhadores DESC LIMIT 20;
```

### P9. Heurística de folha de pagamento

PAT só dá **faixas salariais** (≤5 SM e >5 SM), não salário real. Pra estimar folha mensal:

- SM 2025 = **R$ 1.518**
- Faixa baixa (≤5 SM): assumir média **3 SM** ≈ R$ 4.554/trabalhador
- Faixa alta (>5 SM): assumir média **8 SM** ≈ R$ 12.144/trabalhador (conservador)

```sql
SUM(trab_ate_5sm_unid) * (3 * 1518) + SUM(trab_acima_5sm_unid) * (8 * 1518) AS folha_mensal_estimada
```

**Sempre alertar** que é estimativa grosseira pra ranking relativo, não pra valores absolutos. Pra precisão, cruzar com BDC `employees_count` ou RAIS/CAGED.

---

## 4. Queries-âncora (validadas em snapshot 2025-12-31)

> Queries usam **`gold_pat`** (camada limpa). Para investigação/auditoria, ver §3 de [`silver-pipeline.md`](../../../docs/pat/silver-pipeline.md).

### Q1. Funcionários da Ambev por cidade (caso paradigmático — gold direto)

```sql
SELECT
  uf, municipio,
  COUNT(*) AS unidades,
  SUM(total_trabalhadores) AS trabalhadores,
  ROUND(SUM(folha_mensal_estimada_brl)/1e6, 2) AS folha_milhoes
FROM `data-hacker-488115.gold_pat.empresas_unidades`
WHERE cnpj_basico = '07526557'
GROUP BY 1, 2 ORDER BY trabalhadores DESC LIMIT 15;
```

Resultado (Ambev = 24.874 ativos, 63 municípios):
- **SP - SAO PAULO**: 2.492 trab, folha R$ 25,19 mi (escritório/HQ)
- **SP - JAGUARIUNA**: 2.306 trab, R$ 17,25 mi
- **RJ - RIO DE JANEIRO**: 2.130 trab, R$ 11,18 mi (sede operacional)
- **SP - CAMPINAS**: 1.200 trab, R$ 12,99 mi (outro escritório)

Padrão: % baixa renda baixa → escritório (folha por trabalhador alta), % alta → fábrica.

### Q2. Maior empregador em uma cidade (Juazeiro do Norte/CE — folha já no gold)

```sql
SELECT
  cnpj_basico, razao_social, total_trabalhadores,
  ROUND(folha_mensal_estimada_brl/1e6, 2) AS folha_mi,
  cnae_principal_descricao
FROM `data-hacker-488115.gold_pat.empresas_unidades`
WHERE municipio = 'JUAZEIRO DO NORTE' AND uf = 'CE'
ORDER BY folha_mensal_estimada_brl DESC LIMIT 10;
```

→ ISGH (Hospital Regional do Cariri): 1.192 trab, R$ 6,37 mi/mês.

### Q2b. ARRAY de unidades inline (sem JOIN, gold só)

```sql
SELECT
  razao_social, qtd_unidades_pat_ativas, total_trabalhadores,
  ROUND(folha_mensal_estimada_brl/1e6, 2) AS folha_mi,
  ARRAY_LENGTH(unidades) AS no_array,
  (SELECT u.municipio FROM UNNEST(unidades) u ORDER BY u.trabalhadores DESC LIMIT 1) AS maior_unidade
FROM `data-hacker-488115.gold_pat.empresas`
WHERE cnpj_basico = '07526557';
```

> Para grupos com >50 filiais (Correios, BB, Bradesco), o ARRAY é truncado em top 50 — use `gold_pat.empresas_unidades` flat.

### Q3. Top empregadores por folha estimada (gold)

```sql
SELECT cnpj_basico, razao_social, porte, cnae_principal_descricao,
       qtd_unidades_pat_ativas, total_trabalhadores,
       ROUND(folha_mensal_estimada_brl/1e6, 1) AS folha_mi,
       ROUND(pct_baixa_renda, 1) AS pct_low,
       qtd_ufs_atuacao
FROM `data-hacker-488115.gold_pat.empresas`
ORDER BY folha_mensal_estimada_brl DESC LIMIT 10;
```

Top: UNIMED ARARUAMA (447k — cooperativa), TRE-MG (120k), BRF (101k), BB (95k), Correios (92k), CEF (89k), Bradesco (88k), Petrobras (82k), Sendas/Assaí (76k), Seara (73k).

### Q4. Mercado de facilitadoras de vale por estado (gold — só ativas)

```sql
SELECT
  uf,
  COUNT(*) AS facilitadoras,
  COUNTIF(papel='AMBOS') AS tambem_fornecem,
  ARRAY_AGG(STRUCT(razao_social, capital_social) ORDER BY capital_social DESC NULLS LAST LIMIT 3) AS top3
FROM `data-hacker-488115.gold_pat.servicos_alimentacao`
WHERE eh_facilitadora
GROUP BY 1 ORDER BY facilitadoras DESC;
```

### Q5. Empresa X está no PAT? (gold)

```sql
WITH alvo AS (SELECT '07526557' AS cnpj_basico)
SELECT
  alvo.cnpj_basico,
  IF(g.cnpj_basico IS NULL, 'NÃO está no PAT', 'no PAT') AS status,
  g.razao_social, g.qtd_unidades_pat_ativas, g.total_trabalhadores,
  g.qtd_filiais_rfb_ativas, g.cobertura_pat_pct
FROM alvo
LEFT JOIN `data-hacker-488115.gold_pat.empresas` g USING (cnpj_basico);
```

Se vier "NÃO está no PAT" — diga ao usuário: *"essa empresa não aderiu ao PAT (programa é voluntário; MEI/Simples não se beneficiam da dedução)"*. Não diga "empresa não existe".

### Q6. Distribuição PAT por porte (mostra o viés da base)

```sql
SELECT COALESCE(porte, '(sem porte RFB)') porte,
       COUNT(*) grupos, SUM(total_trabalhadores_ativos) trabalhadores
FROM `data-hacker-488115.silver_pat.empresas_beneficiarias_grupo`
GROUP BY 1 ORDER BY trabalhadores DESC;
```

Esperado: dominado por "DEMAIS" (médias/grandes); microempresa/EPP minoria — confirma viés.

---

## 5. Schemas detalhados (campos principais)

### `silver_pat.empresas_beneficiarias_grupo` (1 linha por CNPJ_BASICO)

| Coluna | Origem |
|---|---|
| `cnpj_basico` | chave (8 dígitos) |
| `razao_social_grupo`, `razao_social_pat` | dim_empresa + fallback PAT |
| `porte`, `cod_porte`, `natureza_juridica`, `cnae_principal_codigo`, `cnae_principal_descricao`, `capital_social` (NUMERIC), `idade_anos`, `optante_simples`, `optante_mei`, `uf_matriz_rfb`, `municipio_matriz_rfb`, `situacao_grupo_descricao` | dim_empresa |
| `unidades_pat`, `unidades_pat_matriz`, `unidades_pat_filial`, `unidades_pat_ativas`, `unidades_pat_inativas` | agregados PAT |
| `total_trabalhadores_grupo`, **`total_trabalhadores_ativos`**, `total_trabalhadores_inativos` | somas com/sem inativos |
| `trabalhadores_ate_5sm_grupo`, `trabalhadores_ate_5sm_ativos`, `trabalhadores_acima_5sm_grupo`, `trabalhadores_acima_5sm_ativos` | faixas salariais |
| `pct_baixa_renda`, **`pct_baixa_renda_ativos`** | derivado |
| `ufs_atuacao` (ARRAY), `qtd_ufs_atuacao`, `municipios_atuacao_top20` | distribuição geográfica |
| `qtd_filiais_ativas_rfb`, `qtd_filiais_total_rfb`, `cobertura_pat_pct` | comparação PAT × RFB |

### `silver_pat.empresas_beneficiarias` (1 linha por CNPJ unidade)

Bronze PAT (`cnpj`, `cnpj_basico`, `razao_social_pat`, `matriz_ou_filial`, `municipio_pat`, `uf_pat`, `no_registro`, `data_cadastro_pat` DATE, `total_trabalhadores_unid`, `trab_ate_5sm_unid`, `trab_acima_5sm_unid`, `situacao_pat`, `_sheet_origem`)

\+ **Endereço RFB** (`bronze_cnpj.estabelecimentos`): `nome_fantasia_rfb`, `situacao_cadastral_rfb`, `data_situacao_rfb`, `cnae_principal_unidade_rfb`, `cnae_principal_descricao_unidade_rfb`, `tipo_logradouro_rfb`, `logradouro_rfb`, `numero_rfb`, `complemento_rfb`, `bairro_rfb`, `cep_rfb`, **`municipio_rfb`**, **`uf_rfb`**, `data_inicio_atividade_unid`

\+ Email (`silver_cnpj.estabelecimentos_dominios`): `email_rfb`, `email_dominio_raiz_rfb`

\+ Atributos do grupo (`silver_cnpj.dim_empresa`): `razao_social_grupo_rfb`, `porte_grupo`, `capital_social_grupo`, `idade_grupo_anos`, `cnae_principal_grupo_descricao`

\+ Flag: **`pat_rfb_divergente`** (BOOL) — `situacao_pat='Ativo' AND situacao_cadastral_rfb='08'`

### `silver_pat.empresas_servicos_alimentacao` (1 linha por CNPJ único)

`cnpj`, `cnpj_basico`, `razao_social`, `matriz_ou_filial`, `municipio_pat`, `uf_pat`, **`eh_facilitadora`** (BOOL), **`eh_fornecedora`** (BOOL), **`papel`** (`AMBOS`/`FACILITADORA`/`FORNECEDORA`)

\+ Por papel: `no_registro_facilitadora`, `data_cadastro_facilitadora`, `situacao_facilitadora`, `sheet_origem_facilitadora` (idem para `_fornecedora`)

\+ Enrichment dim_empresa (mesmo conjunto de _grupo)

---

## 6. Cenários comuns

| Pergunta | Tabela primária | Lembrete |
|---|---|---|
| "Quantos funcionários tem X?" | **`gold_pat.empresas`** | direto, `total_trabalhadores` já é só ativos |
| "Onde X tem unidades?" | **`gold_pat.empresas_unidades`** | endereço RFB completo (`uf`, `municipio` UPPERCASE) |
| "X está no PAT?" | **`gold_pat.empresas`** | "não" é normal pra MEI/Simples — não é "não existe" |
| "Quem opera vale-refeição em SP?" | **`gold_pat.servicos_alimentacao`** | `WHERE eh_facilitadora AND uf='SP'` |
| "Restaurantes que fornecem PAT em [cidade]" | **`gold_pat.servicos_alimentacao`** | `WHERE eh_fornecedora AND municipio='RECIFE'` |
| "Maior empregador em [cidade]" | **`gold_pat.empresas_unidades`** | `WHERE municipio='X' AND uf='Y'`, ORDER BY `folha_mensal_estimada_brl` |
| "Folha de pagamento estimada" | **`gold_pat`** | já calculada em `folha_mensal_estimada_brl` (alerte que é estimativa pra ranking) |
| "Filiais de um grupo (sem JOIN)" | **`gold_pat.empresas`** | UNNEST(unidades) — top 50; flat tem todas |
| "Setor com mais trabalhadores PAT" | **`gold_pat.empresas`** | `GROUP BY cnae_principal_descricao` |
| **Auditoria — cadastros desatualizados** | `silver_pat.empresas_beneficiarias` | filtre `pat_rfb_divergente=true` |
| **Investigação — incluindo zumbis** | `silver_pat.empresas_beneficiarias_grupo` | use `total_trabalhadores_grupo` |

---

## 7. Cobertura CNPJ × PAT (validações)

- 99,98% das unidades PAT batem com `bronze_cnpj.estabelecimentos` (via cnpj_basico+ordem+dv)
- 99,80% têm endereço RFB completo
- 97,8% das beneficiárias têm CNPJ válido (14 dígitos); ~2,2% têm cadastros antigos malformados
- 0,02% têm CNPJ no PAT mas inexistente na RFB (cadastros muito antigos pré-RFB ou erros)

Casos de uso problemáticos:
- **Lojas Americanas**: 1.717 unidades "Ativas" no PAT, 100% baixadas na RFB (recuperação judicial)
- **HSBC**: 944 unidades "Ativas" no PAT, banco saiu do Brasil em 2016
- **Itaú**: 871 filiais antigas "Ativas" no PAT, baixadas pós-fusão Unibanco

Sempre considerar `pat_rfb_divergente` em queries de "operação real hoje".
