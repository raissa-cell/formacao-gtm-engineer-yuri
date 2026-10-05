# `gold_pat.servicos_alimentacao` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** _TODO_
**Linhas (~):** 20,149
**Chave:** _TODO_
**Cluster BY:** `papel`, `uf`, `cnpj_basico`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj` | STRING |  | CNPJ completo (14 dígitos, só números). Chave. |
| `cnpj_basico` | STRING |  | CNPJ raiz (8 dígitos). Identifica grupo econômico. |
| `razao_social` | STRING |  | Razão social RFB (UPPERCASE sem acento) com fallback PAT normalizado se ausente na RFB. |
| `nome_fantasia` | STRING |  |  |
| `eh_facilitadora` | BOOLEAN |  | TRUE se a empresa emite vale-refeição/alimentação (instituição de pagamento ou supermercado-cartão). |
| `eh_fornecedora` | BOOLEAN |  | TRUE se a empresa fornece refeições prontas (cozinha industrial, restaurante coletivo). |
| `papel` | STRING |  | AMBOS / FACILITADORA / FORNECEDORA. AMBOS = empresa opera vale-refeição E fornece alimentação. |
| `no_registro_facilitadora` | STRING |  |  |
| `data_cadastro_facilitadora` | DATE |  |  |
| `situacao_facilitadora` | STRING |  |  |
| `sheet_origem_facilitadora` | STRING |  |  |
| `no_registro_fornecedora` | STRING |  |  |
| `data_cadastro_fornecedora` | DATE |  |  |
| `situacao_fornecedora` | STRING |  |  |
| `sheet_origem_fornecedora` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `cod_porte` | STRING |  |  |
| `porte` | STRING |  |  |
| `capital_social` | NUMERIC |  |  |
| `optante_simples` | BOOLEAN |  |  |
| `optante_mei` | BOOLEAN |  |  |
| `cnae_principal_codigo` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `data_abertura` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `qtd_filiais_total_rfb` | INTEGER |  |  |
| `qtd_filiais_ativas_rfb` | INTEGER |  | Filiais ativas no CNPJ-RFB (pode diferir de unidades cadastradas no PAT). |
| `uf` | STRING |  | UF da RFB (single source of truth, não o PAT centralizado). |
| `municipio` | STRING |  | Município RFB em UPPERCASE (decoded via bronze_cnpj.municipios). |
| `bairro` | STRING |  |  |
| `cep` | STRING |  |  |
| `tipo_logradouro` | STRING |  |  |
| `logradouro` | STRING |  |  |
| `numero` | STRING |  |  |
| `complemento` | STRING |  |  |
| `endereco_completo` | STRING |  | Endereço formatado: TIPO_LOGRADOURO + LOGRADOURO + NUMERO + COMPLEMENTO + BAIRRO. |
| `email` | STRING |  |  |
| `email_dominio_raiz` | STRING |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "26327905001640",
    "cnpj_basico": "26327905",
    "razao_social": "MORSA REFEICOES E SERVICOS LTDA",
    "nome_fantasia": null,
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "180656463 ",
    "data_cadastro_fornecedora": "2018-11-21",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte": "NÃO INFORMADO",
    "capital_social": "98000",
    "optante_simples": true,
    "optante_mei": false,
    "cnae_principal_codigo": "5620101",
    "cnae_principal_descricao": "Fornecimento de alimentos preparados preponderantemente para empresas",
    "data_abertura": "2016-10-10",
    "idade_anos": 10,
    "qtd_filiais_total_rfb": 1,
    "qtd_filiais_ativas_rfb": 0,
    "uf": null,
    "municipio": null,
    "bairro": null,
    "cep": null,
    "tipo_logradouro": null,
    "logradouro": null,
    "numero": null,
    "complemento": null,
    "endereco_completo": "",
    "email": null,
    "email_dominio_raiz": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:35:05.168692+00:00"
  },
  {
    "cnpj": "06222367900136",
    "cnpj_basico": "06222367",
    "razao_social": "Z & A RESTAURANTES LTDA",
    "nome_fantasia": null,
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080136868 ",
    "data_cadastro_fornecedora": "2008-08-21",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte": "NÃO INFORMADO",
    "capital_social": "0",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "5611201",
    "cnae_principal_descricao": "Restaurantes e similares",
    "data_abertura": "2004-04-15",
    "idade_anos": 22,
    "qtd_filiais_total_rfb": 1,
    "qtd_filiais_ativas_rfb": 0,
    "uf": null,
    "municipio": null,
    "bairro": null,
    "cep": null,
    "tipo_logradouro": null,
    "logradouro": null,
    "numero": null,
    "complemento": null,
    "endereco_completo": "",
    "email": null,
    "email_dominio_raiz": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:35:05.168692+00:00"
  },
  {
    "cnpj": "39385133000139",
    "cnpj_basico": "39385133",
    "razao_social": "ROBERTO RICARDO DE MENDONCA",
    "nome_fantasia": null,
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080129070 ",
    "data_cadastro_fornecedora": "2008-08-07",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "cod_natureza_juridica": "2135",
    "natureza_juridica": "Empresário (Individual)",
    "cod_porte": "01",
    "porte": "NÃO INFORMADO",
    "capital_social": "0",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "5611201",
    "cnae_principal_descricao": "Restaurantes e similares",
    "data_abertura": "1993-04-26",
    "idade_anos": 33,
    "qtd_filiais_total_rfb": 1,
    "qtd_filiais_ativas_rfb": 0,
    "uf": null,
    "municipio": null,
    "bairro": null,
    "cep": null,
    "tipo_logradouro": null,
    "logradouro": null,
    "numero": null,
    "complemento": null,
    "endereco_completo": "",
    "email": null,
    "email_dominio_raiz": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:35:05.168692+00:00"
  },
  {
    "cnpj": "0431172900130 ",
    "cnpj_basico": "04311729",
    "razao_social": "JOAO ROCHA LIMA NETO",
    "nome_fantasia": null,
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080097064 ",
    "data_cadastro_fornecedora": "2008-07-23",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "cod_natureza_juridica": "2135",
    "natureza_juridica": "Empresário (Individual)",
    "cod_porte": "01",
    "porte": "NÃO INFORMADO",
    "capital_social": "0",
    "optante_simples": null,
    "optante_mei": null,
    "cnae_principal_codigo": "5611203",
    "cnae_principal_descricao": "Lanchonetes, casas de chá, de sucos e similares",
    "data_abertura": "2001-03-02",
    "idade_anos": 25,
    "qtd_filiais_total_rfb": 1,
    "qtd_filiais_ativas_rfb": 0,
    "uf": null,
    "municipio": null,
    "bairro": null,
    "cep": null,
    "tipo_logradouro": null,
    "logradouro": null,
    "numero": null,
    "complemento": null,
    "endereco_completo": "",
    "email": null,
    "email_dominio_raiz": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:35:05.168692+00:00"
  },
  {
    "cnpj": "25155607000071",
    "cnpj_basico": "25155607",
    "razao_social": "D. CARDOZO EIRELI",
    "nome_fantasia": null,
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080093646 ",
    "data_cadastro_fornecedora": "2008-07-21",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "cod_natureza_juridica": "2305",
    "natureza_juridica": "Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)",
    "cod_porte": "03",
    "porte": "EMPRESA DE PEQUENO PORTE",
    "capital_social": "79000",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "5611201",
    "cnae_principal_descricao": "Restaurantes e similares",
    "data_abertura": "1988-06-27",
    "idade_anos": 38,
    "qtd_filiais_total_rfb": 2,
    "qtd_filiais_ativas_rfb": 0,
    "uf": null,
    "municipio": null,
    "bairro": null,
    "cep": null,
    "tipo_logradouro": null,
    "logradouro": null,
    "numero": null,
    "complemento": null,
    "endereco_completo": "",
    "email": null,
    "email_dominio_raiz": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:35:05.168692+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_pat.servicos_alimentacao\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_pat.servicos_alimentacao`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
