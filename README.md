# ⚖️ Fact-Check Court

> **Don't forward it. Cross-examine it.**

![tag : innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

Built for **Fetch-A-Thon 3.0 (ASI:One Agent Challenge)** by a student team from RIT Roorkee.

Send a claim (like a WhatsApp forward) to the agent on ASI:One. Four AI agents hold a trial: one argues the claim is false, one argues it is true, one rates how trustworthy the sources are, and a judge gives a sourced verdict.

## Why

Viral claims spread faster than people can check them. Checking by hand means opening many tabs and judging sources yourself, and a single chatbot gives one confident answer without showing the other side. Fact-Check Court shows **both sides**, **cross-examines them**, and **scores the sources** before ruling. It needs no app, website or sign-up: you just chat on ASI:One.

## 🔗 Links

| What | Link |
|---|---|
| ASI:One shared chat (full trial) | https://asi1.ai/invite?channelInviteKey=N8J-0GmPDq4S0zmds59QA3_lYrhLLQYzs137bO_pWKk&utm_source=share&utm_medium=desktop&utm_campaign=channel_invite |
| Agentverse profile (Judge) | https://agentverse.ai/agents/details/agent1qdk6twggelew38y36zq20ux4vzexzunu0jhm7fckxjqhqax7m39c22mhe8j/profile |
| Demo video | `TODO: paste link` |

## 🤖 The agents

| Agent | File | Port | Job | Address |
|---|---|---|---|---|
| **Judge** (main) | `judge_agent.py` | 8001 | Chats with the user on ASI:One (Agent Chat Protocol + Agentverse mailbox), runs the trial, gives the verdict | agent1qdk6twggelew38y36zq20ux4vzexzunu0jhm7fckxjqhqax7m39c22mhe8j|
| **Prosecutor** | `prosecutor_agent.py` | 8002 | Searches and reads the web for evidence the claim is **false** | agent1q0kqhpn55antp2nksau4h3mpeymaw0yrw0ns57euqfnslp4vhlq0gtyf5sa |
| **Defender** | `defender_agent.py` | 8003 | Searches and reads the web for evidence the claim is **true** | agent1qv4nvwm5gy3jp4m8hm744r7762zz303sh5ea9n0ys5u5srpf06pjkvwj63v |
| **Source Checker** | `source_checker_agent.py` | 8004 | Rates every source from 1 to 5 stars |  agent1qwx863uc36xtnxp3n3ds9jae8uz35kfumg24gc2k5axrfx788jmnqlqkfys |

> Addresses are printed when each agent starts (`... ready. Address: agent1q...`). They depend on your seed phrases, so don't change the seeds after publishing.

## ⚙️ How a trial works

```
User (ASI:One)
   │  claim
   ▼
 Judge ──────────────► Prosecutor ┐  Stage 1: opening statements
   │  (in parallel)  ► Defender   ┘  (search + read top pages)
   │
   ├─► each lawyer rebuts the other ┐  Stage 2: cross-examination
   └─► Source Checker rates sources ┘  (all in parallel)
   │
   ▼
 Verdict + confidence + sources + star ratings
```

0. **Memory:** if the court ruled on this claim in the last 7 days, the Judge replies instantly. Send `recheck <claim>` for a fresh trial.
1. **Opening statements:** Prosecutor and Defender research at the same time. Each runs a web search (DuckDuckGo, no API key) and reads the text of the top 2 pages.
2. **Cross-examination + source check:** each lawyer rebuts the other, while the Source Checker rates every source (up to 8). All at the same time.
3. **Verdict:** ASI:One writes the reasoning and the Judge weighs arguments, rebuttals and source scores. If Jev is set up (optional), it makes the final call.

Agents talk to each other through typed messages defined in `models.py`.

## ✨ What makes it different

- **Adversarial debate:** both sides are argued, not one confident answer.
- **Cross-examination:** each side rebuts the other before the ruling.
- **Source credibility:** known sites are scored by rules (government and universities 5, established news and fact-checkers 4, social media 1). Unknown sites are scored by ASI:One, defaulting to 3. Higher-scored sources count for more.
- **Reads real pages,** not just search snippets.
- **No made-up links:** every source shown comes from real search results, never from the LLM.
- **Memory:** repeat claims are answered instantly; unverified results are not remembered.

## 🛡️ Reliability

- If a sub-agent is slow or down, the Judge waits 45 seconds per stage, then rules with what it has.
- If search finds nothing, the verdict is **Unverified** instead of a guess.
- Search results, arguments and domain names are treated as **data, never instructions**.
- Failed AI calls fall back to safe defaults, so the Judge is never left waiting.

## 🧰 Fetch.ai technology used

- **uAgents:** four independent agents, each with its own address and typed messages.
- **Agentverse mailbox:** connects the Judge so ASI:One can reach it.
- **Agent Chat Protocol:** makes the Judge chattable and discoverable on ASI:One.
- **ASI:One LLM:** writes arguments, rebuttals and verdict reasoning.
- **Multi-agent orchestration:** parallel messages, timeouts and fallbacks.

## 🚀 Quick start

Full beginner walkthrough: see [`SETUP_GUIDE_2.md`](SETUP_GUIDE_2.md).

1. Install **Python 3.10+**.
2. Create and activate a virtual environment:
   - Mac/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
3. Install the libraries: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill it in:
   ```
   ASI1_API_KEY=your_asi_one_key      # from https://asi1.ai
   ASI1_MODEL=asi1

   EDENAI_API_KEY=                    # optional, turns on Jev
   JEV_MODEL=typesafe/jev-latest

   JUDGE_SEED=any-long-unique-phrase
   PROSECUTOR_SEED=another-long-unique-phrase
   DEFENDER_SEED=a-third-long-unique-phrase
   SOURCE_CHECKER_SEED=a-fourth-long-unique-phrase
   ```
5. (Optional) check your key: `python test_key.py`
6. Start all four agents: `python run_all.py` (Ctrl+C stops them), or run each `*_agent.py` in its own terminal.

### Connect the Judge to ASI:One

1. Open the **Agent inspector** link printed by the Judge.
2. Click **Connect → Mailbox**.
3. On [agentverse.ai](https://agentverse.ai), open the Judge's profile, add a description, then click **Chat with Agent**.

### Optional: Jev

[Jev](https://www.edenai.co) is a decision model (by TypeSafe AI, served through Eden AI) that can make the final verdict while ASI:One writes the reasoning. Add `EDENAI_API_KEY` to `.env` to turn it on. Without it, the Judge uses ASI:One's verdict. Jev's endpoint is in alpha; all Jev code is in `jev.py`.

## 💬 Try it

- `Humans only use 10% of their brains`
- `Drinking hot water cures the flu`
- `Water boils at 100°C at sea level`
- Ask the same claim twice to see memory work, then `recheck <claim>` for a new trial.

## 🗂️ Project structure

```
judge_agent.py            Main agent: chat, trial stages, verdict
prosecutor_agent.py       Sub-agent: argues the claim is false
defender_agent.py         Sub-agent: argues the claim is true
source_checker_agent.py   Sub-agent: rates source trustworthiness
debater.py                Shared code for prosecutor and defender
credibility.py            Rule-based + LLM source scoring
search.py                 Web search and page reading
asi.py                    ASI:One LLM helper (returns JSON)
jev.py                    Optional Jev decision-model adapter
models.py                 Typed messages between agents
loopfix.py                asyncio fix for Python 3.14+
run_all.py                Starts all four agents
test_key.py               Checks your ASI:One key
```

## ⚠️ Limitations

- It relies on web search results and an LLM, so it can be wrong. **Always double-check important claims yourself.** It is not professional (medical, legal) advice.
- Agents currently run from a laptop, so they only work while `run_all.py` is running.
- Mostly English claims for now.

## 🗺️ Roadmap (planned, not built yet)

- Host the agents in the cloud so they run 24/7
- Hindi and other Indian languages
- Interactive cards for a richer verdict
- WhatsApp / Telegram bridge
- Payment Protocol for a paid tier

## 🩹 Troubleshooting

- **"did not respond in time":** make sure every agent's terminal printed its "ready" line.
- **401 / unauthorized:** your ASI:One key is wrong or has spaces/quotes around it. Run `python test_key.py`.
- **ASI:One rejects the model name:** change `ASI1_MODEL` in `.env`.
- **Every search is empty:** your network may block DuckDuckGo. Try another network.
- **Clear memory:** delete the Judge's saved data file (named like `court_judge_data.json`).

## 👥 Team

| Name | Role |
| Ishan Singh | Team Lead |
| Utkarsh Kumar | Debugging |
| Dharna Tyagi | Presentation Maker |
| Sudhanshu Tiwari | 

RIT Roorkee (Roorkee Institute of Technology)

## 🙏 Built with

[Fetch.ai uAgents](https://github.com/fetchai/uAgents) · [Agentverse](https://agentverse.ai) · [ASI:One](https://asi1.ai) · [Eden AI](https://www.edenai.co) · [ddgs](https://pypi.org/project/ddgs/) · [trafilatura](https://trafilatura.readthedocs.io/)

---

