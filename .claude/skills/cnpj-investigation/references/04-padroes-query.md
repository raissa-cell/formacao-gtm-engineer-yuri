# Padrões de Query (SQL Reutilizáveis)

Trechos prontos para BigQuery sobre `data-hacker-488115.bronze_cnpj`. Sempre adapte os filtros.

---

## 1. Universo de PJ ativa (filtro padrão)

```sql
WITH ativos AS (
  SELECT
    e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV,
    e.NOME_FANTASIA, e.UF, e.MUNICIPIO,
    e.CNAE_FISCAL_PRINCIPAL,
    e.DDD1, e.TELEFONE1, e.DDD2, e.TELEFONE2,
    e.CORREIO_ELETRONICO,
    emp.RAZAO_SOCIAL, emp.NATUREZA_JURIDICA, emp.PORTE,
    SAFE_CAST(REPLACE(emp.CAPITAL_SOCIAL, ',', '.') AS FLOAT64) AS capital_social
  FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
  LEFT JOIN (
    SELECT CNPJ_BASICO,
      ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL,
      ANY_VALUE(NATUREZA_JURIDICA) AS NATUREZA_JURIDICA,
      ANY_VALUE(PORTE) AS PORTE,
      ANY_VALUE(CAPITAL_SOCIAL) AS CAPITAL_SOCIAL
    FROM `data-hacker-488115.bronze_cnpj.empresas`
    GROUP BY CNPJ_BASICO
  ) emp USING (CNPJ_BASICO)
  WHERE e.SITUACAO_CADASTRAL = '02'
)
SELECT * FROM ativos LIMIT 100
```

---

## 2. Buscar CNAE pelo nome

```sql
SELECT CODIGO, DESCRICAO
FROM `data-hacker-488115.bronze_cnpj.cnaes`
WHERE LOWER(DESCRICAO) LIKE '%palavra%'
ORDER BY CODIGO
```

Sempre rode isso ANTES de filtrar por CNAE em `estabelecimentos`.

---

## 3. Empresas que combinam CNAE + palavra-chave no nome

```sql
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA,
  e.CNAE_FISCAL_PRINCIPAL, e.UF
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02'
  AND (
    e.CNAE_FISCAL_PRINCIPAL = '4722901'  -- CNAE alvo
    OR UPPER(emp.RAZAO_SOCIAL) LIKE '%TERMO%'
    OR UPPER(emp.RAZAO_SOCIAL) LIKE '%TÊRMO%'  -- variação acentuada
    OR UPPER(e.NOME_FANTASIA) LIKE '%TERMO%'
  )
```

---

## 4. Cruzar empresas com sócio por nome

```sql
WITH socios_alvo AS (
  SELECT DISTINCT CNPJ_BASICO, NOME_SOCIO, FAIXA_ETARIA
  FROM `data-hacker-488115.bronze_cnpj.socios`
  WHERE UPPER(NOME_SOCIO) LIKE '%FULANO%'
    AND UPPER(NOME_SOCIO) LIKE '%SOBRENOME%'
),
empresas_alvo AS (
  -- ver Padrão 3
)
SELECT ea.*, sa.NOME_SOCIO, sa.FAIXA_ETARIA
FROM empresas_alvo ea
JOIN socios_alvo sa USING (CNPJ_BASICO)
```

---

## 5. Detalhe completo de uma empresa (uma view de tudo)

```sql
WITH alvo AS (
  SELECT '12345678' AS CNPJ_BASICO  -- substituir
)
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  CASE e.ID_MATRIZ_FILIAL WHEN '1' THEN 'MATRIZ' ELSE 'FILIAL' END AS tipo,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA,
  e.SITUACAO_CADASTRAL,
  PARSE_DATE('%Y%m%d', NULLIF(e.DATA_INICIO_ATIVIDADE, '0')) AS data_inicio,
  e.CNAE_FISCAL_PRINCIPAL,
  cnae.DESCRICAO AS cnae_desc,
  e.CNAE_FISCAL_SECUNDARIA,
  emp.NATUREZA_JURIDICA,
  nat.DESCRICAO AS natureza_desc,
  emp.PORTE,
  SAFE_CAST(REPLACE(emp.CAPITAL_SOCIAL, ',', '.') AS FLOAT64) AS capital_social,
  TRIM(CONCAT(IFNULL(e.TIPO_LOGRADOURO,''), ' ', IFNULL(e.LOGRADOURO,''),
              ', ', IFNULL(e.NUMERO,''),
              IF(e.COMPLEMENTO != '', CONCAT(' ', e.COMPLEMENTO), ''),
              ' - ', IFNULL(e.BAIRRO,''),
              ' - ', IFNULL(e.CEP,''),
              ' - ', m.DESCRICAO, '/', e.UF)) AS endereco,
  CONCAT(IFNULL(e.DDD1,''), ' ', IFNULL(e.TELEFONE1,'')) AS fone1,
  CONCAT(IFNULL(e.DDD2,''), ' ', IFNULL(e.TELEFONE2,'')) AS fone2,
  e.CORREIO_ELETRONICO
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
JOIN alvo USING (CNPJ_BASICO)
LEFT JOIN (
  SELECT CNPJ_BASICO,
    ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL,
    ANY_VALUE(NATUREZA_JURIDICA) AS NATUREZA_JURIDICA,
    ANY_VALUE(PORTE) AS PORTE,
    ANY_VALUE(CAPITAL_SOCIAL) AS CAPITAL_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
LEFT JOIN `data-hacker-488115.bronze_cnpj.cnaes` cnae
  ON e.CNAE_FISCAL_PRINCIPAL = cnae.CODIGO
LEFT JOIN `data-hacker-488115.bronze_cnpj.naturezas` nat
  ON emp.NATUREZA_JURIDICA = nat.CODIGO
LEFT JOIN `data-hacker-488115.bronze_cnpj.municipios` m
  ON e.MUNICIPIO = m.CODIGO
ORDER BY e.CNPJ_ORDEM
```

---

## 6. Sócios de uma empresa (com qualificação)

```sql
SELECT
  s.NOME_SOCIO,
  s.CNPJ_CPF_SOCIO,
  q.DESCRICAO AS qualificacao,
  PARSE_DATE('%Y%m%d', NULLIF(s.DATA_ENTRADA_SOCIEDADE, '0')) AS data_entrada,
  s.FAIXA_ETARIA,
  CASE s.ID_SOCIO WHEN '1' THEN 'PJ' WHEN '2' THEN 'PF' WHEN '3' THEN 'Estrangeiro' END AS tipo,
  s.NOME_REPRESENTANTE
FROM `data-hacker-488115.bronze_cnpj.socios` s
LEFT JOIN `data-hacker-488115.bronze_cnpj.qualificacoes` q
  ON s.QUALIFICACAO_SOCIO = q.CODIGO
WHERE s.CNPJ_BASICO = '12345678'
ORDER BY data_entrada
```

---

## 7. Buscar por telefone

```sql
WITH numero AS (SELECT '11999998888' AS alvo)
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.UF,
  CONCAT(IFNULL(e.DDD1,''), IFNULL(e.TELEFONE1,'')) AS fone1_raw,
  CONCAT(IFNULL(e.DDD2,''), IFNULL(e.TELEFONE2,'')) AS fone2_raw
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
CROSS JOIN numero
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE
  REGEXP_REPLACE(CONCAT(IFNULL(e.DDD1,''), IFNULL(e.TELEFONE1,'')), r'\D', '') LIKE CONCAT('%', numero.alvo, '%')
  OR REGEXP_REPLACE(CONCAT(IFNULL(e.DDD2,''), IFNULL(e.TELEFONE2,'')), r'\D', '') LIKE CONCAT('%', numero.alvo, '%')
```

---

## 8. Buscar por e-mail (exato e fuzzy)

```sql
-- Exato
SELECT CONCAT(CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV) AS CNPJ, *
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE LOWER(CORREIO_ELETRONICO) = 'fulano@email.com'

-- Fuzzy (parte local + variantes)
SELECT *
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE LOWER(CORREIO_ELETRONICO) LIKE '%fulano%'
   OR LOWER(CORREIO_ELETRONICO) LIKE '%fulan%'
LIMIT 50
```

---

## 9. Empresas em um município (por nome)

```sql
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.CNAE_FISCAL_PRINCIPAL
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
JOIN `data-hacker-488115.bronze_cnpj.municipios` m ON e.MUNICIPIO = m.CODIGO
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02'
  AND m.DESCRICAO = 'PORTO FELIZ'  -- nomes em maiúsculo
  AND e.UF = 'SP'  -- desambiguar (existem múltiplos municípios homônimos)
```

---

## 10. Sócios em comum entre 2 empresas

```sql
WITH socios_a AS (
  SELECT DISTINCT NOME_SOCIO, CNPJ_CPF_SOCIO
  FROM `data-hacker-488115.bronze_cnpj.socios`
  WHERE CNPJ_BASICO = '11111111'
),
socios_b AS (
  SELECT DISTINCT NOME_SOCIO, CNPJ_CPF_SOCIO
  FROM `data-hacker-488115.bronze_cnpj.socios`
  WHERE CNPJ_BASICO = '22222222'
)
SELECT a.NOME_SOCIO, a.CNPJ_CPF_SOCIO
FROM socios_a a JOIN socios_b b USING (CNPJ_CPF_SOCIO)
```

---

## 11. Todas as empresas de um sócio (rede de uma pessoa)

```sql
SELECT
  s.NOME_SOCIO,
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA,
  e.SITUACAO_CADASTRAL, e.UF,
  q.DESCRICAO AS qualificacao,
  PARSE_DATE('%Y%m%d', NULLIF(s.DATA_ENTRADA_SOCIEDADE, '0')) AS data_entrada
FROM `data-hacker-488115.bronze_cnpj.socios` s
JOIN `data-hacker-488115.bronze_cnpj.estabelecimentos` e
  ON s.CNPJ_BASICO = e.CNPJ_BASICO AND e.ID_MATRIZ_FILIAL = '1'
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
LEFT JOIN `data-hacker-488115.bronze_cnpj.qualificacoes` q
  ON s.QUALIFICACAO_SOCIO = q.CODIGO
WHERE s.CNPJ_CPF_SOCIO = '***123456**'  -- CPF mascarado
ORDER BY data_entrada DESC
```

---

## 12. Buscar empresa pelo domínio do site (a partir do e-mail)

```sql
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.UF, e.MUNICIPIO,
  e.CORREIO_ELETRONICO,
  SPLIT(LOWER(e.CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02'
  AND LOWER(e.CORREIO_ELETRONICO) LIKE '%@gabriel.com.br'
   -- ⚠️ usar @ no início do filtro evita falso positivo (ex.: naogabriel.com.br)
```

---

## 13. Domínio + sócio (cruzamento)

Caso clássico: "Existe empresa com site X.com.br cujo sócio se chame Y?"

```sql
WITH empresas_dominio AS (
  SELECT DISTINCT e.CNPJ_BASICO,
         emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.UF,
         e.CORREIO_ELETRONICO
  FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
  LEFT JOIN (
    SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
    FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
  ) emp USING (CNPJ_BASICO)
  WHERE e.SITUACAO_CADASTRAL = '02'
    AND LOWER(e.CORREIO_ELETRONICO) LIKE '%@gabriel.com.br'
)
SELECT
  ed.CNPJ_BASICO, ed.RAZAO_SOCIAL, ed.NOME_FANTASIA, ed.UF,
  ed.CORREIO_ELETRONICO,
  s.NOME_SOCIO, q.DESCRICAO AS qualificacao
FROM empresas_dominio ed
JOIN `data-hacker-488115.bronze_cnpj.socios` s USING (CNPJ_BASICO)
LEFT JOIN `data-hacker-488115.bronze_cnpj.qualificacoes` q
  ON s.QUALIFICACAO_SOCIO = q.CODIGO
WHERE UPPER(s.NOME_SOCIO) LIKE '%ERICK%'
   OR UPPER(s.NOME_SOCIO) LIKE 'ERIC %'
```

---

## 14. Top domínios próprios em um setor

Mapear quais domínios concentram mais CNPJs ativos num setor — útil para detectar grupos econômicos, escritórios de contabilidade, ou ranking de empresas com presença digital.

```sql
WITH provedores_genericos AS (
  SELECT dominio FROM UNNEST([
    'gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com.br',
    'uol.com.br', 'bol.com.br', 'terra.com.br', 'ig.com.br',
    'icloud.com', 'live.com', 'globomail.com', 'r7.com',
    'oi.com.br', 'msn.com', 'ymail.com', 'hotmail.com.br',
    'outlook.com.br', 'live.com.br', 'yahoo.com', 'aol.com',
    'protonmail.com'
  ]) AS dominio
)
SELECT
  SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio,
  COUNT(DISTINCT CNPJ_BASICO) AS empresas
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE SITUACAO_CADASTRAL = '02'
  AND CNAE_FISCAL_PRINCIPAL = '6201501'  -- ex: software
  AND CORREIO_ELETRONICO LIKE '%@%'
  AND SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] NOT IN (
    SELECT dominio FROM provedores_genericos
  )
GROUP BY 1
HAVING empresas >= 3
ORDER BY empresas DESC
LIMIT 50
```

---

## 15. % de empresas com domínio próprio (maturidade digital de um setor)

```sql
WITH provedores_genericos AS (
  SELECT dominio FROM UNNEST([
    'gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com.br',
    'uol.com.br', 'bol.com.br', 'terra.com.br', 'ig.com.br',
    'icloud.com', 'live.com'
  ]) AS dominio
)
SELECT
  e.UF,
  COUNT(*) AS total_empresas,
  COUNTIF(e.CORREIO_ELETRONICO LIKE '%@%') AS com_email,
  COUNTIF(SPLIT(LOWER(e.CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)]
            NOT IN (SELECT dominio FROM provedores_genericos)
          AND e.CORREIO_ELETRONICO LIKE '%@%') AS com_dominio_proprio,
  ROUND(100 * COUNTIF(SPLIT(LOWER(e.CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)]
            NOT IN (SELECT dominio FROM provedores_genericos)
          AND e.CORREIO_ELETRONICO LIKE '%@%') / COUNT(*), 1) AS pct_dominio_proprio
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
WHERE e.SITUACAO_CADASTRAL = '02'
  AND e.CNAE_FISCAL_PRINCIPAL = '6201501'
  AND e.ID_MATRIZ_FILIAL = '1'
GROUP BY 1
ORDER BY pct_dominio_proprio DESC
```

---

## 16. Endereço completo formatado

```sql
TRIM(CONCAT(
  IFNULL(TIPO_LOGRADOURO, ''), ' ',
  IFNULL(LOGRADOURO, ''),
  IF(NUMERO != '', CONCAT(', ', NUMERO), ''),
  IF(COMPLEMENTO != '', CONCAT(' ', COMPLEMENTO), ''),
  IF(BAIRRO != '', CONCAT(' - ', BAIRRO), ''),
  IF(CEP != '', CONCAT(' - CEP ', CEP), ''),
  ' - ', UF
)) AS endereco
```

---

## Dicas de performance

- **Sempre filtre por `SITUACAO_CADASTRAL = '02'` cedo** — reduz a base em ~60%.
- Use `CNPJ_BASICO` (8 dígitos) para JOINs entre tabelas. É indexado.
- Evite `SELECT *` em `estabelecimentos`/`empresas`/`socios`. São tabelas de 30M-70M linhas.
- Use `LIMIT 100` em buscas exploratórias antes de rodar query final.
- `LIKE '%termo%'` faz scan completo. Quando possível, use prefixo (`LIKE 'termo%'`) para indexação.
