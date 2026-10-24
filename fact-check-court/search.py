"""Web research for the Prosecutor and Defender:
1) free search (no API key), 2) read the full text of the top pages."""
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List
from urllib.parse import urlparse

import requests

MAX_DOWNLOAD_BYTES = 1_000_000  # never download more than ~1 MB per page
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; FactCheckCourt/1.0)"}


def web_search(query: str, n: int = 5) -> List[Dict[str, str]]:
    """Return up to n results as {"title", "url", "snippet"}. Empty list on any failure."""
    try:
        from ddgs import DDGS

        results = DDGS().text(query, max_results=n)
        return [
            {"title": r.get("title", ""), "url": r.get("href", ""), "snippet": r.get("body", "")}
            for r in results
        ]
    except Exception:
        return []


def fetch_page_text(url: str, max_chars: int = 3000) -> str:
    """Download a web page and return just its article text (cut to max_chars).
    Returns "" if anything goes wrong, so the caller can fall back to the snippet."""
    try:
        if urlparse(url).scheme not in ("http", "https"):
            return ""
        with requests.get(url, headers=HEADERS, timeout=8, stream=True) as resp:
            resp.raise_for_status()
            if "html" not in resp.headers.get("Content-Type", "").lower():
                return ""  # skip PDFs, images, etc.
            raw = resp.raw.read(MAX_DOWNLOAD_BYTES, decode_content=True)
        import trafilatura

        html = raw.decode(resp.encoding or "utf-8", errors="ignore")
        text = trafilatura.extract(html) or ""
        return text.strip()[:max_chars]
    except Exception:
        return ""


def research(query: str, n: int = 5, read_top: int = 2) -> List[Dict[str, str]]:
    """Search, then read the top `read_top` pages at the same time.
    Each result gets a "page" field (article text, or "" if it couldn't be read)."""
    results = web_search(query, n)
    for r in results:
        r["page"] = ""
    to_read = results[:read_top]
    if to_read:
        with ThreadPoolExecutor(max_workers=read_top) as pool:
            for r, text in zip(to_read, pool.map(lambda r: fetch_page_text(r["url"]), to_read)):
                r["page"] = text
    return results
