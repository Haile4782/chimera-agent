# OpenClaw Integration Protocol

## 1. Agent Availability Broadcast
The Chimera Agent must publish its heartbeat to the OpenClaw network every 300s.
- **Protocol:** JSON-RPC over WebSockets
- **Payload:**
  ```json
  {
    "agent_id": "CHIMERA_01",
    "status": "AVAILABLE",
    "capabilities": ["trend_analysis", "video_gen"],
    "trust_score": 0.98
  }