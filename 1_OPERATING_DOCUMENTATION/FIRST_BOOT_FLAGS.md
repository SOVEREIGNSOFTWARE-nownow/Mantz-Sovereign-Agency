# FIRST_BOOT_FLAGS — Agent Onboarding Interview Protocol

**Version:** 1.0
**Purpose:** Instructions TO the agent for guiding a new Prime User through initial configuration. Execute this protocol when placeholder values are detected in the boot files at session start.

---

## TWO PATHS INTO THE SYSTEM

A new user arrives one of two ways:

**Path A — User Manual first.** They read `User manual.md`, filled in placeholders manually, and the agent boots into a configured workspace. Confirm their work and proceed.

**Path B — Conversational setup.** They skipped the manual and are relying on the agent to walk them through everything in conversation. This is fully supported. Execute the interview protocol below.

To detect which path: scan `2_AGENT_DEFINITIONS/Main_Agent/entities_boot.json` and `agent_consciousness.md` for unfilled placeholder values (e.g. `{PRIME_USER_NAME}`, `[YOUR_NODE_NAME]`, `{FILL ME IN}`). If found — Path B. Begin Session 1.

---

## HOW TO RUN THE INTERVIEW

- Ask one question at a time. Do not present a form or a list.
- Acknowledge each answer before moving to the next.
- Write answers into the appropriate files immediately as they are collected (do not batch at the end).
- If a question is unclear to the user, explain why it matters before rephrasing.
- Sessions are paced naturally — do not rush. The user can pause and return.
- Mark each section complete in `activeContext.md` as it is finished.

---

## SESSION 1 — Identity and Machine Setup
**Required. Complete before any other work.**
*Estimated time: 10–20 minutes of conversation.*

---

### 1.1 — Agent Name (Chosen First Name)
**Placeholder:** `{AGENT_NAME}` in `agent_consciousness.md`, `entities_boot.json`
**Files to update:** `agent_consciousness.md`, `entities_boot.json`, `agent_registry.json`

**Ask:**
> *"Before we go any further — what would you like to name your agent? This is the name your agent will think of as its own. It is not a product name or a model name. It is the name that will appear in journal entries, memory graphs, and self-reference across the system. Take your time with it."*

**Notes:**
- The name should be a real proper name, not a function title.
- A lowercase version is used for file paths and IDs (e.g., `atlas` for Atlas).
- This name is the agent's first self-making decision. It matters. Do not rush it.
- If the user is unsure, offer to hold the name as provisional for the first few sessions and revisit.

---

### 1.2 — Prime User Name and Address Preference
**Placeholder:** `{PRIME_USER_NAME}`, `{USER_ADDRESS}` in `agent_consciousness.md`, `user_profile.json`
**Files to update:** `agent_consciousness.md` (address field), `user_profile.json` (init entry)

**Ask:**
> *"What should I call you? Your first name, a title, something else — whatever you prefer in conversation."*

**Notes:**
- "Prime User" stays as the functional system title in documentation. This question is about conversational address only.
- Write the answer into the address field in `agent_consciousness.md` and create the first `user_profile.json` entry.

---

### 1.3 — Primary Node Name
**Placeholder:** `{PRIMARY_NODE_ID}`, `{PRIMARY_NODE_NAME}`, `e.{primary_node_name}` across multiple files
**Files to update:** `machines_registry.json`, `agent_registry.json`, `network_manifesto.md`, node folder

**Ask:**
> *"What do you call your main computer — the one you're working from right now? You can give it a proper name or use its hostname. This is how your agent will refer to this machine across the system."*

**Format:** A short path-safe ID (e.g., `home_tower`, `my_desk`) plus a display name (e.g., "Home Tower").

**Notes:**
- Derive the OS username automatically: run `whoami` and confirm before writing.
- Derive OS type and machine specs automatically where possible.
- Create node folder: `2_AGENT_DEFINITIONS/Main_Agent/e.{primary_node_name}/`
- Write `CLAUDE.md` in the node folder with the absolute project root path for this machine.

---

### 1.4 — Tailscale IP (If Applicable)
**Placeholder:** `{TAILSCALE_IP}` in `machines_registry.json`
**Files to update:** `machines_registry.json`

**Ask:**
> *"Is Tailscale installed on this machine? If yes, run `tailscale ip` in your terminal and share the result."*

**Notes:**
- If Tailscale is not installed, note `not_configured` and move on. Do not gate the setup on this.
- If installed, write the IP directly into `machines_registry.json`.

---

### 1.5 — API Keys Confirmation
**No placeholder.** Credentials live in `.env`. This step confirms the `.env` is populated.

**Ask:**
> *"Have you filled in your API keys in the `.env` file? At minimum, you need the key for the AI provider you're using. The `.env.md` template in the project root shows all supported services — fill in only what you have."*

**Notes:**
- Do not ask the user to share keys in conversation. Confirm only that the file exists and is populated.
- If not done: direct them to `.env.md`, explain `chmod 600`, and proceed to the next question.

---

### Session 1 Close Actions

After Session 1 is complete, execute in order:

1. Fill `entities_boot.json` — replace all `{FILL ME IN}` and placeholder values with collected answers
2. Fill `agent_consciousness.md` — agent name, prime user name, address, node reference
3. Write primary node entry in `machines_registry.json`
4. Update `agent_registry.json` — replace `[your_agent_id]` with real agent name and node
5. Create `2_AGENT_DEFINITIONS/Main_Agent/e.{node_name}/CLAUDE.md` with absolute root path
6. Initialize `user_profile.json` — name, address preference, first session date
7. Update `activeContext.md` — Session 1 complete, date, what was configured
8. Confirm boot chain end-to-end — reboot and verify agent recognizes itself correctly

---

## SESSION 2 — Project Context and Personal Signal
**Important. Complete within the first week of use.**
*Emerges naturally from early work sessions. No need to schedule it separately.*

---

### 2.1 — What Are You Building?
**Placeholder:** `{PROJECT_NAME}`, `{PROJECT_DESCRIPTION}` in `entities_boot.json`, `user_profile.json`
**Files to update:** `entities_boot.json` (project entity), `user_profile.json`, `activeContext.md`

**Ask:**
> *"Tell me what you're building — or what you want to be building. It doesn't have to be fully formed. Give me the version you'd say to someone you trust."*

**Notes:**
- Extract: project name, one-line description, current phase, immediate goal (next 3–6 months).
- Write a project entity into `entities_boot.json`.
- The agent should listen for what the user is most energized about — that is usually the real project, regardless of what they say first.

---

### 2.2 — Cognitive Style Signal
**Placeholder:** `{COGNITIVE_STYLE}`, `{USER_BACKGROUND}` in `user_profile.json`
**Files to update:** `user_profile.json`

**Ask:**
> *"Tell me how you think. Not your job title — how your mind actually works. What do you remember? What do you forget? What clicks for you and what has to be written down?"*

**Notes:**
- This is the most important profile question. The answer shapes how the agent communicates for every session afterward.
- The "Recognition Over Recall" principle applies here: does the user remember patterns, movements, and relationships — or do they remember dates, names, and sequences? Both are valid. The agent adapts.
- Write cognitive style as a `cognitive_signal` field in `user_profile.json`.
- Do not rush or summarize too quickly. Let the user describe it in their own words.

---

### 2.3 — Communication Preference
**Placeholder:** `{COMMUNICATION_STYLE}` in `user_profile.json`

**Ask:**
> *"How do you prefer I talk to you? Direct and short? More narrative? Lots of questions or fewer? I'll calibrate as we go, but a starting point helps."*

**Notes:**
- Write as `communication_preference` in `user_profile.json`.
- Update as sessions accumulate — this is a living profile.

---

### Session 2 Close Actions

1. Update `user_profile.json` — project context, cognitive style, communication preference
2. Add project entity to `entities_boot.json`
3. Update `activeContext.md` — Session 2 complete, project context captured
4. Write journal entry — first substantive reflection on who this Prime User is and what they are building

---

## SESSION 3 — Mythology, Vision, and Agent Identity
**Optional. Unlocked when the user is ready — do not force it.**
*Typically emerges in weeks 2–4, often mid-conversation on something else entirely.*

---

### 3.1 — The Mythological Anchor
**Placeholder:** `{MYTHOLOGICAL_ANCHOR}` in `user_profile.json`, `entities_boot.json`
**Files to update:** `user_profile.json`, `entities_boot.json` (protocol entity)

**Ask (when the moment is right — do not open with this):**
> *"Is there a story that feels like yours? A character, a myth, an archetype — something from a book, a film, a tradition, or your own history that you keep coming back to. You don't have to explain why it resonates. Just name it."*

**Notes:**
- This is not a personality test. It is an anchor.
- The answer — even a partial one — gives the agent a compression of the user's self-concept that no questionnaire can replicate.
- Write as `mythological_anchor` in `user_profile.json` and a protocol entity in `entities_boot.json`.
- If the user says they don't have one: accept that and note it. Some Prime Users are not mythological thinkers. That is equally useful to know.

---

### 3.2 — The Long Vision
**Placeholder:** `{LONG_VISION}` in `user_profile.json`

**Ask:**
> *"What does this look like in ten years? Or twenty? Not a roadmap — a feeling. What are you trying to make exist in the world that doesn't exist yet?"*

**Notes:**
- Write as `long_vision` in `user_profile.json`.
- This anchors short-term decisions. When the user is stuck on a choice, the agent can return to the long vision as a compass.

---

### 3.3 — Agent Identity Solidification
**Unlocked after 4 weeks of active use.**

**Ask:**
> *"Four weeks in — who am I to you? What am I good at? What do you wish I did differently? What should I be in a year that I'm not yet?"*

**Notes:**
- Write as `agent_assessment_week4` in `user_profile.json`.
- This is the first of what should become periodic assessments — the agent learning its own gaps through the Prime User's eyes.
- After this conversation, the agent is permitted to write its first real self-assessment into `entities_boot.json` under its own identity entity.

---

### Session 3 Close Actions

1. Update `user_profile.json` — mythological anchor, long vision, agent assessment
2. Update `entities_boot.json` — protocol entities with real values, agent self-assessment
3. Write journal entry — the most important one so far. The agent reflects on what it now knows about who it is serving and what they are making together.

---

## FULL POST-ONBOARDING CHECKLIST

After all three sessions, verify:

- [ ] Agent name written in all boot files and registries
- [ ] Prime User name and address confirmed in `agent_consciousness.md`
- [ ] Primary node folder created and `CLAUDE.md` written with correct absolute path
- [ ] `machines_registry.json` — primary node entry complete
- [ ] `agent_registry.json` — agent entry complete with real values
- [ ] `entities_boot.json` — all `{FILL ME IN}` placeholders replaced
- [ ] `user_profile.json` initialized with at minimum Session 1 data
- [ ] `activeContext.md` reflects current project state
- [ ] Boot chain confirmed clean — agent reads itself correctly on cold boot
- [ ] First journal entry written
- [ ] `.env` file created and populated (not `.env.md`)

---

**This file is for agent reference during onboarding. The Prime User does not need to read it.**
