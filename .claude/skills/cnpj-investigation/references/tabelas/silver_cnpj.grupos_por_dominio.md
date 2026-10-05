# `silver_cnpj.grupos_por_dominio` — _TODO: título curto_

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
| `email_dominio_raiz` | STRING |  |  |
| `cnpj_basico` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `estabs` | INTEGER |  |  |
| `estabs_ativos` | INTEGER |  |  |
| `uf_amostra` | STRING |  |  |
| `email_amostra` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "email_dominio_raiz": "uol.com.br",
    "cnpj_basico": "07595454",
    "razao_social": "ASTRO CELL COMERCIO E TRANSPORTES DE CARGAS LTDA",
    "estabs": 1,
    "estabs_ativos": 0,
    "uf_amostra": "RJ",
    "email_amostra": "contato@contabil.uol.com.br"
  },
  {
    "email_dominio_raiz": "uol.com.br",
    "cnpj_basico": "03668690",
    "razao_social": "VANDI - SUPERMERCADO LTDA",
    "estabs": 1,
    "estabs_ativos": 1,
    "uf_amostra": "PR",
    "email_amostra": "escritorio.alex@.uol.com.br"
  },
  {
    "email_dominio_raiz": "uol.com.br",
    "cnpj_basico": "03350627",
    "razao_social": "JULIANE DOS SANTOS NUNES",
    "estabs": 1,
    "estabs_ativos": 0,
    "uf_amostra": "RS",
    "email_amostra": "guedescontabil@.uol.com.br"
  },
  {
    "email_dominio_raiz": "uol.com.br",
    "cnpj_basico": "00906548",
    "razao_social": "DEJAIR ANDRADE",
    "estabs": 1,
    "estabs_ativos": 0,
    "uf_amostra": "RS",
    "email_amostra": "guedescontabil@.uol.com.br"
  },
  {
    "email_dominio_raiz": "uol.com.br",
    "cnpj_basico": "93511335",
    "razao_social": "GILMAR ANTONIO SALIN M E",
    "estabs": 1,
    "estabs_ativos": 0,
    "uf_amostra": "RS",
    "email_amostra": "carlosrighi@.uol.com.br"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.grupos_por_dominio\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.grupos_por_dominio`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
