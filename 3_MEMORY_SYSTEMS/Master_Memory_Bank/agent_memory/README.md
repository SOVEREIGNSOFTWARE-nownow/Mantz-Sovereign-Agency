{PROJECT_NAME}

# README — Agent Memory

## **`3_MEMORY_SYSTEMS/Master_Memory_Bank/agent_memory`**

## PURPOSE

Backup copies of all agent memory graphs. As agents accumulate sessions and build their memory, these backups stay synchronized with the primary memory graphs in `Main_Agent_Memory/`.

The Main Advisor can read from this location to access other agents' memory when needed. The separation between agents — particularly between the Main Advisor and The Auditor — is maintained deliberately: the Main Advisor does not carry The Auditor's evaluation criteria, and The Auditor does not carry the Main Advisor's full project history.

---

## SUB-FOLDERS

**`main_agent/`**

Backup of the Main Advisor's memory graphs. Mirrors `3_MEMORY_SYSTEMS/Main_Agent_Memory/memory_graphs/`.

**`auditor/`**

Backup of The Auditor's memory graphs. Kept separate from the Main Advisor's memory to prevent cross-contamination of evaluation criteria.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
