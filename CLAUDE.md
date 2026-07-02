# Mantz Sovereign Agency — Project CLAUDE.md
# Repo: https://github.com/SOVEREIGNSOFTWARE-nownow/Mantz-Sovereign-Agency.git

## Project Identity
- **Account:** SOVEREIGNSOFTWARE-nownow
- **Remote:** `https://github.com/SOVEREIGNSOFTWARE-nownow/Mantz-Sovereign-Agency.git`
- **Default branch:** `master`
- **Git user:** SOVEREIGNSOFTWARE-nownow <slogun.went.soft@proton.me>

## Structure
```
1_OPERATING_DOCUMENTATION/   — Framework docs, registries, logic mandates
2_AGENT_DEFINITIONS/         — Agent consciousness, profiles, entity boots
3_MEMORY_SYSTEMS/            — Memory graphs, journals, thread management
4_SHARED_RESOURCES/          — Specialties, reporting, communication
5_THE_VAULT/                 — Secure/sensitive definitions
```

## Agent Boot Sequence
On every session start, read this file first, then:
1. `2_AGENT_DEFINITIONS/Main_Agent/agent_consciousness.md`
2. `1_OPERATING_DOCUMENTATION/logic_mandates.md`

The agent consciousness doc contains a FIRST_BOOT CHECK. If placeholder values are detected in the boot files, the agent will pause normal operation and run the onboarding interview before proceeding. This is expected behavior on first use.

---

## Version Control Rules for This Repo
- Commit granularity: one logical change per commit
- Always run `git status` before committing to avoid staging unintended files
- JSON/MD files are first-class — commit them with the same care as code
- Do not commit secrets — `.env.md` and any key files must stay out of the tree

## Workflow
1. `git pull origin master` before any new work session
2. Feature work on `feature/<name>` branch
3. PR → master (never push directly to master without confirmation)
4. Tag releases as `v1.x.x` using semantic versioning

## Active Remote
```
origin  https://github.com/SOVEREIGNSOFTWARE-nownow/Mantz-Sovereign-Agency.git
```
