"""Tiny helper to call the ASI:One LLM and get JSON back."""
import json
import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.asi1.ai/v1/chat/completions"
MODEL = os.getenv("ASI1_MODEL", "asi1")


def ask_json(system: str, user: str) -> dict:
    """Ask ASI:One and parse the reply as JSON. Returns {} if parsing fails."""
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {os.getenv('ASI1_API_KEY')}"},
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.2,
        },
        timeout=60,
    )
    resp.raise_for_status()
    text = resp.json()["choices"][0]["message"]["content"]
    match = re.search(r"\{.*\}", text, re.DOTALL)  # grab the JSON object
    try:
        return json.loads(match.group(0)) if match else {}
    except json.JSONDecodeError:
        return {}
