# `gold_energia.estabelecimentos_360` — _TODO: título curto_

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
| `tensao` | STRING |  |  |
| `cod_id_encr` | STRING |  |  |
| `distribuidora_sigla` | STRING |  |  |
| `distribuidora_nome` | STRING |  |  |
| `distribuidora_cnpj` | STRING |  |  |
| `ponto_conexao` | STRING |  |  |
| `cnae_formatado` | STRING |  |  |
| `cnae` | STRING |  |  |
| `cnae_grupo` | STRING |  |  |
| `classe_consumo` | STRING |  |  |
| `grupo_tensao` | STRING |  |  |
| `grupo_tarifario` | STRING |  |  |
| `situacao_ativa` | STRING |  |  |
| `data_conexao` | STRING |  |  |
| `carga_instalada_kw` | FLOAT |  |  |
| `dem_contratada_kw` | FLOAT |  |  |
| `endereco_completo` | STRING |  |  |
| `logradouro` | STRING |  |  |
| `numero` | STRING |  |  |
| `bairro` | STRING |  |  |
| `cep_formatado` | STRING |  |  |
| `cep` | STRING |  |  |
| `municipio_ibge` | STRING |  |  |
| `uf` | STRING |  |  |
| `lat` | FLOAT |  |  |
| `lon` | FLOAT |  |  |
| `kwh_medio_mensal` | FLOAT |  |  |
| `kwh_total_12m` | FLOAT |  |  |
| `ene_12_meses_kwh` | FLOAT | REPEATED |  |
| `porte_consumo` | STRING |  |  |
| `cnpj` | STRING |  |  |
| `cnpj_basico` | STRING |  |  |
| `nome_fantasia` | STRING |  |  |
| `match_tier` | STRING |  |  |
| `match_score` | FLOAT |  |  |
| `match_n_candidatos` | INTEGER |  |  |
| `uc_tem_ceg_gd` | BOOLEAN |  |  |
| `ceg_gd` | STRING |  |  |
| `cnpj_tem_gd` | BOOLEAN |  |  |
| `gd_potencia_kw` | FLOAT |  |  |
| `gd_fontes` | STRING |  |  |
| `gd_modalidades` | STRING |  |  |
| `elegivel_acl` | BOOLEAN |  |  |
| `no_acl_livre` | BOOLEAN |  |  |
| `no_acl_especial` | BOOLEAN |  |  |
| `grupo_no_acl_livre` | BOOLEAN |  |  |
| `grupo_no_acl_especial` | BOOLEAN |  |  |
| `grupo_n_cnpjs_acl` | INTEGER |  |  |
| `cnpj_eh_consumidor_acl` | BOOLEAN |  |  |
| `cnpj_eh_comercializador` | BOOLEAN |  |  |
| `cnpj_eh_gerador` | BOOLEAN |  |  |
| `cnpj_eh_distribuidor` | BOOLEAN |  |  |
| `cnpj_eh_varejista` | BOOLEAN |  |  |
| `acl_classe_principal` | STRING |  |  |
| `acl_submercados` | STRING |  |  |
| `acl_tipos_energia` | STRING |  |  |
| `acl_n_perfis_cnpj` | INTEGER |  |  |
| `acl_via_varejista` | BOOLEAN |  |  |
| `mwh_acl_12m_cnpj` | FLOAT |  |  |
| `mwh_acl_mensal_medio` | FLOAT |  |  |
| `mwmed_compra_12m` | FLOAT |  |  |
| `mwmed_venda_12m` | FLOAT |  |  |
| `match_qualidade_volumetria` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `porte_empresa` | STRING |  |  |
| `capital_social` | FLOAT |  |  |
| `opcao_simples` | BOOLEAN |  |  |
| `opcao_mei` | BOOLEAN |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `idade_anos` | INTEGER |  |  |
| `situacao_descricao` | STRING |  |  |
| `n_estabelecimentos_ativos` | INTEGER |  |  |
| `ufs_atuacao` | STRING |  |  |
| `n_ufs_atuacao` | INTEGER |  |  |
| `safra` | DATE |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "tensao": "BT",
    "cod_id_encr": "9ED5E4D73FCBAAA76ACF629401809AF297A0233421AACC417E3DF6681D2DA2F8",
    "distribuidora_sigla": "CPFL-PAULISTA",
    "distribuidora_nome": "COMPANHIA PAULISTA DE FORCA E LUZ",
    "distribuidora_cnpj": "33050196000188",
    "ponto_conexao": "453717679",
    "cnae_formatado": "6550-2/00",
    "cnae": "6550200",
    "cnae_grupo": "65502",
    "classe_consumo": "CO9",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "01/08/1988",
    "carga_instalada_kw": 68.0,
    "dem_contratada_kw": null,
    "endereco_completo": "AV IPIRANGA 1147 REPUBLICA",
    "logradouro": "av ipiranga 1147 republica",
    "numero": null,
    "bairro": "AV IPIRANGA 1147 REPUBLICA",
    "cep_formatado": "01039-000",
    "cep": "01039000",
    "municipio_ibge": "3550308",
    "uf": "SP",
    "lat": -23.54043824,
    "lon": -46.63809047,
    "kwh_medio_mensal": 64.63966666666666,
    "kwh_total_12m": 775.6759999999999,
    "ene_12_meses_kwh": [
      100.0,
      70.0,
      86.966,
      80.0,
      170.0,
      50.0,
      16.8,
      30.5,
      50.0,
      50.0,
      23.6,
      47.81
    ],
    "porte_consumo": "baixo",
    "cnpj": null,
    "cnpj_basico": null,
    "nome_fantasia": null,
    "match_tier": null,
    "match_score": null,
    "match_n_candidatos": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "grupo_n_cnpjs_acl": null,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "acl_classe_principal": null,
    "acl_submercados": null,
    "acl_tipos_energia": null,
    "acl_n_perfis_cnpj": null,
    "acl_via_varejista": null,
    "mwh_acl_12m_cnpj": null,
    "mwh_acl_mensal_medio": null,
    "mwmed_compra_12m": null,
    "mwmed_venda_12m": null,
    "match_qualidade_volumetria": null,
    "razao_social": null,
    "natureza_juridica": null,
    "porte_empresa": null,
    "capital_social": null,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": null,
    "idade_anos": null,
    "situacao_descricao": null,
    "n_estabelecimentos_ativos": null,
    "ufs_atuacao": null,
    "n_ufs_atuacao": null,
    "safra": "2024-12-31"
  },
  {
    "tensao": "BT",
    "cod_id_encr": "ADF6621F02521EF5F30E0C8C0B14C758115E1FDED90F6B62AB6EEEC36E22C295",
    "distribuidora_sigla": "CPFL-PAULISTA",
    "distribuidora_nome": "COMPANHIA PAULISTA DE FORCA E LUZ",
    "distribuidora_cnpj": "33050196000188",
    "ponto_conexao": "576656",
    "cnae_formatado": "6810-2/02",
    "cnae": "6810202",
    "cnae_grupo": "68102",
    "classe_consumo": "CO1",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "01/09/1984",
    "carga_instalada_kw": 409.0,
    "dem_contratada_kw": null,
    "endereco_completo": "R COSTA RICA 126 JARDIM AMERICA",
    "logradouro": "r costa rica 126 jardim america",
    "numero": null,
    "bairro": "R COSTA RICA 126 JARDIM AMERICA",
    "cep_formatado": "01437-010",
    "cep": "01437010",
    "municipio_ibge": "3550308",
    "uf": "SP",
    "lat": -23.57257857,
    "lon": -46.67243703,
    "kwh_medio_mensal": 987.7673333333332,
    "kwh_total_12m": 11853.207999999999,
    "ene_12_meses_kwh": [
      1532.8,
      100.0,
      1327.248,
      1057.94,
      1033.83,
      1999.28,
      750.62,
      677.1,
      806.8,
      806.8,
      754.02,
      1006.77
    ],
    "porte_consumo": "medio",
    "cnpj": null,
    "cnpj_basico": null,
    "nome_fantasia": null,
    "match_tier": null,
    "match_score": null,
    "match_n_candidatos": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "grupo_n_cnpjs_acl": null,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "acl_classe_principal": null,
    "acl_submercados": null,
    "acl_tipos_energia": null,
    "acl_n_perfis_cnpj": null,
    "acl_via_varejista": null,
    "mwh_acl_12m_cnpj": null,
    "mwh_acl_mensal_medio": null,
    "mwmed_compra_12m": null,
    "mwmed_venda_12m": null,
    "match_qualidade_volumetria": null,
    "razao_social": null,
    "natureza_juridica": null,
    "porte_empresa": null,
    "capital_social": null,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": null,
    "idade_anos": null,
    "situacao_descricao": null,
    "n_estabelecimentos_ativos": null,
    "ufs_atuacao": null,
    "n_ufs_atuacao": null,
    "safra": "2024-12-31"
  },
  {
    "tensao": "BT",
    "cod_id_encr": "6D47A169F658A0BCB7A5CCCDDAC010144334FDC099E86B6E7FE15B36EEAAA596",
    "distribuidora_sigla": "CPFL-PAULISTA",
    "distribuidora_nome": "COMPANHIA PAULISTA DE FORCA E LUZ",
    "distribuidora_cnpj": "33050196000188",
    "ponto_conexao": null,
    "cnae_formatado": "4731-8/00",
    "cnae": "4731800",
    "cnae_grupo": "47318",
    "classe_consumo": "CO1",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "25/11/1991",
    "carga_instalada_kw": 675.0,
    "dem_contratada_kw": null,
    "endereco_completo": "AV BRG FARIA LIMA 2232 JARDIM PAULISTANO",
    "logradouro": "av brg faria lima 2232 jardim paulistano",
    "numero": null,
    "bairro": "AV BRG FARIA LIMA 2232 JARDIM PAULISTANO",
    "cep_formatado": "01451-000",
    "cep": "01451000",
    "municipio_ibge": "3550308",
    "uf": "SP",
    "lat": -23.57637756,
    "lon": -46.6878264,
    "kwh_medio_mensal": 5463.232833333333,
    "kwh_total_12m": 65558.794,
    "ene_12_meses_kwh": [
      6294.0,
      5433.0,
      8539.074,
      6131.6,
      6737.97,
      5092.8,
      4337.09,
      3100.26,
      5283.8,
      6346.2,
      3033.66,
      5229.34
    ],
    "porte_consumo": "alto",
    "cnpj": null,
    "cnpj_basico": null,
    "nome_fantasia": null,
    "match_tier": null,
    "match_score": null,
    "match_n_candidatos": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "grupo_n_cnpjs_acl": null,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "acl_classe_principal": null,
    "acl_submercados": null,
    "acl_tipos_energia": null,
    "acl_n_perfis_cnpj": null,
    "acl_via_varejista": null,
    "mwh_acl_12m_cnpj": null,
    "mwh_acl_mensal_medio": null,
    "mwmed_compra_12m": null,
    "mwmed_venda_12m": null,
    "match_qualidade_volumetria": null,
    "razao_social": null,
    "natureza_juridica": null,
    "porte_empresa": null,
    "capital_social": null,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": null,
    "idade_anos": null,
    "situacao_descricao": null,
    "n_estabelecimentos_ativos": null,
    "ufs_atuacao": null,
    "n_ufs_atuacao": null,
    "safra": "2024-12-31"
  },
  {
    "tensao": "BT",
    "cod_id_encr": "57E20AA147DDB7E82B7E9D0F02C8EA2742CE893D5861E66D5A7A14D5536652FD",
    "distribuidora_sigla": "CPFL-PAULISTA",
    "distribuidora_nome": "COMPANHIA PAULISTA DE FORCA E LUZ",
    "distribuidora_cnpj": "33050196000188",
    "ponto_conexao": "687776",
    "cnae_formatado": "4771-7/04",
    "cnae": "4771704",
    "cnae_grupo": "47717",
    "classe_consumo": "CO1",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "01/02/1967",
    "carga_instalada_kw": 195.0,
    "dem_contratada_kw": null,
    "endereco_completo": "R OSCAR CINTRA GORDINHO 24 LIBERDADE",
    "logradouro": "r oscar cintra gordinho 24 liberdade",
    "numero": null,
    "bairro": "R OSCAR CINTRA GORDINHO 24 LIBERDADE",
    "cep_formatado": "01512-010",
    "cep": "01512010",
    "municipio_ibge": "3550308",
    "uf": "SP",
    "lat": -23.5542342,
    "lon": -46.62964818,
    "kwh_medio_mensal": 159.43916666666667,
    "kwh_total_12m": 1913.27,
    "ene_12_meses_kwh": [
      225.0,
      50.0,
      0.0,
      232.0,
      218.0,
      215.0,
      155.4,
      115.9,
      183.0,
      198.0,
      126.85,
      194.12
    ],
    "porte_consumo": "baixo",
    "cnpj": null,
    "cnpj_basico": null,
    "nome_fantasia": null,
    "match_tier": null,
    "match_score": null,
    "match_n_candidatos": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "grupo_n_cnpjs_acl": null,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "acl_classe_principal": null,
    "acl_submercados": null,
    "acl_tipos_energia": null,
    "acl_n_perfis_cnpj": null,
    "acl_via_varejista": null,
    "mwh_acl_12m_cnpj": null,
    "mwh_acl_mensal_medio": null,
    "mwmed_compra_12m": null,
    "mwmed_venda_12m": null,
    "match_qualidade_volumetria": null,
    "razao_social": null,
    "natureza_juridica": null,
    "porte_empresa": null,
    "capital_social": null,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": null,
    "idade_anos": null,
    "situacao_descricao": null,
    "n_estabelecimentos_ativos": null,
    "ufs_atuacao": null,
    "n_ufs_atuacao": null,
    "safra": "2024-12-31"
  },
  {
    "tensao": "BT",
    "cod_id_encr": "45CF8AC0642B94AE5F8646B786B7B53D7717A83C749182A7A65EBDBFCF4F54CB",
    "distribuidora_sigla": "CPFL-PAULISTA",
    "distribuidora_nome": "COMPANHIA PAULISTA DE FORCA E LUZ",
    "distribuidora_cnpj": "33050196000188",
    "ponto_conexao": "948131",
    "cnae_formatado": "6202-3/00",
    "cnae": "6202300",
    "cnae_grupo": "62023",
    "classe_consumo": "CO1",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "11/02/2015",
    "carga_instalada_kw": 1.0,
    "dem_contratada_kw": null,
    "endereco_completo": "R BAIA GRANDE S/N VILA BELA",
    "logradouro": "r baia grande s n vila bela",
    "numero": null,
    "bairro": "R BAIA GRANDE S/N VILA BELA",
    "cep_formatado": "03202-000",
    "cep": "03202000",
    "municipio_ibge": "3550308",
    "uf": "SP",
    "lat": -23.58403182,
    "lon": -46.52957339,
    "kwh_medio_mensal": 66.81475,
    "kwh_total_12m": 801.777,
    "ene_12_meses_kwh": [
      74.4,
      74.4,
      75.667,
      74.4,
      64.77,
      74.4,
      60.48,
      44.12,
      74.4,
      72.0,
      43.9,
      68.84
    ],
    "porte_consumo": "baixo",
    "cnpj": "29799290000167",
    "cnpj_basico": "29799290",
    "nome_fantasia": "INCREMENT TECNOLOGIA",
    "match_tier": "C",
    "match_score": 0.3,
    "match_n_candidatos": 3,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "grupo_n_cnpjs_acl": null,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "acl_classe_principal": null,
    "acl_submercados": null,
    "acl_tipos_energia": null,
    "acl_n_perfis_cnpj": null,
    "acl_via_varejista": null,
    "mwh_acl_12m_cnpj": null,
    "mwh_acl_mensal_medio": null,
    "mwmed_compra_12m": null,
    "mwmed_venda_12m": null,
    "match_qualidade_volumetria": null,
    "razao_social": "INCREMENT TECNOLOGIA E INOVACAO LTDA",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "porte_empresa": "NÃO INFORMADO",
    "capital_social": 30000.0,
    "opcao_simples": false,
    "opcao_mei": false,
    "cnae_principal_descricao": "Desenvolvimento e licenciamento de programas de computador customizáveis",
    "idade_anos": 8,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "SP",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_energia.estabelecimentos_360\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_energia.estabelecimentos_360`
WHERE ...
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
