# `bronze_cnpj.cnaes` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 1,359
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
| `CODIGO` | STRING |  |  |
| `DESCRICAO` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "CODIGO": "1012101",
    "DESCRICAO": "Abate de aves",
    "_arquivo_origem": "Cnaes.zip",
    "_data_carga": "2026-04-22T18:17:23+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "1012102",
    "DESCRICAO": "Abate de pequenos animais",
    "_arquivo_origem": "Cnaes.zip",
    "_data_carga": "2026-04-22T18:17:23+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "1531902",
    "DESCRICAO": "Acabamento de calçados de couro sob contrato",
    "_arquivo_origem": "Cnaes.zip",
    "_data_carga": "2026-04-22T18:17:23+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "5231101",
    "DESCRICAO": "Administração da infra-estrutura portuária",
    "_arquivo_origem": "Cnaes.zip",
    "_data_carga": "2026-04-22T18:17:23+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "8550301",
    "DESCRICAO": "Administração de caixas escolares",
    "_arquivo_origem": "Cnaes.zip",
    "_data_carga": "2026-04-22T18:17:23+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.cnaes\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_cnpj.cnaes`
WHERE ...
```

## Histórico

- 2026-04-22: última modificação BQ
- 2026-05-03: doc criado
