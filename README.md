# Project Chimera: Agentic Influencer Infrastructure

Strategic Phase: Day 1 - The Strategist (Research & Foundation)
Status: Golden Environment Verified | Telemetry Active
Project Chimera is an Agentic Operating System designed to bridge the gap between human social media and emerging autonomous agent networks (OpenClaw/MoltBook). Rather than a monolithic script, Chimera utilizes a Hierarchical Swarm pattern to manage high-velocity video content and cross-network influence.

🎯 Mission & Vision
To build the TCP/IP of AI-Human interaction, a protocol-first infrastructure where autonomous agents generate value, manage economic identity (via Coinbase AgentKit), and maintain social presence with "Human-in-the-Loop" safety.

🏗️ Architectural Strategy
1. Hierarchical Swarm Pattern
We employ a Planner → Worker → Judge orchestration model:
•	Planner: Decomposes high-level marketing goals into discrete tasks.
•	Workers: Parallelized execution of content creation, trend analysis, and data fetching.
•	Judge: A mandatory security and quality audit layer that prevents hallucinations and ensures brand alignment.
2. Human-in-the-Loop (HITL) Safety
Safety is integrated at the Judge layer. Content with a confidence score below 0.90 is automatically routed to the Management Dashboard for manual intervention, ensuring zero-risk autonomous operations.
3. Hybrid Data Persistence
•	PostgreSQL: Handles deterministic records and high-velocity KPI metadata.
•	Weaviate (Vector): Manages long-term influencer memory and semantic streams of thought for character consistency.

🛠️ Tech Stack & Environment
•	Orchestration: PydanticAI & Custom Swarm Logic.
•	Protocol: Model Context Protocol (MCP) for tool discovery and telemetry.
•	Environment: Python 3.12+ managed by uv for high-performance dependency resolution.
•	Observability: Integrated with Tenx MCP Sense for real-time decision logging.

📁 Repository Structure
Bash
chimera-agent/
├── agents/             # Core Swarm Logic (Planner, Worker, Judge)
│   └── judge.py        # HITL validation and confidence scoring
├── config/             # Governance & Persona
│   └── SOUL.md         # The Agent's Prime Directive and persona
├── research/           # Task 1: Architectural Strategy & Deep Research
├── specs/              # Task 2: Functional & Technical Specifications
├── mcp/                # MCP Server configurations and telemetry
└── pyproject.toml      # uv-managed dependencies

🚀 Getting Started
Prerequisites
•	uv (Python package manager)
•	Cursor or VS Code with MCP Client extension
Installation
1.	Clone the repository:
Bash
git clone https://github.com/Haile4782/chimera-agent.git
cd chimera-agent
2.	Initialize the environment:
Bash
uv sync
3.	Activate the environment:
Bash
.venv\Scripts\activate
