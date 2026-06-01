{PROJECT_NAME}

# Event Bus — Template

**Status:** Template — no active data. Fill in when building.
**Reference:** framework.md Section V

---

## Drop Path

Events are written as JSON files to:
`<workspace_root>/FRAMEWORK/events/pending/`

A dispatcher reads them and routes to subscribers.

---

## Event Envelope

```json
{
  "event_id": "YYYYMMDD_HHMMSS_<source_service>_<event_type>",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "source_service": "<service_name>",
  "source_machine": "<machine_name>",
  "event_type": "<event_type>",
  "payload": {
    "<key>": "<value>"
  },
  "routing": ["<subscriber_1>", "<subscriber_2>"]
}
```

---

## Event Type Registry

| Event Type | Source Service | Default Routing | Payload Keys |
|---|---|---|---|
| `<event_type>` | `<source_service>` | `<subscriber_1>`, `<subscriber_2>` | `<key1>`, `<key2>` |

---

## Subscriber Registry

| Subscriber | Service | Machine | Delivery Method |
|---|---|---|---|
| `<subscriber_name>` | `<service_name>` | `<machine>` | `file_drop` or `http_webhook` |

---

## Dispatcher Config (Placeholder)

```json
{
  "pending_path": "<workspace_root>/FRAMEWORK/events/pending/",
  "processed_path": "<workspace_root>/FRAMEWORK/events/processed/",
  "poll_interval_seconds": 5,
  "subscribers": {
    "<event_type>": ["<subscriber_1>", "<subscriber_2>"]
  }
}
```

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
