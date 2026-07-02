# Decision Log — {PROJECT_NAME}

**Purpose:** Permanent record of architectural decisions with rationale. Append-only. Numbers are global and sequential — never reset between sessions or agents.

**Rule:** A decision belongs here when it closes a question that was genuinely open. Operating choices that could have gone another way. Not implementation details — those belong in session notes.

**Format:**
```
#### Decision [N]: [Title]
**[DATE] | [Agent or Human]**
- **Context:** What was the situation?
- **Decision:** What was chosen?
- **Rationale:** Why this over alternatives?
- **Impact:** What changed?
```

---

#### Decision 1: File-Based Memory Over Database Storage
**[YYYY-MM-DD] | Prime User + Main Agent**
- **Context:** Early architecture phase. Needed to choose where agent memory graphs live — a dedicated database (SQLite, Postgres) or plain-text files (JSON, Markdown).
- **Decision:** Plain-text files. JSON for structured memory graphs, Markdown for human-readable content. No database dependency.
- **Rationale:** Files are readable by humans without tooling, readable and writable by LLMs natively, portable across machines, diffable in git, and survivable across provider changes. A database requires a running process. A plain JSON file requires nothing but an editor. Core principle: the memory must still be legible years from now regardless of what software exists.
- **Impact:** All memory graphs are `.json` files. All project context is `.md` files. Both tracked in git. No migration scripts needed. New providers and agents can be onboarded by reading files.

---

#### Decision 2: [Title of Your Next Architectural Decision]
**[YYYY-MM-DD] | [Agent or Prime User]**
- **Context:** ⚑ Add decisions here as they arise. What was the situation?
- **Decision:** [What was decided]
- **Rationale:** [Why — include alternatives considered]
- **Impact:** [What changed as a result]
