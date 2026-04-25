"""
CF Worker uprot fallback.

Optional auto-resolve path for `extractors.uprot.bypass_uprot`. When the
local `uprot.txt` cookies are missing or stale, calling the CF Worker
returns a resolved MaxStream URL using its own KV-cached cookies and an
hourly captcha-refresh cron, so the user never sees the placeholder
"Please do the captcha at /uprot" message.

Architecture and reference Worker implementation:
    https://github.com/Pieropapamonello/nello-stream/blob/master/MAMMAMIA_MAXSTREAM_INTEGRATION.md

Enable by setting two environment variables:
    CF_UPROT_WORKER_URL  https://your-worker.workers.dev
    CF_UPROT_WORKER_AUTH your-worker-secret  (optional; only if Worker enforces auth)
"""

import os
import logging

import httpx

from Src.Utilities.config import setup_logging, LEVEL

logger = setup_logging(LEVEL)


def _worker_config():
    url = (os.environ.get("CF_UPROT_WORKER_URL") or "").strip().rstrip("/")
    if not url:
        return None
    auth = (os.environ.get("CF_UPROT_WORKER_AUTH") or "").strip()
    return url, auth


async def resolve_via_worker(client: httpx.AsyncClient, uprot_url: str, timeout: float = 30.0) -> str | None:
    """
    Ask the CF Worker to resolve an uprot.net URL to a MaxStream HLS URL.

    Returns the resolved URL on success, None when the Worker is not
    configured or the resolution fails. Never raises — the caller treats
    a None as "fall back to the local flow / placeholder stream".
    """
    cfg = _worker_config()
    if not cfg or not uprot_url:
        return None
    worker_url, auth = cfg

    headers = {}
    if auth:
        headers["x-worker-auth"] = auth

    try:
        resp = await client.get(
            worker_url,
            params={
                "uprot": "1",
                "url": uprot_url,
                "extract": "1",
                "stream": "0",  # JSON response, not 302 redirect
            },
            headers=headers,
            timeout=timeout,
            follow_redirects=False,
        )
    except Exception as e:
        logger.info(f"CF Worker uprot fetch failed: {e}")
        return None

    if resp.status_code == 200:
        try:
            data = resp.json()
            url = (data or {}).get("url")
            if url:
                logger.info(f"CF Worker uprot resolved (strategy={data.get('strategy')}): {url[:80]}")
                return url
        except Exception as e:
            logger.info(f"CF Worker uprot bad JSON: {e}")
            return None

    logger.info(f"CF Worker uprot non-200: {resp.status_code} body={resp.text[:200]}")
    return None
