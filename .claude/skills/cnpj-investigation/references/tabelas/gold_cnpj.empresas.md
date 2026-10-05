# `gold_cnpj.empresas` — Empresas brasileiras (arquitetura comercial v2)

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** 1 linha por **CNPJ_BASICO** (8 dígitos) com pelo menos 1 estabelecimento ATIVO. Filiais embutidas em `local.filiais[]`.
**Linhas (~):** 27,398,796
**Chave:** `cnpj_basico` (STRING 8d)
**Cluster BY:** `cnpj_basico`, `status_porte`, `local_uf`
**Refresh:** semanal — `cnpj-gold-weekly` segunda 08:00 BRT (após silver de 06:00). Build: `python -m scripts.cnpj.gold_empresas --build`.
**Origem:** `bronze_cnpj.{empresas, estabelecimentos, socios, simples}` + dimensões. Spec: [`docs/cnpj/arquitetura-comercial-v2.md`](../../../../docs/cnpj/arquitetura-comercial-v2.md).

**Descrição BQ:** Camada gold comercial v2 — 8 clusters semânticos (status, regime_tributario, financeiro, industria, local, contato, socios). Códigos RFB resolvidos pra enums; lixo em emails/telefones filtrado; sócios em 4 buckets por tipo.

---

## Quando usar

⭐ **Default pra qualquer pergunta comercial sobre empresa**: porte, setor, NJ, regime tributário, capital social, filiais agregadas, sócios em buckets, busca por nome com enums comerciais. Códigos já resolvidos (`status.porte = 'grande'` em vez de `PORTE='05'`).

**NÃO use** quando precisar de:
- Qualificações específicas fora dos 4 buckets gold (Conselheiro `08`, Beneficiário Final `25`, etc.) → `silver_cnpj.socios` ou `bronze_cnpj.socios`
- `_periodo` históricos / snapshots antigos → `bronze_cnpj.empresas`
- Dado cru com strings em CAPS sem parsing → bronze

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj_basico` | STRING |  |  |
| `cnpj_matriz` | STRING |  |  |
| `nome` | STRING |  |  |
| `nome_fantasia` | STRING |  |  |
| `data_abertura` | DATE |  |  |
| `idade_anos` | FLOAT |  |  |
| `total_filiais` | INTEGER |  |  |
| `status_porte` | STRING |  |  |
| `local_uf` | STRING |  |  |
| `status` | RECORD |  |  |
| `status.operacional` | STRING |  |  |
| `status.porte` | STRING |  |  |
| `status.natureza_juridica` | RECORD |  |  |
| `status.natureza_juridica.codigo` | STRING |  |  |
| `status.natureza_juridica.descricao` | STRING |  |  |
| `status.natureza_juridica.categoria` | STRING |  |  |
| `status.raw_rfb` | RECORD |  |  |
| `status.raw_rfb.situacao_cadastral` | RECORD |  |  |
| `status.raw_rfb.situacao_cadastral.codigo` | STRING |  |  |
| `status.raw_rfb.situacao_cadastral.descricao` | STRING |  |  |
| `status.raw_rfb.situacao_cadastral.data` | DATE |  |  |
| `status.raw_rfb.situacao_cadastral.motivo` | RECORD |  |  |
| `status.raw_rfb.situacao_cadastral.motivo.codigo` | STRING |  |  |
| `status.raw_rfb.situacao_cadastral.motivo.descricao` | STRING |  |  |
| `status.raw_rfb.porte` | RECORD |  |  |
| `status.raw_rfb.porte.codigo` | STRING |  |  |
| `status.raw_rfb.porte.descricao` | STRING |  |  |
| `status.raw_rfb.qualificacao_responsavel` | RECORD |  |  |
| `status.raw_rfb.qualificacao_responsavel.codigo` | STRING |  |  |
| `status.raw_rfb.qualificacao_responsavel.descricao` | STRING |  |  |
| `regime_tributario` | RECORD |  |  |
| `regime_tributario.tipo` | STRING |  |  |
| `regime_tributario.fonte` | STRING |  |  |
| `regime_tributario.historico` | RECORD |  |  |
| `regime_tributario.historico.data_opcao_simples` | DATE |  |  |
| `regime_tributario.historico.data_exclusao_simples` | DATE |  |  |
| `regime_tributario.historico.data_opcao_mei` | DATE |  |  |
| `regime_tributario.historico.data_exclusao_mei` | DATE |  |  |
| `financeiro` | RECORD |  |  |
| `financeiro.capital_social_brl` | FLOAT |  |  |
| `industria` | RECORD |  |  |
| `industria.setor` | STRING |  |  |
| `industria.segmento` | STRING |  |  |
| `industria.cnae_principal` | RECORD |  |  |
| `industria.cnae_principal.codigo` | STRING |  |  |
| `industria.cnae_principal.descricao` | STRING |  |  |
| `industria.cnae_principal.secao` | STRING |  |  |
| `industria.cnae_secundarios` | RECORD | REPEATED |  |
| `industria.cnae_secundarios.codigo` | STRING |  |  |
| `industria.cnae_secundarios.descricao` | STRING |  |  |
| `industria.cnae_secundarios.secao` | STRING |  |  |
| `local` | RECORD |  |  |
| `local.matriz` | RECORD |  |  |
| `local.matriz.cnpj` | STRING |  |  |
| `local.matriz.cep` | STRING |  |  |
| `local.matriz.uf` | STRING |  |  |
| `local.matriz.municipio_codigo` | STRING |  |  |
| `local.matriz.municipio_nome` | STRING |  |  |
| `local.matriz.bairro` | STRING |  |  |
| `local.matriz.logradouro_completo` | STRING |  |  |
| `local.matriz.raw` | RECORD |  |  |
| `local.matriz.raw.tipo_logradouro` | STRING |  |  |
| `local.matriz.raw.logradouro` | STRING |  |  |
| `local.matriz.raw.numero` | STRING |  |  |
| `local.matriz.raw.complemento` | STRING |  |  |
| `local.matriz.geo` | RECORD |  |  |
| `local.matriz.geo.lat` | FLOAT |  |  |
| `local.matriz.geo.lon` | FLOAT |  |  |
| `local.filiais` | RECORD | REPEATED |  |
| `local.filiais.cnpj` | STRING |  |  |
| `local.filiais.uf` | STRING |  |  |
| `local.filiais.municipio_nome` | STRING |  |  |
| `local.filiais.bairro` | STRING |  |  |
| `local.filiais.cep` | STRING |  |  |
| `local.filiais.logradouro_completo` | STRING |  |  |
| `local.filiais.data_abertura` | DATE |  |  |
| `local.filiais.cnae_principal` | RECORD |  |  |
| `local.filiais.cnae_principal.codigo` | STRING |  |  |
| `local.filiais.cnae_principal.descricao` | STRING |  |  |
| `contato` | RECORD |  |  |
| `contato.emails` | RECORD | REPEATED |  |
| `contato.emails.dominio` | STRING |  |  |
| `contato.emails.enderecos` | RECORD | REPEATED |  |
| `contato.emails.enderecos.valor` | STRING |  |  |
| `contato.emails.enderecos.local_part` | STRING |  |  |
| `contato.emails.enderecos.origens` | STRING | REPEATED |  |
| `contato.telefones` | RECORD | REPEATED |  |
| `contato.telefones.ddd` | STRING |  |  |
| `contato.telefones.numero` | STRING |  |  |
| `contato.telefones.e164` | STRING |  |  |
| `contato.telefones.tipo` | STRING |  |  |
| `contato.telefones.origens` | STRING | REPEATED |  |
| `socios` | RECORD |  |  |
| `socios.pessoas_fisicas` | RECORD | REPEATED |  |
| `socios.pessoas_fisicas.nome` | STRING |  |  |
| `socios.pessoas_fisicas.nome_norm` | STRING |  |  |
| `socios.pessoas_fisicas.cpf_visivel` | STRING |  |  |
| `socios.pessoas_fisicas.qualificacao` | RECORD |  |  |
| `socios.pessoas_fisicas.qualificacao.codigo` | STRING |  |  |
| `socios.pessoas_fisicas.qualificacao.descricao` | STRING |  |  |
| `socios.pessoas_fisicas.data_entrada` | DATE |  |  |
| `socios.pessoas_fisicas.faixa_etaria` | RECORD |  |  |
| `socios.pessoas_fisicas.faixa_etaria.codigo` | STRING |  |  |
| `socios.pessoas_fisicas.faixa_etaria.descricao` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais` | RECORD | REPEATED |  |
| `socios.pessoas_juridicas_nacionais.nome` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.nome_norm` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.documento` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.cnpj_basico` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.razao_social` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.qualificacao` | RECORD |  |  |
| `socios.pessoas_juridicas_nacionais.qualificacao.codigo` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.qualificacao.descricao` | STRING |  |  |
| `socios.pessoas_juridicas_nacionais.data_entrada` | DATE |  |  |
| `socios.pessoas_juridicas_estrangeiras` | RECORD | REPEATED |  |
| `socios.pessoas_juridicas_estrangeiras.nome` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.nome_norm` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.documento` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.cnpj_basico` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.razao_social` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.pais` | RECORD |  |  |
| `socios.pessoas_juridicas_estrangeiras.pais.codigo` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.pais.nome` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.qualificacao` | RECORD |  |  |
| `socios.pessoas_juridicas_estrangeiras.qualificacao.codigo` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.qualificacao.descricao` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.data_entrada` | DATE |  |  |
| `socios.pessoas_juridicas_estrangeiras.representante_legal` | RECORD |  |  |
| `socios.pessoas_juridicas_estrangeiras.representante_legal.nome` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.representante_legal.qualificacao` | RECORD |  |  |
| `socios.pessoas_juridicas_estrangeiras.representante_legal.qualificacao.codigo` | STRING |  |  |
| `socios.pessoas_juridicas_estrangeiras.representante_legal.qualificacao.descricao` | STRING |  |  |
| `socios.administradores_diretores` | RECORD | REPEATED |  |
| `socios.administradores_diretores.nome` | STRING |  |  |
| `socios.administradores_diretores.nome_norm` | STRING |  |  |
| `socios.administradores_diretores.cpf_visivel` | STRING |  |  |
| `socios.administradores_diretores.qualificacao` | RECORD |  |  |
| `socios.administradores_diretores.qualificacao.codigo` | STRING |  |  |
| `socios.administradores_diretores.qualificacao.descricao` | STRING |  |  |
| `socios.administradores_diretores.papel` | STRING |  |  |
| `socios.administradores_diretores.representando` | STRING |  |  |
| `socios.administradores_diretores.data_entrada` | DATE |  |  |
| `socios.administradores_diretores.faixa_etaria` | RECORD |  |  |
| `socios.administradores_diretores.faixa_etaria.codigo` | STRING |  |  |
| `socios.administradores_diretores.faixa_etaria.descricao` | STRING |  |  |
| `socios.totais` | RECORD |  |  |
| `socios.totais.pessoas_fisicas` | INTEGER |  |  |
| `socios.totais.pessoas_juridicas_nacionais` | INTEGER |  |  |
| `socios.totais.pessoas_juridicas_estrangeiras` | INTEGER |  |  |
| `socios.totais.administradores_diretores_titulares` | INTEGER |  |  |
| `socios.totais.administradores_diretores_representantes` | INTEGER |  |  |
| `socios.totais.geral` | INTEGER |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_fontes` | STRING | REPEATED |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_basico": "65274133",
    "cnpj_matriz": "65274133000100",
    "nome": "JOAO FRANCISCO GOMES SIMOES",
    "nome_fantasia": null,
    "data_abertura": "2026-02-19",
    "idade_anos": 0.2,
    "total_filiais": 0,
    "status_porte": "grande",
    "local_uf": "SP",
    "status": {
      "operacional": "ativa",
      "porte": "grande",
      "natureza_juridica": {
        "codigo": "4120",
        "descricao": "Produtor Rural (Pessoa Física)",
        "categoria": "individual"
      },
      "raw_rfb": {
        "situacao_cadastral": {
          "codigo": "02",
          "descricao": "ativa",
          "data": "2026-02-19",
          "motivo": {
            "codigo": "00",
            "descricao": "SEM MOTIVO"
          }
        },
        "porte": {
          "codigo": "05",
          "descricao": null
        },
        "qualificacao_responsavel": {
          "codigo": "59",
          "descricao": "Produtor Rural"
        }
      }
    },
    "regime_tributario": {
      "tipo": "nao_simples",
      "fonte": "rfb_dados_abertos",
      "historico": {
        "data_opcao_simples": null,
        "data_exclusao_simples": null,
        "data_opcao_mei": null,
        "data_exclusao_mei": null
      }
    },
    "financeiro": {
      "capital_social_brl": 0.0
    },
    "industria": {
      "setor": "Agropecuária",
      "segmento": null,
      "cnae_principal": {
        "codigo": "0111302",
        "descricao": "Cultivo de milho",
        "secao": "A"
      },
      "cnae_secundarios": [
        {
          "codigo": "0111303",
          "descricao": "Cultivo de trigo",
          "secao": "A"
        },
        {
          "codigo": "0111301",
          "descricao": "Cultivo de arroz",
          "secao": "A"
        },
        {
          "codigo": "0111399",
          "descricao": "Cultivo de outros cereais não especificados anteriormente",
          "secao": "A"
        },
        {
          "codigo": "0112199",
          "descricao": "Cultivo de outras fibras de lavoura temporária não especificadas anteriormente",
          "secao": "A"
        },
        {
          "codigo": "0115600",
          "descricao": "Cultivo de soja",
          "secao": "A"
        },
        {
          "codigo": "0116499",
          "descricao": "Cultivo de outras oleaginosas de lavoura temporária não especificadas anteriormente",
          "secao": "A"
        },
        {
          "codigo": "0119903",
          "descricao": "Cultivo de batata-inglesa",
          "secao": "A"
        },
        {
          "codigo": "0119904",
          "descricao": "Cultivo de cebola",
          "secao": "A"
        },
        {
          "codigo": "0119905",
          "descricao": "Cultivo de feijão",
          "secao": "A"
        },
        {
          "codigo": "0119906",
          "descricao": "Cultivo de mandioca",
          "secao": "A"
        },
        {
          "codigo": "0119999",
          "descricao": "Cultivo de outras plantas de lavoura temporária não especificadas anteriormente",
          "secao": "A"
        },
        {
          "codigo": "0151201",
          "descricao": "Criação de bovinos para corte",
          "secao": "A"
        },
        {
          "codigo": "0151202",
          "descricao": "Criação de bovinos para leite",
          "secao": "A"
        },
        {
          "codigo": "0152102",
          "descricao": "Criação de eqüinos",
          "secao": "A"
        },
        {
          "codigo": "0153902",
          "descricao": "Criação de ovinos, inclusive para produção de lã",
          "secao": "A"
        },
        {
          "codigo": "0154700",
          "descricao": "Criação de suínos",
          "secao": "A"
        }
      ]
    },
    "local": {
      "matriz": {
        "cnpj": "65274133000100",
        "cep": "13707899",
        "uf": "SP",
        "municipio_codigo": "6317",
        "municipio_nome": "CASA BRANCA",
        "bairro": "RURAL",
        "logradouro_completo": "sitio vila colina sn",
        "raw": {
          "tipo_logradouro": "SITIO",
          "logradouro": "VILA COLINA",
          "numero": "S/N",
          "complemento": null
        },
        "geo": null
      },
      "filiais": []
    },
    "contato": {
      "emails": [],
      "telefones": [
        {
          "ddd": "19",
          "numero": "82920800",
          "e164": "+551982920800",
          "tipo": "fixo",
          "origens": [
            "rfb_telefone1_matriz"
          ]
        }
      ]
    },
    "socios": {
      "pessoas_fisicas": [],
      "pessoas_juridicas_nacionais": [],
      "pessoas_juridicas_estrangeiras": [],
      "administradores_diretores": [],
      "totais": {
        "pessoas_fisicas": 0,
        "pessoas_juridicas_nacionais": 0,
        "pessoas_juridicas_estrangeiras": 0,
        "administradores_diretores_titulares": 0,
        "administradores_diretores_representantes": 0,
        "geral": 0
      }
    },
    "_periodo": "202604",
    "_data_carga": "2026-05-02T23:17:26.474149+00:00",
    "_fontes": [
      "rfb_bronze_202604"
    ]
  },
  {
    "cnpj_basico": "65277889",
    "cnpj_matriz": "65277889000102",
    "nome": "CESAR AUGUSTO THOMAZELA  E OUTRA",
    "nome_fantasia": null,
    "data_abertura": "2026-02-18",
    "idade_anos": 0.2,
    "total_filiais": 0,
    "status_porte": "grande",
    "local_uf": "SP",
    "status": {
      "operacional": "ativa",
      "porte": "grande",
      "natureza_juridica": {
        "codigo": "4120",
        "descricao": "Produtor Rural (Pessoa Física)",
        "categoria": "individual"
      },
      "raw_rfb": {
        "situacao_cadastral": {
          "codigo": "02",
          "descricao": "ativa",
          "data": "2026-02-18",
          "motivo": {
            "codigo": "00",
            "descricao": "SEM MOTIVO"
          }
        },
        "porte": {
          "codigo": "05",
          "descricao": null
        },
        "qualificacao_responsavel": {
          "codigo": "59",
          "descricao": "Produtor Rural"
        }
      }
    },
    "regime_tributario": {
      "tipo": "nao_simples",
      "fonte": "rfb_dados_abertos",
      "historico": {
        "data_opcao_simples": null,
        "data_exclusao_simples": null,
        "data_opcao_mei": null,
        "data_exclusao_mei": null
      }
    },
    "financeiro": {
      "capital_social_brl": 0.0
    },
    "industria": {
      "setor": "Agropecuária",
      "segmento": null,
      "cnae_principal": {
        "codigo": "0111302",
        "descricao": "Cultivo de milho",
        "secao": "A"
      },
      "cnae_secundarios": [
        {
          "codigo": "0115600",
          "descricao": "Cultivo de soja",
          "secao": "A"
        },
        {
          "codigo": "0113000",
          "descricao": "Cultivo de cana-de-açúcar",
          "secao": "A"
        },
        {
          "codigo": "0116401",
          "descricao": "Cultivo de amendoim",
          "secao": "A"
        },
        {
          "codigo": "0111399",
          "descricao": "Cultivo de outros cereais não especificados anteriormente",
          "secao": "A"
        },
        {
          "codigo": "0133404",
          "descricao": "Cultivo de cítricos, exceto laranja",
          "secao": "A"
        }
      ]
    },
    "local": {
      "matriz": {
        "cnpj": "65277889000102",
        "cep": "13507899",
        "uf": "SP",
        "municipio_codigo": "6979",
        "municipio_nome": "RIO CLARO",
        "bairro": "AREA RURAL DE RIO CLARO",
        "logradouro_completo": "area rural sn",
        "raw": {
          "tipo_logradouro": "AREA",
          "logradouro": "RURAL",
          "numero": "S/N",
          "complemento": null
        },
        "geo": null
      },
      "filiais": []
    },
    "contato": {
      "emails": [],
      "telefones": [
        {
          "ddd": "19",
          "numero": "91817550",
          "e164": "+551991817550",
          "tipo": "fixo",
          "origens": [
            "rfb_telefone1_matriz"
          ]
        }
      ]
    },
    "socios": {
      "pessoas_fisicas": [],
      "pessoas_juridicas_nacionais": [],
      "pessoas_juridicas_estrangeiras": [],
      "administradores_diretores": [
        {
          "nome": "CESAR AUGUSTO THOMAZELA",
          "nome_norm": "cesar augusto thomazela",
          "cpf_visivel": "***698438**",
          "qualificacao": {
            "codigo": "59",
            "descricao": "Produtor Rural"
          },
          "papel": "titular",
          "representando": null,
          "data_entrada": "2026-02-18",
          "faixa_etaria": {
            "codigo": "5",
            "descricao": null
          }
        },
        {
          "nome": "LAIS MOMESSO GIMENES MESCHIATTI",
          "nome_norm": "lais momesso gimenes meschiatti",
          "cpf_visivel": "***080238**",
          "qualificacao": {
            "codigo": "59",
            "descricao": "Produtor Rural"
          },
          "papel": "titular",
          "representando": null,
          "data_entrada": "2026-02-18",
          "faixa_etaria": {
            "codigo": "4",
            "descricao": null
          }
        }
      ],
      "totais": {
        "pessoas_fisicas": 0,
        "pessoas_juridicas_nacionais": 0,
        "pessoas_juridicas_estrangeiras": 0,
        "administradores_diretores_titulares": 2,
        "administradores_diretores_representantes": 0,
        "geral": 2
      }
    },
    "_periodo": "202604",
    "_data_carga": "2026-05-02T23:17:26.474149+00:00",
    "_fontes": [
      "rfb_bronze_202604"
    ]
  },
  {
    "cnpj_basico": "65290687",
    "cnpj_matriz": "65290687000192",
    "nome": "CILMARA CONSONI NASCIMENTO",
    "nome_fantasia": null,
    "data_abertura": "2026-02-20",
    "idade_anos": 0.2,
    "total_filiais": 0,
    "status_porte": "grande",
    "local_uf": "SP",
    "status": {
      "operacional": "ativa",
      "porte": "grande",
      "natureza_juridica": {
        "codigo": "4120",
        "descricao": "Produtor Rural (Pessoa Física)",
        "categoria": "individual"
      },
      "raw_rfb": {
        "situacao_cadastral": {
          "codigo": "02",
          "descricao": "ativa",
          "data": "2026-02-20",
          "motivo": {
            "codigo": "00",
            "descricao": "SEM MOTIVO"
          }
        },
        "porte": {
          "codigo": "05",
          "descricao": null
        },
        "qualificacao_responsavel": {
          "codigo": "59",
          "descricao": "Produtor Rural"
        }
      }
    },
    "regime_tributario": {
      "tipo": "nao_simples",
      "fonte": "rfb_dados_abertos",
      "historico": {
        "data_opcao_simples": null,
        "data_exclusao_simples": null,
        "data_opcao_mei": null,
        "data_exclusao_mei": null
      }
    },
    "financeiro": {
      "capital_social_brl": 0.0
    },
    "industria": {
      "setor": "Agropecuária",
      "segmento": null,
      "cnae_principal": {
        "codigo": "0111302",
        "descricao": "Cultivo de milho",
        "secao": "A"
      },
      "cnae_secundarios": [
        {
          "codigo": "0115600",
          "descricao": "Cultivo de soja",
          "secao": "A"
        },
        {
          "codigo": "0113000",
          "descricao": "Cultivo de cana-de-açúcar",
          "secao": "A"
        }
      ]
    },
    "local": {
      "matriz": {
        "cnpj": "65290687000192",
        "cep": "19886899",
        "uf": "SP",
        "municipio_codigo": "6301",
        "municipio_nome": "CANDIDO MOTA",
        "bairro": "ESTRADA AGUA DA JACUTINGA",
        "logradouro_completo": "sitio sao joao 0",
        "raw": {
          "tipo_logradouro": "SITIO",
          "logradouro": "SAO JOAO",
          "numero": "0",
          "complemento": null
        },
        "geo": null
      },
      "filiais": []
    },
    "contato": {
      "emails": [
        {
          "dominio": "fetaesp.org.br",
          "enderecos": [
            {
              "valor": "strpalmital2@fetaesp.org.br",
              "local_part": "strpalmital2",
              "origens": [
                "rfb_matriz"
              ]
            }
          ]
        }
      ],
      "telefones": [
        {
          "ddd": "18",
          "numero": "33511399",
          "e164": "+551833511399",
          "tipo": "fax",
          "origens": [
            "rfb_fax_matriz",
            "rfb_telefone1_matriz"
          ]
        }
      ]
    },
    "socios": {
      "pessoas_fisicas": [],
      "pessoas_juridicas_nacionais": [],
      "pessoas_juridicas_estrangeiras": [],
      "administradores_diretores": [],
      "totais": {
        "pessoas_fisicas": 0,
        "pessoas_juridicas_nacionais": 0,
        "pessoas_juridicas_estrangeiras": 0,
        "administradores_diretores_titulares": 0,
        "administradores_diretores_representantes": 0,
        "geral": 0
      }
    },
    "_periodo": "202604",
    "_data_carga": "2026-05-02T23:17:26.474149+00:00",
    "_fontes": [
      "rfb_bronze_202604"
    ]
  },
  {
    "cnpj_basico": "65282883",
    "cnpj_matriz": "65282883000115",
    "nome": "ALESSANDRO DAL BEN",
    "nome_fantasia": null,
    "data_abertura": "2026-02-20",
    "idade_anos": 0.2,
    "total_filiais": 0,
    "status_porte": "grande",
    "local_uf": "SP",
    "status": {
      "operacional": "ativa",
      "porte": "grande",
      "natureza_juridica": {
        "codigo": "4120",
        "descricao": "Produtor Rural (Pessoa Física)",
        "categoria": "individual"
      },
      "raw_rfb": {
        "situacao_cadastral": {
          "codigo": "02",
          "descricao": "ativa",
          "data": "2026-02-20",
          "motivo": {
            "codigo": "00",
            "descricao": "SEM MOTIVO"
          }
        },
        "porte": {
          "codigo": "05",
          "descricao": null
        },
        "qualificacao_responsavel": {
          "codigo": "59",
          "descricao": "Produtor Rural"
        }
      }
    },
    "regime_tributario": {
      "tipo": "nao_simples",
      "fonte": "rfb_dados_abertos",
      "historico": {
        "data_opcao_simples": null,
        "data_exclusao_simples": null,
        "data_opcao_mei": null,
        "data_exclusao_mei": null
      }
    },
    "financeiro": {
      "capital_social_brl": 0.0
    },
    "industria": {
      "setor": "Agropecuária",
      "segmento": null,
      "cnae_principal": {
        "codigo": "0111302",
        "descricao": "Cultivo de milho",
        "secao": "A"
      },
      "cnae_secundarios": [
        {
          "codigo": "0115600",
          "descricao": "Cultivo de soja",
          "secao": "A"
        }
      ]
    },
    "local": {
      "matriz": {
        "cnpj": "65282883000115",
        "cep": "19864899",
        "uf": "SP",
        "municipio_codigo": "6367",
        "municipio_nome": "CRUZALIA",
        "bairro": "SITIO SAO DONATO",
        "logradouro_completo": "area rural sn",
        "raw": {
          "tipo_logradouro": "AREA",
          "logradouro": "RURAL",
          "numero": "SN",
          "complemento": null
        },
        "geo": null
      },
      "filiais": []
    },
    "contato": {
      "emails": [],
      "telefones": [
        {
          "ddd": "18",
          "numero": "97935360",
          "e164": "+551897935360",
          "tipo": "fixo",
          "origens": [
            "rfb_telefone1_matriz"
          ]
        }
      ]
    },
    "socios": {
      "pessoas_fisicas": [],
      "pessoas_juridicas_nacionais": [],
      "pessoas_juridicas_estrangeiras": [],
      "administradores_diretores": [],
      "totais": {
        "pessoas_fisicas": 0,
        "pessoas_juridicas_nacionais": 0,
        "pessoas_juridicas_estrangeiras": 0,
        "administradores_diretores_titulares": 0,
        "administradores_diretores_representantes": 0,
        "geral": 0
      }
    },
    "_periodo": "202604",
    "_data_carga": "2026-05-02T23:17:26.474149+00:00",
    "_fontes": [
      "rfb_bronze_202604"
    ]
  },
  {
    "cnpj_basico": "65298778",
    "cnpj_matriz": "65298778000174",
    "nome": "EUGENIO SARTORI NETO E OUTRA",
    "nome_fantasia": null,
    "data_abertura": "2026-02-19",
    "idade_anos": 0.2,
    "total_filiais": 0,
    "status_porte": "grande",
    "local_uf": "SP",
    "status": {
      "operacional": "ativa",
      "porte": "grande",
      "natureza_juridica": {
        "codigo": "4120",
        "descricao": "Produtor Rural (Pessoa Física)",
        "categoria": "individual"
      },
      "raw_rfb": {
        "situacao_cadastral": {
          "codigo": "02",
          "descricao": "ativa",
          "data": "2026-02-19",
          "motivo": {
            "codigo": "00",
            "descricao": "SEM MOTIVO"
          }
        },
        "porte": {
          "codigo": "05",
          "descricao": null
        },
        "qualificacao_responsavel": {
          "codigo": "59",
          "descricao": "Produtor Rural"
        }
      }
    },
    "regime_tributario": {
      "tipo": "nao_simples",
      "fonte": "rfb_dados_abertos",
      "historico": {
        "data_opcao_simples": null,
        "data_exclusao_simples": null,
        "data_opcao_mei": null,
        "data_exclusao_mei": null
      }
    },
    "financeiro": {
      "capital_social_brl": 0.0
    },
    "industria": {
      "setor": "Agropecuária",
      "segmento": null,
      "cnae_principal": {
        "codigo": "0111302",
        "descricao": "Cultivo de milho",
        "secao": "A"
      },
      "cnae_secundarios": [
        {
          "codigo": "0115600",
          "descricao": "Cultivo de soja",
          "secao": "A"
        },
        {
          "codigo": "0119999",
          "descricao": "Cultivo de outras plantas de lavoura temporária não especificadas anteriormente",
          "secao": "A"
        }
      ]
    },
    "local": {
      "matriz": {
        "cnpj": "65298778000174",
        "cep": "19383899",
        "uf": "SP",
        "municipio_codigo": "0818",
        "municipio_nome": "RIBEIRAO DOS INDIOS",
        "bairro": "EST. VICINAL P/ STO. ANASTACIO",
        "logradouro_completo": "area sitio esperanca km 3 sn",
        "raw": {
          "tipo_logradouro": "AREA",
          "logradouro": "SITIO ESPERANCA, KM 3",
          "numero": "SN",
          "complemento": null
        },
        "geo": null
      },
      "filiais": []
    },
    "contato": {
      "emails": [],
      "telefones": [
        {
          "ddd": "43",
          "numero": "99727292",
          "e164": "+554399727292",
          "tipo": "fixo",
          "origens": [
            "rfb_telefone1_matriz"
          ]
        },
        {
          "ddd": "18",
          "numero": "32622110",
          "e164": "+551832622110",
          "tipo": "fax",
          "origens": [
            "rfb_fax_matriz"
          ]
        },
        {
          "ddd": "18",
          "numero": "32621977",
          "e164": "+551832621977",
          "tipo": "fixo",
          "origens": [
            "rfb_telefone2_matriz"
          ]
        }
      ]
    },
    "socios": {
      "pessoas_fisicas": [],
      "pessoas_juridicas_nacionais": [],
      "pessoas_juridicas_estrangeiras": [],
      "administradores_diretores": [
        {
          "nome": "LUCILENE DE FATIMA SARTORI",
          "nome_norm": "lucilene de fatima sartori",
          "cpf_visivel": "***284179**",
          "qualificacao": {
            "codigo": "59",
            "descricao": "Produtor Rural"
          },
          "papel": "titular",
          "representando": null,
          "data_entrada": "2026-02-19",
          "faixa_etaria": {
            "codigo": "6",
            "descricao": null
          }
        },
        {
          "nome": "EUGENIO SARTORI NETO",
          "nome_norm": "eugenio sartori neto",
          "cpf_visivel": "***160539**",
          "qualificacao": {
            "codigo": "59",
            "descricao": "Produtor Rural"
          },
          "papel": "titular",
          "representando": null,
          "data_entrada": "2026-02-19",
          "faixa_etaria": {
            "codigo": "6",
            "descricao": null
          }
        }
      ],
      "totais": {
        "pessoas_fisicas": 0,
        "pessoas_juridicas_nacionais": 0,
        "pessoas_juridicas_estrangeiras": 0,
        "administradores_diretores_titulares": 2,
        "administradores_diretores_representantes": 0,
        "geral": 2
      }
    },
    "_periodo": "202604",
    "_data_carga": "2026-05-02T23:17:26.474149+00:00",
    "_fontes": [
      "rfb_bronze_202604"
    ]
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_cnpj.empresas\` LIMIT 5'`

## Quirks e armadilhas

- **Município é UPPERCASE sem acento** (segue padrão RFB). `local.matriz.municipio_nome = 'BELO HORIZONTE'` — não `'Belo Horizonte'`.
- **CNAE como prefix**: pra grupo (restaurantes/bares `5611-2/01` a `'05`), use `STARTS_WITH(industria.cnae_principal.codigo, '5611')`. Pra holdings específicas: `codigo = '6463800'`.
- **Filiais ATIVAS embutidas** — Baixadas/Inaptas estão **fora** do array. Pra ver filial fechada, use `bronze_cnpj.estabelecimentos`.
- **`status_porte` e `local_uf` (raiz) são denormalizações** de `status.porte` e `local.matriz.uf` — só servem pra CLUSTER BY funcionar. Os campos canônicos são os aninhados.
- **`pat = NULL` na maioria** — ~99% das 27.4M empresas não têm PAT (programa opcional). PAT vem de JOIN com `gold_pat.empresas`, não embutido aqui.
- **Capital social já parseado** (FLOAT64). Não precisa do `SAFE_CAST(REPLACE(...))` que é necessário em bronze.
- **Sócios PJ estrangeiros podem ter `cnpj_basico_socio = NULL`** quando o documento não é CNPJ brasileiro — não JOIN com gold_cnpj nesse caso.
- **`industria.segmento` sempre `null`** — placeholder pra v2.1 (dicionário comercial sub-CNAE).
- **`local.matriz.geo` sempre `null`** — geocoding ainda não rodou.

## Tabelas relacionadas

- [`gold_cnpj.pessoas`](gold_cnpj.pessoas.md) — pessoas PF deduplicadas com array de CNPJs onde aparecem (cross-empresa)
- [`gold_pat.empresas`](gold_pat.empresas.md) — JOIN por `cnpj_basico` pra trazer total trabalhadores, folha estimada, cobertura PAT
- [`gold_energia.estabelecimentos_consumo_certo`](gold_energia.estabelecimentos_consumo_certo.md) — JOIN por `cnpj_basico` (agregar UCs antes); kwh, distribuidora, ACL
- [`bronze_cnpj.empresas`](bronze_cnpj.empresas.md) — fonte cru RFB
- [`silver_cnpj.estabelecimentos_dominios`](silver_cnpj.estabelecimentos_dominios.md) — emails/dominios separados (pré-filtro)
- [`silver_cnpj.socios`](silver_cnpj.socios.md) — sócios denormalizados sem categorização em buckets

## Templates SQL

### Caso A: lookup direto por CNPJ_BASICO
```sql
SELECT *
FROM `data-hacker-488115.gold_cnpj.empresas`
WHERE cnpj_basico = '16501555';     -- Stone Pagamentos
```

### Caso B: empresas grandes Financeiro com filial em UF X (nested + scalar filters)
```sql
SELECT cnpj_basico, nome, financeiro.capital_social_brl, total_filiais
FROM `data-hacker-488115.gold_cnpj.empresas`
WHERE status.porte = 'grande'
  AND industria.setor = 'Financeiro'
  AND status.operacional = 'ativa'
  AND EXISTS (SELECT 1 FROM UNNEST(local.filiais) f WHERE f.uf = 'RJ')
ORDER BY financeiro.capital_social_brl DESC
LIMIT 50;
```

### Caso C: ICP composto — empresas com sócio PJ estrangeiro dos EUA + capital ≥ R$ 100M
```sql
SELECT
  e.cnpj_basico, e.nome, e.financeiro.capital_social_brl,
  ARRAY(SELECT pj.razao_social FROM UNNEST(e.socios.pessoas_juridicas_estrangeiras) pj
        WHERE pj.pais.codigo = 'US') AS holdings_us
FROM `data-hacker-488115.gold_cnpj.empresas` e
WHERE e.status.operacional = 'ativa'
  AND e.financeiro.capital_social_brl >= 100000000
  AND EXISTS (
    SELECT 1 FROM UNNEST(e.socios.pessoas_juridicas_estrangeiras) pj
    WHERE pj.pais.codigo = 'US'
  )
ORDER BY e.financeiro.capital_social_brl DESC;
```

### Caso D: distribuição por setor + porte (agg)
```sql
SELECT industria.setor, status.porte, COUNT(*) AS empresas
FROM `data-hacker-488115.gold_cnpj.empresas`
WHERE status.operacional = 'ativa'
GROUP BY 1, 2
ORDER BY empresas DESC;
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
