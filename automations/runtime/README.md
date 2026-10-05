# Runtime (launchd)

Automações agendadas rodam de `~/gtm-automation`, **nunca** de `~/Desktop` ou `~/Documents` (o macOS bloqueia o launchd nessas pastas; sintoma: `exit 126`).

```bash
mkdir -p ~/gtm-automation
cp automations/comment-to-dm/{collect_to_nuvia.py,score_engagement.py,run_round.sh,weights.json} ~/gtm-automation/
cp .env ~/gtm-automation/.env
chmod +x ~/gtm-automation/run_round.sh
```

Plist de exemplo: `automations/autodm-keepalive/com.exemplo.autodm-keepalive.plist`. Regras:
- Troque `/Users/SEU_USUARIO` pelo seu usuário (launchd não expande `~`).
- Troque o prefixo `com.exemplo` por algo seu.
- Instale: `cp arquivo.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/arquivo.plist`
- Logs em `~/gtm-automation/*.log`.
- Em Linux, use cron/systemd com o mesmo princípio: runtime fora de pastas protegidas.
