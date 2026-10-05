# `silver_cnpj.dim_empresa` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 67,642,315
**Chave:** _TODO_
**Cluster BY:** `cnpj_basico`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj_basico` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `nome_fantasia` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `cod_porte` | STRING |  |  |
| `porte` | STRING |  |  |
| `capital_social` | FLOAT |  |  |
| `opcao_simples` | BOOLEAN |  |  |
| `opcao_mei` | BOOLEAN |  |  |
| `cnae_principal` | STRING |  |  |
| `cnaes_secundarios` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `uf_matriz` | STRING |  |  |
| `cod_municipio_matriz` | STRING |  |  |
| `municipio_matriz` | STRING |  |  |
| `data_abertura` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `situacao_matriz` | STRING |  |  |
| `situacao_descricao` | STRING |  |  |
| `n_estabelecimentos_ativos` | INTEGER |  |  |
| `n_estabelecimentos_total` | INTEGER |  |  |
| `ufs_atuacao` | STRING |  |  |
| `n_ufs_atuacao` | INTEGER |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_basico": "10116720",
    "razao_social": "ELEICAO 2008 COMITE FINANCEIRO MUNICIPAL UNICO RO PPS",
    "nome_fantasia": null,
    "cod_natureza_juridica": "3999",
    "natureza_juridica": "Associação Privada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal": "9492800",
    "cnaes_secundarios": null,
    "cnae_principal_descricao": "Atividades de organizações políticas",
    "uf_matriz": "RO",
    "cod_municipio_matriz": "0002",
    "municipio_matriz": "ALTO ALEGRE DOS PARECIS",
    "data_abertura": "2008-07-12",
    "idade_anos": 18,
    "situacao_matriz": "08",
    "situacao_descricao": "BAIXADA",
    "n_estabelecimentos_ativos": 0,
    "n_estabelecimentos_total": 1,
    "ufs_atuacao": "RO",
    "n_ufs_atuacao": 1,
    "_data_carga": "2026-04-26T02:08:46.102746+00:00"
  },
  {
    "cnpj_basico": "10117053",
    "razao_social": "ELEICAO 2008 COMITE FINANCEIRO MUNICIPAL UNICO RO PR",
    "nome_fantasia": null,
    "cod_natureza_juridica": "3999",
    "natureza_juridica": "Associação Privada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal": "9492800",
    "cnaes_secundarios": null,
    "cnae_principal_descricao": "Atividades de organizações políticas",
    "uf_matriz": "RO",
    "cod_municipio_matriz": "0002",
    "municipio_matriz": "ALTO ALEGRE DOS PARECIS",
    "data_abertura": "2008-07-12",
    "idade_anos": 18,
    "situacao_matriz": "08",
    "situacao_descricao": "BAIXADA",
    "n_estabelecimentos_ativos": 0,
    "n_estabelecimentos_total": 1,
    "ufs_atuacao": "RO",
    "n_ufs_atuacao": 1,
    "_data_carga": "2026-04-26T02:08:46.102746+00:00"
  },
  {
    "cnpj_basico": "10116907",
    "razao_social": "ELEICAO 2008 COMITE FINANCEIRO MUNICIPAL UNICO RO PT",
    "nome_fantasia": null,
    "cod_natureza_juridica": "3999",
    "natureza_juridica": "Associação Privada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal": "9492800",
    "cnaes_secundarios": null,
    "cnae_principal_descricao": "Atividades de organizações políticas",
    "uf_matriz": "RO",
    "cod_municipio_matriz": "0002",
    "municipio_matriz": "ALTO ALEGRE DOS PARECIS",
    "data_abertura": "2008-07-12",
    "idade_anos": 18,
    "situacao_matriz": "08",
    "situacao_descricao": "BAIXADA",
    "n_estabelecimentos_ativos": 0,
    "n_estabelecimentos_total": 1,
    "ufs_atuacao": "RO",
    "n_ufs_atuacao": 1,
    "_data_carga": "2026-04-26T02:08:46.102746+00:00"
  },
  {
    "cnpj_basico": "10118956",
    "razao_social": "ELEICAO 2008 COMITE FINANCEIRO MUNICIPAL UNICO RO PMDB",
    "nome_fantasia": null,
    "cod_natureza_juridica": "3999",
    "natureza_juridica": "Associação Privada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal": "9492800",
    "cnaes_secundarios": null,
    "cnae_principal_descricao": "Atividades de organizações políticas",
    "uf_matriz": "RO",
    "cod_municipio_matriz": "0002",
    "municipio_matriz": "ALTO ALEGRE DOS PARECIS",
    "data_abertura": "2008-07-12",
    "idade_anos": 18,
    "situacao_matriz": "08",
    "situacao_descricao": "BAIXADA",
    "n_estabelecimentos_ativos": 0,
    "n_estabelecimentos_total": 1,
    "ufs_atuacao": "RO",
    "n_ufs_atuacao": 1,
    "_data_carga": "2026-04-26T02:08:46.102746+00:00"
  },
  {
    "cnpj_basico": "10118442",
    "razao_social": "ELEICAO 2008 COMITE FINANCEIRO MUNICIPAL PARA VEREADOR RO PSB",
    "nome_fantasia": null,
    "cod_natureza_juridica": "3999",
    "natureza_juridica": "Associação Privada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal": "9492800",
    "cnaes_secundarios": null,
    "cnae_principal_descricao": "Atividades de organizações políticas",
    "uf_matriz": "RO",
    "cod_municipio_matriz": "0002",
    "municipio_matriz": "ALTO ALEGRE DOS PARECIS",
    "data_abertura": "2008-07-12",
    "idade_anos": 18,
    "situacao_matriz": "08",
    "situacao_descricao": "BAIXADA",
    "n_estabelecimentos_ativos": 0,
    "n_estabelecimentos_total": 1,
    "ufs_atuacao": "RO",
    "n_ufs_atuacao": 1,
    "_data_carga": "2026-04-26T02:08:46.102746+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.dim_empresa\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.dim_empresa`
WHERE ...
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
