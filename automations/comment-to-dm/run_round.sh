#!/bin/bash
# Tudo em UTC: timestamps de log e comparação de prazo não dependem do fuso da máquina.
export TZ=UTC
# Runtime da automação comment-to-dm, FORA do Desktop.
# O macOS (TCC) bloqueia qualquer acesso do launchd a ~/Desktop, então scripts,
# ledger, .env e logs vivem aqui. O espelho pra pasta do projeto é feito pelo
# resumo horário do Claude Code, que tem a permissão que o launchd não tem.
set -u
CONFIG="$1"; DEADLINE="${2:-}"   # sem prazo = roda sempre (modo sob demanda)
HERE="$(cd "$(dirname "$0")" && pwd)"
LOG="$HERE/rounds.log"
now=$(date +%s)
if [ -n "$DEADLINE" ]; then
  deadline=$(/usr/bin/env python3 -c "import sys,datetime;print(int(datetime.datetime.fromisoformat(sys.argv[1]).timestamp()))" "$DEADLINE" 2>/dev/null || echo 0)
else
  deadline=0
fi
if [ "$deadline" -gt 0 ] && [ "$now" -gt "$deadline" ]; then
  echo "[$(date -Iseconds)] prazo vencido ($DEADLINE), nada a fazer" >> "$LOG"; exit 0
fi
echo "[$(date -Iseconds)] === rodada ===" >> "$LOG"
cd "$HERE" || exit 1
/usr/bin/env python3 collect_to_nuvia.py --config "$CONFIG" >> "$LOG" 2>&1
rc=$?; echo "[$(date -Iseconds)] collect exit=$rc" >> "$LOG"
if [ "${SKIP_SCORE:-0}" = "1" ]; then
  echo "[$(date -Iseconds)] score pulado (SKIP_SCORE=1)" >> "$LOG"
else
  /usr/bin/env python3 score_engagement.py --config "$CONFIG" >> "$LOG" 2>&1
  rc=$?; echo "[$(date -Iseconds)] score exit=$rc" >> "$LOG"
fi
