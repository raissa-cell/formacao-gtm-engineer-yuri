# `bronze_cnpj.motivos` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 63
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
    "CODIGO": "00",
    "DESCRICAO": "SEM MOTIVO",
    "_arquivo_origem": "Motivos.zip",
    "_data_carga": "2026-04-22T18:18:01+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "01",
    "DESCRICAO": "EXTINCAO POR ENCERRAMENTO LIQUIDACAO VOLUNTARIA",
    "_arquivo_origem": "Motivos.zip",
    "_data_carga": "2026-04-22T18:18:01+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "02",
    "DESCRICAO": "INCORPORACAO",
    "_arquivo_origem": "Motivos.zip",
    "_data_carga": "2026-04-22T18:18:01+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "03",
    "DESCRICAO": "FUSAO",
    "_arquivo_origem": "Motivos.zip",
    "_data_carga": "2026-04-22T18:18:01+00:00",
    "_periodo": "202604"
  },
  {
    "CODIGO": "04",
    "DESCRICAO": "CISAO TOTAL",
    "_arquivo_origem": "Motivos.zip",
    "_data_carga": "2026-04-22T18:18:01+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.motivos\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_cnpj.motivos`
WHERE ...
```

## Histórico

- 2026-04-22: última modificação BQ
- 2026-05-03: doc criado
