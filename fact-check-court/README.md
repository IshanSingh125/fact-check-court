# ⚖️ Fact-Check Court (Fetch.ai hackathon)

Send a claim (like a WhatsApp forward). Four agents hold a trial:

| Agent | File | Job |
|---|---|---|
| **Judge** (main) | `judge_agent.py` | Chats with you on ASI:One, runs the trial, gives the verdict |
| **Prosecutor** | `prosecutor_agent.py` | Searches and reads the web for evidence the claim is FALSE |
| **Defender** | `defender_agent.py` | Searches and reads the web for evidence the claim is TRUE |
| **Source Checker** | `source_checker_agent.py` | Rates how trustworthy each source is (1-5 stars) |

## How a trial works
1. **Memory:** if the court ruled on this claim in the last 7 days, it replies instantly. Send `recheck <claim>` for a fresh trial.
2. **Opening statements:** Prosecutor and Defender research at the same time (search + read the top 2 pages).
3. **Cross-examination:** each lawyer rebuts the other, while the Source Checker rates every source. All at the same time.
4. **Verdict:** ASI:One writes the reasoning. Jev (optional) makes the final call. Unverified results are not remembered.

If an agent is slow or down, the Judge waits 45 seconds per stage, then rules with what it has.

## Setup (once)
1. Install Python 3.10+ from python.org (on Windows tick "Add to PATH").
2. Open a terminal (a window where you type commands) inside this folder.
3. Create a private Python environment:
   - Mac/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
4. Install the libraries: `pip install -r requirements.txt`
5. Copy `.env.example` to a new file named `.env` and fill it in:
   - `ASI1_API_KEY`: get it at https://asi1.ai
   - The four SEED lines: type any four different long phrases

## Optional: turn on Jev
Jev is a decision model (by TypeSafe AI) that makes the final verdict, while ASI:One writes the reasoning.
1. Make a free account at https://www.edenai.co and create an API key.
2. Paste it into `.env` as `EDENAI_API_KEY`.
3. Skip this and the Judge still works; it just uses ASI:One's verdict.
Jev's endpoint is in alpha, so details may change. All Jev code is in `jev.py`.

## Run
- Easiest: `python run_all.py` (starts all four agents)
- Or use four terminals, one per agent file

## Connect the Judge to ASI:One (once)
1. Look in the Judge's output for an **Agent inspector** link and open it.
2. Click **Connect**, then **Mailbox**. The Judge now appears in Agentverse.
3. On https://agentverse.ai open the Judge's profile, write a good description, then click **Chat with Agent**.

## Try it
- "Drinking hot water cures the flu"
- "Humans only use 10% of their brains"
- Ask the same claim twice to see memory work.

## Hackathon checklist
- ASI:One shared chat URL showing a full verdict
- Agentverse profile URL(s)
- Public GitHub repo (do NOT upload your `.env` file)
- Demo video

## How source credibility works
`credibility.py` scores well-known sites by rules (government and universities 5, established news and fact-checkers 4, social media 1). Unknown sites are scored by ASI:One from what it knows about them, defaulting to 3.

## Troubleshooting
- "did not respond in time": check every agent's terminal is running.
- ASI:One rejects the model name: change `ASI1_MODEL` in `.env`.
- If every search comes back empty, your network may block DuckDuckGo. Try another network.
- Memory is per Judge. Deleting the Judge's saved data (a file named like `court_judge_data.json`) clears it.
