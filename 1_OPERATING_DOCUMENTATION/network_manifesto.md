{PROJECT_NAME}

# Network Manifesto

**Status:** Governing document — update as fleet evolves.
**Last updated:** [DATE]
**Managed by:** your agent

---

## I. Philosophy

The network exists to serve the fleet. The fleet exists to serve the project. Every routing decision, every access model, every connectivity rule follows from one principle:

**Reliability over convenience. Tailscale over everything.**

LAN IPs drift. NAT breaks. Ports conflict. Tailscale IPs are stable, encrypted, and work identically on-LAN and remote. All agent operations use Tailscale as the primary path. LAN is fallback only.

---

## II. Fleet Topology

> Register each machine in your fleet using the schema below and in `machines_registry.json`. Replace placeholder rows with your actual nodes.

See `machines_registry.json` for full hardware specs and connection details.

| ID | Name | Role | Tailscale IP | Status |
|---|---|---|---|---|
| `[NODE_ID]` | [Your Primary Machine Name] | Primary workstation — development, agent ops, KVM host | `[TAILSCALE_IP]` | primary |
| `[NODE_ID]` | [Secondary Node Name] | Secondary agent node — road use, Apple management, etc. | `[TAILSCALE_IP]` | active |
| `[NODE_ID]` | [Server Node Name] | Headless server — always-on, pipeline host | `[TAILSCALE_IP]` | always_on |
| `[NODE_ID]` | [Home Machine Name] | Smart home brain — sensors, robotics, local inference | `[TAILSCALE_IP]` | active |
| `[NODE_ID]` | [Mobile Command Name] | Mobile command — connects TO fleet, not a target | `[TAILSCALE_IP]` | mobile_command |

**Network fabric:** Tailscale overlay mesh. All nodes joined to the same Tailscale network.
**LAN subnet:** `[YOUR_LAN_SUBNET]` — verify with `ip addr`. Tailscale IPs are preferred for all agent ops.

---

## III. Primary Node as Hub

Your primary workstation is the operational anchor of the fleet.

- All Samba shares originate from the primary node
- Secondary VMs and agent nodes run on or connect through the primary node
- All tunneling and remote management routes through or from the primary node
- Your agent's primary instance runs here — this is where the project lives

**Rule:** Your agent does not work directly on remote machines. The agent tunnels in and manages from the primary node position. SSH for inspection and command execution only. Never persistent interactive sessions on remote nodes unless building or debugging that node.

---

## IV. Samba Architecture

The primary node runs Samba (smbd/nmbd) and exposes shares to secondary nodes and VMs. Define your shares here as you create them.

| Share Name | Source Path | Purpose |
|---|---|---|
| `SOVEREIGN_AGENCY` | `[absolute path to your SA folder]` | Primary SA workspace — canonical source of truth |
| `SHARED` | `[SA-relative: 4_SHARED_RESOURCES]` | Shared tooling and resources |
| `[SHARE_NAME]` | `[path]` | `[purpose]` |

**Rule:** SOVEREIGN_AGENCY is the canonical source of truth. Any sync mirrors are secondary. Never treat a mirror as authoritative.

---

## V. Agent Access Model

All agent SSH access uses key authentication. No passwords in flight.

- **Key:** `~/.ssh/[your_agent_key_name]` (ed25519 recommended)
- **Sudoers:** `/etc/sudoers.d/[your-agent-sudoers-file]` — NOPASSWD for operational efficiency
- **No credentials stored** in any project file — keys only, referenced by path hint

> ⚑ FIRST_BOOT: Your agent's SSH key name and sudoers file name are set during initial node configuration. Record them in `machines_registry.json → agent_access`.

Setup status per machine: see `machines_registry.json → agent_access.setup_status`.

---

## VI. Connectivity Rules

1. **Always use Tailscale IPs** for agent remote operations — stable across LAN and remote
2. **LAN IPs are fallback** — use only when Tailscale is unavailable; verify with `ip addr` before trusting
3. **NAT is fragile** — VM NAT interfaces are internet-only; do not rely on NAT for fleet connectivity
4. **Mobile command devices are controllers, not targets** — they connect TO fleet nodes; nothing connects back via SSH
5. **New nodes must join Tailscale** before being added to the fleet — Tailscale IP is the registration requirement

---

## VII. Expansion Protocol

When adding a new machine to the fleet:

1. Install Tailscale and join the mesh — record the assigned IP
2. Install SSH server, add your agent's public key to `~/.ssh/authorized_keys`
3. Configure NOPASSWD sudoers for the agent user
4. Add entry to `machines_registry.json`
5. Update `agent_access.setup_status`
6. If the machine will run an agent instance, create its node folder in `2_AGENT_DEFINITIONS/Main_Advisor/e.[node_name]/` and write its CLAUDE.md with the correct absolute SA root path

---

**WETGOLD**

`This document is a wet-gold README and must exist in .txt, .md, .pdf, .json, and .mmd (if applicable).`
