# Gold CNPJ v2 — Arquitetura Comercial (BQ + Elastic)

A camada `gold_cnpj` é a **fonte canônica pra análise comercial** (vendas, ICP, prospecção). Implementa a arquitetura comercial v2 documentada em `docs/cnpj/arquitetura-comercial-v2.md`. Tudo cruzamento com PAT, energia, CVM, BDC parte daqui.

**Use `gold_cnpj` quando**: a pergunta é comercial (porte, setor, regime tributário, filiais, sócios cross-tipo, capital social, busca por nome). É a camada com:
- Códigos RFB já resolvidos pra enums comerciais (`status.porte = "grande"` vs `PORTE='05'`)
- Filiais embutidas no doc da matriz (não 17 docs irmãos)
- Sócios separados em 4 buckets por tipo (PF/PJ_NAC/PJ_EXT/ADMIN)
- Email/telefone limpos (lixo filtrado)
- Hierarquia CNAE + setor macro

**Use `silver_cnpj` ou `bronze_cnpj` quando**: precisa do dado cru RFB (auditoria, debug, snapshots históricos por `_periodo`, ou qualificações fora dos 4 buckets gold).

---

## 1. Tabelas gold_cnpj

| Tabela | Linhas | Granularidade | Cluster | Chave |
|---|---:|---|---|---|
| `gold_cnpj.empresas` | ~27,4M | 1 doc por CNPJ_BASICO ATIVO | `(cnpj_basico, status_porte, local_uf)` | `cnpj_basico` (8d) |
| `gold_cnpj.pessoas` | ~10,2M | 1 doc por pessoa PF deduplicada | `(nome_norm, cpf_visivel)` | `id` (= `nome_norm + '_' + cpf_visivel`) |

### 1.1 `gold_cnpj.empresas` — 8 clusters semânticos

```sql
-- Schema completo (155 campos, simplificado pra essenciais)
CREATE TABLE gold_cnpj.empresas (
  -- IDENTIDADE (raiz)
  cnpj_basico               STRING,           -- 8d, chave primária
  cnpj_matriz               STRING,           -- 14d
  nome                      STRING,           -- razão social (renomeado)
  nome_fantasia             STRING,
  data_abertura             DATE,
  idade_anos                FLOAT64,
  total_filiais             INT64,            -- só ATIVAS

  -- DENORMALIZADOS (clusterizáveis, copiados de status/local pra CLUSTER BY funcionar)
  status_porte              STRING,           -- "mei" | "micro" | "pequena" | "grande"
  local_uf                  STRING,           -- UF da matriz

  -- CLUSTER 1: STATUS
  status STRUCT<
    operacional             STRING,           -- "ativa" | "baixada" | "inapta" | "suspensa" | "nula"
    porte                   STRING,           -- enum
    natureza_juridica STRUCT<
      codigo                STRING,           -- "2062"
      descricao             STRING,           -- "Sociedade Empresária Limitada"
      categoria             STRING            -- "empresarial"|"governo"|"sem_fins_lucrativos"|"individual"|"organismo_internacional"
    >,
    raw_rfb STRUCT<
      situacao_cadastral STRUCT<codigo STRING, descricao STRING, data DATE,
                                motivo STRUCT<codigo STRING, descricao STRING>>,
      porte STRUCT<codigo STRING, descricao STRING>,
      qualificacao_responsavel STRUCT<codigo STRING, descricao STRING>
    >
  >,

  -- CLUSTER 2: REGIME TRIBUTÁRIO
  regime_tributario STRUCT<
    tipo                    STRING,           -- "mei" | "simples_nacional" | "nao_simples"
    fonte                   STRING,           -- "rfb_dados_abertos"
    historico STRUCT<
      data_opcao_simples    DATE,
      data_exclusao_simples DATE,
      data_opcao_mei        DATE,
      data_exclusao_mei     DATE
    >
  >,

  -- CLUSTER 3: FINANCEIRO
  financeiro STRUCT<
    capital_social_brl      FLOAT64           -- já parseado
  >,

  -- CLUSTER 4: INDÚSTRIA (CNAE + setor macro)
  industria STRUCT<
    setor                   STRING,           -- "Tecnologia"|"Financeiro"|"Comércio"|...
    segmento                STRING,           -- placeholder v2.1
    cnae_principal STRUCT<codigo STRING, descricao STRING, secao STRING>,
    cnae_secundarios ARRAY<STRUCT<codigo STRING, descricao STRING, secao STRING>>
  >,

  -- CLUSTER 5: LOCAL (matriz + filiais ATIVAS embutidas)
  local STRUCT<
    matriz STRUCT<
      cnpj                  STRING,           -- 14d
      cep                   STRING,           -- 8d, sem pontuação
      uf                    STRING,
      municipio_codigo      STRING,
      municipio_nome        STRING,           -- UPPERCASE!
      bairro                STRING,
      logradouro_completo   STRING,           -- normalizado
      raw STRUCT<tipo_logradouro STRING, logradouro STRING, numero STRING, complemento STRING>,
      ibge STRUCT<microrregiao STRING, mesorregiao STRING, regiao_geografica STRING>,
      geo STRUCT<lat FLOAT64, lon FLOAT64>    -- null hoje
    >,
    filiais ARRAY<STRUCT<
      cnpj STRING, uf STRING, municipio_nome STRING, bairro STRING,
      cep STRING, logradouro_completo STRING, data_abertura DATE,
      cnae_principal STRUCT<codigo STRING, descricao STRING>
    >>
  >,

  -- CLUSTER 6: CONTATO (lixo filtrado)
  contato STRUCT<
    emails ARRAY<STRUCT<
      dominio STRING,                          -- ex: "stone.com.br"
      enderecos ARRAY<STRUCT<valor STRING, local_part STRING, origens ARRAY<STRING>>>
    >>,
    telefones ARRAY<STRUCT<
      ddd STRING, numero STRING, e164 STRING,  -- "+5511..."
      tipo STRING,                              -- "fixo" | "celular" | "fax"
      origens ARRAY<STRING>
    >>
  >,

  -- CLUSTER 7: SÓCIOS (4 buckets por tipo)
  socios STRUCT<
    pessoas_fisicas ARRAY<STRUCT<
      nome STRING, nome_norm STRING, cpf_visivel STRING,
      qualificacao STRUCT<codigo STRING, descricao STRING>,
      data_entrada DATE,
      faixa_etaria STRUCT<codigo STRING, descricao STRING>
    >>,
    pessoas_juridicas_nacionais ARRAY<STRUCT<
      nome STRING, nome_norm STRING, documento STRING,
      cnpj_basico STRING, razao_social STRING,
      qualificacao STRUCT<codigo STRING, descricao STRING>,
      data_entrada DATE
    >>,
    pessoas_juridicas_estrangeiras ARRAY<STRUCT<
      nome STRING, nome_norm STRING, documento STRING,
      cnpj_basico STRING, razao_social STRING,
      pais STRUCT<codigo STRING, nome STRING>,
      qualificacao STRUCT<codigo STRING, descricao STRING>,
      data_entrada DATE,
      representante_legal STRUCT<nome STRING,
                                  qualificacao STRUCT<codigo STRING, descricao STRING>>
    >>,
    administradores_diretores ARRAY<STRUCT<
      nome STRING, nome_norm STRING, cpf_visivel STRING,
      qualificacao STRUCT<codigo STRING, descricao STRING>,
      papel STRING,                            -- "titular" | "representante"
      representando STRING,
      data_entrada DATE,
      faixa_etaria STRUCT<codigo STRING, descricao STRING>
    >>,
    totais STRUCT<
      pessoas_fisicas INT64,
      pessoas_juridicas_nacionais INT64,
      pessoas_juridicas_estrangeiras INT64,
      administradores_diretores_titulares INT64,
      administradores_diretores_representantes INT64,
      geral INT64
    >
  >,

  -- METADATA
  _periodo                  STRING,           -- "202604"
  _data_carga               TIMESTAMP,
  _fontes                   ARRAY<STRING>     -- ["rfb_bronze_202604"]
)
CLUSTER BY cnpj_basico, status_porte, local_uf;
```

### 1.2 `gold_cnpj.pessoas` — 1 doc por pessoa PF

```sql
CREATE TABLE gold_cnpj.pessoas (
  id                        STRING,           -- nome_norm + '_' + cpf_visivel
  nome                      STRING,
  nome_norm                 STRING,           -- chave de busca
  cpf_visivel               STRING,           -- "***123456**"
  faixa_etaria STRUCT<codigo STRING, descricao STRING>,
  qtd_empresas              INT64,
  primeiro_vinculo_data     DATE,
  ultimo_vinculo_data       DATE,
  qualificacoes_aparece ARRAY<STRUCT<codigo STRING, descricao STRING, qtd INT64>>,
  empresas_cnpj_basicos     ARRAY<STRING>,    -- só CNPJs (lookup join)
  contato STRUCT<email STRING, telefone STRING, linkedin STRING>,  -- placeholder v2.1
  biografia                 STRING,
  links_publicos            ARRAY<STRING>,
  _periodo, _data_carga, _fontes
)
CLUSTER BY nome_norm, cpf_visivel;
```

---

## 2. Cruzamentos canônicos com outras tabelas

A força do BQ está nos JOINs. Tudo cruzamento usa **`cnpj_basico`** (8d) como chave universal.

### 2.1 PAT (Programa de Alimentação do Trabalhador)

**Tabelas relevantes em `gold_pat`:**

| Tabela | Granularidade | Quando usar |
|---|---|---|
| `gold_pat.empresas` | 1/CNPJ_BASICO | métricas agregadas: `total_trabalhadores`, `folha_mensal_estimada_brl`, `qtd_unidades_pat_ativas` |
| `gold_pat.empresas_unidades` | 1/CNPJ 14d | unidades flat por estabelecimento |
| `gold_pat.servicos_alimentacao` | 1/CNPJ × papel | facilitadoras (cartões) + fornecedoras (cozinha) ATIVAS |

**JOIN básico CNPJ + PAT:**
```sql
SELECT
  e.cnpj_basico, e.nome, e.industria.setor,
  pat.total_trabalhadores, pat.folha_mensal_estimada_brl,
  pat.qtd_municipios_atuacao
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN `data-hacker-488115.gold_pat.empresas` pat USING (cnpj_basico)
WHERE pat.total_trabalhadores > 50;
```

### 2.2 Energia (consumo BDGD/ANEEL)

**Tabela:** `gold_energia.estabelecimentos_consumo_certo` (granularidade: 1/UC, 1 CNPJ pode ter várias UCs).

**Campos-chave**: `kwh_medio_mensal`, `kwh_total_12m`, `distribuidora_nome`, `classe_consumo`, `grupo_tensao` (BT/MT/AT), `elegivel_acl`, `cnpj_tem_gd`, `lat`, `lon`, `municipio_ibge`.

**Agregação por CNPJ_BASICO** (1 empresa pode ter várias UCs):
```sql
WITH energia_por_cnpj AS (
  SELECT
    cnpj_basico,
    SUM(kwh_medio_mensal) AS kwh_total_grupo,
    AVG(kwh_medio_mensal) AS kwh_medio_uc,
    COUNT(*) AS qtd_ucs,
    ANY_VALUE(distribuidora_nome) AS distribuidora_amostra,
    LOGICAL_OR(elegivel_acl) AS tem_uc_acl,
    SUM(IFNULL(gd_potencia_kw, 0)) AS gd_total_kw
  FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
  GROUP BY cnpj_basico
)
SELECT e.cnpj_basico, e.nome, en.kwh_total_grupo, en.qtd_ucs
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN energia_por_cnpj en USING (cnpj_basico)
WHERE en.kwh_total_grupo >= 1000;
```

### 2.3 Pessoas (sócios/diretores)

**`gold_cnpj.pessoas`** já dedupa pessoas PF e mantém array de empresas onde aparece.

**Buscar empresas onde uma pessoa aparece** (via gold_cnpj.pessoas):
```sql
SELECT empresas_cnpj_basicos AS cnpjs_vinculados, qtd_empresas
FROM `data-hacker-488115.gold_cnpj.pessoas`
WHERE nome_norm = 'pedro zinner';
```

**Cruzar de volta com gold_cnpj.empresas:**
```sql
WITH pessoa AS (
  SELECT empresas_cnpj_basicos AS cnpjs
  FROM `data-hacker-488115.gold_cnpj.pessoas`
  WHERE nome_norm = 'pedro zinner'
)
SELECT e.cnpj_basico, e.nome, e.industria.setor, e.local.matriz.uf
FROM `data-hacker-488115.gold_cnpj.empresas` e, pessoa p
WHERE e.cnpj_basico IN UNNEST(p.cnpjs);
```

**Dentro do doc da empresa (sócio embutido):**
```sql
SELECT e.cnpj_basico, e.nome, adm.nome AS diretor, adm.qualificacao.descricao
FROM `data-hacker-488115.gold_cnpj.empresas` e,
UNNEST(e.socios.administradores_diretores) AS adm
WHERE adm.nome_norm = 'pedro zinner';
```

### 2.4 Bronze CNPJ (quando precisa do cru)

Quando gold v2 não tem o que precisa (ex: `_periodo` antigo, qualificação fora dos 4 buckets), volta pra `bronze_cnpj.*` com filtros padrão (`SITUACAO_CADASTRAL='02'`, `ANY_VALUE` em `empresas`, etc.). Detalhes em `references/01-tabelas-cnpj.md`.

---

## 3. Filtros canônicos no gold_cnpj.empresas

**Empresas operacionais comerciais (tira MEI, governo, OSC, MEI individual):**
```sql
WHERE status.operacional = 'ativa'
  AND status.natureza_juridica.categoria = 'empresarial'
  AND status.porte != 'mei'
```

**Por município (atenção: UPPERCASE!):**
```sql
WHERE local.matriz.municipio_nome = 'BELO HORIZONTE'
  AND local.matriz.uf = 'MG'
```

**Por setor (enum, não código CNAE):**
```sql
WHERE industria.setor = 'Financeiro'
```

**Por CNAE específico (prefix pra grupo):**
```sql
WHERE STARTS_WITH(industria.cnae_principal.codigo, '5611')   -- restaurantes/bares
```

**Recém-abertas:**
```sql
WHERE data_abertura >= DATE_SUB(CURRENT_DATE(), INTERVAL 24 MONTH)
```

**Com filial em UF específica:**
```sql
WHERE EXISTS (SELECT 1 FROM UNNEST(local.filiais) f WHERE f.uf = 'RJ')
```

**Com sócio PJ estrangeiro de país X:**
```sql
WHERE EXISTS (
  SELECT 1 FROM UNNEST(socios.pessoas_juridicas_estrangeiras) pj
  WHERE pj.pais.codigo = 'US'
)
```

**Com email corporativo de domínio específico:**
```sql
WHERE EXISTS (
  SELECT 1 FROM UNNEST(contato.emails) e
  WHERE e.dominio = 'stone.com.br'
)
```

**Capital social numérico:**
```sql
WHERE financeiro.capital_social_brl >= 1000000000   -- ≥ R$ 1bi
```

---

## 4. Templates SQL — perguntas-âncora

### 4.1 Cidades de MG com X empresas onde PAT > 50 funcionários

```sql
SELECT
  pat.municipio_matriz AS cidade,
  COUNT(DISTINCT pat.cnpj_basico) AS empresas,
  SUM(pat.total_trabalhadores) AS total_trabalhadores
FROM `data-hacker-488115.gold_pat.empresas` pat
WHERE pat.uf_matriz = 'MG'
  AND pat.total_trabalhadores > 50
GROUP BY cidade
ORDER BY empresas DESC;
```

> Se quiser filtrar lista específica de cidades: `AND pat.municipio_matriz IN ('BELO HORIZONTE', 'UBERLANDIA', 'CONTAGEM', ...)`.

### 4.2 Empresas em Maricá (RJ) ordenadas por consumo de energia

```sql
WITH energia AS (
  SELECT
    cnpj_basico,
    SUM(kwh_medio_mensal) AS kwh_total,
    AVG(kwh_medio_mensal) AS kwh_medio_uc,
    COUNT(*) AS qtd_ucs,
    ANY_VALUE(distribuidora_nome) AS distribuidora
  FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
  WHERE municipio_ibge = '3302858'   -- IBGE Maricá-RJ
  GROUP BY cnpj_basico
)
SELECT
  e.cnpj_basico,
  e.nome,
  e.industria.setor,
  e.industria.cnae_principal.descricao AS cnae,
  e.status.porte,
  ROUND(en.kwh_total, 0) AS kwh_total_grupo,
  en.qtd_ucs,
  en.distribuidora
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN energia en USING (cnpj_basico)
WHERE e.status.operacional = 'ativa'
ORDER BY en.kwh_total DESC
LIMIT 100;
```

> Não use `local.matriz.municipio_nome = 'MARICA'` aqui — pode ter empresas com matriz em outro município mas UC em Maricá. O filtro `municipio_ibge` na tabela energia é mais preciso.

### 4.3 Empresas grandes Financeiro com filial RJ + capital ≥ 1bi

```sql
SELECT
  e.cnpj_basico, e.nome, e.financeiro.capital_social_brl,
  ARRAY(SELECT f.uf FROM UNNEST(e.local.filiais) f) AS ufs_filiais
FROM `data-hacker-488115.gold_cnpj.empresas` e
WHERE e.status.porte = 'grande'
  AND e.industria.setor = 'Financeiro'
  AND e.financeiro.capital_social_brl >= 1000000000
  AND EXISTS (SELECT 1 FROM UNNEST(e.local.filiais) f WHERE f.uf = 'RJ')
ORDER BY e.financeiro.capital_social_brl DESC;
```

### 4.4 Cross-pessoa: rede de uma pessoa via CNPJ + setor

```sql
WITH alvo AS (
  SELECT empresas_cnpj_basicos AS cnpjs
  FROM `data-hacker-488115.gold_cnpj.pessoas`
  WHERE nome_norm = 'andre street de aguiar'
)
SELECT
  e.cnpj_basico, e.nome,
  e.industria.setor, e.local.matriz.uf,
  e.financeiro.capital_social_brl
FROM `data-hacker-488115.gold_cnpj.empresas` e, alvo
WHERE e.cnpj_basico IN UNNEST(alvo.cnpjs)
ORDER BY e.financeiro.capital_social_brl DESC;
```

### 4.5 ICP composto: empresa grande, setor X, com PAT, abertas <5 anos, com email corporativo

```sql
SELECT
  e.cnpj_basico, e.nome, e.idade_anos,
  e.industria.setor, pat.total_trabalhadores,
  ARRAY(SELECT em.dominio FROM UNNEST(e.contato.emails) em LIMIT 3) AS dominios
FROM `data-hacker-488115.gold_cnpj.empresas` e
LEFT JOIN `data-hacker-488115.gold_pat.empresas` pat USING (cnpj_basico)
WHERE e.status.operacional = 'ativa'
  AND e.status.porte IN ('media', 'grande')
  AND e.industria.setor = 'Comércio'
  AND e.idade_anos < 5
  AND ARRAY_LENGTH(e.contato.emails) > 0
  AND pat.total_trabalhadores >= 30
ORDER BY pat.total_trabalhadores DESC
LIMIT 100;
```

### 4.6 Top consumidores de energia em todo MG (cruza com porte)

```sql
WITH energia_mg AS (
  SELECT cnpj_basico, SUM(kwh_medio_mensal) AS kwh_total
  FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
  WHERE uf = 'MG'
  GROUP BY cnpj_basico
  HAVING kwh_total > 0
)
SELECT
  e.cnpj_basico, e.nome, e.industria.setor, e.status.porte,
  ROUND(en.kwh_total, 0) AS kwh_total_grupo
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN energia_mg en USING (cnpj_basico)
ORDER BY en.kwh_total DESC
LIMIT 50;
```

---

## 5. Acesso ao Elastic (mesmo gold espelhado)

`gold_cnpj.empresas` e `gold_cnpj.pessoas` também estão no **Elastic DEV** como índices `gold_cnpj_empresas` e `gold_cnpj_pessoas` (mapping em `infra/bigquery/cnpj/gold_mappings/*.json`). Use Elastic quando:
- Lookup por CNPJ_BASICO (1 doc, latência ms)
- Search texto livre por nome (analyzer pt-br + fuzziness)
- Dashboard Kibana

Use BQ pra **JOINs com gold_pat/gold_energia/etc.** — Elastic não tem JOIN nativo (cross-index exige 2 queries ou enrich processor).

---

## 6. Anti-padrões e armadilhas

1. **Não use `gold_cnpj.empresas` quando precisar de qualificações fora dos 4 buckets** (ex: qualif `08` = Conselheiro de Administração ainda não foi categorizada explicitamente). Vai pra `silver_cnpj.socios` ou `bronze_cnpj.socios`.

2. **`local.matriz.municipio_nome` é UPPERCASE**, sem acentos (segue padrão RFB). `'BELO HORIZONTE'` não `'Belo Horizonte'`.

3. **CNAE como prefix**: pra restaurantes/bares (`5611-2/01` a `5611-2/05`), use `STARTS_WITH(codigo, '5611')`. Pra holdings (`6463-8/00`), use `codigo = '6463800'`.

4. **Filiais ATIVAS embutidas** — Baixadas/Inaptas estão fora. Pra ver histórico de filial fechada, use `bronze_cnpj.estabelecimentos`.

5. **Empresas zero PAT são MAIORIA**: ~99% das 27.4M têm `pat = NULL`. PAT é programa opcional restrito a empregadores formais.

6. **Empresas zero energia também**: nem toda empresa tem UC própria (subloca, condomínio, sem operação física). ~94% sem dado.

7. **Múltiplas linhas por CNPJ_BASICO no `bronze_cnpj.empresas`** já foram dedupadas no gold via `ANY_VALUE`. Não precisa repetir.

8. **`SAFE_CAST(REPLACE(CAPITAL_SOCIAL, ',', '.') AS FLOAT64)`** só é necessário em bronze. No gold já está `FLOAT64` parseado.

9. **Sócios PJ estrangeiros sem `cnpj_basico`** — alguns documentos não são CNPJ brasileiro válido. Não JOIN com gold_cnpj.empresas (vai dar NULL).

10. **Pedro Zinner em `gold_cnpj.pessoas`**: o array `empresas_cnpj_basicos` cobre QUALQUER vínculo PF (cotista OU diretor). Pra distinguir, ver o array `qualificacoes_aparece`.

---

## 7. Pontos de evolução planejados

Roadmap em `docs/elastic/elastic-development/backlog/`. Próximos enrichs no doc gold:
- `pat` cluster — métricas PAT embutidas no doc
- `energia` cluster — consumo agregado embutido
- `cvm` cluster — companhias abertas (DFP/ITR)
- `bdc` cluster — contatos verificados (BigDataCorp)
- `industria.segmento` — sub-classificação comercial (SaaS B2B, Varejo Alimentar, etc.)
- `local.matriz.geo` — lat/lon via geocoding

Por enquanto, esses enrichs viram **JOIN com tabela paralela** (gold_pat, gold_energia) em vez de campo no doc.
