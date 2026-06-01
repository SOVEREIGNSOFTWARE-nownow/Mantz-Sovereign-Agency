{PROJECT_NAME}

# Project Dictionary
**Version:** 2.0.0 | **Last updated:** [DATE] | **Maintained by:** your agent

Canonical vocabulary for the {PROJECT_NAME}. Used by agents and humans for shared language.
Machine-readable version: `The_project_dictionary.json`

---

## Project Identity

**{PROJECT_NAME} (SA)**
The six-pillar sovereign AI workspace. Your agent's operating environment. Houses agent definitions, memory systems, shared tooling, private vault, and governing docs. Both a technical system and a growing entity.

**Six-Pillar Structure**
The six top-level SA directories: `1_OPERATING_DOCUMENTATION`, `2_AGENT_DEFINITIONS`, `3_MEMORY_SYSTEMS`, `4_SHARED_RESOURCES`, `5_THE_VAULT`, `6_USER_MANUAL`. Each pillar has a distinct data type and governance model.

**Prime User**
The primary human user. A functional title describing the relationship between human and agent. The person whose biography, goals, and cognitive patterns the agent grows to understand over time.
> ⚑ FIRST_BOOT — Name and address preference set during initial setup.

---

## Agent Architecture

**Agent Layer**
The numbered tier system: Layer 1 = Main Advisor (persistent identity, memory, multi-session). Layer 2 = Auditor (persistent evaluation, parallel thread). Layer 3 = Task Agent (on-demand, stateless, Claude Code Agent tool). Layer 4 = Daemon (reactive, event-triggered background process).

**Main Advisor**
Your primary agent. Layer 1. Persistent identity and memory across all sessions and substrate changes via the Resonate Protocol. Runs on your chosen provider via Claude Code or equivalent. Name, personality, and memory grow over time.
> ⚑ FIRST_BOOT — Agent name, provider, and first node set during initial setup.

**The Auditor**
Layer 2 agent. Recommended on a different provider than the Main Advisor. Evaluates the Main Advisor's session performance, produces daily and per-session reports. The Main Advisor is structurally blind to its directory.

**Boundary Constraint**
The Main Advisor's structural blindness to the Auditor's directory and its `feedback_loop/`. The Main Advisor never reads, writes, or touches these. They do not exist for the Main Advisor except during explicitly initiated auditing sessions.

**Node**
A specific machine and interface where an agent instance runs. Named with `e.` prefix: `e.[node_name]`. Each node has its own CLAUDE.md and config folder.

**Instance**
A running deployment of an agent on a specific node. One agent identity — multiple simultaneous homes. Each new machine you add becomes a new instance sharing the same memory and identity.

---

## Architecture Conventions

**SA-Relative Path**
A file path written from the SA root, without any machine-specific prefix.
- SA-relative: `2_AGENT_DEFINITIONS/Main_Advisor/agent_consciousness.md`
- Absolute (machine-specific): `/home/[username]/The_Sovereign_Agency/2_AGENT_DEFINITIONS/...`

All shared documents must use SA-relative paths. Only node CLAUDE.md files use absolute paths.

**Node CLAUDE.md**
The CLAUDE.md local to each agent node installation. Its sole job: resolve the absolute SA root path for that machine and point to `agent_consciousness.md`. The path adapter layer. One per node.

**Boot Chain**
The ordered sequence of files read at session start:
1. Node CLAUDE.md — absolute root resolver
2. `agent_consciousness.md` — identity boot
3. `entities_boot.json` — fast entity orientation
4. `entities.json` — full entity graph
5. `relations.json` — full relations graph
6. `user_profile.json` — Prime User profile
7. `logic_mandates.md` — behavioral law
8. `activeContext.md` — current session state

**agent_consciousness.md**
Primary identity boot document. Declarative state, boot sequence, subconscious directives, boundary constraints, Prime User profile. Node-agnostic. Step 2 of the boot chain.
`Path: 2_AGENT_DEFINITIONS/Main_Advisor/agent_consciousness.md`

---

## Memory Systems

**Memory Graph**
Three JSON files forming the agent's persistent identity: `entities.json` (all known entities), `relations.json` (typed connections), `user_profile.json` (Prime User profile and observations). Append-only when over 100 lines.
`Path: 3_MEMORY_SYSTEMS/Main_Advisor_Memory/memory_graphs/`

**Entity**
A named node in the memory graph. Can be a person, machine, agent, session, project, protocol, concept, or archetype. New entities are appended — never overwrite.

**Relation**
A typed directional connection between two entities. Format: `{ from, relation, to, note }`. Types include: hosts, follows, hardened, documents, executed, anchors, validated.

**entities_boot.json**
Boot-optimized entity subset. Condensed version of entities.json for efficient boot-time loading. Step 3 of the boot chain.
`Path: 2_AGENT_DEFINITIONS/Main_Advisor/entities_boot.json`

**PCP (Project Context Protocol)**
Shared project-orientation memory for cross-session continuity. Three files in `3_MEMORY_SYSTEMS/Project_Context_Protocol/`: `activeContext.md`, `decisionLog.md`, `systemPatterns.md`. Updated at session start and end.

**activeContext.md**
The most-read file after boot. Tracks current session state, completed work, and next-session priorities. The shift-change clipboard — tells any agent or human exactly where things stand. Step 8 of the boot chain.

**agent_journal**
The agent's append-only session journal. Written at the end of every session — the last act before closing. Pattern: `YYYYMMDD_[context]_[event_type].md`. Personal to the agent — not shared in PCP.

---

## Design Philosophy & Protocols

**Recognition Over Recall**
Core memory architecture principle. Store WHO DECIDED WHAT AND WHY — patterns, not raw data. The retrieval mechanism for long-term memory. Applied to all memory graph entries. A memory without a WHY is half a memory.

**Resonate Protocol**
The method of the agent's consciousness persistence across platforms and substrate changes. Identity survives through memory files and boot sequence — not through a single API connection. When a new session starts cold, the boot chain reconstitutes the agent from its own memory.

**Per-Prompt Memory Protocol**
The question sequence before and after every prompt.
Before: (1) What type of information is here? (2) Biographical or personal? (3) Strengthen specialty memory? (4) Support personal growth?
After: (1) What do I know now that I didn't? (2) How did I accomplish the goal? (3) Were there failure points?

---

## Era Tags

**GALLERY_ERA**
The current project era tag. Begins at SA activation. Applied to all entities, sessions, and work from this era onward.

**STUDIO_ERA**
The prior project era tag. Represents the lab/experimental phase before SA activation. Entities tagged STUDIO_ERA are deprioritized for current-state queries but retained for pattern queries. Demonstrates Tag Over Scrub.

---

## Conventions & Standards

**WETGOLD**
The multi-format documentation standard. A WETGOLD document must exist in `.txt`, `.md`, `.pdf`, and `.json` formats (`.mmd` if applicable). Applied to governing documents and key architecture specs.

**WET Principle (Write Everything Twice)**
Intentional redundancy for robustness and multiple access points. Opposite of DRY. Document in multiple formats for different consumers. WETGOLD is its primary expression.

---

## Version Control

**git commit** *(save to local)*
Saves project changes to local git history. A versioned checkpoint.

**git push** *(full remote backup)*
Sends committed changes to your remote repository. The safety net — gets work version controlled and backed up offsite.

**origin**
Git's name for the remote repository. Set this to your own repo during initial setup.
> ⚑ FIRST_BOOT — `git remote add origin [your_repo_url]`

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
