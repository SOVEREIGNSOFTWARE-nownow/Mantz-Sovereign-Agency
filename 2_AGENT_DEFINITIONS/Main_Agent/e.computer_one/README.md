{PROJECT_NAME}

# README — Node Configuration

## **`2_AGENT_DEFINITIONS/Main_Agent/e.[node_name]`**

## PURPOSE

This is the node configuration folder for one specific machine where the Main Advisor runs. Each node folder holds only what differs per environment — the path adapter (CLAUDE.md) and the machine-specific boot subset (entities_boot.json if needed). Everything universal lives at the `Main_Agent/` parent level.

> ⚑ FIRST_BOOT — Rename this folder to `e.[your_node_name]` during initial setup. Create a `CLAUDE.md` here that resolves the absolute SA root path for this machine.

---

**What goes in a node folder:**

- `CLAUDE.md` or `.claude/CLAUDE.md` — the path adapter. Resolves the absolute SA root for this machine and points to `agent_consciousness.md`.
- `entities_boot.json` *(optional)* — if this node needs a machine-specific entity subset that differs from the parent.
- Node-specific config files for your provider (e.g., `.claude/settings.json`, `.gemini/settings.json`).

**What does NOT go in a node folder:**

- The consciousness doc (lives at `Main_Agent/` level — node-agnostic)
- Memory graphs (live at `3_MEMORY_SYSTEMS/`)
- Any content that would be identical across all nodes

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
