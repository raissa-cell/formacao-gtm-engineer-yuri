# Análise de Domínios (a partir de `CORREIO_ELETRONICO`)

O campo `estabelecimentos.CORREIO_ELETRONICO` guarda o e-mail cadastrado na RFB. A parte após o `@` é uma **chave analítica forte** que permite:

1. **Encontrar empresas pelo site** ("qual empresa tem site `gabriel.com.br`?")
2. **Filtrar empresas com domínio próprio** (mais maduras / com presença digital)
3. **Identificar grupos econômicos** (várias empresas usando o mesmo domínio = mesma operação)
4. **Cruzar com pessoas** ("empresa cujo site é X + sócio chamado Y")

---

## Extração do domínio

```sql
SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio
```

`SAFE_OFFSET(1)` retorna `NULL` se o e-mail estiver malformado (sem `@`). Sempre use ele em vez de `[OFFSET(1)]` para evitar erros.

---

## Classificação: provedor genérico vs. domínio próprio

### Provedores genéricos (NÃO são site da empresa)

```sql
-- Lista canônica
WITH provedores_genericos AS (
  SELECT dominio FROM UNNEST([
    'gmail.com', 'googlemail.com',
    'hotmail.com', 'hotmail.com.br', 'outlook.com', 'outlook.com.br', 'live.com', 'live.com.br', 'msn.com',
    'yahoo.com', 'yahoo.com.br', 'ymail.com',
    'uol.com.br', 'bol.com.br', 'terra.com.br', 'ig.com.br', 'r7.com', 'oi.com.br',
    'icloud.com', 'me.com', 'mac.com',
    'globomail.com', 'globo.com',
    'aol.com', 'protonmail.com', 'tutanota.com',
    'zipmail.com.br', 'click21.com.br'
  ]) AS dominio
)
```

### Domínio próprio

Tudo que **não** está na lista acima. Heurística: se o domínio termina em `.com.br`, `.net.br`, `.org.br`, `.adv.br`, `.ind.br`, `.med.br` (e não está na lista de genéricos), é provavelmente o site institucional.

### Códigos de país

`.br` (Brasil), `.com` sem `.br` (genérico internacional), `.co` (curto/startup), `.io` (tech), `.ai` (tech/AI), `.app` (apps).

---

## Padrões de query

### Padrão A — Buscar empresas por domínio exato

```sql
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.UF, e.MUNICIPIO,
  e.CORREIO_ELETRONICO
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02'
  AND LOWER(e.CORREIO_ELETRONICO) LIKE '%@gabriel.com.br'
```

> ⚠️ Use `LIKE '%@dominio.com.br'` (com `@` antes) — sem isso, captura falsos positivos como `naogabriel.com.br`.

### Padrão B — Empresas com domínio próprio (filtro setorial)

```sql
WITH provedores_genericos AS (
  SELECT dominio FROM UNNEST([
    'gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com.br',
    'uol.com.br', 'bol.com.br', 'terra.com.br', 'ig.com.br',
    'icloud.com', 'live.com', 'globomail.com', 'r7.com',
    'oi.com.br', 'msn.com', 'ymail.com', 'hotmail.com.br',
    'outlook.com.br', 'live.com.br', 'yahoo.com'
  ]) AS dominio
)
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  emp.RAZAO_SOCIAL,
  SPLIT(LOWER(e.CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio,
  e.UF
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) emp USING (CNPJ_BASICO)
WHERE e.SITUACAO_CADASTRAL = '02'
  AND e.CNAE_FISCAL_PRINCIPAL = '6201501'  -- ex.: desenvolvimento de software
  AND e.CORREIO_ELETRONICO IS NOT NULL
  AND e.CORREIO_ELETRONICO != ''
  AND SPLIT(LOWER(e.CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] NOT IN (
    SELECT dominio FROM provedores_genericos
  )
```

### Padrão C — Top domínios em um setor (concentração)

```sql
SELECT
  SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio,
  COUNT(DISTINCT CNPJ_BASICO) AS empresas
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE SITUACAO_CADASTRAL = '02'
  AND CNAE_FISCAL_PRINCIPAL = '6201501'
  AND CORREIO_ELETRONICO LIKE '%@%'
GROUP BY 1
HAVING empresas >= 5
ORDER BY empresas DESC
LIMIT 50
```

> Domínios com 5+ CNPJs ativos sob o mesmo são candidatos a:
> - Grupo econômico (matriz + filiais ou empresas-irmãs)
> - Contador/escritório de contabilidade que usa o próprio domínio
> - Coworking/holding compartilhada

### Padrão D — Domínio + Sócio (cruzamento)

```sql
WITH empresas_dominio AS (
  SELECT DISTINCT e.CNPJ_BASICO, e.CORREIO_ELETRONICO,
         emp.RAZAO_SOCIAL, e.NOME_FANTASIA, e.UF
  FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
  LEFT JOIN (
    SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
    FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
  ) emp USING (CNPJ_BASICO)
  WHERE e.SITUACAO_CADASTRAL = '02'
    AND LOWER(e.CORREIO_ELETRONICO) LIKE '%@gabriel.com.br'
)
SELECT
  CONCAT(ed.CNPJ_BASICO) AS CNPJ_BASICO,
  ed.RAZAO_SOCIAL, ed.NOME_FANTASIA, ed.UF, ed.CORREIO_ELETRONICO,
  s.NOME_SOCIO, q.DESCRICAO AS qualificacao
FROM empresas_dominio ed
JOIN `data-hacker-488115.bronze_cnpj.socios` s USING (CNPJ_BASICO)
LEFT JOIN `data-hacker-488115.bronze_cnpj.qualificacoes` q
  ON s.QUALIFICACAO_SOCIO = q.CODIGO
WHERE UPPER(s.NOME_SOCIO) LIKE '%ERICK%'
   OR UPPER(s.NOME_SOCIO) LIKE 'ERIC %'
```

### Padrão E — Empresas que compartilham mesmo domínio (rede por e-mail)

```sql
WITH empresas_por_dominio AS (
  SELECT
    SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio,
    CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV,
    NOME_FANTASIA, UF, MUNICIPIO
  FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
  WHERE SITUACAO_CADASTRAL = '02'
    AND LOWER(CORREIO_ELETRONICO) LIKE '%@exemplo.com.br'
)
SELECT
  CONCAT(CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV) AS CNPJ,
  e.RAZAO_SOCIAL, NOME_FANTASIA, UF
FROM empresas_por_dominio
LEFT JOIN (
  SELECT CNPJ_BASICO, ANY_VALUE(RAZAO_SOCIAL) AS RAZAO_SOCIAL
  FROM `data-hacker-488115.bronze_cnpj.empresas` GROUP BY CNPJ_BASICO
) e USING (CNPJ_BASICO)
ORDER BY e.RAZAO_SOCIAL
```

### Padrão F — Inferir domínio "provável" da empresa pelo nome de fantasia

Útil quando o usuário pergunta "qual o site de X?" mas o e-mail é do contador. Heurística:

```sql
-- Tenta achar empresa cujo domínio bate com slug do nome
WITH alvo AS (
  SELECT 'casa do beef' AS termo, 'casadobeef' AS slug
)
SELECT
  CONCAT(e.CNPJ_BASICO, e.CNPJ_ORDEM, e.CNPJ_DV) AS CNPJ,
  e.NOME_FANTASIA, e.CORREIO_ELETRONICO
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e, alvo
WHERE e.SITUACAO_CADASTRAL = '02'
  AND LOWER(e.NOME_FANTASIA) LIKE CONCAT('%', alvo.termo, '%')
  AND (LOWER(e.CORREIO_ELETRONICO) LIKE CONCAT('%@', alvo.slug, '%')
       OR LOWER(e.CORREIO_ELETRONICO) LIKE CONCAT('%@', alvo.termo, '%'))
```

---

## Heurísticas de leitura

### Sinais de empresa madura digitalmente

- E-mail com domínio próprio (não-genérico)
- Domínio bate com slug do nome fantasia (ex.: fantasia "Exemplo" + e-mail `@exemplo.com.br`)
- Múltiplos estabelecimentos compartilham o mesmo domínio (rede consolidada)

### Sinais de e-mail do contador (não da empresa)

- Domínio é de escritório de contabilidade (`@contabilidade*.com.br`, `@conta-*.com.br`)
- Mesmo e-mail aparece em **dezenas** de CNPJs sem relação aparente
- Parte local genérica (`contato@`, `contabil@`, `fiscal@`) com domínio que tem 50+ CNPJs

```sql
-- Detectar prováveis contadores
SELECT
  SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)] AS dominio,
  COUNT(DISTINCT CNPJ_BASICO) AS num_empresas
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE CORREIO_ELETRONICO LIKE '%contabil%@%'
   OR CORREIO_ELETRONICO LIKE '%contador%@%'
GROUP BY 1
HAVING num_empresas >= 10
ORDER BY num_empresas DESC
```

### Sinais de mesmo grupo econômico

Se 3+ CNPJs ativos compartilham:
- Mesmo domínio próprio (não-genérico) **E**
- Mesmo CEP ou bairro **OU** mesmo sócio em comum

→ forte indício de holding ou rede.

---

## Casos de uso comuns

### "Qual a empresa do site X.com.br?"

Padrão A. Reportar todos os CNPJs que usam aquele domínio + flag se for matriz/filial.

### "Existe empresa com site X + sócio chamado Y?"

Padrão D. Cruzamento direto.

### "Quantas empresas no setor Z têm site próprio?"

Padrão B + contagem. Reportar:
- Total ativo no setor
- Quantos têm e-mail
- Quantos têm domínio próprio (não-genérico)
- % com presença digital

### "Mapear todas as empresas do grupo @exemplo.com.br"

Padrão E. Tabular CNPJ, fantasia, UF, sócios.

### "Esse e-mail (joao@padariax.com.br) bate em outros CNPJs?"

Padrão A com filtro pelo e-mail completo OU pelo domínio.

---

## Limitações

- **1 e-mail por estabelecimento**: a RFB cadastra apenas um. Pode estar desatualizado, ser do contador, ou não existir mais.
- **Domínio próprio ≠ site ativo**: o domínio pode ter sido cadastrado e expirado. Não é validação de site online.
- **Match por nome**: empresa com fantasia "Gabriel" pode não ter site `gabriel.com.br` — pode usar `@gmail.com` ou domínio diferente. Sempre reporte o que está na base, não o que "deveria estar".
- **Privacidade**: o e-mail é dado pessoal mesmo sendo público. Reporte-o quando relevante para a pergunta, sem inflar contexto desnecessário.
