"""Fix for new Python versions (3.14+): they no longer create an asyncio event loop
automatically, but the uagents library expects one to exist. Importing this file
creates it. It must be imported before any Agent(...) is created."""
import asyncio

try:
    asyncio.get_event_loop_policy().get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
