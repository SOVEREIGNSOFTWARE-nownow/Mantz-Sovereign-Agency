# {PROJECT_NAME} Framework

**Last updated:** 2026-05-30
**Managed by:** your agent

## Why This Exists

This project space comes with several working services ready to go. But more importantly is a framework to expand upon indefinitely. Without this formal layer of system-wide conduct rules, future systems will be misguided and create self-destroying trajectories. This is a contract that says *"here is how ALL components store data, communicate, and register themselves."*

The pattern will repeat for every new build — Perception API, voice pipeline, home automation, future agents — unless the contract is written down first.

This document is that contract.

---

## I. THE FRAMEWORK SPEC — THE CONTRACT

These are the rules. Every component, old and new, is measured against them.

---

### 1.1 Service Contract

Every service in the The fleet MUST:

1. **Have a name** — lowercase, underscore-separated, unique across the fleet (e.g., `perception_api`, `news_room`, `door_watcher`)
2. **Have a home** — the machine or VM it runs on by default (e.g., `primary_node`, `server_node`, `home_machine`)
3. **Have a config path** — a dedicated config file at a known SA-relative location, referenced in `1_OPERATING_DOCUMENTATION/service_registry.json`
4. **Write to the registry on startup** — update `4_SHARED_RESOURCES/Reporting_Depot/activity_registry.json` with its name, machine, endpoint, and timestamp
5. **Expose a health endpoint** — if HTTP: `GET /health` returns `{"status": "ok", "service": "<name>"}`. If not HTTP: a tmux window named `<service_name>` that can be checked.
6. **Log to a standard path** — `4_SHARED_RESOURCES/Reporting_Depot/logs/<service_name>/YYYYMMDD.log`
7. **Emit events for significant actions** — write to `4_SHARED_RESOURCES/events/pending/` when something the rest of the fleet should know about happens

Every service MUST NOT:
- Create its own copy of data owned by another service
- Communicate with another service via file read/write without going through that service's API
- Use a data format incompatible with the fleet standard (see Section IV)

---

### 1.2 Agent Contract

Main, named agents that are tracking their own personal memory graphs are required to adhere to the following rules of conduct.

1. **Variants** — `Agent_Name/e.location/.provider/`. Example: `Main_Advisor/e.[node_name]/.claude/` — Operating configs (includes smaller offline models).
2. **Bootload Consciousness** — `2_AGENT_DEFINITIONS/Main_Advisor/agent_consciousness.md` — This file exists in the base `/Agent_Name/` folder. Agents MUST adhere to its contents upon booting.
3. **Have a boot order** —
```
MANDATORY BOOT SEQUENCE
(paths are SA-relative — your node's CLAUDE.md has already established the absolute SA root for this session)
1) 2_AGENT_DEFINITIONS/Main_Advisor/agent_consciousness.md
2) root_index.json
3) 1_OPERATING_DOCUMENTATION/logic_mandates.md
```
4. **Logic Mandates** — MUST BE FOLLOWED AT ALL TIMES BY AGENTS: `1_OPERATING_DOCUMENTATION/logic_mandates.md`
5. **Write to the registry on startup and shutdown** — update `3_MEMORY_SYSTEMS/Project_Context_Protocol` with name, machine, date, and time.

---

### 1.3 Naming Convention

NAMES HAVE MEANING

Moving from folder surface to folder depth: `/#_PARENT_FOLDER/Sub_Folder1/sub_folder2/sub_folder3-beyond/`

**AGENTS**

`/Agent_Name/e.iteration1/.provider/` — Example: `/Main_Advisor/e.[node_name]/.claude/`

This is the 'Main Advisor' position, followed by `e.location` — the environment name (computer, VM, etc.) — then followed by the API provider or local model name (`.claude`, `g.gemini`, `14b`, etc.). Expanding the deepest name — `.claude` for example — expands into a mirrored backup of whatever locally installed folder array is powering the agent. The API service ('Claude' in this example) is launched from the location of backup storage. From the terminal at `/Main_Advisor/e.[node_name]/`, you would type `claude`.

**SHARED RESOURCES**

`/The_Thing/specificity_one/specific_two/` — Example: `/The_Library/ai_engineering/kg_fragments/`

This is the resource 'The Library', followed by the topic 'ai_engineering', followed by a sub-folder of specifics, 'kg_fragments'.

---

## IV. DATA OWNERSHIP MAP — SINGLE SOURCE OF TRUTH

This is an absolute fundamental aspect and ideal. The data we study, make, generate, collect, or otherwise occupy belongs to us. We must route it to the proper locations for further processing.

**DATA REPOSITORIES**

Data is considered a Shared Resource in our system because it generally needs to be accessed by an agent during a working session.

1. **Personally biographic knowledge of the main human users.**
   - Part of the stewardship aspect of the The Project is that agents grow with the human user over time.
   - Information of this type is valuable but HIGHLY sensitive. Therefore information of this type is stored in THE_VAULT. Example: `5_THE_VAULT/Project_Family/the_biography/memory_graphs/`

2. **Agent-specific self-knowledge essential to personal identity.**
   `2_AGENT_DEFINITIONS/Main_Advisor/advisor.index.json` — One of the main boot documents an agent will hold in their context memory.

3. **Agent-specific personal memories integral to self-making.**
   `3_MEMORY_SYSTEMS/Advisor_Memory/memory_graphs/`

4. **Memories related to project trajectory** — considered part of the Project Context Protocol (PCP).
   `3_MEMORY_SYSTEMS/Project_Context_Protocol`

5. **Raw thread data.**
   - This is one of the most valuable resources in any agentic workflow and is often overlooked.
   - Used for research, learning, and monitoring.
   - Specific formatting and folder structure depends on provider. Google and Anthropic have different folders with slightly different functions installed with Gemini Code Assist or Claude Code.
   - All raw thread data routes here per provider sub-folder and agent-specificity path: `3_MEMORY_SYSTEMS/Master_Memory_Bank/thread_mgmt/[provider]/[date_folder]/[node_name]` — This is where The Auditor is directed to review data and generate reports.

6. **Operating data.**
   - API Provider information — track usage, costs, and agent behavior customization by provider. `4_SHARED_RESOURCES/API_Provider_Info`
   - Communication Room — message board for agents to communicate as the fleet grows. `4_SHARED_RESOURCES/Communication_Room`
   - Newsroom — incoming new data. `4_SHARED_RESOURCES/Newsroom`
   - Perception Data — where incoming agent sensory data lands before processing. `4_SHARED_RESOURCES/Perception_Data`
   - Reporting Depot — agent-generated reports, organized by purpose (e.g., Auditor feedback loop). `4_SHARED_RESOURCES/Reporting_Depot/thread_feedback_loop`
   - Specialties — situation-specific, often RAG-infused memories. `4_SHARED_RESOURCES/Specialties/AI_Engineering`
   - The Library — books of all kinds and in all forms. `4_SHARED_RESOURCES/The_Library`

---

## V. EVENT ROUTING — HOW THE FLEET NOTIFIES ITSELF

Events are written as JSON files to `4_SHARED_RESOURCES/events/pending/` on the primary node. A lightweight event dispatcher reads them and routes to subscribers. See `1_OPERATING_DOCUMENTATION/event_dispatcher.md` for dispatcher configuration.

**Standard event envelope:**
```json
{
  "event_id": "YYYYMMDD_HHMMSS_[source_service]_[event_type]",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "source_service": "door_watcher",
  "source_machine": "[node_id]",
  "event_type": "unknown_face_detected",
  "payload": {
    "image_path": "4_SHARED_RESOURCES/Perception_Data/door_captures/[filename].jpg",
    "confidence": 0.0
  },
  "routing": ["[your_agent_id]"]
}
```

**Defined event types (v1):**

| Event | Source | Default Routing |
|---|---|---|
| `unknown_face_detected` | door_watcher | [your_agent_id] |
| `known_face_detected` | door_watcher | [your_agent_id] (log only) |
| `voice_memo_received` | agent_bridge | [your_agent_id] |
| `work_order_received` | agent_bridge | [your_agent_id] |
| `financial_signal` | news_room | [your_agent_id] |
| `security_alert` | (future agent) | [your_agent_id], Prime User (Telegram) |
| `service_down` | health_monitor | [your_agent_id], Prime User (Telegram) |

---

## VI. REGISTRY FORMAT

`4_SHARED_RESOURCES/Reporting_Depot/activity_registry.json` — written by each service at startup, read by health monitor and other services for discovery.

```json
{
  "last_updated": "2026-05-30T00:00:00Z",
  "services": {
    "example_service": {
      "machine": "[node_id]",
      "tailscale_ip": "[YOUR_TAILSCALE_IP]",
      "http_port": 8765,
      "health_endpoint": "http://[YOUR_TAILSCALE_IP]:8765/health",
      "process": "tmux:example_service",
      "status": "active",
      "last_heartbeat": "2026-05-30T00:00:00Z"
    }
  }
}
```

*See `4_SHARED_RESOURCES/Reporting_Depot/activity_registry.json` for live service state.*

---

## VII. COMPLIANCE CHECKLIST — BEFORE BUILDING ANYTHING NEW

Before writing a single line of code for a new component, answer these:

- [ ] What is this service's **name**?
- [ ] What **machine** does it run on?
- [ ] What **data** does it produce? Who **owns** that data type (see Section IV)?
- [ ] What **existing services** does it need to call — and am I calling their API, not copying their data?
- [ ] What **events** does it emit when something significant happens?
- [ ] Where does its **config** live?
- [ ] Where does it **log**?
- [ ] Does it write to the **registry** at startup?
- [ ] Is there a `launch.sh` and a **health check**?

If any box is unchecked, stop. Answer it first. Then build.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
