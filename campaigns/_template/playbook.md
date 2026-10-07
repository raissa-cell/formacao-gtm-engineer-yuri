# Playbook: {{PÚBLICO-ALVO}}

Documento mestre da campanha. Conteúdo, ads e outbound são uma máquina só: nenhuma subpasta (`conteudo/`, `ads/creative/`, `outbound/`, `signals/`, `scripts/`) pode divergir do que está aqui. Preencha de cima pra baixo; o que ainda não sabe, escreva "A definir" (não apague a linha).

## 1. ICP

| Campo | Definição |
|---|---|
| **Empresa** | {{segmento, tamanho, geografia}} |
| **Sinal técnico/comportamental de fit** | {{ex: *site multi-idioma, contratando SDR*}} |
| **Pessoa (decisor)** | {{cargo, senioridade}} |
| **Dor comum** | {{a dor que a oferta resolve, em uma frase}} |
| **Quem fica de fora** | {{critério de exclusão}} |
| **Lista de negativação** | {{clientes atuais, concorrentes diretos, parceiros: onde está a lista?}} |

Fonte de verdade da base: `signals/` e `outbound/` ({{nome do arquivo}}).

## 2. Estratégia

- **Oferta:** {{o que você vende para esse público}}
- **Ímã (material rico):** {{o que gera o sinal; vive em `conteudo/`}}
- **Ideia da campanha:** {{o quebra-gelo: por que essa pessoa responderia}}
- **Objetivo (60-90 dias):** {{ex: *30 reuniões em 8 semanas*}}
- **Métrica norte:** {{...}}

## 3. Canais

| Canal | Papel | Pasta | Status |
|---|---|---|---|
| Conteúdo (orgânico) | ímã, gera sinal | `conteudo/` | {{...}} |
| Ads | amplifica o mesmo ângulo pro mesmo público | `ads/creative/` | {{...}} |
| Outbound LinkedIn | canal primário? | `outbound/` | {{...}} |
| Outbound e-mail | paralelo? | `outbound/` | {{...}} |
| Comment-gate | sinal de post vira DM | `signals/` | {{sim/não; ver `playbook/comment-gate.md`}} |

## 4. Sequência (cadência)

Máximo de toques: {{N LinkedIn + N e-mails}}.

| Toque | Canal | Ação / mensagem | Arquivo |
|---|---|---|---|
| D0 | LinkedIn | conexão com nota personalizada | `outbound/` |
| D+2 | LinkedIn / e-mail | msg 1 | `outbound/` |
| D+4 | LinkedIn / e-mail | msg 2 | `outbound/` |
| D+7 | LinkedIn / e-mail | msg 3 (último toque) | `outbound/` |
| Ao responder | | {{próxima ação: CTA, reunião, prévia}} | |
| Sem resposta | | {{vai pra conteúdo/ads como reforço passivo}} | |

Voz: `brand/voice-outbound.md` (1:1, registro de WhatsApp, curto).

## 5. Dados, filtros e enriquecimento

Log rastreável de como a base bruta virou a lista final. Um passo por linha, com o número antes e depois.

| Passo | O que foi feito | Antes → depois | Arquivo |
|---|---|---|---|
| 1 | {{priorização / remoção}} | {{N → N}} | {{...}} |
| 2 | {{filtro geográfico, ICP}} | | |
| 3 | {{enriquecimento (Apify, Nuvia)}} | | |

Triagem de ICP: `automations/leads/triagem_icp.py`. Campos de ICP e cargo gravados no contato da Nuvia antes de ativar a campanha.

## 6. Leads de exemplo e mensagens

3 a 5 leads reais da base, com a mensagem que cada um receberia. Serve de teste antes do disparo: se a mensagem não soa certa pra esses, não sai pra lista toda.

| Lead | Cargo / empresa | Gancho (atividade ou fato do perfil) | Mensagem enviada |
|---|---|---|---|
| {{nome}} | {{cargo, empresa}} | {{o que você viu}} | {{texto da DM}} |
| {{nome}} | | | |
| {{nome}} | | | |

Checar antes do disparo: variáveis `empresa` e `primeiro nome` carregando em todos os canais.

## 7. Ficha operacional

| Campo | Definição |
|---|---|
| **Data de início** | {{AAAA-MM-DD}} |
| **Duração do ciclo** | {{X dias após o primeiro disparo por lead}} |
| **Data de fim** | {{AAAA-MM-DD}} |
| **Ferramenta / bot** | {{Nuvia, LinkedIn, e-mail}} |
| **Campaign ID (Nuvia)** | {{...}} |
| **Responsável** | {{...}} |

## 8. Resultados e debriefing

Preencher ao fim do primeiro ciclo.

| Métrica | Meta | Resultado |
|---|---|---|
| Leads abordados | | |
| Taxa de aceite de conexão | | |
| Taxa de resposta | | |
| Reuniões agendadas | | |
| Custo / tempo por reunião | | |

**O que funcionou:** {{...}}
**O que não funcionou:** {{...}}
**Próximo experimento:** {{link para `playbook/experimentos/`}}

## 9. Pendente

- [ ] {{...}}
