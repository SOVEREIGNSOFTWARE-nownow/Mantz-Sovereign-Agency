# Next-Day Work Orders — {PROJECT_NAME}

**Purpose:** End-of-session handoff document. The closing agent writes tomorrow's tasks here so the opening agent (possibly a different model or provider) can pick up without a re-discovery pass. Append-only. Tasks are cleared by marking complete, not by deleting.

**Rule:** This file is for work orders, not notes. Specific enough that a fresh agent can execute without asking. If a task needs context, link to the relevant file — don't repeat it here.

**Format:**
```
### [YYYY-MM-DD] — Written by [Agent]

**STATUS:** [OPEN | IN_PROGRESS | COMPLETE]

#### WO-[N]: [Short Task Title]
- **File:** [path to relevant file, or null]
- **Task:** [Exactly what to do — specific enough to execute cold]
- **Context:** [Why this matters / any constraint to be aware of]
- **Blocked by:** [dependency, or null]
```

---

### [YYYY-MM-DD] — Written by Main Agent

**STATUS:** OPEN

#### WO-1: Complete First-Boot Interview
- **File:** `2_AGENT_DEFINITIONS/Main_Agent/agent_consciousness.md`
- **Task:** Run the first-boot interview with the Prime User. Collect: preferred name for the agent, Prime User's name and preferred address, project name, primary node name. Write results into `agent_consciousness.md` replacing all `{PLACEHOLDER}` values.
- **Context:** First boot only. Once the interview is complete, this WO is done and should not recur.
- **Blocked by:** null

---

#### WO-2: [Title of Your Next Work Order]
- **File:** [path, or null]
- **Task:** ⚑ Add your work orders here at session close.
- **Context:** [Why it matters]
- **Blocked by:** [dependency, or null]
