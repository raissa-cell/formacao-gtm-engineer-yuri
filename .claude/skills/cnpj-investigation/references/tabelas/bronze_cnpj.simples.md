# `bronze_cnpj.simples` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 48,097,045
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
| `CNPJ_BASICO` | STRING |  |  |
| `OPCAO_SIMPLES` | STRING |  |  |
| `DATA_OPCAO_SIMPLES` | STRING |  |  |
| `DATA_EXCLUSAO_SIMPLES` | STRING |  |  |
| `OPCAO_MEI` | STRING |  |  |
| `DATA_OPCAO_MEI` | STRING |  |  |
| `DATA_EXCLUSAO_MEI` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "CNPJ_BASICO": "59998329",
    "OPCAO_SIMPLES": "S",
    "DATA_OPCAO_SIMPLES": "20250320",
    "DATA_EXCLUSAO_SIMPLES": "00000000",
    "OPCAO_MEI": "N",
    "DATA_OPCAO_MEI": "00000000",
    "DATA_EXCLUSAO_MEI": "00000000",
    "_arquivo_origem": "Simples.zip",
    "_data_carga": "2026-04-22T18:18:14+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "60078250",
    "OPCAO_SIMPLES": "S",
    "DATA_OPCAO_SIMPLES": "20230101",
    "DATA_EXCLUSAO_SIMPLES": "00000000",
    "OPCAO_MEI": "N",
    "DATA_OPCAO_MEI": "00000000",
    "DATA_EXCLUSAO_MEI": "00000000",
    "_arquivo_origem": "Simples.zip",
    "_data_carga": "2026-04-22T18:18:14+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "60121111",
    "OPCAO_SIMPLES": "S",
    "DATA_OPCAO_SIMPLES": "20250327",
    "DATA_EXCLUSAO_SIMPLES": "00000000",
    "OPCAO_MEI": "N",
    "DATA_OPCAO_MEI": "00000000",
    "DATA_EXCLUSAO_MEI": "00000000",
    "_arquivo_origem": "Simples.zip",
    "_data_carga": "2026-04-22T18:18:14+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "60184162",
    "OPCAO_SIMPLES": "S",
    "DATA_OPCAO_SIMPLES": "20260101",
    "DATA_EXCLUSAO_SIMPLES": "00000000",
    "OPCAO_MEI": "N",
    "DATA_OPCAO_MEI": "00000000",
    "DATA_EXCLUSAO_MEI": "00000000",
    "_arquivo_origem": "Simples.zip",
    "_data_carga": "2026-04-22T18:18:14+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "60235707",
    "OPCAO_SIMPLES": "S",
    "DATA_OPCAO_SIMPLES": "20250403",
    "DATA_EXCLUSAO_SIMPLES": "00000000",
    "OPCAO_MEI": "N",
    "DATA_OPCAO_MEI": "00000000",
    "DATA_EXCLUSAO_MEI": "00000000",
    "_arquivo_origem": "Simples.zip",
    "_data_carga": "2026-04-22T18:18:14+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.simples\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_cnpj.simples`
WHERE ...
```

## Histórico

- 2026-04-22: última modificação BQ
- 2026-05-03: doc criado
