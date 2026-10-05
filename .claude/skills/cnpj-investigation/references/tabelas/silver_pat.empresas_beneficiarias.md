# `silver_pat.empresas_beneficiarias` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 521,245
**Chave:** _TODO_
**Cluster BY:** `cnpj_basico`, `uf_pat`
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
| `razao_social_pat` | STRING |  |  |
| `matriz_ou_filial` | STRING |  |  |
| `municipio_pat` | STRING |  |  |
| `uf_pat` | STRING |  |  |
| `no_registro` | STRING |  |  |
| `data_cadastro_pat` | DATE |  |  |
| `total_trabalhadores_unid` | INTEGER |  |  |
| `trab_ate_5sm_unid` | INTEGER |  |  |
| `trab_acima_5sm_unid` | INTEGER |  |  |
| `situacao_pat` | STRING |  |  |
| `_sheet_origem` | STRING |  |  |
| `nome_fantasia_rfb` | STRING |  |  |
| `situacao_cadastral_rfb` | STRING |  |  |
| `data_situacao_rfb` | DATE |  |  |
| `cnae_principal_unidade_rfb` | STRING |  |  |
| `cnae_principal_descricao_unidade_rfb` | STRING |  |  |
| `tipo_logradouro_rfb` | STRING |  |  |
| `logradouro_rfb` | STRING |  |  |
| `numero_rfb` | STRING |  |  |
| `complemento_rfb` | STRING |  |  |
| `bairro_rfb` | STRING |  |  |
| `cep_rfb` | STRING |  |  |
| `municipio_rfb` | STRING |  |  |
| `uf_rfb` | STRING |  |  |
| `data_inicio_atividade_unid` | DATE |  |  |
| `email_rfb` | STRING |  |  |
| `email_dominio_raiz_rfb` | STRING |  |  |
| `razao_social_grupo_rfb` | STRING |  |  |
| `porte_grupo` | STRING |  |  |
| `capital_social_grupo` | NUMERIC |  |  |
| `idade_grupo_anos` | INTEGER |  |  |
| `cnae_principal_grupo_descricao` | STRING |  |  |
| `pat_rfb_divergente` | BOOLEAN |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "85560480900102",
    "cnpj_basico": "85560480",
    "razao_social_pat": "Pessoa Fsica com Empregados",
    "matriz_ou_filial": "Matriz",
    "municipio_pat": "Pato Branco",
    "uf_pat": "PR",
    "no_registro": "3656667   ",
    "data_cadastro_pat": "2025-08-07",
    "total_trabalhadores_unid": 1,
    "trab_ate_5sm_unid": 1,
    "trab_acima_5sm_unid": 0,
    "situacao_pat": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "nome_fantasia_rfb": null,
    "situacao_cadastral_rfb": null,
    "data_situacao_rfb": null,
    "cnae_principal_unidade_rfb": null,
    "cnae_principal_descricao_unidade_rfb": null,
    "tipo_logradouro_rfb": null,
    "logradouro_rfb": null,
    "numero_rfb": null,
    "complemento_rfb": null,
    "bairro_rfb": null,
    "cep_rfb": null,
    "municipio_rfb": null,
    "uf_rfb": null,
    "data_inicio_atividade_unid": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "razao_social_grupo_rfb": null,
    "porte_grupo": null,
    "capital_social_grupo": null,
    "idade_grupo_anos": null,
    "cnae_principal_grupo_descricao": null,
    "pat_rfb_divergente": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:08.939292+00:00"
  },
  {
    "cnpj": "82990590100258",
    "cnpj_basico": "82990590",
    "razao_social_pat": "Pessoa Fsica com Empregados",
    "matriz_ou_filial": "Matriz",
    "municipio_pat": "Chapada dos Guimarães",
    "uf_pat": "MT",
    "no_registro": "3691829   ",
    "data_cadastro_pat": "2025-11-07",
    "total_trabalhadores_unid": 1,
    "trab_ate_5sm_unid": 1,
    "trab_acima_5sm_unid": 0,
    "situacao_pat": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "nome_fantasia_rfb": null,
    "situacao_cadastral_rfb": null,
    "data_situacao_rfb": null,
    "cnae_principal_unidade_rfb": null,
    "cnae_principal_descricao_unidade_rfb": null,
    "tipo_logradouro_rfb": null,
    "logradouro_rfb": null,
    "numero_rfb": null,
    "complemento_rfb": null,
    "bairro_rfb": null,
    "cep_rfb": null,
    "municipio_rfb": null,
    "uf_rfb": null,
    "data_inicio_atividade_unid": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "razao_social_grupo_rfb": null,
    "porte_grupo": null,
    "capital_social_grupo": null,
    "idade_grupo_anos": null,
    "cnae_principal_grupo_descricao": null,
    "pat_rfb_divergente": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:08.939292+00:00"
  },
  {
    "cnpj": "90004594000158",
    "cnpj_basico": "90004594",
    "razao_social_pat": "CONDOMINIO EDIFICIO SOLAR BARROCO",
    "matriz_ou_filial": "Matriz",
    "municipio_pat": "Curitiba",
    "uf_pat": "PR",
    "no_registro": "0589870   ",
    "data_cadastro_pat": "2008-07-21",
    "total_trabalhadores_unid": 6,
    "trab_ate_5sm_unid": 6,
    "trab_acima_5sm_unid": 0,
    "situacao_pat": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "nome_fantasia_rfb": null,
    "situacao_cadastral_rfb": null,
    "data_situacao_rfb": null,
    "cnae_principal_unidade_rfb": null,
    "cnae_principal_descricao_unidade_rfb": null,
    "tipo_logradouro_rfb": null,
    "logradouro_rfb": null,
    "numero_rfb": null,
    "complemento_rfb": null,
    "bairro_rfb": null,
    "cep_rfb": null,
    "municipio_rfb": null,
    "uf_rfb": null,
    "data_inicio_atividade_unid": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "razao_social_grupo_rfb": null,
    "porte_grupo": null,
    "capital_social_grupo": null,
    "idade_grupo_anos": null,
    "cnae_principal_grupo_descricao": null,
    "pat_rfb_divergente": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:08.939292+00:00"
  },
  {
    "cnpj": "40088304800118",
    "cnpj_basico": "40088304",
    "razao_social_pat": "Pessoa Fsica com Empregados",
    "matriz_ou_filial": "Matriz",
    "municipio_pat": "Bauru",
    "uf_pat": "SP",
    "no_registro": "3681858   ",
    "data_cadastro_pat": "2025-10-10",
    "total_trabalhadores_unid": 1,
    "trab_ate_5sm_unid": 1,
    "trab_acima_5sm_unid": 0,
    "situacao_pat": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "nome_fantasia_rfb": null,
    "situacao_cadastral_rfb": null,
    "data_situacao_rfb": null,
    "cnae_principal_unidade_rfb": null,
    "cnae_principal_descricao_unidade_rfb": null,
    "tipo_logradouro_rfb": null,
    "logradouro_rfb": null,
    "numero_rfb": null,
    "complemento_rfb": null,
    "bairro_rfb": null,
    "cep_rfb": null,
    "municipio_rfb": null,
    "uf_rfb": null,
    "data_inicio_atividade_unid": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "razao_social_grupo_rfb": null,
    "porte_grupo": null,
    "capital_social_grupo": null,
    "idade_grupo_anos": null,
    "cnae_principal_grupo_descricao": null,
    "pat_rfb_divergente": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:08.939292+00:00"
  },
  {
    "cnpj": "67215555000178",
    "cnpj_basico": "67215555",
    "razao_social_pat": "ALPHA DISPLAY INDUSTRIA E COMERCIO LTDA",
    "matriz_ou_filial": "Matriz",
    "municipio_pat": "São Paulo",
    "uf_pat": "SP",
    "no_registro": "0806951   ",
    "data_cadastro_pat": "2008-08-11",
    "total_trabalhadores_unid": 188,
    "trab_ate_5sm_unid": 178,
    "trab_acima_5sm_unid": 10,
    "situacao_pat": "Inativo",
    "_sheet_origem": "Beneficiárias-INATIVO",
    "nome_fantasia_rfb": null,
    "situacao_cadastral_rfb": null,
    "data_situacao_rfb": null,
    "cnae_principal_unidade_rfb": null,
    "cnae_principal_descricao_unidade_rfb": null,
    "tipo_logradouro_rfb": null,
    "logradouro_rfb": null,
    "numero_rfb": null,
    "complemento_rfb": null,
    "bairro_rfb": null,
    "cep_rfb": null,
    "municipio_rfb": null,
    "uf_rfb": null,
    "data_inicio_atividade_unid": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "razao_social_grupo_rfb": null,
    "porte_grupo": null,
    "capital_social_grupo": null,
    "idade_grupo_anos": null,
    "cnae_principal_grupo_descricao": null,
    "pat_rfb_divergente": false,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:08.939292+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_pat.empresas_beneficiarias\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_pat.empresas_beneficiarias`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
