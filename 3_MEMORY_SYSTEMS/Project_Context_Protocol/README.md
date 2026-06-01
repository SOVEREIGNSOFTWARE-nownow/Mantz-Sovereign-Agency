{PROJECT_NAME}

# README — Project Context Protocol

## **`3_MEMORY_SYSTEMS/Project_Context_Protocol`**

## PURPOSE

Shared project orientation memory for human/agent working sessions. This is not personal agent memory — it is the layer that keeps all working agents and the Prime User oriented to the same current state of the project.

When the Main Advisor boots for a new session, this is the last thing it reads before responding — a snapshot of where things were left, what decisions have been made, and what patterns govern the work.

---

## FILES

**`activeContext.md`**

The current session state. Updated at the start and end of every meaningful session. Contains: what was worked on last, what is in progress, what comes next.

**`decisionLog.md`**

Append-only log of architectural and design decisions — what was decided, why, and when. The institutional memory of *how* this project makes choices.

**`systemPatterns.md`**

Established conventions and patterns. Not personal to any agent. Not project state. The behavioral layer — how this project operates.

---

## WRITE RULE

Always update `activeContext.md` at the start and end of meaningful sessions. `decisionLog.md` and `systemPatterns.md` are append-only.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
