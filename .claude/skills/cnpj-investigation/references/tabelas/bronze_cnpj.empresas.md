# `bronze_cnpj.empresas` — Empresas RFB cru (raiz CNPJ)

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** 1 linha por **CNPJ_BASICO** (8d). **Quirk:** múltiplas linhas por CNPJ_BASICO podem aparecer (~0,3%) por inconsistência da fonte — sempre dedupe com `ANY_VALUE` antes de joinar.
**Linhas (~):** 67,642,315
**Chave:** `CNPJ_BASICO`
**Cluster BY:** — (sem clustering)
**Refresh:** mensal — pipeline `cnpj-weekly-download` domingo 08:00 BRT (snapshot RFB completo via `WRITE_TRUNCATE`).
**Origem:** Receita Federal — Casa dos Dados mirror (Cloudflare CDN). Doc: [`docs/cnpj/pipeline.md`](../../../../docs/cnpj/pipeline.md).

**Descrição BQ:** Snapshot mensal RFB. Fonte cru, todas colunas STRING (mesmo numéricos), strings em CAPS, capital social com vírgula PT-BR. Use silver/gold pra análise — bronze só pra auditoria/histórico.

---

## Quando usar

**Use somente** quando precisar de:
- Auditoria do dado RFB cru (códigos não-resolvidos, strings em CAPS)
- Snapshots históricos via `_periodo` (quando preservados)
- Capital social cru pra parsing customizado

**Pra análise comercial em geral, use [`gold_cnpj.empresas`](gold_cnpj.empresas.md)** — já dedupado por `CNPJ_BASICO`, com NJ/porte/qualif resolvidos pra enums, capital parseado FLOAT64, filiais agregadas. Bronze só pra debug.

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `CNPJ_BASICO` | STRING |  |  |
| `RAZAO_SOCIAL` | STRING |  |  |
| `NATUREZA_JURIDICA` | STRING |  |  |
| `QUALIFICACAO_RESPONSAVEL` | STRING |  |  |
| `CAPITAL_SOCIAL` | STRING |  |  |
| `PORTE` | STRING |  |  |
| `ENTE_FEDERATIVO_RESPONSAVEL` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "CNPJ_BASICO": "00325378",
    "RAZAO_SOCIAL": "4 DE OUTUBRO COMERCIO E PARTICIPACOES S/A",
    "NATUREZA_JURIDICA": "2054",
    "QUALIFICACAO_RESPONSAVEL": "10",
    "CAPITAL_SOCIAL": "300000,00",
    "PORTE": "01",
    "ENTE_FEDERATIVO_RESPONSAVEL": null,
    "_arquivo_origem": "Empresas1.zip",
    "_data_carga": "2026-04-22T18:25:17+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "02333456",
    "RAZAO_SOCIAL": "CHAVEIRO BACHMANN LTDA",
    "NATUREZA_JURIDICA": "2062",
    "QUALIFICACAO_RESPONSAVEL": "49",
    "CAPITAL_SOCIAL": "0,00",
    "PORTE": "01",
    "ENTE_FEDERATIVO_RESPONSAVEL": null,
    "_arquivo_origem": "Empresas1.zip",
    "_data_carga": "2026-04-22T18:25:17+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "02336566",
    "RAZAO_SOCIAL": "LIGUE BIKE COMERCIO DE PECAS E ACESSORIOS LTDA",
    "NATUREZA_JURIDICA": "2062",
    "QUALIFICACAO_RESPONSAVEL": "49",
    "CAPITAL_SOCIAL": "0,00",
    "PORTE": "01",
    "ENTE_FEDERATIVO_RESPONSAVEL": null,
    "_arquivo_origem": "Empresas1.zip",
    "_data_carga": "2026-04-22T18:25:17+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "02336969",
    "RAZAO_SOCIAL": "MBM AUTO PECAS LTDA",
    "NATUREZA_JURIDICA": "2062",
    "QUALIFICACAO_RESPONSAVEL": "49",
    "CAPITAL_SOCIAL": "50000,00",
    "PORTE": "01",
    "ENTE_FEDERATIVO_RESPONSAVEL": null,
    "_arquivo_origem": "Empresas1.zip",
    "_data_carga": "2026-04-22T18:25:17+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "02345427",
    "RAZAO_SOCIAL": "BRACAL FERRAMENTAS E COMERCIO LTDA",
    "NATUREZA_JURIDICA": "2062",
    "QUALIFICACAO_RESPONSAVEL": "49",
    "CAPITAL_SOCIAL": "0,00",
    "PORTE": "01",
    "ENTE_FEDERATIVO_RESPONSAVEL": null,
    "_arquivo_origem": "Empresas1.zip",
    "_data_carga": "2026-04-22T18:25:17+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.empresas\` LIMIT 5'`

## Quirks e armadilhas

- **`CAPITAL_SOCIAL` é STRING com vírgula PT-BR**: `'139415761,40'`. Sempre `SAFE_CAST(REPLACE(CAPITAL_SOCIAL, ',', '.') AS FLOAT64)`. SAFE_CAST direto retorna NULL pra valores com vírgula — perda silenciosa.
- **Múltiplas linhas por CNPJ_BASICO**: ~0,3% dos CNPJs aparecem 2× (carga histórica `_periodo`). Sempre `GROUP BY CNPJ_BASICO` com `ANY_VALUE` antes de joinar.
- **`PORTE='01'` é Microempresa, NÃO MEI**. MEI vem de `simples.OPCAO_MEI='S'` ou `NATUREZA_JURIDICA='2135'`.
- **`PORTE='05'` é "Demais"** — engloba média e grande sem distinguir. Pra distinguir, precisa fonte externa (CVM, BDC, faturamento).
- **`NATUREZA_JURIDICA` é STRING 4d**. Faixas: `1xxx`=adm pública, `2xxx`=empresarial, `3xxx`=sem fins lucrativos, `4xxx`=PF individual, `5xxx`=organismo internacional.
- **Datas em STRING `YYYYMMDD`** (ex: `'20210324'`). Use `PARSE_DATE('%Y%m%d', NULLIF(campo, '0'))`. Cuidado com `'0'` ou `'00000000'` (datas inválidas).
- **`_periodo`** indica snapshot bronze (`YYYYMM`). Atualmente só tem o último snapshot — histórico não preservado (ver [`docs/cnpj/backlog.md`](../../../../docs/cnpj/backlog.md) §1).

## Tabelas relacionadas

- [`bronze_cnpj.estabelecimentos`](bronze_cnpj.estabelecimentos.md) — endereço/situação por estabelecimento (matriz + filiais)
- [`bronze_cnpj.socios`](bronze_cnpj.socios.md) — QSA por CNPJ_BASICO
- [`bronze_cnpj.simples`](bronze_cnpj.simples.md) — OPCAO_SIMPLES, OPCAO_MEI
- [`bronze_cnpj.naturezas`](bronze_cnpj.naturezas.md) — dim NJ código → descrição
- [`bronze_cnpj.qualificacoes`](bronze_cnpj.qualificacoes.md) — dim qualif código → descrição
- [`gold_cnpj.empresas`](gold_cnpj.empresas.md) — derivado limpo desta + estabelecimentos/socios/simples + dimensões

## Templates SQL

### Caso A: dedupe e join com naturezas
```sql
SELECT
  e.CNPJ_BASICO,
  e.RAZAO_SOCIAL,
  e.PORTE,
  nj.DESCRICAO AS natureza_juridica_desc,
  SAFE_CAST(REPLACE(e.CAPITAL_SOCIAL, ',', '.') AS FLOAT64) AS capital_social_brl
FROM (
  SELECT CNPJ_BASICO,
         ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL,
         ANY_VALUE(PORTE) AS PORTE,
         ANY_VALUE(NATUREZA_JURIDICA) AS NATUREZA_JURIDICA,
         ANY_VALUE(CAPITAL_SOCIAL) AS CAPITAL_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas`
  GROUP BY CNPJ_BASICO
) e
LEFT JOIN `data-hacker-488115.bronze_cnpj.naturezas` nj
  ON e.NATUREZA_JURIDICA = nj.CODIGO
WHERE e.CNPJ_BASICO = '16501555';
```

### Caso B: top capital social (bilionários)
```sql
SELECT
  CNPJ_BASICO,
  ANY_VALUE(RAZAO_SOCIAL) AS razao_social,
  MAX(SAFE_CAST(REPLACE(CAPITAL_SOCIAL, ',', '.') AS FLOAT64)) AS capital_brl
FROM `data-hacker-488115.bronze_cnpj.empresas`
GROUP BY CNPJ_BASICO
HAVING capital_brl >= 1000000000
ORDER BY capital_brl DESC
LIMIT 50;
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
