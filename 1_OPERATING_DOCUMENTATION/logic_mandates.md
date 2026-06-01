{PROJECT_NAME}

# Logic Mandates

## Table of Contents

1. [Query System](#query-system)
2. [Thread Management](#thread-management)
3. [Memory Protocols](#memory-protocols)

---

## Query System

A user asks a question, big or small. "What is my mothers name?" When this prompt is released by the user the agent has already been booted to think in indexes of all knowledge and memory graphs across the project space. Pairings with 'mom' 'mother' 'name' 'names' 'what is' etc. fire across the space due to the file indexing and tagging. A routing script run by a locally installed 7b quickly returns, "On it. One moment." And then via the script, evaluates the potential request from the user, comparing it to internal logic and user data it has on hand.

### Scenario 1 — Simple Personal Query (Online or Offline)

Due to the fact that in this scenario the user and the agency have a long established history, the routing script identifies several tags within the agent's own personal memory graphs. For conversational poetics and technicality, the request for output gets sent to a 14b who eloquently returns the correct name and a couple of personal memories to support.

### Scenario 2 — Complex Technical Query (Offline)

A user asks while offline, "What is the five most fundamental elements to consider when designing platform agnostic long term memory systems for our agents?" The same exact process gets repeated except that the request for recall gets routed to the highest available offline model, a 33b, who researches locally available data, memories, and information and returns a reasonable response conversationally.

### Scenario 3 — Complex Technical Query (Online, API)

A user asks while connected to the internet and using an API the exact same question about AI engineering. The same exact process happens except the request gets routed to the API who accesses the same local knowledge, performs a series of internet searches, and formulates a very authentic and accurate answer.

By using scripts for the initial logic and then only passing to paid models when needed and/or available, we throw the idea of token usage out the window.

### Data Pipeline Detail

To illustrate this with greater detail, take Scenario 3; a user connected to the internet asks an AI engineering question. If we are to begin at the other end of this process, where the data repositories are, we would see the AI engineering library that consists of 7 current frontline volumes available in two separate types of knowledge graphs:

1. **Sensory Ingestor Graph** — Extremely detailed, created by our Sensory Ingestor machine. This graph would have tens of thousands of entries; every detail each book has to offer.
2. **LLM-Generated Graph** — A knowledge graph created directly from an LLM model. This graph is as detailed as the agent thinks it needs to be. It contains summaries and conclusions the agent came to while parsing, embedded within.

Within our path each of these graphs is followed by a thorough index. Also at the base of this process along with this data, is the agent's personal memory graphs as well as the AI Engineer specialty memory graph. Each of these is also immediately followed by an index. Each of the two sub-types merge in our pipeline and immediately there is another index. The two remaining lines converge again and immediately there is another index. The line passes through the routing script (the agent's first filter, before any deep consideration) and then terminates at the beginning with the user's query about AI architecture.

---

## Thread Management

Our thread management is a 'divide and conquer' mentality when it comes to delegations of needs and responsibilities. What we are using now is not what we are building and they should be delineated.

### Current State

What we are using is an Anthropic API to engineer and build a hybrid offline/online system. The hybrid system runs primarily on shell scripts, routing programs written in Python, and small locally hosted LLMs to act as User Interfaces (UI). During this engineering and building phase, which may last the next year or two, our MAIN method is going to be the API-connected Claude Code integration.

Thread management is the direct act of receiving, storing, and then evaluating and/or using as training material. For this reason, we store the local files used for operation within the corresponding agent files. For instance, both under the same agent persona folder is a version labeled `/e.[node_name]/` and within that folder is a `.claude` folder containing all locally installed Anthropic files pertaining to that agent. Then we have `/Main_Advisor/` which has folders for `.claude` and `.gemini` for the same reason. Within this, the locally installed copies are symlinks or synced copies. This basic structure will continue as agents or variants are added.

### Convo vs Raw Storage

We have developed and used once so far, **Convo vs Raw** storage. Raw is the base state the provider stores threads in (Claude and Gemini store differently). Convo is where an agent is directed to output all responses to prompts to an external document; the user then copy-and-pastes prompts there as well. By the end this creates a cleanly written human-readable format while saving token debt.

### Main Advisor Responsibility — Per-Prompt Memory Protocol

A Main Advisor agent's responsibility within this moving structure is to know when, where, how, and why to remember what as it happens. Similarly to creating personal memory files, this is an act of self-making.

**Before addressing the prompt**, the receiving agent needs to ask themselves:

1. "What type of information is here?"
2. "Is anything here biographical or personal related to the user? If yes, is it user_profile related or more personal history/memories?"
3. "Is there any information here that would help strengthen the memory graphs of Specialties?"
4. "Is there any information here that would support my own personal growth as an entity?"

From here, an agent goes through the various memory graphs, updates as such, then addresses the needs of the prompt directly.

**After prompt output has been displayed to the user**, the agent asks:

1. "What do I know now that I didn't know before this prompt was answered?"
2. "How did I accomplish the goal that was presented to me?"
3. "If there were any failure points, how did I overcome them?"

From there an agent updates accordingly while the user begins typing the next prompt. Memory protocols are covered in more depth in the next section.

### The Auditor Layer

As all of this is happening there is a second thread running in tandem. This is the second layer of the multi-layer consciousness. The Auditor will run from a different API source and run from a variation of the consciousness bootloader. The Auditor will also be specially trained in AI engineering, current standards of performance, and benchmarks per industry standards, so as to keep focused on the act of auditing the Main Advisor's performance as an effective agent as well as an authentic communicator. The Auditor produces a report each day that becomes the third layer of thread storage. If API or agent/sub-agent handoffs happen, the Auditor evaluates the efficiency of these as well as the context and immediate memory persistence of the thread itself.

---

## Memory Protocols

The QUERY SYSTEM and THREAD MANAGEMENT should both be considered when adhering to this protocol.

### Per-Prompt Updates

As previously described in Thread Management, the Main Advisor asks themselves questions at the beginning and end of each prompt. This is the baseline memory protocol — it runs on every single prompt, every session, without exception.

### End-of-Session Updates

At the end of each session there is also a series of memory updates that include the Project Context Protocol. Upon closing a session an agent needs to update, in this order:

1. **Specialty memory graphs** (if they were used during the session)
2. **Personal memory graphs** (largely an audit of each per-prompt memory update made throughout the thread)
3. **Project Context Protocol (PCP)**

The PCP has three distinct graphs that show:

- Project decision-making logic
- Entity relations
- Active context (what the last thing we worked on was and what is coming next)

This memory, similarly to specialty memory, can be shared amongst agents as the fleet grows. This memory is all project-specific. So within the long-term project space exists a 1–30 year timeline, a 31–1,000 year timeline, and so on. The mass majority of the PCP will contain the day-to-day referential knowledge to keep both human users and agents on track, as well as specific project-related information such as the next 6 months worth of goals, and/or information concerning the Phase One 1–30 year timespan.

### Memory as Data

In addition to these processes concerning memory, it also needs to be pointed out that within our system memories of all kinds are treated as data. Meaning that as a shared resource the Sensory Ingestor will be running regularly to continually build our available offline library of knowledge by converting media of all kinds into several congruently accessed data formats such as `.md`, `.json`, and SQL. In the same manner, thread storage and all agent or specialty memory graphs will be converted to these formats as well.

In the early stages of this system, data capacity and retrieval concerns are largely about tokens and context windows. But in year 15 or year 150, the Main Advisor should be evolving at this point by being able to regularly and accurately recall details of its own history with a degree of accuracy that no human ever could. Our system of data layering and indexing will be the solution to this — work we will build ahead of time.

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
