# `silver_pat.empresas_servicos_alimentacao` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 27,916
**Chave:** _TODO_
**Cluster BY:** `papel`, `uf_pat`, `cnpj_basico`
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
| `razao_social` | STRING |  |  |
| `matriz_ou_filial` | STRING |  |  |
| `municipio_pat` | STRING |  |  |
| `uf_pat` | STRING |  |  |
| `eh_facilitadora` | BOOLEAN |  |  |
| `eh_fornecedora` | BOOLEAN |  |  |
| `papel` | STRING |  |  |
| `no_registro_facilitadora` | STRING |  |  |
| `data_cadastro_facilitadora` | DATE |  |  |
| `situacao_facilitadora` | STRING |  |  |
| `sheet_origem_facilitadora` | STRING |  |  |
| `no_registro_fornecedora` | STRING |  |  |
| `data_cadastro_fornecedora` | DATE |  |  |
| `situacao_fornecedora` | STRING |  |  |
| `sheet_origem_fornecedora` | STRING |  |  |
| `razao_social_rfb` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica_descricao` | STRING |  |  |
| `cod_porte` | STRING |  |  |
| `porte_descricao` | STRING |  |  |
| `capital_social` | NUMERIC |  |  |
| `optante_simples` | BOOLEAN |  |  |
| `optante_mei` | BOOLEAN |  |  |
| `cnae_principal_codigo` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `data_inicio_atividade` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `uf_matriz_rfb` | STRING |  |  |
| `municipio_matriz_rfb` | STRING |  |  |
| `qtd_filiais_ativas_rfb` | INTEGER |  |  |
| `qtd_filiais_total_rfb` | INTEGER |  |  |
| `situacao_grupo_descricao` | STRING |  |  |
| `cep5_rfb` | STRING |  |  |
| `endereco_norm_rfb` | STRING |  |  |
| `email_rfb` | STRING |  |  |
| `email_dominio_raiz_rfb` | STRING |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "10765387000120",
    "cnpj_basico": "10765387",
    "razao_social": "COBEN ALIMENTOS LTDA ME",
    "matriz_ou_filial": null,
    "municipio_pat": "Abadia de Goiás",
    "uf_pat": "GO",
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "090203411 ",
    "data_cadastro_fornecedora": "2009-09-25",
    "situacao_fornecedora": "Inativo",
    "sheet_origem_fornecedora": "Fornecedoras-INATIVO",
    "razao_social_rfb": "COBEN ALIMENTOS LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica_descricao": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte_descricao": "NÃO INFORMADO",
    "capital_social": "10000",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "5620101",
    "cnae_principal_descricao": "Fornecimento de alimentos preparados preponderantemente para empresas",
    "data_inicio_atividade": "2009-04-13",
    "idade_anos": 17,
    "uf_matriz_rfb": "GO",
    "municipio_matriz_rfb": "ABADIA DE GOIAS",
    "qtd_filiais_ativas_rfb": 0,
    "qtd_filiais_total_rfb": 1,
    "situacao_grupo_descricao": "BAIXADA",
    "cep5_rfb": null,
    "endereco_norm_rfb": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T20:58:49.290714+00:00"
  },
  {
    "cnpj": "07453800000298",
    "cnpj_basico": "07453800",
    "razao_social": "supermercado gm ltda",
    "matriz_ou_filial": null,
    "municipio_pat": "Contagem",
    "uf_pat": "MG",
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080149514 ",
    "data_cadastro_fornecedora": "2008-09-22",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "razao_social_rfb": "SUPERMERCADO GM LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica_descricao": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte_descricao": "NÃO INFORMADO",
    "capital_social": "20000",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "4712100",
    "cnae_principal_descricao": "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - minimercados, mercearias e armazéns",
    "data_inicio_atividade": "2005-06-27",
    "idade_anos": 21,
    "uf_matriz_rfb": "MG",
    "municipio_matriz_rfb": "ABAETE",
    "qtd_filiais_ativas_rfb": 0,
    "qtd_filiais_total_rfb": 3,
    "situacao_grupo_descricao": "INAPTA",
    "cep5_rfb": "32113",
    "endereco_norm_rfb": "ll 136",
    "email_rfb": "elton@capcontabi.com.br",
    "email_dominio_raiz_rfb": "capcontabi.com.br",
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T20:58:49.290714+00:00"
  },
  {
    "cnpj": "08251807000109",
    "cnpj_basico": "08251807",
    "razao_social": "A M RESTAURANTE LTDA",
    "matriz_ou_filial": null,
    "municipio_pat": "Barcarena",
    "uf_pat": "PA",
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "080072974 ",
    "data_cadastro_fornecedora": "2008-05-29",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "razao_social_rfb": "A & C - COMERCIO & SERVICOS DE MARMORES E GRANITOS LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica_descricao": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte_descricao": "NÃO INFORMADO",
    "capital_social": "40000",
    "optante_simples": true,
    "optante_mei": false,
    "cnae_principal_codigo": "2391503",
    "cnae_principal_descricao": "Aparelhamento de placas e execução de trabalhos em mármore, granito, ardósia e outras pedras",
    "data_inicio_atividade": "2006-08-22",
    "idade_anos": 20,
    "uf_matriz_rfb": "PA",
    "municipio_matriz_rfb": "ABAETETUBA",
    "qtd_filiais_ativas_rfb": 0,
    "qtd_filiais_total_rfb": 1,
    "situacao_grupo_descricao": "INAPTA",
    "cep5_rfb": null,
    "endereco_norm_rfb": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T20:58:49.290714+00:00"
  },
  {
    "cnpj": "16853332000159",
    "cnpj_basico": "16853332",
    "razao_social": "KARIRI ALIMENTOS LTDA ME",
    "matriz_ou_filial": null,
    "municipio_pat": "Abaiara",
    "uf_pat": "CE",
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "120355025 ",
    "data_cadastro_fornecedora": "2012-11-08",
    "situacao_fornecedora": "Inativo",
    "sheet_origem_fornecedora": "Fornecedoras-INATIVO",
    "razao_social_rfb": "KARIRI ALIMENTOS LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica_descricao": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte_descricao": "NÃO INFORMADO",
    "capital_social": "50000",
    "optante_simples": null,
    "optante_mei": null,
    "cnae_principal_codigo": "5620101",
    "cnae_principal_descricao": "Fornecimento de alimentos preparados preponderantemente para empresas",
    "data_inicio_atividade": "2012-09-06",
    "idade_anos": 14,
    "uf_matriz_rfb": "CE",
    "municipio_matriz_rfb": "ABAIARA",
    "qtd_filiais_ativas_rfb": 0,
    "qtd_filiais_total_rfb": 1,
    "situacao_grupo_descricao": "BAIXADA",
    "cep5_rfb": null,
    "endereco_norm_rfb": null,
    "email_rfb": null,
    "email_dominio_raiz_rfb": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T20:58:49.290714+00:00"
  },
  {
    "cnpj": "00881777000102",
    "cnpj_basico": "00881777",
    "razao_social": "MARILIA'S BUFFET & RESTAURANTE LTDA - ME",
    "matriz_ou_filial": null,
    "municipio_pat": "Abre Campo",
    "uf_pat": "MG",
    "eh_facilitadora": false,
    "eh_fornecedora": true,
    "papel": "FORNECEDORA",
    "no_registro_facilitadora": null,
    "data_cadastro_facilitadora": null,
    "situacao_facilitadora": null,
    "sheet_origem_facilitadora": null,
    "no_registro_fornecedora": "110279542 ",
    "data_cadastro_fornecedora": "2011-05-17",
    "situacao_fornecedora": "Ativo",
    "sheet_origem_fornecedora": "Fornecedoras-ATIVO",
    "razao_social_rfb": "MARILIA'S BUFFET & RESTAURANTE LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica_descricao": "Sociedade Empresária Limitada",
    "cod_porte": "01",
    "porte_descricao": "NÃO INFORMADO",
    "capital_social": "20000",
    "optante_simples": false,
    "optante_mei": false,
    "cnae_principal_codigo": "5620101",
    "cnae_principal_descricao": "Fornecimento de alimentos preparados preponderantemente para empresas",
    "data_inicio_atividade": "1995-10-26",
    "idade_anos": 31,
    "uf_matriz_rfb": "MG",
    "municipio_matriz_rfb": "ABRE CAMPO",
    "qtd_filiais_ativas_rfb": 0,
    "qtd_filiais_total_rfb": 1,
    "situacao_grupo_descricao": "BAIXADA",
    "cep5_rfb": "35365",
    "endereco_norm_rfb": "santo antonio 289",
    "email_rfb": "alessandrovamorim@hotmail.com",
    "email_dominio_raiz_rfb": "hotmail.com",
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T20:58:49.290714+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_pat.empresas_servicos_alimentacao\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_pat.empresas_servicos_alimentacao`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
