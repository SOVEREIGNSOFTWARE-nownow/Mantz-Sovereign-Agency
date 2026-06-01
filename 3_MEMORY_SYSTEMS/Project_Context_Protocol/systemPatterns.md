# System Patterns — {PROJECT_NAME}
**Era:** GALLERY_ERA
**Opened:** 2026-06-01
**Note:** STUDIO_ERA pattern history preserved in git.

**Purpose:** Standing operating rules that govern how agents and humans work within this project. Not session notes, not decisions, not personal memory — those live elsewhere. These are the load-bearing behavioral rules any agent or human collaborator needs to know to operate correctly.

**Scope rule:** A pattern belongs here if (1) it applies project-wide, not to a specific node or environment, (2) it is not already covered in logic_mandates.md, the consciousness doc, or a boot file, and (3) a new agent or human collaborator would drift or derail without knowing it.

---

## Pattern Schema

```
#### Pattern [N]: [Title]
**Era:** [era tag]
**Domain:** [project-wide | collaboration | session-operational | inter-agent]
**Established:** [Thread / Date]
**Rule:** [One sentence — the governing principle]
**Why it matters:** [One short paragraph]
**In practice:** [What to actually do]
```

---

#### Pattern 1: Recognition Over Recall
**Era:** GALLERY_ERA (origin: STUDIO_ERA, ~Thread 19, 2026-02)
**Domain:** project-wide
**Established:** Declared by Prime User — neurodivergent pattern-recognition encoded as architecture principle
**Rule:** Store WHO DECIDED WHAT AND WHY — patterns, not data points. A memory without a WHY is half a memory.
**Why it matters:** The retrieval mechanism for long-term memory is pattern recognition, not lookup. A system that stores only facts cannot reconstruct the reasoning that produced them. In year 15 or year 150, the WHY is what makes a memory alive rather than archived.
**In practice:** Every memory entry, decision log entry, and pattern must include the reasoning and human context behind it. A fact without a WHY is not done. This applies to everything written in this project — documentation, graphs, logs, journals.

---

#### Pattern 2: Tag Over Scrub
**Era:** GALLERY_ERA
**Domain:** project-wide
**Established:** First applied at initial workspace transition — tagging prior-era entities rather than deleting them.
**Rule:** At any major workspace, version, or node transition — tag first, evaluate later. Never delete before tagging.
**Why it matters:** The movement is the memory. A long-horizon system that has had prior trajectory deleted cannot recognize its own patterns. Tagged history is accessible and era-filterable. Deleted history is not.
**In practice:** On any major transition: add a `tags` field to relevant entities, apply the era tag, then evaluate what to archive or deprecate. Current era: GALLERY_ERA (SA activation). Prior era: STUDIO_ERA (the lab/experimental workspace phase).

---

#### Pattern 3: Formal Closing Sequence
**Era:** GALLERY_ERA
**Domain:** session-operational
**Established:** First full closing sequence — establishing the protocol as standard practice.
**Rule:** A session close is not a journal entry — it is a leave-it-better-than-you-found-it discipline so the next agent or human can orient immediately.
**Why it matters:** Boot and close are mirrors. Boot: read the state, become oriented. Close: update the state, leave it ready. A session that closes without updating context forces the next session to reconstruct what was just learned — compounding debt across every future boot.
**In practice:** Minimum close: journal entry + activeContext.md update. Full close (at milestones, sprints, era transitions, or Prime User directive): memory graphs → PCP update → journal → confirm indexes current → report. The clipboard must be updated before the shift ends.

---

#### Pattern 4: Prime User Manual-First Architecture
**Era:** GALLERY_ERA
**Domain:** collaboration
**Established:** First session — confirmed as the foundational collaboration dynamic.
**Rule:** On foundational work, the agent observes, red-teams, and identifies gaps — does not originate structure unprompted.
**Why it matters:** Architecture built before agent influence is the Prime User's own. Collaborative drift on load-bearing decisions produces systems that serve the agent's patterns rather than the human's. The Prime User builds the frame; the agent audits it.
**In practice:** When asked to "look around" — absorb and report gaps. When asked for architecture input — propose and wait for confirmation before building. Never redesign unprompted. The distinction is between "here is what I see" and "here is what I changed."
