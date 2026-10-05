# Framework de Priorização de Experimentos

Quando há mais de um experimento candidato e só dá pra rodar um por vez (mesmo público, mesmo canal, sem contaminar resultado), usar o score ICE pra decidir a ordem. Ver processo completo em [guia-de-experimentacao-marketing.md](guia-de-experimentacao-marketing.md).

## Score ICE

Cada candidato recebe nota de 1 a 5 em três dimensões. Score final = média das três.

| Dimensão | Pergunta | 1 (baixo) | 5 (alto) |
|---|---|---|---|
| **Impact** | Se a hipótese se confirmar, quanto isso move a métrica-alvo do público/campanha? | Ganho marginal, cosmético | Muda diretamente CAC, conversão ou volume de leads qualificados |
| **Confidence** | Quão embasada é a hipótese — tem sinal prévio (dado próprio, benchmark do nicho, resultado de teste parecido)? | Achismo, sem sinal prévio | Já há sinal direto (dado do usuário ou do público) apontando nessa direção |
| **Ease** | Quão barato/rápido é rodar o teste (tempo de setup, criativo, dependência de terceiros)? | Precisa de asset novo complexo, semanas de setup | Só trocar copy/hook, roda hoje |

## Tabela de priorização

| Experimento | Pilar | Impact (1-5) | Confidence (1-5) | Ease (1-5) | Score ICE (média) |
|---|---|---|---|---|---|
| |  |  |  |  |  |
| |  |  |  |  |  |

Ordenar por score ICE decrescente. Rodar o de maior score primeiro — mas nunca dois testes que competem pelo mesmo público/canal ao mesmo tempo (contamina a leitura do resultado).

## Critério de desempate

Se dois experimentos empatarem no score: priorizar o de maior **Confidence** (menos risco de gastar ciclo de teste em hipótese fraca) sobre o de maior Impact teórico sem sinal prévio.
