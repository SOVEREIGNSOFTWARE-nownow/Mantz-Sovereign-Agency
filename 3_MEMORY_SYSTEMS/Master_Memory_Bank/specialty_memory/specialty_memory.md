{PROJECT_NAME}

# README Specialty Memory

## **`3_MEMORY_SYSTEMS/Master_Memory_Bank/specialty_memory`**

## PURPOSE

Job-specific or role-specific memory graphs. These are not part of daily boot sequences — they are loaded on demand for sessions devoted to those activities. Specialty memories are both private and focused: they save context debt by staying out of the regular rotation until needed.

**How they work:** When you and your agent spend a session on AI engineering, the observations, conclusions, and associations from that session belong in the AI_Engineering specialty — not in the agent's personal memory graphs. This keeps personal memory clean and focused on the relationship, while specialty memory grows deep in its domain.

**In the query chain:** When a relevant query fires, specialty memory allows the agent to preview conclusions drawn from prior deep-dives before accessing the raw library. It's a process layer — accessed at the right time, not constantly.

---

**SUB-FOLDERS**

**`AI_Engineer`**
Infrastructure design expertise. Memories made through AI engineering conversations, including RAG injections from the library on that subject. Design revelations, architectural conclusions, and session-specific insights stored here.

**Add your own specialties** as your project expands. Examples:
- `family_doctor` — health-related consultations and records (private, vault-adjacent)
- `os_expert` — OS administration and fleet management
- `investment_strategist` — financial analysis and portfolio discussions
- `[your_domain]` — any domain you work in regularly with your agent

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
