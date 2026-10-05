# `silver_cnpj.empresas_por_socio_pj` — _TODO: título curto_

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
| `socio_cnpj_basico` | STRING |  |  |
| `socio_razao_social` | STRING |  |  |
| `controladas` | RECORD | REPEATED |  |
| `controladas.empresa_cnpj_basico` | STRING |  |  |
| `controladas.empresa_razao_social` | STRING |  |  |
| `controladas.qualificacao_nome` | STRING |  |  |
| `controladas.data_entrada_sociedade` | DATE |  |  |
| `n_controladas` | INTEGER |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "socio_cnpj_basico": "06056990",
    "socio_razao_social": "JOSE CELSO GONTIJO ENGENHARIA S/A",
    "controladas": [
      {
        "empresa_cnpj_basico": "55738472",
        "empresa_razao_social": "CONSORCIO SANTO ANTONIO",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2024-06-28"
      },
      {
        "empresa_cnpj_basico": "43251423",
        "empresa_razao_social": "BONANZA EMPRENDIMENTOS IMOBILIARIOS LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2024-05-24"
      },
      {
        "empresa_cnpj_basico": "52989990",
        "empresa_razao_social": "AQUILA EMPREENDIMENTOS IMOBILIARIOS LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2023-11-24"
      },
      {
        "empresa_cnpj_basico": "52989950",
        "empresa_razao_social": "ORION EMPREENDIMENTOS IMOBILIARIOS LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2023-11-24"
      },
      {
        "empresa_cnpj_basico": "52671281",
        "empresa_razao_social": "TABOQUINHA EMPREENDIMENTOS IMOBILIARIOS LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2023-10-25"
      },
      {
        "empresa_cnpj_basico": "53179816",
        "empresa_razao_social": "JOSE CELSO GONTIJO ENGENHARIA - SCP VALPARAISO",
        "qualificacao_nome": "Sócio Ostensivo",
        "data_entrada_sociedade": "2023-08-01"
      },
      {
        "empresa_cnpj_basico": "51321814",
        "empresa_razao_social": "CONSORCIO-CONCEICAO TAIPAS",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2023-07-06"
      },
      {
        "empresa_cnpj_basico": "50299657",
        "empresa_razao_social": "CONSORCIO MERCADO GOIANO",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2023-04-12"
      },
      {
        "empresa_cnpj_basico": "47962927",
        "empresa_razao_social": "CONSORCIO EDECONSIL/JCGONTIJO",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2022-09-15"
      },
      {
        "empresa_cnpj_basico": "44383942",
        "empresa_razao_social": "REC CONSTRUCOES E EMPREENDIMENTOS IMOBILIARIOS LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2021-11-26"
      },
      {
        "empresa_cnpj_basico": "23962124",
        "empresa_razao_social": "CONSORCIO JCGONTIJO COMIM",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2016-01-13"
      },
      {
        "empresa_cnpj_basico": "10387986",
        "empresa_razao_social": "CONSORCIO NOVO TERMINAL",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2008-09-01"
      },
      {
        "empresa_cnpj_basico": "08083737",
        "empresa_razao_social": "CONSORCIO JCG/SANTAMONICA",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2006-05-19"
      },
      {
        "empresa_cnpj_basico": "07724241",
        "empresa_razao_social": "CONSORCIO FONT VIEILLE",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2005-11-28"
      }
    ],
    "n_controladas": 14
  },
  {
    "socio_cnpj_basico": "03452218",
    "socio_razao_social": "JOSE FEITOZA NUNES",
    "controladas": [
      {
        "empresa_cnpj_basico": "43561462",
        "empresa_razao_social": "NEW FIELD CONSORCIO DE ENERGIA 2",
        "qualificacao_nome": "Sociedade Consorciada",
        "data_entrada_sociedade": "2025-04-29"
      }
    ],
    "n_controladas": 1
  },
  {
    "socio_cnpj_basico": "18546604",
    "socio_razao_social": "JOSE CARLOS BEE ADMINISTRACAO E PARTICIPACOES LTDA",
    "controladas": [
      {
        "empresa_cnpj_basico": "40170832",
        "empresa_razao_social": "JCL PARTICIPACOES LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2020-12-21"
      },
      {
        "empresa_cnpj_basico": "07379959",
        "empresa_razao_social": "BEE & CIA LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2013-12-16"
      }
    ],
    "n_controladas": 2
  },
  {
    "socio_cnpj_basico": "13920413",
    "socio_razao_social": "JOSE CHARLES PEREIRA NUNES LTDA",
    "controladas": [
      {
        "empresa_cnpj_basico": "42329344",
        "empresa_razao_social": "ARMAZZEM LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2021-06-15"
      }
    ],
    "n_controladas": 1
  },
  {
    "socio_cnpj_basico": "06190984",
    "socio_razao_social": "JOSE CLODOALDO FERREIRA LTDA",
    "controladas": [
      {
        "empresa_cnpj_basico": "64710666",
        "empresa_razao_social": "SPIRANDELI ENERGIA SPE LTDA",
        "qualificacao_nome": "Sócio",
        "data_entrada_sociedade": "2026-01-24"
      }
    ],
    "n_controladas": 1
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.empresas_por_socio_pj\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.empresas_por_socio_pj`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
