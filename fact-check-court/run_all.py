"""Starts all four agents with one command: python run_all.py  (Ctrl+C stops them)."""
import subprocess
import sys
import time

# The judge starts last, so the sub-agents are ready when it is.
SCRIPTS = [
    "prosecutor_agent.py",
    "defender_agent.py",
    "source_checker_agent.py",
    "judge_agent.py",
]

procs = []
try:
    for script in SCRIPTS:
        procs.append(subprocess.Popen([sys.executable, script]))
        time.sleep(2)  # let each one start before the next
    for p in procs:
        p.wait()
except KeyboardInterrupt:
    pass
finally:
    for p in procs:
        p.terminate()
