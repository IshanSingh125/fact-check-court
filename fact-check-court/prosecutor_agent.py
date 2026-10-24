"""SUB-AGENT 1: argues the claim is false/misleading. Run: python prosecutor_agent.py"""
from debater import build_debater

agent = build_debater("court_prosecutor", "PROSECUTOR_SEED", 8002, "prosecution")

if __name__ == "__main__":
    agent.run()
