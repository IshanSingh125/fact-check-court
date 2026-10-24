"""SUB-AGENT 2: argues the claim is true. Run: python defender_agent.py"""
from debater import build_debater

agent = build_debater("court_defender", "DEFENDER_SEED", 8003, "defense")

if __name__ == "__main__":
    agent.run()
