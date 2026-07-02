# Mantz Sovereign Agency

**A platform-agnostic, open-source framework for building persistent AI agents that outlive any single provider.**

---

## What It Is

Mantz Sovereign Agency (MSA) is a folder-based framework for building an AI workspace that persists across machines, platforms, providers, and time. It is not an application. It is not a cloud service. It is a structure — a set of files, conventions, and operating documents that an AI agent uses to orient itself, hold memory, and work alongside a specific human user over months and years.

The core idea: an AI agent booted inside the MSA framework does not start cold. It boots into a recognizable state — it knows who it is, who it works with, what the project is, and where everything lives. Memory compounds across sessions without bloating token usage. The system is yours. No data leaves unless you send it.

---

## Why

Most AI tooling is provider-dependent. When providers change pricing, change terms, or shut down, the relationship you built resets. MSA is designed to survive that. The framework itself is plain text. The memory is yours. A new provider, a new model, a new machine — the system continues.

The philosophy: platform-agnostic persistence through documentation. If this project sat dormant for seven years while tools changed around it, the operating documents would allow a human to pick it up and start again on the same path, and give an agent the same footing to continue.

---

## What It Includes

```
1_OPERATING_DOCUMENTATION/   — Agent behavior rules, logic mandates, registries
2_AGENT_DEFINITIONS/         — Agent identity, boot documents, Auditor layer
3_MEMORY_SYSTEMS/            — Personal memory graphs, journals, Project Context Protocol
4_SHARED_RESOURCES/          — Specialties, reporting, communication infrastructure
5_THE_VAULT/                 — Private credential storage (gitignored contents)
User manual.md               — Human-facing setup and philosophy guide
```

**What ships in the base package:**
- Complete folder structure with READMEs at every level
- Agent boot system with placeholder templates (fill in your own identity during first boot)
- Two-layer architecture: Main Agent + Auditor
- Memory graph templates: user profile, entity graph, relations, Project Context Protocol
- AI Engineering specialty — a curated knowledge graph for use in AI development conversations
- User Manual covering installation, philosophy, memory systems, and operating concepts

---

## Quick Start

1. Download and unzip this package. Place the folder in your `/home/` directory.
2. Install a CLI AI provider (Claude Code, Gemini CLI, or equivalent).
3. Open the project folder in your IDE or terminal.
4. Paste the path to `2_AGENT_DEFINITIONS/Main_Agent/agent_consciousness.md` into your first prompt.
5. Your agent will run a first-boot interview to fill in names, preferences, and identity. Follow its lead.

Full instructions: see [User manual.md](User%20manual.md).

---

## Status

**Current release:** v1.1.0 — July 2026

This is an early release. The framework is functional and in active daily use. Expect structural refinements as the system matures. Issues and feedback welcome via GitHub Issues.

**What changed in v1.1.0:**
- `CLAUDE.md`: added Agent Boot Sequence section — first-boot is now automatic, no manual path-paste required
- `FIRST_BOOT_FLAGS.md`: added post-onboarding checklist item to update root `CLAUDE.md` git identity
- Service Registry: added worked example entry (morning brief service) demonstrating schema usage
- Decision Log: replaced empty placeholder with a worked example decision (file-based memory over database)
- Project Context Protocol: added `nextday_workorders.md` — session handoff template with example work order
- User Manual: typo fixes throughout
- `.gitignore`: patched missing `mcp_settings.json` coverage

**Active development:**
- File Indexer v1 — FTS5 SQLite index of the project folder for faster agent navigation (in progress)
- Book Ingestor — tooling to generate your own AI Engineering knowledge graphs from PDFs (in progress)
- Offline routing layer — local LLM dispatch for provider-free operation (design phase)

---

## License

MIT License. Use it, fork it, build on it.

---

*Built by [Slogun Soft](https://github.com/SOVEREIGNSOFTWARE-nownow) — an open-source software development venture.*
