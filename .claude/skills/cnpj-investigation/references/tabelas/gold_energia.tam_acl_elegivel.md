# `gold_energia.tam_acl_elegivel` — _TODO: título curto_

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
    "tensao": "MT",
    "cod_id_encr": "7CB676D57114874E00C536916E6DCAD2A5D3CB8C9A5ABC06335DF359CD9A6EF9",
    "distribuidora_sigla": "CERMC",
    "distribuidora_nome": "COOPERATIVA DE ELETRIFICACAO E DESENVOLVIMENTO DA REGIAO DE MOGI DAS CRUZES",
    "distribuidora_cnpj": "52548732000114",
    "ponto_conexao": "1803",
    "cnae_formatado": "4731-8/00",
    "cnae": "4731800",
    "cnae_grupo": "47318",
    "classe_consumo": "CO1",
    "grupo_tensao": "MT",
    "grupo_tarifario": "A4",
    "situacao_ativa": "AT",
    "data_conexao": "21/03/1975",
    "carga_instalada_kw": 35.0,
    "dem_contratada_kw": 52.0,
    "endereco_completo": "Rural",
    "logradouro": "rural",
    "numero": null,
    "bairro": "Posto da Serra",
    "cep_formatado": "13670-000",
    "cep": "13670000",
    "municipio_ibge": "3547502",
    "uf": "SP",
    "lat": -21.77516812,
    "lon": -47.53696589,
    "kwh_medio_mensal": 22992.25,
    "kwh_total_12m": 275907.0,
    "ene_12_meses_kwh": [
      23550.0,
      22583.0,
      24678.0,
      23084.0,
      23477.0,
      21402.0,
      21916.0,
      21711.0,
      23886.0,
      23451.0,
      22904.0,
      23265.0
    ],
    "porte_consumo": "muito_alto",
    "cnpj": "36343345000195",
    "cnpj_basico": "36343345",
    "nome_fantasia": "MEGA MOVEIS",
    "match_tier": "B",
    "match_score": 1.0,
    "match_n_candidatos": 13,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": true,
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
    "razao_social": "DJONATO DANIEL DA SILVA AMARAL",
    "natureza_juridica": "Empresário (Individual)",
    "porte_empresa": "NÃO INFORMADO",
    "capital_social": 10000.0,
    "opcao_simples": true,
    "opcao_mei": false,
    "cnae_principal_descricao": "Comércio varejista de móveis",
    "idade_anos": 6,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "RS",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  },
  {
    "tensao": "MT",
    "cod_id_encr": "1D5DD51FB9341EC51F587CA8495750EDB2A78CE350FF02816E0458A633F564BC",
    "distribuidora_sigla": "EMT",
    "distribuidora_nome": "ENERGISA MATO GROSSO - DISTRIBUIDORA DE ENERGIA S.A.",
    "distribuidora_cnpj": "03467321000199",
    "ponto_conexao": "6141747PON",
    "cnae_formatado": "4511-1/01",
    "cnae": "4511101",
    "cnae_grupo": "45111",
    "classe_consumo": "CO1",
    "grupo_tensao": "MT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "14/05/1986",
    "carga_instalada_kw": 103500.0,
    "dem_contratada_kw": 100.0,
    "endereco_completo": "RUA FERNANDO CORREA DA COSTA",
    "logradouro": "rua fernando correa da costa",
    "numero": null,
    "bairro": "JD. GUANABARA",
    "cep_formatado": "78740-000",
    "cep": "78740000",
    "municipio_ibge": "5107602",
    "uf": "MT",
    "lat": -16.45321909,
    "lon": -54.64982197,
    "kwh_medio_mensal": 0.0,
    "kwh_total_12m": 0.0,
    "ene_12_meses_kwh": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "porte_consumo": "baixo",
    "cnpj": "65740925000114",
    "cnpj_basico": "65740925",
    "nome_fantasia": "CAROLINO VEICULOS",
    "match_tier": "B",
    "match_score": 0.86,
    "match_n_candidatos": 1,
    "uc_tem_ceg_gd": true,
    "ceg_gd": "GD.MT.000.605.866",
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": true,
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
    "razao_social": "CAROLINO VEICULOS LTDA",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "porte_empresa": "EMPRESA DE PEQUENO PORTE",
    "capital_social": 300000.0,
    "opcao_simples": true,
    "opcao_mei": false,
    "cnae_principal_descricao": "Comércio a varejo de automóveis, camionetas e utilitários usados",
    "idade_anos": 0,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "MT",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  },
  {
    "tensao": "MT",
    "cod_id_encr": "F9CA4044FC874991A5D751FA45E85A9126A42DE234DF8502836D256F38D6A324",
    "distribuidora_sigla": "CERAL ANITÁPOLIS",
    "distribuidora_nome": "COOPERATIVA DE DISTRIBUICAO DE ENERGIA ELETRICA DE ANITAPOLIS - CERAL",
    "distribuidora_cnpj": "75826404000138",
    "ponto_conexao": "10793",
    "cnae_formatado": "4120-4/00",
    "cnae": "4120400",
    "cnae_grupo": "41204",
    "classe_consumo": "IN",
    "grupo_tensao": "MT",
    "grupo_tarifario": "A4",
    "situacao_ativa": "AT",
    "data_conexao": "03/01/2014",
    "carga_instalada_kw": 290.0,
    "dem_contratada_kw": 30.0,
    "endereco_completo": "SC 447 - KM 30",
    "logradouro": "sc",
    "numero": "447",
    "bairro": "RIO FIORITA",
    "cep_formatado": "88860-000",
    "cep": "88860000",
    "municipio_ibge": "4217600",
    "uf": "SC",
    "lat": -28.57566946,
    "lon": -49.43895326,
    "kwh_medio_mensal": 3940.0,
    "kwh_total_12m": 47280.0,
    "ene_12_meses_kwh": [
      4289.0,
      3754.0,
      4398.0,
      4888.0,
      4776.0,
      4482.0,
      4667.0,
      4581.0,
      2877.0,
      2526.0,
      2956.0,
      3086.0
    ],
    "porte_consumo": "alto",
    "cnpj": "20355520000124",
    "cnpj_basico": "20355520",
    "nome_fantasia": "JSA CONTABILIDADE",
    "match_tier": "B",
    "match_score": 1.0,
    "match_n_candidatos": 1,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": true,
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
    "razao_social": "SOLANGE ALBERTON DE SOUZA",
    "natureza_juridica": "Empresário (Individual)",
    "porte_empresa": "NÃO INFORMADO",
    "capital_social": 15000.0,
    "opcao_simples": true,
    "opcao_mei": false,
    "cnae_principal_descricao": "Atividades de contabilidade",
    "idade_anos": 12,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "SC",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  },
  {
    "tensao": "MT",
    "cod_id_encr": "81017963487038AD0F7B554901211184A8E0FA622AF1A6D22E95B18ED3098CA3",
    "distribuidora_sigla": "EQUATORIAL PA",
    "distribuidora_nome": "EQUATORIAL PARA DISTRIBUIDORA DE ENERGIA S.A.",
    "distribuidora_cnpj": "04895728000180",
    "ponto_conexao": "113820984",
    "cnae_formatado": "4511-1/01",
    "cnae": "4511101",
    "cnae_grupo": "45111",
    "classe_consumo": "CO9",
    "grupo_tensao": "MT",
    "grupo_tarifario": "A4",
    "situacao_ativa": "AT",
    "data_conexao": "23/11/2020",
    "carga_instalada_kw": 364795.0,
    "dem_contratada_kw": 85.0,
    "endereco_completo": "R. MUNICIPALIDADE",
    "logradouro": "r municipalidade",
    "numero": null,
    "bairro": "REDUTO",
    "cep_formatado": "66053-180",
    "cep": "66053180",
    "municipio_ibge": "1501402",
    "uf": "PA",
    "lat": -1.44441753,
    "lon": -48.49359699,
    "kwh_medio_mensal": 19472.906666666666,
    "kwh_total_12m": 233674.88,
    "ene_12_meses_kwh": [
      20978.91,
      18147.63,
      19523.25,
      19554.91,
      18648.75,
      18219.81,
      19712.11,
      20134.7,
      19651.84,
      19189.43,
      19187.86,
      20725.68
    ],
    "porte_consumo": "muito_alto",
    "cnpj": "17677769000141",
    "cnpj_basico": "17677769",
    "nome_fantasia": "CONDOMINIO DO EDIFICIO COMERCIAL 203 OFFICES",
    "match_tier": "B",
    "match_score": 0.86,
    "match_n_candidatos": 5,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": true,
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
    "razao_social": "CONDOMINIO DO EDIFICIO COMERCIAL 203 OFFICES",
    "natureza_juridica": "Condomínio Edilício",
    "porte_empresa": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": "Condomínios prediais",
    "idade_anos": 13,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "AL",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  },
  {
    "tensao": "MT",
    "cod_id_encr": "936B4C107B6218B1ED76BE4BAC85B8F2F1AC7EDE57E157A037FF2971FDB7C1F3",
    "distribuidora_sigla": "ESS",
    "distribuidora_nome": "ENERGISA SUL-SUDESTE - DISTRIBUIDORA DE ENERGIA S.A.",
    "distribuidora_cnpj": "07282377000120",
    "ponto_conexao": "2114670474",
    "cnae_formatado": "0210-1/05",
    "cnae": "0210105",
    "cnae_grupo": "02101",
    "classe_consumo": "CO1",
    "grupo_tensao": "MT",
    "grupo_tarifario": "B3",
    "situacao_ativa": "AT",
    "data_conexao": "11/01/2018",
    "carga_instalada_kw": 7516.0,
    "dem_contratada_kw": 30.0,
    "endereco_completo": "SIT QUINTA NUNES DA COSTA - GLEBA C, 0",
    "logradouro": "sit quinta nunes da costa gleba c",
    "numero": "0",
    "bairro": "RURAL",
    "cep_formatado": "13830-000",
    "cep": "13830000",
    "municipio_ibge": "3548005",
    "uf": "SP",
    "lat": -22.62006389,
    "lon": -46.92520591,
    "kwh_medio_mensal": 0.0,
    "kwh_total_12m": 0.0,
    "ene_12_meses_kwh": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "porte_consumo": "baixo",
    "cnpj": "15912430000157",
    "cnpj_basico": "15912430",
    "nome_fantasia": null,
    "match_tier": "A",
    "match_score": 1.0,
    "match_n_candidatos": 1,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "gd_fontes": null,
    "gd_modalidades": null,
    "elegivel_acl": true,
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
    "razao_social": "6. TABELIONATO DE PROTESTO DE TITULOS DO FORO CENTRAL DA COMARCA DA REGIAO METROPOLITANA DE CURITIBA",
    "natureza_juridica": "Serviço Notarial e Registral (Cartório)",
    "porte_empresa": "DEMAIS",
    "capital_social": 0.0,
    "opcao_simples": null,
    "opcao_mei": null,
    "cnae_principal_descricao": "Cartórios",
    "idade_anos": 14,
    "situacao_descricao": "ATIVA",
    "n_estabelecimentos_ativos": 1,
    "ufs_atuacao": "PR",
    "n_ufs_atuacao": 1,
    "safra": "2024-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_energia.tam_acl_elegivel\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_energia.tam_acl_elegivel`
WHERE ...
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
