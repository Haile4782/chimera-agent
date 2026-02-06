# Project Chimera: Agentic Influencer Infrastructure 🚀

## 🛡️ Strategic Phase: Day 3 - The Governor (Infrastructure & Governance)
**Status:** Unified Main Branch | CI/CD Active | MCP Telemetry Online

Project Chimera is an **Agentic Operating System** designed to bridge the gap between human social media and emerging autonomous agent networks (OpenClaw/MoltBook). Utilizing a **Hierarchical swarm pattern**, Chimera manages high-velocity content and cross-network influence with strict engineering governance.

## 🎯 Mission & Vision
To architect the TCP/IP of AI-Human interaction a protocol-first infrastructure where autonomous agents generate value, manage economic identity (via Coinbase AgentKit), and maintain social presence with **Human-in-the-Loop (HITL)** safety.

## 🏗️ Architectural Strategy

### **Hierarchical Swarm Pattern (Planner → Worker → Judge)**
Chimera bypasses fragile vibe-coding in favor of a robust orchestration model:
* **Planner:** Decomposes marketing goals into executable agentic tasks.
* **Workers:** Parallelized execution of content generation and trend analysis.
* **Judge:** A mandatory quality audit layer enforcing brand alignment and safety.


### **Governance & Spec-Driven Development (SDD)**
We adhere to **SDD principles**, where Intent (Specs) is the source of truth.
* **Truth:** Code is validated against 'specs/technical.md' and 'specs/functional.md'.
* **Safety Net:** A TDD approach ensures the factory rejects non-compliant implementations.
* **AI Oversight:** Integrated **CodeRabbit AI** for automated PR reviews and security auditing.

## 🛠️ Tech Stack & Environment
* **Orchestration:** PydanticAI & Swarm Logic.
* **Protocol:** Model Context Protocol (MCP) via **Tenx MCP Sense** for real-time observability.
* **Environment:** Python 3.11 managed by **uv** for high-performance dependency resolution.
* **CI/CD:** GitHub Actions enforcing linting, security scans, and spec-validation.

## 📁 Repository Structure
```bash
chimera-agent/
├── .cursor/          # IDE Context Rules & MCP configuration
├── .github/          # CI/CD Governance Pipeline (main.yml)
├── agents/           # Core Swarm Logic (Planner, Worker, Judge)
├── config/           # Governance & Persona Definitions
├── research/         # Domain Architecture & Strategy Documentation
├── skills/           # Agentic Capabilities (Youtube, Transcription, etc.)
├── specs/            # Master, Functional, and Technical Specifications
├── tests/            # TDD Safety Net (Validated failing tests)
├── Dockerfile        # Multi-stage production-ready container
└── Makefile          # The Orchestrator's standard command interface
```

## 🚀 Getting Started

Prerequisites
  • uv (Python package manager)
  • Docker Desktop (for containerized validation)
  • Tenx MCP Sense (Connected for telemetry logging)
Installation & Validation
  1. Clone & Sync:
      git clone https://github.com/Haile4782/chimera-agent.git
      cd chimera-agent
      uv sync
  2. Run TDD Safety Net:
      uv run pytest tests/ -v
  3. Run via Orchestrator Interface:
      make test
      make spec-check
  4. Containerized Execution:
      docker build -t chimera-agent .
      docker run chimera-agent
	  
Lead Architect: [Haiyleyesus Abayneh]

Project: 10Academy Project Chimera Challenge (Feb 2026)