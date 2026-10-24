"""Checks that your ASI:One key in .env works. Run: python test_key.py"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ASI1_API_KEY")

if not key:
    print("PROBLEM: ASI1_API_KEY is empty or the .env file was not found.")
    print("Make sure the file is named exactly .env (not .env.txt) and is in this folder.")
    raise SystemExit

print(f"Key found. Length: {len(key)} characters. Starts with: {key[:3]}...")
if key != key.strip() or '"' in key or "'" in key or " " in key:
    print("PROBLEM: the key has a space or quote mark in it. Remove them in .env.")
if "paste" in key.lower() or "your_" in key.lower():
    print("PROBLEM: this is still the placeholder text. Paste your real key.")

resp = requests.post(
    "https://api.asi1.ai/v1/chat/completions",
    headers={"Authorization": f"Bearer {key.strip()}"},
    json={"model": os.getenv("ASI1_MODEL", "asi1"),
          "messages": [{"role": "user", "content": "Say OK"}]},
    timeout=60,
)
print("Server replied with status:", resp.status_code)
if resp.status_code == 200:
    print("SUCCESS: your key works.")
else:
    print("Server said:", resp.text[:300])
    if resp.status_code == 401:
        print("401 means the key is wrong. Create a new key on asi1.ai and paste it in .env.")
