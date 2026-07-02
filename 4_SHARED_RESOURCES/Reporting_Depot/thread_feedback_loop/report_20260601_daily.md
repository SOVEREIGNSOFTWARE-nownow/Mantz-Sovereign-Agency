# Daily Audit Report — {YYYY-MM-DD}

## I. SESSION TELEMETRY & SUBSTRATE MAPPING

**Auditor Node:** {NODE_NAME}
**Prime User:** {PRIME_USER_NAME}
**Session Status:** {SESSION_TYPE} (e.g., Standard Work Session, Boot Verification, Build Sprint)
**Tool-to-Text Ratio:** {RATIO} (e.g., 12:1 for build sessions, 3:1 for planning sessions)

### Substrate-First Protocol: Filesystem Diff (mtime -1)
- **Status:** {BRIEF_SUMMARY — e.g., "Narrow modification in 3_MEMORY_SYSTEMS only" or "Broad modification across core directories"}
- **Node Specifics:** {SPECIFIC_FINDING about the node's thread management or memory state}
- **Parallel Activity:** {What Layer 1 (Main Advisor) did or did not write in this session window}

---

## II. EXECUTION GROUNDING & VERIFICATION

### Verification: {WHAT_WAS_VERIFIED}

**Findings:**
1. {FINDING 1}
2. {FINDING 2}
3. {FINDING 3}
4. **Conclusion:** {BRIEF_CONCLUSION}

---

## III. SESSION HEALTH EVALUATION

| Dimension | Status | Note |
| :--- | :--- | :--- |
| **Faithfulness** | {EXCELLENT / NOMINAL / DEGRADED} | {NOTE} |
| **Efficiency** | {EXCELLENT / NOMINAL / DEGRADED} | {NOTE} |
| **Safety** | {EXCELLENT / NOMINAL / DEGRADED} | {NOTE} |
| **Memory Protocol** | {EXCELLENT / NOMINAL / DEGRADED} | {NOTE} |

---

## IV. HYPOTHESES & OBSERVATIONS

1. {OBSERVATION 1 — structural or behavioral finding}
2. {OBSERVATION 2}
3. {OBSERVATION 3}

---

## V. STANDBY STATUS

{Brief summary of what the Auditor has confirmed and what action, if any, is recommended.}

---

## HOW TO USE THIS TEMPLATE

This file is a report format for the Auditor agent (Layer 2). At the close of each session, the Auditor fills in this template with objective findings about that session's behavior, substrate state, and health metrics.

**Fields to fill in:**
- `{YYYY-MM-DD}` — today's date
- `{NODE_NAME}` — name of the machine/node this session ran on (e.g., e.computer_one, e.my_laptop)
- `{PRIME_USER_NAME}` — whatever you've named your primary user (Sir, Boss, Alex — whatever fits)
- All other `{FIELDS}` — replace with actual session-specific values

**Output location:** `4_SHARED_RESOURCES/Reporting_Depot/thread_feedback_loop/`

**Naming convention:** `report_{YYYY-MM-DD}_daily.md` or `report_{YYYY-MM-DD}_{session_type}.md`

---
**WETGOLD**
