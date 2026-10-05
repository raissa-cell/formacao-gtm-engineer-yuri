# `silver_cnpj.rede_executivos` — _TODO: título curto_

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
| `socio_nome_norm` | STRING |  |  |
| `socio_nome` | STRING |  |  |
| `n_empresas` | INTEGER |  |  |
| `amostra_cnpjs` | STRING | REPEATED |  |

## Sample (5 linhas reais)

```json
[
  {
    "socio_nome_norm": "marcio antonio bernardes",
    "socio_nome": "MARCIO ANTONIO BERNARDES",
    "n_empresas": 6,
    "amostra_cnpjs": [
      "07230314",
      "14294693",
      "49170574",
      "57071797",
      "72991573",
      "74467184"
    ]
  },
  {
    "socio_nome_norm": "renato souza de medeiros",
    "socio_nome": "RENATO SOUZA DE MEDEIROS",
    "n_empresas": 5,
    "amostra_cnpjs": [
      "04467314",
      "56688184",
      "57447585",
      "59572298",
      "85339679"
    ]
  },
  {
    "socio_nome_norm": "cassiano welter bocchese",
    "socio_nome": "CASSIANO WELTER BOCCHESE",
    "n_empresas": 6,
    "amostra_cnpjs": [
      "02647448",
      "03241515",
      "05404742",
      "14238235",
      "53353507",
      "90312810"
    ]
  },
  {
    "socio_nome_norm": "alesandra de andrade",
    "socio_nome": "ALESANDRA DE ANDRADE",
    "n_empresas": 8,
    "amostra_cnpjs": [
      "06632149",
      "13728424",
      "15082896",
      "17915005",
      "34407667",
      "45904060",
      "62330695",
      "63122002"
    ]
  },
  {
    "socio_nome_norm": "raimundo roque pinto filho",
    "socio_nome": "RAIMUNDO ROQUE PINTO FILHO",
    "n_empresas": 7,
    "amostra_cnpjs": [
      "11833336",
      "14677308",
      "15114342",
      "15262275",
      "29410814",
      "33717986",
      "64795187"
    ]
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.rede_executivos\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.rede_executivos`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
