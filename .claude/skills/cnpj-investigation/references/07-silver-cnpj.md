# `silver_cnpj` — descoberta de grupo econômico (domínios + sócios denormalizados)

A camada **`silver_cnpj`** existe pra responder rapidamente perguntas que em `bronze_cnpj` exigem JOINs pesados ou parsing de texto repetido (extrair domínio do email, normalizar nome de sócio, denormalizar razão social do sócio PJ).

**Use silver primeiro. Volte pra bronze só se a silver não tiver o campo que precisa.**

> Doc operacional do pipeline: [`docs/cnpj/silver-pipeline.md`](../../../docs/cnpj/silver-pipeline.md)  
> Doc semântico (referência completa): [`docs/cnpj/silver-dicionario.md`](../../../docs/cnpj/silver-dicionario.md)

---

## 1. O que tem em `silver_cnpj`

### 1.1 Duas tabelas (físicas)

| Tabela | Linhas (~) | Granularidade | Cluster | Pra quê |
|---|---:|---|---|---|
| `silver_cnpj.estabelecimentos_dominios` | 49M (25,5M ativos) | 1 linha por **estabelecimento com email** | `(email_dominio_raiz, uf)` | Encontrar grupo via domínio do email |
| `silver_cnpj.socios` | 27,5M | 1 linha por **vínculo sócio↔empresa** | `(socio_nome_norm, socio_cnpj_basico)` | Buscar pessoa, holding, conglomerado |

**Diferença vs. bronze:**

- `estabelecimentos_dominios` **filtra** estabs sem `CORREIO_ELETRONICO` válido + adiciona campos derivados (`email_dominio`, `email_dominio_raiz`, `email_eh_pessoal_provider`, `cep5`, `endereco_norm`).
- `socios` é **denormalizada**: `qualificacao_nome` resolvido (não só código), `empresa_razao_social` denormalizada, `socio_razao_social` (se PJ) via lookup, `socio_nome_norm` normalizado pra busca direta.

### 1.2 Seis views (lentes prontas)

| View | Pergunta que responde |
|---|---|
| `silver_cnpj.grupos_por_dominio` | "Que CNPJs/razões usam o domínio X como e-mail?" |
| `silver_cnpj.empresas_por_endereco` | "Quem está nesse endereço/CEP segundo o CNPJ?" |
| `silver_cnpj.socios_por_pessoa` | "Em que empresas a pessoa Y aparece como sócia?" |
| `silver_cnpj.empresas_por_socio_pj` | "Que empresas são controladas pela holding Z (CNPJ raiz)?" |
| `silver_cnpj.grupos_via_socios` | "Que outros CNPJ_BASICOs compartilham sócio PJ com este?" |
| `silver_cnpj.rede_executivos` | "Quem são os board members serial (≥5 empresas)?" |

---

## 2. Quando usar silver vs. bronze

| Pergunta do usuário | Camada | Por quê |
|---|---|---|
| "Que empresas usam `@stone.com.br` como email?" | **silver** | Domínio já parseado e indexado |
| "Em que empresas a Maria Silva aparece como sócia?" | **silver** | `socio_nome_norm` permite busca direta sem `UPPER()+LIKE` |
| "Que empresas são controladas pela holding `49436665`?" | **silver** | `empresas_por_socio_pj` já lista direto |
| "Quem são os sócios da empresa 60.701.190?" | **silver** | `socios` traz `qualificacao_nome` resolvida |
| "Quais CNAEs essa empresa atua?" | **bronze** | `cnae_principal` está em ambas; secundárias só em bronze |
| "Endereço completo + telefone?" | **bronze** | silver não traz `complemento`, `ddd`, `telefone` |
| "Capital social, porte, MEI?" | **bronze** (`empresas`+`simples`) | silver não importa esses campos |
| "Buscar por palavra-chave em razão social" | **bronze** | silver tem `razao_social` mas não está clusterizada por nome |

**Regra prática:** silver é pra buscar **por domínio, sócio, ou endereço normalizado**. Pra qualquer outro filtro, ainda volta pra bronze.

---

## 3. Schemas em detalhe

### 3.1 `silver_cnpj.estabelecimentos_dominios`

```
cnpj14, cnpj_basico, razao_social, nome_fantasia, natureza_juridica
situacao_cadastral
email, email_local, email_dominio, email_dominio_raiz
email_eh_pessoal_provider  (BOOL — true se gmail/hotmail/uol/yahoo/etc.)
uf, cep8, cep5
cnae_principal
tipo_logradouro, logradouro, numero
endereco_norm  (logradouro lower sem acento + numero stripped)
_periodo, _data_carga
```

**eTLD+1 BR computado:** `mail.stone.com.br` → `email_dominio_raiz = stone.com.br`.

**Lista pessoal-provider (filtrada com `WHERE NOT email_eh_pessoal_provider`):** `gmail.com`, `hotmail.com`, `outlook.com`, `yahoo.com[.br]`, `live.com`, `uol.com.br`, `bol.com.br`, `terra.com.br`, `icloud.com`, `msn.com`, `ig.com.br`, `oi.com.br`, `globo.com`, `globomail.com`, `me.com`.

### 3.2 `silver_cnpj.socios`

```
empresa_cnpj_basico, empresa_razao_social, empresa_natureza_juridica
socio_tipo  ('PF' | 'PJ' | 'ESTRANGEIRO')
socio_nome, socio_nome_norm  (lower sem acento; CHAVE DE BUSCA)
socio_documento  (CNPJ-completo se PJ, CPF mascarado se PF)
socio_cnpj_basico  (NULL se PF; primeiros 8 dígitos se PJ)
socio_razao_social  (NULL se PF; razão da empresa-sócia se PJ)
socio_cpf_visible  (CPF mascarado pra desambiguar homônimos)
qualificacao_codigo, qualificacao_nome  (nome RESOLVIDO via JOIN)
data_entrada_sociedade  (DATE — já parseado de YYYYMMDD)
representante_legal_documento, representante_legal_nome, representante_legal_qualificacao_*
pais_codigo, pais_nome
faixa_etaria
_periodo, _data_carga
```

---

## 4. Casos de uso (templates SQL)

### 4.1 "Que empresas formam o grupo econômico do domínio X?"

```sql
SELECT *
FROM `data-hacker-488115.silver_cnpj.grupos_por_dominio`
WHERE email_dominio_raiz = 'stone.com.br'
ORDER BY estabs_ativos DESC;
```

→ retorna ~30 razões (Stone Pagamentos, Stone Logística, Pagar.me, Linx, Buy4 Processamento, Cappta, Instituto Stone Impacto, STNE Investimentos, Stone Franchising/DTVM/Cartões/SCD…) — incluindo aquisições com nome diferente.

### 4.2 "Em que empresas a pessoa Y aparece como sócia?"

```sql
SELECT
  socio_nome,
  n_empresas,
  empresas
FROM `data-hacker-488115.silver_cnpj.socios_por_pessoa`
WHERE socio_nome_norm = 'pedro zinner';
-- empresas é ARRAY<STRUCT<cnpj_basico, razao_social, qualificacao_nome, data_entrada>>
```

→ devolve as 40 empresas em que Pedro Zinner (CEO Stone) figura como sócio PF, com qualificação e data de entrada.

> ⚠️ `socio_nome_norm` é lowercase sem acento. **Sempre normalizar o input do usuário** antes de filtrar:
> ```python
> import unicodedata, re
> q = re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', user_input).encode('ascii','ignore').decode().lower()).strip()
> ```
> ou em SQL:
> ```sql
> WHERE socio_nome_norm = TRIM(REGEXP_REPLACE(
>   REGEXP_REPLACE(NORMALIZE_AND_CASEFOLD(@input, NFKD), r'[^a-z0-9 ]', ' '),
>   r'\s+', ' '))
> ```

### 4.3 "Que empresas são controladas pela holding Z?"

```sql
SELECT
  socio_razao_social,
  n_controladas,
  controladas
FROM `data-hacker-488115.silver_cnpj.empresas_por_socio_pj`
WHERE socio_cnpj_basico = '49436665';  -- STNE Investimentos S.A.
```

### 4.4 "Que outros CNPJs compartilham holding com este?"

```sql
SELECT
  IF(cnpj_a = '16501555', cnpj_b, cnpj_a) AS cnpj_irmao,
  holdings_em_comum,
  n_holdings_em_comum
FROM `data-hacker-488115.silver_cnpj.grupos_via_socios`
WHERE cnpj_a = '16501555' OR cnpj_b = '16501555'
ORDER BY n_holdings_em_comum DESC;
```

→ acha CNPJs-irmãos pelo critério "compartilha pelo menos 1 sócio PJ".

### 4.5 "Triangulação — domínio + sócio PJ pra confirmar grupo"

```sql
WITH grupo_dom AS (
  SELECT DISTINCT cnpj_basico FROM `silver_cnpj.estabelecimentos_dominios`
  WHERE email_dominio_raiz = 'stone.com.br' AND situacao_cadastral = '02'
),
grupo_soc AS (
  SELECT DISTINCT empresa_cnpj_basico AS cnpj_basico FROM `silver_cnpj.socios`
  WHERE socio_cnpj_basico = '49436665'  -- STNE Investimentos
)
SELECT cnpj_basico, 'domain' AS via FROM grupo_dom
UNION ALL
SELECT cnpj_basico, 'socio_pj' FROM grupo_soc;
```

A **interseção** (CNPJs em ambas) é o núcleo confirmado do grupo.

### 4.6 "Quem está neste endereço?" (descoberta inversa)

```sql
SELECT
  cnpj14, razao_social, situacao_cadastral,
  email_dominio_raiz, cnae_principal
FROM `data-hacker-488115.silver_cnpj.empresas_por_endereco`
WHERE uf = 'SP'
  AND cep5 = '04534'                    -- Joaquim Floriano, Itaim
  AND endereco_norm LIKE 'joaquim floriano%413%'
ORDER BY situacao_cadastral, razao_social;
```

→ revela todos os CNPJs que declararam aquele endereço fiscal, com os domínios usados — útil pra detectar coworking, contadores, ou conglomerado num mesmo prédio.

### 4.7 "Sócios em comum entre duas empresas"

```sql
WITH a AS (SELECT socio_documento, socio_nome_norm, socio_tipo
           FROM `silver_cnpj.socios` WHERE empresa_cnpj_basico = '16501555'),
     b AS (SELECT socio_documento, socio_nome_norm, socio_tipo
           FROM `silver_cnpj.socios` WHERE empresa_cnpj_basico = '16810540')
SELECT
  a.socio_tipo,
  COALESCE(a.socio_nome_norm, a.socio_documento) AS socio
FROM a JOIN b USING (socio_documento)
ORDER BY 1, 2;
```

→ confirma laço entre Stone Pagamentos e Stone Logística (sócios PF como Pedro Zinner, Tatiana Malamud, Andre Monteiro + sócio PJ STNE Investimentos).

### 4.8 "Empresas com domínio próprio em um setor (descobrir maturidade digital)"

```sql
SELECT
  email_dominio_raiz,
  COUNT(*) AS estabs,
  COUNTIF(situacao_cadastral = '02') AS estabs_ativos,
  ANY_VALUE(razao_social) AS razao_amostra
FROM `silver_cnpj.estabelecimentos_dominios`
WHERE NOT email_eh_pessoal_provider           -- exclui gmail/hotmail/etc.
  AND cnae_principal = '6201501'              -- desenvolvimento de software
  AND situacao_cadastral = '02'
GROUP BY email_dominio_raiz
HAVING estabs_ativos >= 3                    -- domínios com presença múltipla
ORDER BY estabs_ativos DESC
LIMIT 50;
```

### 4.9 "Top board members serial (PFs em N+ empresas)"

```sql
SELECT *
FROM `silver_cnpj.rede_executivos`
ORDER BY n_empresas DESC
LIMIT 30;
```

→ revela executivos/sócios profissionais que aparecem em dezenas de CNPJs (gestores serial, board fixo de fundos, etc.).

### 4.10 "Sócios PJ estrangeiros (capital externo)"

```sql
SELECT
  pais_nome,
  COUNT(DISTINCT empresa_cnpj_basico) AS empresas_com_socio_dali,
  ARRAY_AGG(DISTINCT socio_nome ORDER BY socio_nome LIMIT 5) AS amostra_socios
FROM `silver_cnpj.socios`
WHERE socio_tipo = 'ESTRANGEIRO'
GROUP BY pais_nome
ORDER BY empresas_com_socio_dali DESC
LIMIT 20;
```

### 4.11 "Concentração geográfica de um grupo"

```sql
SELECT uf, COUNT(*) AS estabs
FROM `silver_cnpj.estabelecimentos_dominios`
WHERE email_dominio_raiz = 'stone.com.br'
  AND situacao_cadastral = '02'
GROUP BY uf
ORDER BY estabs DESC;
```

### 4.12 "Empresas que mudaram de holding (rotação societária)"

```sql
SELECT
  empresa_cnpj_basico,
  ANY_VALUE(empresa_razao_social) AS razao,
  COUNT(DISTINCT socio_cnpj_basico) AS holdings_distintas,
  ARRAY_AGG(STRUCT(socio_razao_social, data_entrada_sociedade)
            ORDER BY data_entrada_sociedade) AS historico_holdings
FROM `silver_cnpj.socios`
WHERE socio_tipo = 'PJ'
GROUP BY empresa_cnpj_basico
HAVING holdings_distintas >= 3
ORDER BY holdings_distintas DESC
LIMIT 50;
```

→ empresas com ≥3 holdings distintas no histórico = candidatas a rastreio de M&A.

---

## 5. Por que silver vence bronze nesses cenários

| Cenário | Bronze (custo) | Silver (custo) |
|---|---|---|
| Buscar por domínio | scan 70M linhas + REGEXP_EXTRACT em runtime | scan clusterizado em `email_dominio_raiz` (<1s) |
| Buscar pessoa pelo nome | `UPPER(NOME_SOCIO) LIKE '%X%'` em 27,5M (com falsos positivos por acento) | `socio_nome_norm = ?` direto (cluster) |
| Sócio PJ → controladas | self-join `socios` × parse SUBSTR + JOIN empresas | view `empresas_por_socio_pj` pronta |
| Razão social do sócio PJ | sub-query manual em cada análise | denormalizado em `socio_razao_social` |
| Qualificação do sócio | JOIN com `qualificacoes` toda vez | denormalizado em `qualificacao_nome` |
| Endereço normalizado pra cruzar | regex inline | `endereco_norm` + `cep5` pré-computados |

---

## 6. Limitações da silver

- **Snapshot mensal**: silver é rebuildada após cada snapshot bronze. Não é tempo real.
- **Não tem `simples`/MEI**: para descobrir se é optante do Simples ou MEI, ainda precisa `bronze_cnpj.simples`.
- **Não tem CNAEs secundários**: `cnae_principal` está; secundárias só em bronze.
- **Não tem telefone/complemento**: silver foca em busca/identidade; campos descritivos completos ficam em bronze.
- **`email` é único por estabelecimento**: limitação herdada da RFB. Pode ser do contador, não do dono.
- **Casos-âncora atualizados em cada build** (ver `silver-dicionario.md` §6): `stone.com.br=439 ativos`, `arpexcapital.com.br=16`, `pedro_zinner=40 vínculos`, etc. Use pra sanity check.

---

## 7. Quando combinar silver + bronze

Padrão comum: **pivota na silver, enriquece em bronze**.

```sql
-- Pega CNPJs do grupo via silver, depois puxa atributos completos da bronze
WITH grupo AS (
  SELECT DISTINCT cnpj_basico
  FROM `silver_cnpj.estabelecimentos_dominios`
  WHERE email_dominio_raiz = 'stone.com.br'
    AND situacao_cadastral = '02'
)
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL,
  e.NOME_FANTASIA,
  e.CNAE_FISCAL_PRINCIPAL,
  cnae.DESCRICAO AS cnae_descricao,
  e.UF, e.MUNICIPIO,
  CONCAT(IFNULL(e.DDD1,''), IFNULL(e.TELEFONE1,'')) AS telefone,
  s.OPCAO_SIMPLES, s.OPCAO_MEI,
  SAFE_CAST(REPLACE(emp.CAPITAL_SOCIAL, ',', '.') AS FLOAT64) AS capital_social
FROM `bronze_cnpj.estabelecimentos` e
JOIN grupo USING (CNPJ_BASICO)
JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL,
         ANY_VALUE(CAPITAL_SOCIAL) AS CAPITAL_SOCIAL
  FROM `bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
LEFT JOIN `bronze_cnpj.cnaes` cnae ON e.CNAE_FISCAL_PRINCIPAL = cnae.CODIGO
LEFT JOIN `bronze_cnpj.simples` s USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02';
```

→ silver dá o **universo certo** (sem homônimos), bronze dá os **atributos completos** (CNAE descrito, telefone, capital, regime tributário).

---

## 8. Casos-âncora pra sanity check (devem retornar valores próximos)

Se as queries abaixo derem zero ou números muito diferentes do esperado, alertar — pode ser que a silver não foi atualizada após o último snapshot bronze.

```sql
-- 1. Domínio Stone — esperado ~439 ativos
SELECT COUNT(*) FROM `silver_cnpj.estabelecimentos_dominios`
WHERE email_dominio_raiz='stone.com.br' AND situacao_cadastral='02';

-- 2. Domínio Arpex Capital — esperado ~16 ativos
SELECT COUNT(*) FROM `silver_cnpj.estabelecimentos_dominios`
WHERE email_dominio_raiz='arpexcapital.com.br' AND situacao_cadastral='02';

-- 3. Pedro Zinner como sócio PF — esperado ≥1 (≈40)
SELECT COUNT(*) FROM `silver_cnpj.socios`
WHERE socio_nome_norm='pedro zinner' AND socio_tipo='PF';

-- 4. STNE Investimentos como holding — esperado ≥1 controlada
SELECT COUNT(DISTINCT empresa_cnpj_basico) FROM `silver_cnpj.socios`
WHERE socio_cnpj_basico = '49436665';

-- 5. Total da silver — esperado ≥25M ativos com domínio
SELECT COUNTIF(situacao_cadastral='02') FROM `silver_cnpj.estabelecimentos_dominios`;
```
