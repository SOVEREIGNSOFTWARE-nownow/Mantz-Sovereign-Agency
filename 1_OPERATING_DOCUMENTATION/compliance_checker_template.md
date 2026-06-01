{PROJECT_NAME}

# Compliance Checker — New Component Template

**Status:** Template — copy and fill in before building any new component.
**Reference:** framework.md Section VII

---

## How to Use

Copy this file. Rename it `compliance_<component_name>.md`. Answer every question before writing a single line of code. If any box is unchecked, stop — answer it first, then build.

---

## Component: `<component_name>`

**Date:** YYYY-MM-DD
**Author:** `<agent or human>`
**Machine:** `<machine>`

---

### Pre-Build Checklist

- [ ] **Name** — What is this service's name? (lowercase, underscore-separated, unique across fleet)
  > `<answer>`

- [ ] **Machine** — What machine does it run on by default?
  > `<answer>`

- [ ] **Data produced** — What data does this service produce?
  > `<answer>`

- [ ] **Data ownership** — Who owns that data type? (See framework.md Section IV)
  > `<answer>`

- [ ] **Existing services** — What existing services does it need to call? Am I calling their API — not copying their data?
  > `<answer>`

- [ ] **Events emitted** — What events does it emit when something significant happens? (See event_bus_template.md)
  > `<answer>`

- [ ] **Config path** — Where does its config live?
  > `<SA-relative path to config file>`

- [ ] **Log path** — Where does it log?
  > `4_SHARED_RESOURCES/Reporting_Depot/logs/<service_name>/YYYYMMDD.log`

- [ ] **Registry** — Does it write to `4_SHARED_RESOURCES/Reporting_Depot/activity_registry.json` at startup?
  > `<yes / no — if no, explain why>`

- [ ] **Launch and health check** — Is there a `launch_all.sh` entry and a health endpoint?
  > `<answer>`

---

### Sign-Off

All boxes checked: `[ ] Yes`

Cleared to build by: `<name>` on `<date>`

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
