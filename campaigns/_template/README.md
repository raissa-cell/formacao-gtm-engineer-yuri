# Campanha: {{PÚBLICO-ALVO}}

> Copie esta pasta: `cp -r campaigns/_template campaigns/<publico>`. Uma campanha é organizada por PÚBLICO, não por canal: conteúdo, ads e outbound para o mesmo público vivem aqui.

## ICP
- Quem é: {{segmento, tamanho, geografia}}
- Cargo decisor: {{...}}
- Sinal técnico/comportamental que indica fit: {{ex: *site multi-idioma, contratando SDR*}}
- Quem fica de fora: {{...}}

## Oferta
{{o que você vende para esse público e o ímã (material rico) que gera o sinal}}

## Estrutura
| Pasta | O que vai aqui |
|---|---|
| `playbook.md` | documento mestre: ICP, estratégia, canais, sequência, leads de exemplo, data de início e resultados |
| `conteudo/` | posts, carrosséis e o material rico, no formato `AAAA-MM/<nome-do-post>/` |
| `ads/creative/` | criativos e copy de anúncios |
| `outbound/` | listas tratadas, sequências de DM/e-mail, mensagens |
| `signals/` | quem comentou, visitou, baixou; ledger de engajamento (contém dados pessoais, ignorado pelo git) |
| `scripts/` | scripts só desta campanha |

## Funil e métricas
- Meta da campanha: {{ex: *30 reuniões em 8 semanas*}}
- Métrica principal: {{...}}
- Experimentos ativos: link para `playbook/experimentos/`
