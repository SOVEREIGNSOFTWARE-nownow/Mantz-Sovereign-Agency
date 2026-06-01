{PROJECT_NAME}

# README — Thread Management

## **`3_MEMORY_SYSTEMS/Master_Memory_Bank/thread_mgmt`**

## PURPOSE

All session thread data lives here, organized by provider and month. Two parallel storage formats are maintained for each provider — raw and conversation — serving different purposes.

---

## STORAGE FORMATS

**`[month_year]_raw/`**

The native storage format from the provider. Each provider (Claude Code, Gemini CLI, etc.) generates its own format. All locally stored provider folders are symlinked or synced here as the canonical location.

**`[month_year]_convo/`**

The human-readable version. During each session, the agent outputs all responses to an external markdown document in real time. The Prime User copies their prompts into the same document as they happen. The result is a clean, readable record of the full conversation — useful for review, training, and long-term reference.

---

## CURRENT CONTENTS

**`claude/`** — Claude Code CLI session data. Contains `06_2026_raw/` (provider native) and `06_2026_convo/` (human-readable session documents).

Additional provider folders are added as they are configured.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
