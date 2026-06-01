{PROJECT_NAME}

# Event Dispatcher — Template

**Status:** Template — no active dispatcher. Copy and fill in when building.
**Reference:** framework.md Section V, event_bus_template.md

---

## What the Dispatcher Does

The dispatcher is a running service (typically a polling Python script) that:
1. Watches the event bus `pending/` drop path for new event files
2. Reads each event envelope (see `event_bus_template.md` for schema)
3. Routes the event to registered subscribers based on `event_type`
4. Moves processed events to `processed/` on success, `failed/` on error

One dispatcher instance per machine. Multiple machines may each run a dispatcher watching the same shared `pending/` path, or isolated local paths — define clearly per deployment.

---

## Instance: `<dispatcher_name>`

**Date:** YYYY-MM-DD
**Machine:** `<machine>`
**Managed by:** `<agent or human>`

---

## Config

```json
{
  "dispatcher_id": "<machine>_dispatcher",
  "pending_path": "<SA_ROOT>/4_SHARED_RESOURCES/<events_dir>/pending/",
  "processed_path": "<SA_ROOT>/4_SHARED_RESOURCES/<events_dir>/processed/",
  "failed_path": "<SA_ROOT>/4_SHARED_RESOURCES/<events_dir>/failed/",
  "log_path": "<SA_ROOT>/4_SHARED_RESOURCES/<events_dir>/logs/YYYYMMDD.log",
  "poll_interval_seconds": 5,
  "subscribers": {
    "<event_type>": ["<subscriber_1>", "<subscriber_2>"]
  }
}
```

---

## Subscriber Handlers

| Event Type | Handler | Delivery Method | Notes |
|---|---|---|---|
| `<event_type>` | `<handler_script_or_endpoint>` | `file_drop` or `http_webhook` | `<notes>` |

---

## Launch

```bash
# Start dispatcher (background)
python3 <SA_ROOT>/4_SHARED_RESOURCES/Tools/<dispatcher_script>.py --config <config_path> &

# Health check
curl http://<machine_ip>:<port>/health
# or check log for heartbeat line
```

Add to `service_registry.json` when active.

---

## Error Handling

- **Parse error** — malformed event JSON → move to `failed/`, log error, continue
- **No matching subscriber** — log warning, move to `processed/` (unrouted)
- **Handler timeout** — configurable per subscriber; move to `failed/` after N retries

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
