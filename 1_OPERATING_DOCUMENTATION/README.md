{PROJECT_NAME}

# README — Operating Documentation

## **`1_OPERATING_DOCUMENTATION`**

## PURPOSE

This directory contains all governing documentation for how agents operate within this environment — combined with how the environment receives new additions and expands appropriately without fragmenting as those expansions happen.

## CONTENTS

| File | What it is |
|---|---|
| `framework.md` | The architectural constitution — service contracts, communication standards, naming conventions, data ownership map, event routing, compliance checklist |
| `logic_mandates.md` | Operational protocols — Query System, Thread Management, Memory Protocols; governs per-prompt agent behavior |
| `machines_registry.json` | Authoritative machine registry — hardware specs, network info, SSH config, role, and status for every node in the fleet |
| `agent_registry.json` | Canonical agent catalog — machine assignment, autonomy level, version, status, launch command, memory graph paths |
| `service_registry.json` | Service registry — what is running where, ports, health endpoints, process type, and status |
| `{PROJECT_NAME}_project_dictionary.json` | Project glossary — shared vocabulary for terms, conventions, and concepts used across the system |
| `{PROJECT_NAME}_project_dictionary.md` | Human-readable project dictionary — canonical vocabulary for agents and humans |
| `compliance_checker_template.md` | Pre-build checklist template — answer every question before writing any new component |
| `event_bus_template.md` | Event bus scaffold — event envelope format, type registry, subscriber registry, dispatcher config |
| `lifecycle_manager_template.md` | Lifecycle manager scaffold — launch_all.sh template, health check table, restart procedure |
| `event_dispatcher.md` | Event dispatcher template — dispatcher config, subscriber handlers, error handling |
| `network_manifesto.md` | Network governing document — topology template, connectivity rules, expansion protocol |
| `FIRST_BOOT_FLAGS.md` | First boot interview guide — all placeholders requiring personalization, with interview questions |

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
