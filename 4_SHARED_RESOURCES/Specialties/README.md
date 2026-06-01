{PROJECT_NAME}

# README — Specialties

## **`4_SHARED_RESOURCES/Specialties`**

## PURPOSE

Specialties are focused domain knowledge bases that agents load on demand. Think of them as uniforms — when an agent puts one on, they gain access to the accumulated knowledge and session memory of every agent who has operated in that role before them.

This shared memory is meaningful: if one agent has built up two years of AI engineering practice history in the specialty, the next agent who boots into that role reads that practice history. Two agents, one evolving body of professional knowledge.

---

## Active Specialties

| Folder | Domain | Status |
|---|---|---|
| `AI_Engineering/` | AI engineering, model deployment, agent design, RAG, prompt engineering | Active |

---

## How Specialties Work

At session boot, after identity and memory graphs are loaded, the agent loads the relevant Specialty. It injects:

1. Domain knowledge (from the compiled knowledge graph)
2. Specialty session memory (accumulated across all agents who held this role)
3. Role-specific context and constraints

At session close, the specialty memory is updated — the agent's work in that role is recorded for the next session.

---

## Growing This Folder

Every major project domain is a candidate for a Specialty. As projects mature, distill their operational knowledge into a Specialty that any agent can load. Examples: investment strategy, system administration, legal research, health monitoring.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
