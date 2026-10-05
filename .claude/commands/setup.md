---
description: Onboarding da sua máquina de GTM. Entrevista você e preenche brand/, .env e a primeira campanha.
---

Conduza o onboarding do aluno. Uma pergunta por vez, em PT-BR, sem despejar o formulário inteiro.

1. **Checagem**: existe `.env`? Se não, rode `cp .env.example .env` e explique onde pegar cada chave (só as que ele já tiver; Nuvia e Apify primeiro).
2. **Entrevista de marca**: pergunte nome, papel, ICP de leitor, arquétipo/tom, 3 pilares, vícios proibidos, trajetória e pontos de contato. Preencha `brand/voice.md`, `brand/voice-outbound.md` e `brand/background.md` substituindo todos os `{{...}}`. Mostre o resultado e espere OK antes de salvar.
3. **Design**: pergunte cores, fontes e ferramenta visual; preencha `brand/design.md`.
4. **Placeholders globais**: troque `{{SEU_NOME}}`, `{{SEU_LINKEDIN_SLUG}}`, `{{LINK_COMUNIDADE}}`, `{{SEU_USUARIO_GITHUB}}` nos arquivos onde aparecem (`grep -rn "{{SEU" .`), só nos que ele já souber.
5. **Primeira campanha**: pergunte o público-alvo e copie `campaigns/_template/` para `campaigns/<publico>/`.
6. **Nuvia**: se o MCP estiver conectado, rode `whoami` e preencha `.claude/skills/nuvia-crm/references/conta-nuvia-template.md`, salvando como `conta-nuvia.md` na mesma pasta (contém IDs da conta dele, já ignorado pelo git). Atualize a linha 13 da `nuvia-crm/SKILL.md` para apontar para esse arquivo.
7. **Fechamento**: liste o que ficou pendente e sugira o próximo passo (`campaign-plan` para planejar a campanha).

Regras: nunca invente dado do aluno; se ele não souber, deixe o `{{...}}` e anote como pendente.
