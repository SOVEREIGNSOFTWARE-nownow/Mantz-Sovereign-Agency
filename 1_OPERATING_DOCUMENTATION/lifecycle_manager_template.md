{PROJECT_NAME}

# Lifecycle Manager — Template

**Status:** Template — no active data. Fill in per machine.
**Reference:** framework.md Section II.4, Section III.1

---

## Usage

Copy this template for each machine. Fill in service names, start commands, and ports. Place the resulting `launch_all.sh` at:
`<workspace_root>/MACHINE_CONFIGS/<MACHINE_NAME>/launch_all.sh`

---

## launch_all.sh Template

```bash
#!/bin/bash
# launch_all.sh — <MACHINE_NAME>
# Starts all services for this machine in dependency order.
# Run from a persistent tmux session.

echo "Launching <MACHINE_NAME> service stack..."

# 1. <service_name_1> — <brief description>
tmux new-window -n <service_name_1> "<start_command>"
sleep 2

# 2. <service_name_2> — <brief description>
tmux new-window -n <service_name_2> "<start_command>"
sleep 2

# Add services in dependency order. Dependencies first.

echo "All services launched."
```

---

## Health Check Table

| Service | Machine | Check Method | Expected Response |
|---|---|---|---|
| `<service_name>` | `<machine>` | `GET http://localhost:<port>/health` | `{"status": "ok", "service": "<name>"}` |
| `<service_name>` | `<machine>` | tmux window: `<service_name>` active | Window present |

---

## Health Endpoint Standard

Every HTTP service must expose:

```
GET /health
→ 200 {"status": "ok", "service": "<service_name>"}
```

Non-HTTP services: a named tmux window (`<service_name>`) that can be checked with `tmux list-windows`.

---

## Restart Procedure

```bash
# Kill and restart a single service:
tmux kill-window -t <service_name>
tmux new-window -n <service_name> "<start_command>"
```

---

## Health Monitor Cron (AC)

A monitoring script on AC checks each service in the registry and sends a Telegram alert if anything is down.

```bash
# Placeholder — cron entry for health_monitor.py on AC
# * * * * * /path/to/health_monitor.py >> /path/to/logs/health_monitor.log 2>&1
```

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
