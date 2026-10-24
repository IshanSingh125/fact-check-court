# Fact-Check Court: Complete Beginner Setup Guide

Follow the parts in order. Don't skip ahead. Each part ends with a "✅ You're done when" line so you know it worked.

**Words you'll see**
- **Terminal:** a text window where you type commands. Nothing scary: you type a line, press Enter.
- **Folder:** the place on your computer where all the project files live.
- **API key:** a long secret password that lets your program use a service (like ASI:One).
- **Agent:** a small program that does one job and can send messages to other agents.

---

## Part 1: Get the files in one folder (5 min)

1. Create a new folder on your Desktop called `fact-check-court`.
2. Put ALL the files I sent you inside it. No sub-folders. You should see:

| Type | Files |
|---|---|
| Agents (you run these) | `judge_agent.py`, `prosecutor_agent.py`, `defender_agent.py`, `source_checker_agent.py` |
| Helpers | `debater.py`, `credibility.py`, `jev.py`, `asi.py`, `search.py`, `models.py` |
| Setup | `run_all.py`, `requirements.txt`, `.env.example`, `README.md`, `SETUP_GUIDE.md` |

3. If `.env.example` is missing, that's normal: files starting with a dot are often hidden or not downloaded. You'll create the file yourself in Part 5.

✅ You're done when: one folder contains all the `.py` files.

---

## Part 2: Install the tools (15 min)

### 2a. Python (the language the agents are written in)
1. Go to **python.org/downloads** and download the newest Python 3 (3.10 or higher).
2. Run the installer.
   - **Windows:** on the first screen, TICK the box **"Add Python to PATH"**, then click Install Now. This is the most common beginner mistake.
   - **Mac:** just click through the installer.
3. Check it worked (see Part 3 for how to open a terminal, then type):
   - Windows: `python --version`
   - Mac: `python3 --version`
   - You should see something like `Python 3.12.1`.

### 2b. A text editor (optional but very helpful)
Install **Visual Studio Code** (free) from **code.visualstudio.com**. It makes editing the `.env` file and reading code much easier. Then in VS Code: File → Open Folder → pick `fact-check-court`.

✅ You're done when: the Python version command prints a number.

---

## Part 3: Open a terminal inside your folder (2 min)

- **Windows:** open the `fact-check-court` folder in File Explorer, click the address bar at the top, type `cmd`, press Enter. A black window opens.
- **Mac:** in Finder, right-click the folder → **New Terminal at Folder**. (If you don't see it: System Settings → Keyboard → Keyboard Shortcuts → Services → turn on "New Terminal at Folder".)
- **In VS Code:** menu Terminal → New Terminal.

**Use Command Prompt (`cmd`) on Windows, not PowerShell.** PowerShell often blocks the next step.

To check you're in the right place, type `dir` (Windows) or `ls` (Mac) and press Enter. You should see your `.py` files listed.

✅ You're done when: the terminal lists your project files.

---

## Part 4: Create a private Python environment and install libraries (5 min)

A "virtual environment" is a clean box for this project's libraries, so nothing clashes with other things on your computer.

**Windows (cmd):**
```
python -m venv .venv
.venv\Scripts\activate
```
**Mac:**
```
python3 -m venv .venv
source .venv/bin/activate
```
After this, you should see `(.venv)` at the start of your terminal line. That means it's active.

Now install the libraries (works the same on both):
```
pip install -r requirements.txt
```
Wait a few minutes while it downloads. Lots of text scrolling is normal.

**Important:** every time you open a NEW terminal later, repeat only the "activate" line (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` on Mac) before running anything.

✅ You're done when: the install finishes without a red "ERROR" at the end.

---

## Part 5: Get your keys and fill in the `.env` file (10 min)

### 5a. ASI:One API key (required)
1. Go to **asi1.ai** and sign in or create an account.
2. Look for a **Developer** / **API keys** section (usually in your profile or account menu) and create a key. Copy it.
3. If you can't find it, search "ASI:One API key" in the Fetch.ai docs at innovationlab.fetch.ai.

### 5b. Jev key (optional)
Jev is the extra decision model. You can skip this and the project still works.
1. Make an account at **edenai.co** and create an API key.

### 5c. Create the `.env` file
This file holds your secrets. It must be named exactly `.env` and sit in the project folder.

- **Easiest (VS Code):** right-click in the file list → New File → name it `.env` → paste the text below.
- **Windows without VS Code:** open Notepad, paste the text, then File → Save As, change "Save as type" to **All Files**, name it `.env`, save inside your folder.
- **Mac:** open the Terminal in your folder and run `cp .env.example .env`, then open `.env` in any editor. If `.env.example` is missing, use TextEdit → Format → Make Plain Text, and save as `.env`.

Paste and fill this in:
```
ASI1_API_KEY=paste_your_asi_one_key_here
ASI1_MODEL=asi1

EDENAI_API_KEY=
JEV_MODEL=typesafe/jev-latest

JUDGE_SEED=my-judge-secret-phrase-banana-rocket-4821
PROSECUTOR_SEED=my-prosecutor-secret-phrase-purple-tiger-9937
DEFENDER_SEED=my-defender-secret-phrase-silver-comet-2204
SOURCE_CHECKER_SEED=my-checker-secret-phrase-green-falcon-7715
```
- No spaces around the `=` sign and no quote marks.
- The four SEED lines: make up your OWN long phrases. They must all be different. A seed decides an agent's permanent address, so don't change them later or the addresses change.
- Leave `EDENAI_API_KEY=` empty to skip Jev.

✅ You're done when: `.env` exists in the folder with your ASI:One key pasted in.

---

## Part 6: Run the agents (5 min)

Make sure `(.venv)` shows in your terminal, then:
```
python run_all.py
```
This starts all four agents. You'll see lines of text from each. Look for:
- `Source checker ready. Address: agent1q...`
- `prosecution ready. Address: agent1q...` and `defense ready. Address: agent1q...`
- From the Judge: a line about an **Agent inspector** with a long link starting with `https://agentverse.ai/inspect/...`

**Copy and save all four `agent1q...` addresses somewhere.** You need them for the README later.

To stop everything: click the terminal and press **Ctrl + C**.

If it fails, jump to the Troubleshooting part at the bottom.

✅ You're done when: all four agents are printing text and you can see the inspector link.

---

## Part 7: Connect the Judge to Agentverse (10 min)

This is what makes your agent appear online so ASI:One can reach it.

1. Copy the **Agent inspector** link from the Judge's output and open it in your browser.
2. Sign in to Agentverse if asked (you can use the same account type you used for ASI:One, or create one at agentverse.ai).
3. Click **Connect**, then choose **Mailbox**, then finish/confirm.
4. Go to **agentverse.ai** → your **Agents** page → look under **Local Agents**. You should see `court_judge`.
5. Open it and give it a clear **description/README**. Something like: "Fact-Check Court: send any claim and a prosecutor, defender and source checker agent will investigate it and a judge gives a verdict with sources." Good descriptions help ASI:One find your agent.

✅ You're done when: the Judge appears in your Agentverse agents list and shows as connected.

---

## Part 8: Test it in ASI:One chat (10 min)

1. On the Judge's Agentverse page, click **Chat with Agent** (this opens it in ASI:One). If you don't see it, go to asi1.ai and find your agent by name.
2. Send: `Humans only use 10% of their brains`
3. Watch the messages arrive: "Court is in session", then "Cross-examination under way", then the verdict.
4. Send the same claim again. It should reply instantly with "🧠 already ruled".
5. Send `recheck Humans only use 10% of their brains` to force a new trial.
6. Try a few more: a true claim ("Water boils at 100°C at sea level"), a false one, and a nonsense one, to see how it behaves.

Keep your computer on and `run_all.py` running the whole time you test.

✅ You're done when: you get a full verdict with sources and star ratings.

---

## Part 9: Put the project on GitHub (15 min)

The hackathon needs a public GitHub repository.

1. Create a free account at **github.com**.
2. Click **+** (top right) → **New repository**. Name it `fact-check-court`. Set it to **Public**. Click Create.
3. On the next page click **"uploading an existing file"**.
4. Drag in ALL your project files.
   - **DO NOT upload `.env`** (it contains your secret keys).
   - **DO NOT upload the `.venv` folder.**
   - You can upload `.env.example` (it has no secrets).
5. Click **Commit changes**.
6. Optional but smart: create a file called `.gitignore` in the repo with these three lines, so secrets and junk are never added by accident:
```
.env
.venv/
__pycache__/
```
If you ever upload `.env` by mistake: delete it from GitHub AND make new API keys, because the old ones are now exposed.

### README requirements from the hackathon
Your `README.md` must include:
- Each agent's **name and address** (the four `agent1q...` addresses from Part 6).
- The **innovationlab badge** and the **hackathon badge**. Copy the exact badge lines from the hackathon's hackpack page: **fetch.ai/events/hackathons/fetch-a-thon-3/hackpack**.
- Links to any extra resources needed to run it (ASI:One, Eden AI).

You can edit README.md directly on GitHub (click the pencil icon).

✅ You're done when: your repo is public, has no `.env`, and the README lists agent names and addresses.

---

## Part 10: Submission checklist (Devpost)

- [ ] **Public ASI:One shared chat URL** showing a complete trial (use the Share option in the ASI:One chat).
- [ ] **Agentverse agent profile URL** for each agent you submit (the Judge at minimum).
- [ ] **Public GitHub repo URL**.
- [ ] **Demo video, 3 to 5 minutes.**
- [ ] **Short description:** the problem (misinformation spreads fast), target users (students, families, anyone getting forwards), and the outcome (a sourced verdict in seconds).

### Demo video plan (about 4 minutes)
1. (30 sec) The problem: a viral false forward.
2. (30 sec) Your solution and the four agents (show a simple diagram).
3. (90 sec) Live trial in ASI:One: send a claim, show the verdict, sources and stars.
4. (30 sec) Send it again to show memory.
5. (30 sec) How it works: agents talking, ASI:One reasoning, Jev deciding.
6. (30 sec) What's next.

Before you record: test 3 claims in advance, pick the best one, close other windows, and record the screen with your phone's or computer's built-in screen recorder.

**Check the deadline.** The pages I found didn't state a submission deadline (only October 24). Look at your Devpost page or the event dashboard, or ask the organizers.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'python' is not recognized` (Windows) | Reinstall Python and tick "Add Python to PATH". Close and reopen the terminal. |
| `command not found: python` (Mac) | Use `python3` instead, or activate the environment first. |
| `No module named 'uagents'` (or any module) | You forgot to activate the environment, or the install failed. Run the activate line, then `pip install -r requirements.txt` again. |
| Nothing prints / `.venv` activate fails in PowerShell | Use Command Prompt (`cmd`) instead. |
| `401` or "unauthorized" errors | Your ASI:One key is wrong or has spaces/quotes around it. Fix `.env`. |
| ASI:One rejects the model name | Change `ASI1_MODEL` in `.env` to a model name listed in the ASI:One API docs. |
| Port already in use | An old copy is still running. Close all terminals, or restart your computer, then run again. |
| "did not respond in time" in the verdict | One of the sub-agents isn't running. Check each agent printed its "ready" line. Run `python run_all.py` again. |
| Every search is empty | Your network may block DuckDuckGo. Try a different network, such as a phone hotspot. |
| Jev errors in the output | Jev's service is in alpha. Clear `EDENAI_API_KEY` in `.env` to run without it. |
| Judge doesn't appear in Agentverse | Redo Part 7. Make sure you chose **Mailbox** and the Judge is still running. |
| Changes to `.env` have no effect | Stop (Ctrl+C) and run `python run_all.py` again. |

If you get stuck, copy the last 20 lines from your terminal and send them to me. The exact error message is what I need.

---

## Part 11: Keeping it working

- Your agents only work while your computer is on, connected to the internet, and `run_all.py` is running. Keep it running during judging.
- Don't change the SEED lines after you've submitted, or all addresses change.
- The reasoning and ranking come from ASI:One, the verdict from Jev (if turned on), and the connection between everything from Agentverse.
