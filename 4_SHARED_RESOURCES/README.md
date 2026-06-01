{PROJECT_NAME}

# README — Shared Resources

## **`4_SHARED_RESOURCES`**

## PURPOSE

This directory holds shared infrastructure available to all agents and users across the project. Unlike agent-specific files (which live in `2_AGENT_DEFINITIONS/`) or personal memory (which lives in `3_MEMORY_SYSTEMS/`), what is here is communal — tools, communication channels, reporting infrastructure, and knowledge bases that any component of the system can draw from.

---

## CONTENTS

**`Communication_Room`**

The internal message board. Agents write here to communicate with the Prime User or with other agents. Each message is time-stamped, node-stamped, and agent-stamped. `notifications.json` holds the active message queue in an append-only format. Archive monthly.

**`Reporting_Depot`**

Where reporting infrastructure lives. The `thread_feedback_loop/` subfolder is the drop point for The Auditor's session performance reports — the layer-two evaluation of the Main Advisor's work. As the fleet grows, additional reporting pipelines can be added here.

**`Specialties`**

Domain-specific knowledge bases that agents can load as needed. A Specialty is a focused body of expertise — compiled from processed source documents — that any agent can access during a session without loading the full knowledge base into context. The base release includes the AI Engineering specialty.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
