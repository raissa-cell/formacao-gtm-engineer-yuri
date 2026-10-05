# Guia de Experimentação de Marketing

Framework pra rodar testes controlados nos 3 pilares (Conteúdo, Ads, Outbound) sem virar achismo. Um experimento só conta como experimento se tiver hipótese registrada, métrica de sucesso definida antes do teste e uma decisão explícita no final.

## 1. O que é (e o que não é) um experimento aqui

É experimento: mudar UMA variável, com hipótese clara, e medir o efeito contra uma baseline conhecida.

Não é experimento: publicar um post diferente "pra ver o que rola", trocar copy de ad sem registrar o motivo, ou testar 3 coisas ao mesmo tempo e tentar atribuir o resultado depois.

Se não dá pra isolar a variável, não é teste — é só operação normal.

## 2. Tipos de variável testável por pilar

| Pilar | O que costuma variar |
|---|---|
| Conteúdo | Tema, hook (linha 1-2), formato (carrossel vs vídeo vs texto), dia/hora de publicação, CTA (comment-gate vs aberto) |
| Ads | Ângulo/criativo, público, oferta/material rico, formato de anúncio |
| Outbound | Linha de abertura, canal (LinkedIn DM vs email vs WhatsApp), sequência (cadência de follow-up), personalização vs template |

Lembrete das premissas do `CLAUDE.md`: campanhas são organizadas por público-alvo, não por canal. Isso não obriga o experimento a ser multicanal — dá pra testar isolado num canal só (ex: só ads, só conteúdo). O que não pode é o aprendizado ficar preso ao canal onde nasceu: um ângulo validado em ads pro público de imobiliárias PT precisa ser transplantado pra conteúdo e outbound do mesmo público, e vice-versa. Teste isolado por canal é válido; aprendizado isolado por canal não é.

## 3. Processo (5 etapas)

1. **Hipótese** — preencher [template-hipotese.md](template-hipotese.md) antes de rodar qualquer coisa. Sem hipótese registrada, não roda.
2. **Priorização** — se há mais de um candidato a testar, usar [framework-priorizacao.md](framework-priorizacao.md) pra decidir a ordem.
3. **Execução** — rodar o teste isolando a variável. Duração/amostra mínima definida na hipótese, não decidida "no olho" no meio do teste.
4. **Análise** — é aqui que o aprendizado é gerado, não no registro. Calcular significância, checar se atingiu o limiar definido na hipótese, interpretar o porquê do resultado (inclusive quando ele não bate com a hipótese).
5. **Registro** — preencher [template-registro-resultados.md](template-registro-resultados.md) com o resultado da análise e a decisão (adotar / descartar / iterar). Registro é documentação da análise já feita, não o lugar de analisar. Todo teste rodado gera um registro, mesmo os que "não deram em nada" — não rodar de novo o que já foi descartado sem saber.

## 4. Regras não-negociáveis

- Uma variável por teste. Se quer testar hook E formato, são dois experimentos.
- Baseline sempre explícita — contra o quê está comparando (o post/ad/sequência anterior com performance conhecida).
- Sample size mínimo definido antes de rodar, não ajustado durante pra "forçar" significância.
- Análise estatística rigorosa — significância calculada de verdade (não "B teve número maior que A"), amostra mínima respeitada, sem parar o teste cedo só porque o resultado parcial agradou.
- Todo experimento tem dono e data de decisão — não fica em limbo.
- Resultado negativo é resultado. Registra do mesmo jeito.

## 5. Nomenclatura da pasta do experimento

Cada experimento vira uma subpasta em `playbook/experimentos/` no formato:

```
YYYY-MM-[CANAL]-[XXX]-[NOME]
```

- **YYYY-MM** — ano-mês de início do experimento.
- **CANAL** — `CNT` (Conteúdo), `ADS`, `OUT` (Outbound) ou `MIX` (multicanal, quando o teste roda em mais de um canal ao mesmo tempo por desenho, não por acaso).
- **XXX** — número sequencial global do experimento, começando em `0001`, sem reiniciar por canal ou por mês.
- **NOME** — nome curto e descritivo do experimento, kebab-case (ex: `criativos-coloridos`, `btn-laranja`).

Exemplo: `2026-07-ADS-0001-btn-laranja`.

Dentro da subpasta, seguir os templates: hipótese preenchida vira `hipotese.md`, resultado da análise vira `resultado.md`.

## 6. Métricas de referência

Usar a [Fórmula de taxa de engajamento](../../02%20Always-On/Docs/) já padronizada pro projeto — (Likes + Comentários×3 + Reposts×5)/(Seguidores×100) — em vez de taxa de engajamento genérica de mercado, pra manter os testes de conteúdo comparáveis entre si.
