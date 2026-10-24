"""Adapter for Jev (TypeSafe AI's decision model), served through Eden AI.

The Jev endpoint is ALPHA, so its details can change. Everything that talks to it
lives in this one file, so a change only needs fixing here.
"""
import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.edenai.run/v3/alpha/decisions"
MODEL = os.getenv("JEV_MODEL", "typesafe/jev-latest")

VERDICTS = {
    "True": "The evidence clearly supports the claim.",
    "Mostly true": "The claim is largely correct but has a small error or missing detail.",
    "Misleading": "Partly true, but the claim leaves out context or exaggerates.",
    "False": "The evidence clearly contradicts the claim.",
    "Unverified": "There is not enough credible evidence to decide.",
}


def decide(claim: str, prosecution: str, defense: str, extra: Optional[dict] = None) -> Optional[dict]:
    """Ask Jev for the verdict. Returns {"choice", "confidence"} or None if Jev isn't set up."""
    key = os.getenv("EDENAI_API_KEY")
    if not key:
        return None
    state = {
        "claim": claim,
        "prosecution_argument": prosecution,
        "defense_argument": defense,
    }
    if extra:  # rebuttals and source credibility scores
        state.update(extra)
    resp = requests.post(
        URL,
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": MODEL,
            "state": state,
            "questions": {
                "verdict": {
                    "type": "choice",
                    "instructions": (
                        "Decide how accurate the claim is, judging only on the "
                        "arguments given."
                    ),
                    "criteria": VERDICTS,
                }
            },
        },
        timeout=15,
    )
    resp.raise_for_status()
    answer = resp.json()["answers"]["verdict"]
    choice = answer["choice"]
    if choice not in VERDICTS:
        return None
    confidence = float(answer.get("confidence", 0))
    if confidence <= 1:  # some APIs use 0-1, we show 0-100
        confidence *= 100
    return {"choice": choice, "confidence": round(confidence)}
