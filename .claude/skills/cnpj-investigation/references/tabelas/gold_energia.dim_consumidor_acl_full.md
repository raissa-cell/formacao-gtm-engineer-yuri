# `gold_energia.dim_consumidor_acl_full` — _TODO: título curto_

**Tipo:** VIEW
**Camada:** gold
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
| `cnpj` | STRING |  |  |
| `cnpj_basico` | STRING |  |  |
| `nome_empresarial` | STRING |  |  |
| `classe_acl` | STRING |  |  |
| `n_perfis` | INTEGER |  |  |
| `submercados` | STRING |  |  |
| `tipos_energia` | STRING |  |  |
| `atende_via_varejista` | BOOLEAN |  |  |
| `mwh_acl_12m` | FLOAT |  |  |
| `mwh_acl_mensal_medio` | FLOAT |  |  |
| `ultimo_mes_consumo` | DATE |  |  |
| `mwmed_compra_12m` | FLOAT |  |  |
| `mwmed_venda_12m` | FLOAT |  |  |
| `mwmed_compra_medio` | FLOAT |  |  |
| `kwh_grupo_bdgd_12m` | FLOAT |  |  |
| `n_ucs_bdgd_grupo` | INTEGER |  |  |
| `n_ucs_grupo_a_grupo` | INTEGER |  |  |
| `ratio_ccee_bdgd` | FLOAT |  |  |
| `match_qualidade` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `razao_social` | STRING |  |  |
| `porte_empresa` | STRING |  |  |
| `capital_social` | FLOAT |  |  |
| `cnae_principal` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `uf_matriz` | STRING |  |  |
| `municipio_matriz` | STRING |  |  |
| `data_abertura` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `opcao_simples` | BOOLEAN |  |  |
| `opcao_mei` | BOOLEAN |  |  |
| `n_estabelecimentos_ativos` | INTEGER |  |  |
| `n_ufs_atuacao` | INTEGER |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "00205375000430",
    "cnpj_basico": "00205375",
    "nome_empresarial": "P.1 ADMINISTRACAO EM COMPLEXOS IMOBILIARIOSLTDA",
    "classe_acl": "Especial",
    "n_perfis": 1,
    "submercados": "SUDESTE",
    "tipos_energia": null,
    "atende_via_varejista": false,
    "mwh_acl_12m": 2779.124714,
    "mwh_acl_mensal_medio": 277.9124714,
    "ultimo_mes_consumo": "2026-02-01",
    "mwmed_compra_12m": 3.8518199636179995,
    "mwmed_venda_12m": null,
    "mwmed_compra_medio": 0.38518199636179995,
    "kwh_grupo_bdgd_12m": null,
    "n_ucs_bdgd_grupo": null,
    "n_ucs_grupo_a_grupo": null,
    "ratio_ccee_bdgd": null,
    "match_qualidade": "sem_match",
    "_data_carga": "2026-04-26T02:07:16.416200+00:00",
    "razao_social": "P.1 ADMINISTRACAO EM COMPLEXOS IMOBILIARIOSLTDA",
    "porte_empresa": "DEMAIS",
    "capital_social": 113280.0,
    "cnae_principal": "7020400",
    "cnae_principal_descricao": "Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica",
    "uf_matriz": "SP",
    "municipio_matriz": "SAO PAULO",
    "data_abertura": "1994-09-23",
    "idade_anos": 32,
    "opcao_simples": null,
    "opcao_mei": null,
    "n_estabelecimentos_ativos": 4,
    "n_ufs_atuacao": 1
  },
  {
    "cnpj": "00373732000127",
    "cnpj_basico": "00373732",
    "nome_empresarial": "BIANCHINI INDUSTRIA DE PLASTICOS LTDA",
    "classe_acl": "Especial",
    "n_perfis": 1,
    "submercados": "SUL",
    "tipos_energia": null,
    "atende_via_varejista": false,
    "mwh_acl_12m": 9350.927632,
    "mwh_acl_mensal_medio": 935.0927632,
    "ultimo_mes_consumo": "2026-02-01",
    "mwmed_compra_12m": 13.026253133045,
    "mwmed_venda_12m": null,
    "mwmed_compra_medio": 1.3026253133044998,
    "kwh_grupo_bdgd_12m": null,
    "n_ucs_bdgd_grupo": null,
    "n_ucs_grupo_a_grupo": null,
    "ratio_ccee_bdgd": null,
    "match_qualidade": "sem_match",
    "_data_carga": "2026-04-26T02:07:16.416200+00:00",
    "razao_social": "BIANCHINI INDUSTRIA DE PLASTICOS LTDA",
    "porte_empresa": "DEMAIS",
    "capital_social": 16392148.0,
    "cnae_principal": "2229303",
    "cnae_principal_descricao": "Fabricação de artefatos de material plástico para uso na construção, exceto tubos e acessórios",
    "uf_matriz": "RS",
    "municipio_matriz": "TAPEJARA",
    "data_abertura": "1994-12-30",
    "idade_anos": 32,
    "opcao_simples": null,
    "opcao_mei": null,
    "n_estabelecimentos_ativos": 2,
    "n_ufs_atuacao": 1
  },
  {
    "cnpj": "00373732000127",
    "cnpj_basico": "00373732",
    "nome_empresarial": "BIANCHINI INDUSTRIA DE PLASTICOS LTDA",
    "classe_acl": "Livre",
    "n_perfis": 1,
    "submercados": "SUL",
    "tipos_energia": null,
    "atende_via_varejista": false,
    "mwh_acl_12m": 9350.927632,
    "mwh_acl_mensal_medio": 935.0927632,
    "ultimo_mes_consumo": "2026-02-01",
    "mwmed_compra_12m": 13.026253133045,
    "mwmed_venda_12m": null,
    "mwmed_compra_medio": 1.3026253133044998,
    "kwh_grupo_bdgd_12m": null,
    "n_ucs_bdgd_grupo": null,
    "n_ucs_grupo_a_grupo": null,
    "ratio_ccee_bdgd": null,
    "match_qualidade": "sem_match",
    "_data_carga": "2026-04-26T02:07:16.416200+00:00",
    "razao_social": "BIANCHINI INDUSTRIA DE PLASTICOS LTDA",
    "porte_empresa": "DEMAIS",
    "capital_social": 16392148.0,
    "cnae_principal": "2229303",
    "cnae_principal_descricao": "Fabricação de artefatos de material plástico para uso na construção, exceto tubos e acessórios",
    "uf_matriz": "RS",
    "municipio_matriz": "TAPEJARA",
    "data_abertura": "1994-12-30",
    "idade_anos": 32,
    "opcao_simples": null,
    "opcao_mei": null,
    "n_estabelecimentos_ativos": 2,
    "n_ufs_atuacao": 1
  },
  {
    "cnpj": "00392172000158",
    "cnpj_basico": "00392172",
    "nome_empresarial": "PAPEL TANGARA LTDA",
    "classe_acl": "Livre",
    "n_perfis": 2,
    "submercados": "SUL",
    "tipos_energia": null,
    "atende_via_varejista": false,
    "mwh_acl_12m": 9271.71616,
    "mwh_acl_mensal_medio": 927.1716159999999,
    "ultimo_mes_consumo": "2026-02-01",
    "mwmed_compra_12m": 12.822829337125999,
    "mwmed_venda_12m": null,
    "mwmed_compra_medio": 1.2822829337126,
    "kwh_grupo_bdgd_12m": null,
    "n_ucs_bdgd_grupo": null,
    "n_ucs_grupo_a_grupo": null,
    "ratio_ccee_bdgd": null,
    "match_qualidade": "sem_match",
    "_data_carga": "2026-04-26T02:07:16.416200+00:00",
    "razao_social": "PAPEL TANGARA LTDA",
    "porte_empresa": "DEMAIS",
    "capital_social": 2000000.0,
    "cnae_principal": "1742799",
    "cnae_principal_descricao": "Fabricação de produtos de papel para uso doméstico e higiênico-sanitário não especificados anteriormente",
    "uf_matriz": "SC",
    "municipio_matriz": "PINHEIRO PRETO",
    "data_abertura": "1995-01-16",
    "idade_anos": 31,
    "opcao_simples": false,
    "opcao_mei": false,
    "n_estabelecimentos_ativos": 1,
    "n_ufs_atuacao": 1
  },
  {
    "cnpj": "00392172000158",
    "cnpj_basico": "00392172",
    "nome_empresarial": "PAPEL TANGARA LTDA",
    "classe_acl": "Especial",
    "n_perfis": 1,
    "submercados": "SUL",
    "tipos_energia": null,
    "atende_via_varejista": false,
    "mwh_acl_12m": 9271.71616,
    "mwh_acl_mensal_medio": 927.1716159999999,
    "ultimo_mes_consumo": "2026-02-01",
    "mwmed_compra_12m": 12.822829337125999,
    "mwmed_venda_12m": null,
    "mwmed_compra_medio": 1.2822829337126,
    "kwh_grupo_bdgd_12m": null,
    "n_ucs_bdgd_grupo": null,
    "n_ucs_grupo_a_grupo": null,
    "ratio_ccee_bdgd": null,
    "match_qualidade": "sem_match",
    "_data_carga": "2026-04-26T02:07:16.416200+00:00",
    "razao_social": "PAPEL TANGARA LTDA",
    "porte_empresa": "DEMAIS",
    "capital_social": 2000000.0,
    "cnae_principal": "1742799",
    "cnae_principal_descricao": "Fabricação de produtos de papel para uso doméstico e higiênico-sanitário não especificados anteriormente",
    "uf_matriz": "SC",
    "municipio_matriz": "PINHEIRO PRETO",
    "data_abertura": "1995-01-16",
    "idade_anos": 31,
    "opcao_simples": false,
    "opcao_mei": false,
    "n_estabelecimentos_ativos": 1,
    "n_ufs_atuacao": 1
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_energia.dim_consumidor_acl_full\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_energia.dim_consumidor_acl_full`
WHERE ...
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
