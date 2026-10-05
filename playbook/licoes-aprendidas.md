# Lições aprendidas (leia antes de automatizar)

- **launchd não lê `~/Desktop`** (macOS TCC): o job falha calado com `exit 126`. O runtime vive em `~/gtm-automation`; o repo guarda a fonte.
- **Script é infraestrutura, conteúdo é dado.** Legenda, mídia, thread e data entram por argumento ou arquivo na pasta do post, nunca hardcoded em `.py`.
- **Um CTA por post.** Nunca empilhar comment-gate com comunidade ou follow.
- **Dedup antes de criar contato na Nuvia**: por `linkedin_identifier` (LinkedIn) ou `phone_number` (WhatsApp), nunca por nome (a busca é sensível a acento).
- **Carregar a skill `nuvia-crm` antes de QUALQUER escrita** na Nuvia. Telefone-sentinela sem checar duplicidade corrompe contato real.
- **Limite de raspagem = o que foi pedido.** "Últimos 20 comentários" = `maxItems: 20`. O ator cobra por item.
- **Agendar no cron usa o fuso da máquina**, não o do destinatário. Converta o horário-alvo (`date`) antes de escrever o cron.
- **Validar antes de gravar prompt de agente**: mostre o texto no chat, espere OK, depois grave e registre.
- **Enrollment é snapshot**: leads acrescentados à lista depois do enroll ficam invisíveis até um bulk enroll.
- **Triagem de ICP por script**, não de cabeça.
- **Taxa de engajamento**: (Likes + Comentários×3 + Reposts×5) / (Seguidores×100). Use sempre a mesma para comparar posts.
