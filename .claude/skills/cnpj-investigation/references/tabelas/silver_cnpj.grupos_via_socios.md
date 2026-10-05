# `silver_cnpj.grupos_via_socios` — _TODO: título curto_

**Tipo:** VIEW
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** (view, sem contagem)
**Chave:** _TODO_
**Cluster BY:** —
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj_a` | STRING |  |  |
| `cnpj_b` | STRING |  |  |
| `holdings_em_comum` | STRING | REPEATED |  |
| `n_holdings_em_comum` | INTEGER |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_a": "36829095",
    "cnpj_b": "40392489",
    "holdings_em_comum": [
      "31237773"
    ],
    "n_holdings_em_comum": 1
  },
  {
    "cnpj_a": "36829095",
    "cnpj_b": "40683562",
    "holdings_em_comum": [
      "31237773"
    ],
    "n_holdings_em_comum": 1
  },
  {
    "cnpj_a": "41000737",
    "cnpj_b": "41237643",
    "holdings_em_comum": [
      "31237773"
    ],
    "n_holdings_em_comum": 1
  },
  {
    "cnpj_a": "36253782",
    "cnpj_b": "36829507",
    "holdings_em_comum": [
      "31237773"
    ],
    "n_holdings_em_comum": 1
  },
  {
    "cnpj_a": "45095118",
    "cnpj_b": "45432389",
    "holdings_em_comum": [
      "31237773"
    ],
    "n_holdings_em_comum": 1
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.grupos_via_socios\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.grupos_via_socios`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
