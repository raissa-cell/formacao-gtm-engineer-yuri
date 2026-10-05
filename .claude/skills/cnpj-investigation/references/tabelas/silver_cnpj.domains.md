# `silver_cnpj.domains` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 1,187,303
**Chave:** _TODO_
**Cluster BY:** `domain_type`, `domain`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `domain` | STRING |  |  |
| `qtd_cnpjs` | INTEGER |  |  |
| `domain_type` | STRING |  |  |
| `is_valid` | BOOLEAN |  |  |
| `updated_at` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "domain": "jlscontabil.com",
    "qtd_cnpjs": 1,
    "domain_type": "contabilidade",
    "is_valid": null,
    "updated_at": "2026-05-03T00:13:12.763940+00:00"
  },
  {
    "domain": "contabilidadelarissa.com",
    "qtd_cnpjs": 1,
    "domain_type": "contabilidade",
    "is_valid": null,
    "updated_at": "2026-05-03T00:13:12.763940+00:00"
  },
  {
    "domain": "contabiliezi.com.br",
    "qtd_cnpjs": 1,
    "domain_type": "contabilidade",
    "is_valid": null,
    "updated_at": "2026-05-03T00:13:12.763940+00:00"
  },
  {
    "domain": "dr-contabilrp.com.br",
    "qtd_cnpjs": 1,
    "domain_type": "contabilidade",
    "is_valid": null,
    "updated_at": "2026-05-03T00:13:12.763940+00:00"
  },
  {
    "domain": "guavivacontabilidade.com.br",
    "qtd_cnpjs": 1,
    "domain_type": "contabilidade",
    "is_valid": null,
    "updated_at": "2026-05-03T00:13:12.763940+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.domains\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.domains`
WHERE ...
```

## Histórico

- 2026-05-03: última modificação BQ
- 2026-05-03: doc criado
