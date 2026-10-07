# Playbook: concessionárias automotivas

Documento mestre da campanha. Conteúdo, ads e outbound devem seguir as definições abaixo.

## 1. ICP

| Campo | Definição |
|---|---|
| **Empresa** | Grupos ou redes brasileiras com concessionárias autorizadas organizadas por marca/bandeira e quatro ou mais unidades; podem representar várias montadoras |
| **Sinal técnico/comportamental de fit** | Ads ativos, entrada de novos leads pelo WhatsApp, volume comercial relevante e estrutura para assumir oportunidades qualificadas |
| **Pessoa (decisor)** | Diretor comercial, de marketing, de operações ou executivo; gerentes/coordenadores de Comercial, CRM/BDC e Performance como champions |
| **Dor comum** | Organizar o primeiro atendimento, a qualificação, o acompanhamento e o direcionamento do lead ao time correto |
| **Quem fica de fora** | Revendas multimarcas independentes sem bandeira autorizada; redes com menos de quatro unidades; empresas sem Ads ou WhatsApp comercial; contatos sem responsabilidade sobre vendas, demanda, atendimento ou CRM |
| **Lista de negativação** | A definir |

Definição canônica do ICP: [`../../playbook/icp-patagon-ai.md`](../../playbook/icp-patagon-ai.md). Fontes da campanha: `outbound/leads.md` e `fontes.md`.

## 2. Estratégia

- **Oferta:** a Patagon AI atende, qualifica e acompanha leads pelo WhatsApp até o momento de envolver o time comercial.
- **Ímã:** a definir.
- **Ideia da campanha:** abrir a conversa a partir de um fato verificável da empresa e de uma responsabilidade real do cargo, conectando escala de unidades, aquisição paga e fluxo comercial no WhatsApp ao processo de atendimento.
- **Objetivo (60-90 dias):** a definir.
- **Métrica norte:** reuniões qualificadas agendadas.

### Regra de personalização

1. Priorizar fatos da empresa diretamente ligados ao pitch: bandeira atendida, número de unidades, campanhas ativas, expansão, entrada pelo WhatsApp e estrutura comercial.
2. Relacionar o fato à responsabilidade real do cargo.
3. Tratar qualquer dor como hipótese ou pergunta, nunca como problema confirmado.
4. Não usar faculdade, localização ou elogio genérico quando não houver ponte comercial direta.
5. Utilizar um único CTA de baixo atrito.

## 3. Canais

| Canal | Papel | Pasta | Status |
|---|---|---|---|
| Conteúdo (orgânico) | Apoio e construção de contexto | `conteudo/` | A definir |
| Ads | Reforço para o mesmo ICP | `ads/creative/` | A definir |
| Outbound LinkedIn | Pesquisa e possível abertura | `outbound/` | Em preparação |
| Outbound e-mail | Canal do exercício atual | `outbound/` | Três modelos aprovados |
| Comment-gate | Sinal de post vira DM | `signals/` | A definir |

## 4. Sequência (cadência)

Máximo de toques: a definir. O exercício atual cobre somente o primeiro e-mail frio.

| Toque | Canal | Ação / mensagem | Arquivo |
|---|---|---|---|
| D0 | E-mail | E-mail frio personalizado | `outbound/email-sequence.md` |
| D+2 | E-mail / LinkedIn | Follow-up 1 | A definir |
| D+4 | E-mail / LinkedIn | Follow-up 2 | A definir |
| D+7 | E-mail / LinkedIn | Último toque | A definir |
| Ao responder | | Qualificar interesse e definir próximo passo | A definir |
| Sem resposta | | Reforço passivo por conteúdo/ads | A definir |

Voz: `brand/voice-outbound.md`.

## 5. Dados, filtros e enriquecimento

| Passo | O que foi feito | Antes → depois | Arquivo |
|---|---|---|---|
| 1 | Seleção manual de lideranças comerciais automotivas | 3 → 3 | `outbound/leads.md` |
| 2 | Leitura dos perfis no LinkedIn | 3 → 3 | `outbound/leads.md` |
| 3 | Pesquisa de fatos oficiais das empresas | 3 → 3 | `fontes.md` |
| 4 | Loop de redator + revisor, máximo de três rodadas | 3 → 3 aprovados | `outbound/email-sequence.md` |

## 6. Leads de exemplo e mensagens

> **Atenção:** os três contatos abaixo foram usados no exercício da aula antes da definição atual do ICP. Pertencer a um grupo que representa várias montadoras não os elimina: é preciso confirmar que o grupo opera concessionárias autorizadas por bandeira e validar Ads, entrada e volume de novos leads no WhatsApp. Até essa verificação, são exemplos de copy e pesquisa — não uma lista aprovada para disparo.

| Lead | Cargo / empresa | Gancho aprovado | Mensagem |
|---|---|---|---|
| Fabio Calligari | Diretor Executivo, Grupo Líder | Mais de 100 unidades, 11 marcas e quatro estados | `outbound/email-sequence.md` |
| Lindomar Oliveira | Coordenador Comercial, Grupo Saga | Mais de 110 lojas, 19 marcas e jornadas de veículos, consórcio, seguros e serviços | `outbound/email-sequence.md` |
| Sandro Toledo | Diretor Comercial, GAC Navesa | Operação multimarcas e mais de 25 anos com CRM e ciclo completo de vendas | `outbound/email-sequence.md` |

Checar antes do disparo: e-mail válido, consentimentos aplicáveis e variáveis `empresa` e `primeiro nome`. Nenhuma mensagem foi enviada neste exercício.

## 7. Ficha operacional

| Campo | Definição |
|---|---|
| **Data de início** | A definir |
| **Duração do ciclo** | A definir |
| **Data de fim** | A definir |
| **Ferramenta / bot** | A definir |
| **Campaign ID (Nuvia)** | A definir |
| **Responsável** | Raissa |

## 8. Resultados e debriefing

| Métrica | Meta | Resultado |
|---|---|---|
| Leads abordados | A definir | 0 |
| Taxa de resposta | A definir | Não iniciado |
| Reuniões agendadas | A definir | Não iniciado |
| Custo / tempo por reunião | A definir | Não iniciado |

**O que funcionou:** ganchos de empresa + cargo produziram mensagens mais relevantes que formação ou elogios genéricos.

**O que não funcionou:** transformar escala em dor presumida; CTA de sim/não; fatos sem confirmação; frase de proposta truncada.

**Próximo experimento:** validar os modelos com a turma e definir a cadência completa.

## 9. Pendente

- [ ] Validar a oferta e os três modelos com a turma.
- [ ] Requalificar os três leads históricos contra o ICP atual antes de qualquer disparo.
- [ ] Confirmar os endereços de e-mail dos leads.
- [ ] Definir ferramenta, datas, meta e lista de negativação.
- [ ] Escrever follow-ups somente após a validação do primeiro e-mail.
