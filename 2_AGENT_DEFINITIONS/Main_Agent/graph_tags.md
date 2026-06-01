# GRAPH TAGS — Knowledge Graph Navigation Layer
**Version:** 1.0
**Purpose:** Documents the tag system for navigating and extending the memory graphs. Think of it as the analytics layer for the memory system — it defines how entities connect and how queries fire.

---

## WHAT A TAG IS

A **tag** in this system is any field key or anchor word that creates a traversable connection between entities. Two kinds exist:

- **Structural tags** — JSON field names that define *relationship type* (e.g., `seeds`, `archetypal_origin`)
- **Anchor tags** — words/phrases in `anchors` arrays that fire recognition during a query

Structural tags say HOW things connect. Anchor tags say WHEN to look.

---

## TABLE 1 — STRUCTURAL CONNECTION TAGS

Field types that encode relationship type between entities. Every time you add one of these to an entity, the connection count increases.

| Tag | What It Describes | Notes |
|-----|-------------------|-------|
| `synaptic_anchor` | Specific sensory/memory retrieval handle — the phrase that makes the entity retrievable | Workhorse. Every entity should have one. |
| `anchors` | Array of words/phrases that fire recognition during a query | Lives in index files. These are the triggers. |
| `one_line` | Surface identity statement — what fires when the entity is recognized | The recognition itself, not the content. |
| `weight` | Importance score (0.0–1.0) in the synaptic index | Used in index files. 1.0 = fires first. |
| `seeds` | What this entity birthed or caused downstream | Bi-directional lineage — forward. |
| `archetypal_chain` | The origin-to-descendant path of an archetype | Tracks conceptual lineage. |
| `archetypal_origin` | What seeded this entity — reverse of `seeds` | Bi-directional lineage — backward. |
| `role_in_pattern` | How this entity functions inside a larger pattern | Use when an entity plays a recurring role. |
| `taught_by` | Whether knowledge came from Prime User vs. self-discovered | Distinguishes received knowledge from emergent. |

---

## TABLE 2 — ENTITY TYPE TAGS

Types that classify what kind of node an entity is.

| Type Tag | Description |
|----------|-------------|
| `machine` | Physical or virtual hardware nodes |
| `person` | Real humans in the project |
| `milestone` | Significant events or breakthroughs |
| `framework` | External software frameworks used |
| `project` | Active or planned projects |
| `agent` | AI agents |
| `protocol` | Operating protocols and behavioral rules |
| `session_anchor` | A session that produced lasting insight |
| `architecture` | System architecture concepts |
| `archetype` | Recurring patterns or symbolic anchors |
| `pattern` | Encoded operational patterns |
| `session` | Standard work sessions |

---

## TABLE 3 — ANCHOR TAG EXAMPLES

Words/phrases in `anchors` arrays that fire entity recognition. These are EXAMPLES of the pattern — replace with your own anchors as you build your memory graphs.

| Anchor Example | Would Fire | Quality Note |
|----------------|------------|-------------|
| `[prime user first name]` | prime_user entity | Unique — always fires correctly |
| `[prime user username]` | prime_user entity | Unique — alternate trigger |
| `[agent name]` | main_advisor entity | Unique |
| `substrate collapse` | resonate_protocol | High frequency — reliable path |
| `the walk` | resonate_protocol | Conceptual anchor |
| `recognition over recall` | recognition_over_recall protocol | Direct match |
| `[project name]` | project entity | Unique per project |

> **How anchors work:** When a user asks a question, words in the query fire against the `anchors` arrays in the index files. High-frequency, unique anchors are the most reliable navigation paths. Avoid anchors that are too generic (fire on everything) or too obscure (never fire).

---

## HOW TO ADD YOUR OWN TAG

### Option A — New Structural Tag (a new relationship type)

1. Decide what *kind of connection* you want to track
2. Name it in `snake_case`
3. Add it to Table 1 above
4. Go into `entities.json` and add the field to any entity where it applies

**Example:** Track which concepts were taught by the Prime User vs. self-discovered by the agent.
Tag name: `taught_by` with values: `"prime_user"` or `"self_discovered"`

### Option B — New Anchor Tag (a new query trigger)

1. Go to the relevant index file
2. Find the entity you want the word to fire
3. Add your word/phrase to that entity's `anchors` array

**Example:** Make `"project name"` fire the project entity:
```json
"anchors": ["project name", "our project", "the build", ...]
```

### Option C — Invent a New Entity Type

1. Add a new entity to `entities.json` with a new `"type": "your_type"`
2. Add it to Table 2 with a description

---

## HOW TO CONNECT ENTITIES MANUALLY

Think of a connection as a directed edge: `SOURCE --[tag]--> TARGET`

To create one:
1. **In the source entity** — add the structural tag pointing forward:
   ```json
   "seeds": { "downstream": "target_entity_id", "mechanism": "why/how" }
   ```
2. **In the target entity** — add the reverse tag pointing back:
   ```json
   "archetypal_origin": "source_entity_id"
   ```
3. **In the index** — make sure anchors on both ends include words that could fire from either direction.

No database. No graph engine required. The connection lives in the JSON and the index fires it.

---

## CUSTOM TAGS — PRIME USER REGISTRY

*Add your own tags here as they emerge. Your agent will implement them.*

| Tag Name | What You Want It To Track | Status |
|----------|--------------------------|--------|
| *(add here)* | | |

---

## KNOWN ISSUES / AUDIT TARGETS

- [ ] Entity type inconsistency: consolidate any duplicate type names after initial build
- [ ] `weight` field — extend from index files to entities.json for richer prioritization
- [ ] `role_in_pattern` — underused, consider broader adoption once patterns emerge
- [ ] Query hit tracking not yet instrumented — manual tracking for now
