"""SUB-AGENT 3: rates how trustworthy each source is. Run: python source_checker_agent.py"""
import asyncio
import os

from dotenv import load_dotenv
import loopfix  # noqa: F401  (must come before any Agent is created)
from uagents import Agent, Context

from credibility import rate_sources
from models import SourceCheckRequest, SourceRating, SourceReport

load_dotenv()

agent = Agent(
    name="court_source_checker",
    seed=os.getenv("SOURCE_CHECKER_SEED", "change-me-court_source_checker"),
    port=8004,
    endpoint=["http://127.0.0.1:8004/submit"],
)


@agent.on_event("startup")
async def hello(ctx: Context):
    ctx.logger.info(f"Source checker ready. Address: {agent.address}")


@agent.on_message(model=SourceCheckRequest)
async def handle(ctx: Context, sender: str, msg: SourceCheckRequest):
    ctx.logger.info(f"Checking {len(msg.sources)} sources")
    try:
        rated = await asyncio.to_thread(rate_sources, msg.sources)
    except Exception as e:  # never leave the judge waiting
        ctx.logger.error(f"Source check failed: {e}")
        rated = {s: (3, "Could not be checked") for s in msg.sources}
    await ctx.send(sender, SourceReport(
        claim_id=msg.claim_id,
        ratings=[SourceRating(source=s, score=v[0], reason=v[1]) for s, v in rated.items()],
    ))


if __name__ == "__main__":
    agent.run()
