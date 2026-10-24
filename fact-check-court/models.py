from typing import List

from uagents import Model


# ---- Round 1: opening statements -------------------------------------------
class ClaimRequest(Model):
    """Judge -> Prosecutor / Defender."""
    claim_id: str
    claim: str


class Argument(Model):
    """Prosecutor / Defender -> Judge."""
    claim_id: str
    side: str  # "prosecution" or "defense"
    argument: str
    sources: List[str]  # each one looks like "Title - https://url"


# ---- Round 2: cross-examination --------------------------------------------
class RebuttalRequest(Model):
    """Judge -> Prosecutor / Defender: here is what the other side said."""
    claim_id: str
    claim: str
    own_argument: str
    opponent_argument: str


class Rebuttal(Model):
    """Prosecutor / Defender -> Judge."""
    claim_id: str
    side: str
    rebuttal: str


# ---- Source checking ---------------------------------------------------------
class SourceCheckRequest(Model):
    """Judge -> Source Checker."""
    claim_id: str
    sources: List[str]


class SourceRating(Model):
    source: str  # exactly as it was sent
    score: int  # 1 (unreliable) to 5 (very reliable)
    reason: str


class SourceReport(Model):
    """Source Checker -> Judge."""
    claim_id: str
    ratings: List[SourceRating]
