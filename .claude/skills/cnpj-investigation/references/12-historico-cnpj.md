# Cookbook — usando o histórico CNPJ pra mapear mudanças

Receitas prontas pra consultar `silver_cnpj_history.*_versionada` e detectar evolução temporal de empresas brasileiras.

> **Quando NÃO usar este doc**: pra qualquer consulta normal sobre o estado atual de uma empresa, use **`silver_cnpj.*`** ou **`gold_cnpj.*`**. Essas tabelas têm o snapshot vigente, são mais rápidas (menores) e são as fontes oficiais. O histórico é **complemento** — pra análises profundas, quando a pergunta envolve "o que mudou", "desde quando", "trajetória", "entrou/saiu".

---

## 1. Quando usar (e quando não)

| Pergunta | Use | Não use |
|---|---|---|
| "Qual o capital atual desta empresa?" | `silver_cnpj.empresas` | histórico |
| "Esta empresa está ativa hoje?" | `silver_cnpj.estabelecimentos` | histórico |
| "Quem é sócio deste CNPJ agora?" | `silver_cnpj.socios` | histórico |
| "Quando esta empresa aumentou capital?" | **`silver_cnpj_history.empresas_versionada`** | silver_cnpj |
| "Esta empresa já foi baixada e voltou?" | **`silver_cnpj_history.estabelecimentos_versionada`** | silver_cnpj |
| "Quem entrou e saiu do quadro societário no último ano?" | **`silver_cnpj_history.socios_versionada`** | silver_cnpj |
| "Empresas que aderiram ao MEI nos últimos 6 meses" | **`silver_cnpj_history.simples_versionada`** | silver_cnpj |
| "Trajetória completa do CNPJ X" | **histórico** | silver_cnpj |
| "Empresas que mudaram de UF" | **histórico** | silver_cnpj |

**Regra de bolso**: se a query usa `_periodo_inicio`, `_periodo_fim`, `LAG()`, ou compara versões — é histórico. Se só precisa do "agora" — silver/gold normal.

---

## 2. Tabelas disponíveis

Todas em `data-hacker-488115.silver_cnpj_history.*`:

| Tabela | Chave | Comparáveis (que detectam mudanças) |
|---|---|---|
| `empresas_versionada` | `CNPJ_BASICO` | `RAZAO_SOCIAL`, `CAPITAL_SOCIAL`, `PORTE`, `NATUREZA_JURIDICA`, `QUALIFICACAO_RESPONSAVEL`, `ENTE_FEDERATIVO_RESPONSAVEL` |
| `estabelecimentos_versionada` | `CNPJ_BASICO + CNPJ_ORDEM + CNPJ_DV` | `SITUACAO_CADASTRAL`, `LOGRADOURO`, `NUMERO`, `BAIRRO`, `CEP`, `UF`, `MUNICIPIO`, `CNAE_FISCAL_PRINCIPAL`, `CNAE_FISCAL_SECUNDARIA`, `NOME_FANTASIA`, `CORREIO_ELETRONICO`, `TELEFONE1`, `TELEFONE2`, `DATA_INICIO_ATIVIDADE`, `DATA_SITUACAO_CADASTRAL`, `MOTIVO_SITUACAO_CADASTRAL`, etc. (29 colunas) |
| `socios_versionada` | `CNPJ_BASICO + NOME_SOCIO + DATA_ENTRADA_SOCIEDADE` | `QUALIFICACAO_SOCIO`, `CNPJ_CPF_SOCIO`, `REPRESENTANTE_LEGAL`, `NOME_REPRESENTANTE`, `FAIXA_ETARIA` |
| `simples_versionada` | `CNPJ_BASICO` | `OPCAO_SIMPLES`, `OPCAO_MEI`, `DATA_OPCAO_SIMPLES`, `DATA_EXCLUSAO_SIMPLES`, `DATA_OPCAO_MEI`, `DATA_EXCLUSAO_MEI` |

### Schema das versionadas

Toda linha tem 3 colunas SCD Type 2 além do dataset:

```
_versao_hash      INT64    — FARM_FINGERPRINT das colunas comparáveis (identifica versões idênticas)
_periodo_inicio   STRING   — primeiro YYYYMM em que essa versão foi observada (ex: '202405')
_periodo_fim      STRING   — último YYYYMM em que essa versão foi observada (ex: '202411')
```

Range de períodos cobertos: **2023-05 a 2026-04** (mensal, 36 períodos).

### Como ler 1 linha versionada

```
CNPJ_BASICO=33000167  RAZAO_SOCIAL=PETROBRAS  CAPITAL_SOCIAL=205431960490,52
_periodo_inicio=202305  _periodo_fim=202604
```

→ "Esta versão (Petrobras com este capital) foi observada de **maio/2023** até **abril/2026** (todo o range), ou seja: estável."

```
CNPJ_BASICO=12345678  CAPITAL_SOCIAL=10000000  _periodo_inicio=202305  _periodo_fim=202410
CNPJ_BASICO=12345678  CAPITAL_SOCIAL=50000000  _periodo_inicio=202411  _periodo_fim=202604
```

→ "CNPJ aumentou capital de R$10M pra R$50M entre **out/2024 e nov/2024**."

---

## 3. Como consultar — patterns básicos

### 3.1 Trajetória de 1 CNPJ específico

```sql
SELECT _periodo_inicio, _periodo_fim,
       RAZAO_SOCIAL, CAPITAL_SOCIAL, PORTE
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
WHERE CNPJ_BASICO = '33000167'  -- Petrobras
ORDER BY _periodo_inicio;
```

- 1 linha → estável.
- N linhas → mudou N-1 vezes.

### 3.2 Versão vigente em uma data específica

```sql
-- Qual era o capital deste CNPJ em julho/2024?
SELECT RAZAO_SOCIAL, CAPITAL_SOCIAL
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
WHERE CNPJ_BASICO = '12345678'
  AND _periodo_inicio <= '202407'
  AND _periodo_fim >= '202407';
```

### 3.3 Filtrar quem mudou pelo menos uma vez

```sql
WITH counts AS (
  SELECT CNPJ_BASICO, COUNT(*) AS n_versoes
  FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
  GROUP BY CNPJ_BASICO
)
SELECT * FROM counts WHERE n_versoes >= 2;
```

### 3.4 Pegar última versão de cada CNPJ

```sql
SELECT *
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
QUALIFY ROW_NUMBER() OVER (PARTITION BY CNPJ_BASICO ORDER BY _periodo_inicio DESC) = 1;
```

---

## 4. Tipos de mudança detectáveis

### 4.1 Empresas (cadastro PJ)

| Campo | O que detecta | Volume típico (sobre 67M CNPJs) |
|---|---|---:|
| `RAZAO_SOCIAL` | rebrand, formalização ME→LTDA, mudança de nome empresa individual | 4.2M (6.3%) |
| `CAPITAL_SOCIAL` | aporte, AGE, redução de capital | 1.6M (2.4%) |
| `PORTE` | crescimento (ME→EPP→DEMAIS) ou redução | 242K (0.4%) |
| `NATUREZA_JURIDICA` | mudança de tipo societário (LTDA→S/A, etc) | 833K (1.2%) |
| `QUALIFICACAO_RESPONSAVEL` | mudança de cargo do administrador | 961K (1.4%) |

### 4.2 Estabelecimentos (CNPJ completo 14 dígitos)

| Campo | O que detecta | Volume típico (sobre 70M unidades) |
|---|---|---:|
| `SITUACAO_CADASTRAL` | ativação/baixa/suspensão/inaptidão | **10.9M (15.4%)** |
| `LOGRADOURO`, `NUMERO`, `CEP`, `BAIRRO` | mudança de endereço | ~3M (~4%) |
| `MUNICIPIO` | mudança de cidade | 892K (1.3%) |
| `UF` | mudança de estado | 232K (0.3%) |
| `CNAE_FISCAL_PRINCIPAL` | pivô de negócio | 2.6M (3.7%) |
| `CNAE_FISCAL_SECUNDARIA` | adição/remoção de atividades | 2.7M (3.8%) |
| `NOME_FANTASIA` | rebrand do estabelecimento | 874K (1.2%) |
| `CORREIO_ELETRONICO` | troca de email | 2.6M (3.6%) |
| `TELEFONE1` | troca de telefone | 2.5M (3.5%) |

**Códigos de SITUACAO_CADASTRAL**: `01`=NULA, `02`=ATIVA, `03`=SUSPENSA, `04`=INAPTA, `08`=BAIXADA.

### 4.3 Sócios

| Tipo | O que detecta | Volume típico |
|---|---|---:|
| Sócio que **entrou** | `_periodo_inicio > '202305'` (snapshot mais antigo) | 9.7M empresas |
| Sócio que **saiu** | `_periodo_fim < '202604'` (snapshot mais recente) | 6.2M empresas |
| Sócio temporário | entrou e saiu dentro do range | 1.2M empresas |
| Mudança de qualificação | mesma chave (CNPJ+nome+data_entrada), `QUALIFICACAO_SOCIO` mudou | dezenas de milhares |
| Mudança de nome (mesma pessoa) | `DATA_ENTRADA_SOCIEDADE + CNPJ_CPF_SOCIO` iguais, `NOME_SOCIO` diferente | dezenas de milhares (estado civil, correção) |

**Atenção**: a chave do `socios_versionada` inclui `NOME_SOCIO`. Mudança de nome (ex: "TARCIANE OLIVEIRA SOARES" → "TARCIANE SOARES OLIVEIRA") aparece como saída + entrada. Pra detectar a mesma pessoa, joinar por `(CNPJ_BASICO, CNPJ_CPF_SOCIO, DATA_ENTRADA_SOCIEDADE)`.

### 4.4 Simples / MEI

| Transição | Volume típico |
|---|---:|
| Aderiram ao Simples (N→S) | 86K |
| Saíram do Simples (S→N) | 8.8M |
| Aderiram ao MEI (N→S) | 44K |
| Saíram do MEI (S→N) | 7.6M |

---

## 5. Receitas por caso de uso

### 5.1 "Top 10 maiores aumentos de capital social no último ano"

```sql
WITH com_versoes AS (
  SELECT CNPJ_BASICO FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
  GROUP BY CNPJ_BASICO HAVING COUNT(*) >= 2
),
extremos AS (
  SELECT v.CNPJ_BASICO,
    MIN_BY(STRUCT(v.RAZAO_SOCIAL, v.CAPITAL_SOCIAL, v._periodo_inicio), v._periodo_inicio) AS antiga,
    MAX_BY(STRUCT(v.CAPITAL_SOCIAL, v._periodo_fim), v._periodo_fim) AS nova
  FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada` v
  JOIN com_versoes USING (CNPJ_BASICO)
  WHERE v._periodo_fim >= '202504'  -- só ativas no último ano
  GROUP BY v.CNPJ_BASICO
)
SELECT
  CNPJ_BASICO, antiga.RAZAO_SOCIAL,
  SAFE_CAST(REPLACE(antiga.CAPITAL_SOCIAL, ',', '.') AS BIGNUMERIC) AS cap_antigo,
  SAFE_CAST(REPLACE(nova.CAPITAL_SOCIAL, ',', '.') AS BIGNUMERIC) AS cap_novo,
  antiga._periodo_inicio AS desde, nova._periodo_fim AS ate
FROM extremos
WHERE SAFE_CAST(REPLACE(antiga.CAPITAL_SOCIAL,',','.') AS BIGNUMERIC) > 1000000
  AND SAFE_CAST(REPLACE(nova.CAPITAL_SOCIAL,',','.') AS BIGNUMERIC) > SAFE_CAST(REPLACE(antiga.CAPITAL_SOCIAL,',','.') AS BIGNUMERIC) * 10
ORDER BY cap_novo - cap_antigo DESC
LIMIT 10;
```

### 5.2 "Empresas que mudaram de UF (mudança de estado)"

```sql
WITH mudou AS (
  SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV,
    ARRAY_AGG(DISTINCT UF IGNORE NULLS ORDER BY UF) AS ufs
  FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
  GROUP BY CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV
  HAVING ARRAY_LENGTH(ARRAY_AGG(DISTINCT UF IGNORE NULLS)) >= 2
)
SELECT * FROM mudou LIMIT 100;
-- ~232K estabelecimentos no total
```

### 5.3 "Estabelecimentos baixados nos últimos 12 meses (com data exata)"

```sql
WITH versoes AS (
  SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV, SITUACAO_CADASTRAL,
    _periodo_inicio, _periodo_fim,
    LAG(SITUACAO_CADASTRAL) OVER (
      PARTITION BY CNPJ_BASICO,CNPJ_ORDEM,CNPJ_DV ORDER BY _periodo_inicio
    ) AS prev_sit
  FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
)
SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV,
  prev_sit AS situacao_anterior,
  SITUACAO_CADASTRAL AS situacao_nova,
  _periodo_inicio AS data_mudanca
FROM versoes
WHERE prev_sit = '02' AND SITUACAO_CADASTRAL = '08'
  AND _periodo_inicio >= '202504';  -- últimos 12 meses
```

### 5.4 "Trajetória completa de 1 CNPJ (todos os datasets)"

```sql
DECLARE alvo STRING DEFAULT '33000167';  -- Petrobras

-- Empresa
SELECT 'empresas' AS dataset, _periodo_inicio, _periodo_fim,
  TO_JSON_STRING(STRUCT(RAZAO_SOCIAL, CAPITAL_SOCIAL, PORTE)) AS dados
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
WHERE CNPJ_BASICO = alvo

UNION ALL SELECT 'estabelecimentos',  _periodo_inicio, _periodo_fim,
  TO_JSON_STRING(STRUCT(CNPJ_ORDEM, CNPJ_DV, SITUACAO_CADASTRAL, UF, MUNICIPIO, CNAE_FISCAL_PRINCIPAL))
FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
WHERE CNPJ_BASICO = alvo

UNION ALL SELECT 'socios', _periodo_inicio, _periodo_fim,
  TO_JSON_STRING(STRUCT(NOME_SOCIO, QUALIFICACAO_SOCIO, DATA_ENTRADA_SOCIEDADE))
FROM `data-hacker-488115.silver_cnpj_history.socios_versionada`
WHERE CNPJ_BASICO = alvo

UNION ALL SELECT 'simples', _periodo_inicio, _periodo_fim,
  TO_JSON_STRING(STRUCT(OPCAO_SIMPLES, OPCAO_MEI))
FROM `data-hacker-488115.silver_cnpj_history.simples_versionada`
WHERE CNPJ_BASICO = alvo

ORDER BY dataset, _periodo_inicio;
```

### 5.5 "Empresas onde fulano entrou como sócio"

```sql
SELECT s.CNPJ_BASICO, s.NOME_SOCIO, s.QUALIFICACAO_SOCIO,
  s._periodo_inicio AS entrou_em,
  s._periodo_fim AS visto_ate,
  e.RAZAO_SOCIAL
FROM `data-hacker-488115.silver_cnpj_history.socios_versionada` s
LEFT JOIN `data-hacker-488115.silver_cnpj.empresas` e USING (CNPJ_BASICO)
WHERE UPPER(s.NOME_SOCIO) LIKE '%FULANO DE TAL%'
  AND s._periodo_inicio > '202305';  -- entrou DEPOIS do snapshot mais antigo
```

### 5.6 "Empresas que aderiram ao Simples nos últimos 12 meses"

```sql
WITH versoes AS (
  SELECT CNPJ_BASICO, OPCAO_SIMPLES, _periodo_inicio,
    LAG(OPCAO_SIMPLES) OVER (PARTITION BY CNPJ_BASICO ORDER BY _periodo_inicio) AS prev
  FROM `data-hacker-488115.silver_cnpj_history.simples_versionada`
)
SELECT CNPJ_BASICO, _periodo_inicio AS aderiu_em
FROM versoes
WHERE prev = 'N' AND OPCAO_SIMPLES = 'S'
  AND _periodo_inicio >= '202504';
```

### 5.7 "Empresas que mudaram CNAE principal (pivô de negócio)"

```sql
WITH mudou AS (
  SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV,
    ARRAY_AGG(STRUCT(CNAE_FISCAL_PRINCIPAL AS cnae, _periodo_inicio AS p) ORDER BY _periodo_inicio) AS hist
  FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
  GROUP BY CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV
  HAVING COUNT(DISTINCT CNAE_FISCAL_PRINCIPAL) >= 2
)
SELECT
  CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV,
  hist[OFFSET(0)].cnae AS cnae_inicial,
  hist[OFFSET(ARRAY_LENGTH(hist)-1)].cnae AS cnae_atual,
  hist[OFFSET(ARRAY_LENGTH(hist)-1)].p AS desde
FROM mudou
LIMIT 100;
```

### 5.8 "Sócios que entraram E saíram no mesmo ano (sinal de instabilidade)"

```sql
SELECT CNPJ_BASICO, NOME_SOCIO,
  _periodo_inicio AS entrou,
  _periodo_fim AS saiu,
  TIMESTAMP_DIFF(
    PARSE_TIMESTAMP('%Y%m', _periodo_fim),
    PARSE_TIMESTAMP('%Y%m', _periodo_inicio),
    MONTH
  ) AS meses_no_quadro
FROM `data-hacker-488115.silver_cnpj_history.socios_versionada`
WHERE _periodo_inicio > '202305'    -- entrou após início
  AND _periodo_fim < '202604'        -- saiu antes do fim
  AND _periodo_inicio[0:4] = _periodo_fim[0:4]  -- mesmo ano
ORDER BY meses_no_quadro;
```

### 5.9 "Empresa em dificuldade: ATIVA → INAPTA recente"

```sql
WITH versoes AS (
  SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV, SITUACAO_CADASTRAL,
    _periodo_inicio, _periodo_fim,
    LAG(SITUACAO_CADASTRAL) OVER (
      PARTITION BY CNPJ_BASICO,CNPJ_ORDEM,CNPJ_DV ORDER BY _periodo_inicio
    ) AS prev
  FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
)
SELECT *,
  CASE
    WHEN prev = '02' AND SITUACAO_CADASTRAL = '04' THEN '▼ ficou_inapta'
    WHEN prev = '02' AND SITUACAO_CADASTRAL = '03' THEN '▼ suspensa'
    WHEN prev = '04' AND SITUACAO_CADASTRAL = '02' THEN '▲ recuperou'
  END AS evento
FROM versoes
WHERE _periodo_inicio >= '202510'
  AND ((prev = '02' AND SITUACAO_CADASTRAL IN ('03','04'))
       OR (prev = '04' AND SITUACAO_CADASTRAL = '02'));
```

### 5.10 "Empresa que ressuscitou (BAIXADA → ATIVA)"

```sql
WITH versoes AS (
  SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV, SITUACAO_CADASTRAL,
    _periodo_inicio,
    LAG(SITUACAO_CADASTRAL) OVER (
      PARTITION BY CNPJ_BASICO,CNPJ_ORDEM,CNPJ_DV ORDER BY _periodo_inicio
    ) AS prev
  FROM `data-hacker-488115.silver_cnpj_history.estabelecimentos_versionada`
)
SELECT CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV, _periodo_inicio AS data_reativacao
FROM versoes
WHERE prev = '08' AND SITUACAO_CADASTRAL = '02';
-- raros — ~3.900 ocorrências em 36 meses
```

---

## 6. Boas práticas

### 6.1 Sempre filtrar por chave (cluster)

Tabelas versionadas são clusterizadas por chave principal. Filtros pela chave fazem cluster pruning automático:

```sql
-- ✅ FAST (cluster pruning)
WHERE CNPJ_BASICO = '12345678'
WHERE CNPJ_BASICO IN ('12345678', '87654321')

-- ❌ SLOW (full scan)
WHERE LOWER(RAZAO_SOCIAL) LIKE '%foo%'
```

Pra busca por razão social ou CNAE, primeiro filtre pela tabela `silver_cnpj.empresas` (busca textual indexada lá), depois join no histórico:

```sql
WITH alvos AS (
  SELECT CNPJ_BASICO FROM `data-hacker-488115.silver_cnpj.empresas`
  WHERE LOWER(RAZAO_SOCIAL) LIKE '%palmeiras%'
)
SELECT v.* FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada` v
JOIN alvos USING (CNPJ_BASICO);
```

### 6.2 Sempre filtrar por `_periodo_inicio` quando faz sentido

Reduz o conjunto processado. Period-pruning por intervalo é eficiente:

```sql
-- "Mudanças nos últimos 6 meses"
WHERE _periodo_inicio >= '202510'
```

### 6.3 Use `silver_cnpj_history.<dataset>` mas NÃO `bronze_cnpj_history.<dataset>`

- `silver_cnpj_history.*_versionada`: 273M linhas, comprimida (1 linha por versão estável). **Use SEMPRE.**
- `bronze_cnpj_history.<dataset>`: 1.3B+ linhas (1 linha por (CNPJ × período)). Só pra debug/auditoria, queries 5× mais caras.

### 6.4 Casos âncora pra debug

Se sua query retorna resultados estranhos, valide com casos conhecidos:

```sql
-- Petrobras: estável, 1 linha
SELECT _periodo_inicio, _periodo_fim
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
WHERE CNPJ_BASICO = '33000167';
-- esperado: 1 linha 202305→202604

-- Petra Holdings: aumentou capital ~3000×
SELECT _periodo_inicio, _periodo_fim, CAPITAL_SOCIAL
FROM `data-hacker-488115.silver_cnpj_history.empresas_versionada`
WHERE CNPJ_BASICO = '13517041'
ORDER BY _periodo_inicio;
-- esperado: 2+ linhas, capital crescendo
```

### 6.5 Cuidado com BIGNUMERIC e formato pt-BR

`CAPITAL_SOCIAL` vem como STRING formato pt-BR (`120000000000,00`). Pra fazer aritmética:

```sql
SAFE_CAST(REPLACE(CAPITAL_SOCIAL, ',', '.') AS BIGNUMERIC)
```

`SAFE_CAST` retorna NULL em valores inválidos em vez de erro.

---

## 7. Limitações conhecidas

| Limite | Detalhe |
|---|---|
| **Granularidade temporal** | mensal (1 mês mínimo entre eventos detectáveis). Mudanças que aconteceram e foram revertidas no mesmo mês ficam invisíveis |
| **Range histórico** | maio/2023 → abril/2026 (36 meses). Antes disso, RFB SERPRO+ não tem dados |
| **Renomeação de pessoa** | sócio com mudança de nome aparece como saída + entrada (chave inclui NOME_SOCIO). Use `CNPJ_CPF_SOCIO + DATA_ENTRADA_SOCIEDADE` pra detectar mesma pessoa |
| **CNPJ baixado e re-aberto** | aparece como entidades distintas. Pra ligar, joinar `socios_versionada` por `CNPJ_CPF_SOCIO + NOME_SOCIO` cross-CNPJ |
| **Histórico antes de 2023-05** | indisponível. Capital ou razão social anteriores ao primeiro snapshot ficam desconhecidos |

---

## 8. Como o histórico é alimentado

- **Backfill one-shot** (já feito): 36 snapshots da RFB SERPRO+ baixados e processados.
- **Cadência mensal**: hook em `scripts/cnpj/download.py` produtivo (`cnpj-weekly-download`, domingo 08:00 BRT) preserva `bronze_cnpj` na partição `bronze_cnpj_history.<dataset>$<periodo>` antes do TRUNCATE; rebuild da versionada ocorre depois.
- **Latência**: 1 a 7 dias após o release público da RFB.

Detalhes em [`historico-pipeline.md`](historico-pipeline.md).

---

## 9. Referência rápida

```
SILVER (default — estado atual)        SILVER HISTORY (complemento — mudanças)
silver_cnpj.empresas                   silver_cnpj_history.empresas_versionada
silver_cnpj.estabelecimentos           silver_cnpj_history.estabelecimentos_versionada
silver_cnpj.socios                     silver_cnpj_history.socios_versionada
silver_cnpj.simples                    silver_cnpj_history.simples_versionada
                                       (+ _versao_hash, _periodo_inicio, _periodo_fim)
```

**Quando em dúvida**: comece pela silver normal. Se a pergunta envolve "mudança", "trajetória", "entrou/saiu", "desde quando" — vá pro histórico.
