# `<dataset>.<tabela>` — _título curto descritivo_

**Tipo:** TABLE | VIEW
**Camada:** bronze | silver | gold
**Granularidade:** 1 linha por _<unidade>_
**Linhas (~):** _N_
**Chave:** _campo(s) que identificam unicamente uma linha_
**Cluster BY:** _campos pra particionamento físico (se TABLE)_
**Refresh:** mensal | semanal | sob demanda
**Origem:** _de onde vem o dado (RFB, PAT/MTE, BDGD/ANEEL, derivado de X, etc.)_

**Descrição BQ:** _description da tabela no BQ (`bq show <ref>`)_

---

## Quando usar

_1-3 frases. Pra responder X. Não use pra Y — em vez disso use Z._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `coluna1` | STRING | REQUIRED | descrição |
| `coluna2` | INT64 |  | descrição |

(gerado por `_gen_table_doc.py` — não editar manualmente)

## Sample (5 linhas reais)

```json
[
  { "coluna1": "...", "coluna2": 123 }
]
```

(gerado por `_gen_table_doc.py`)

## Quirks e armadilhas

- _Padrão comum que causa bug._
- _Ex: capital_social é STRING com vírgula → `SAFE_CAST(REPLACE(..., ',', '.') AS FLOAT64)`._
- _Ex: SITUACAO_CADASTRAL='02' obrigatório pra filtrar ATIVA — sem isso 60% é ruído._

## Tabelas relacionadas

- [`<dataset>.<outra>`](<dataset>.<outra>.md) — descrição da relação (FK, dimensão, derivado de)

## Templates SQL

### Caso A: _descrição curta_
```sql
SELECT ...
FROM `data-hacker-488115.<dataset>.<tabela>`
WHERE ...
```

### Caso B: _descrição curta_
```sql
SELECT ...
```

## Histórico

- AAAA-MM-DD: criado
