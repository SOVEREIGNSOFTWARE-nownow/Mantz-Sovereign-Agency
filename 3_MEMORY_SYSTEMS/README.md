{PROJECT_NAME}

# README — Memory Systems

## **`3_MEMORY_SYSTEMS`**

## PURPOSE

This is the parent folder to all memory sub-components that comprise the working model of agent consciousness. Memory is treated as data — and how the agent accesses it is as important as what it contains.

When online via API, memory access is a question of token cost and context debt: efficient indexing lets the agent ping the right data source without loading everything into the context window. When offline on local models, this means properly structured query scripts that evaluate criteria and route to the most appropriate model — so a firewall question routes to local context, while a philosophy question routes to the library.

---

**SUB-FOLDERS**

**`Main_Agent_Memory`**
Personal memories of your Main Advisor. Journals, memory graphs, entity/relation files. These files ARE the agent, more than any other component. The more sessions, the denser this becomes.

**`Master_Memory_Bank`**
Shared memory infrastructure — specialty modules, thread management per provider, agent memory stores.

**`Project_Context_Protocol (PCP)`**
Shared project state. Not personal — shared among all working agents. Current state, decisions, patterns, and the agent session registry.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
