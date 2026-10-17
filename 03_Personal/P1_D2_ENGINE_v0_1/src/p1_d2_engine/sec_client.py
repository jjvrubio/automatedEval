from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import requests


class SecClient:
    """Small cached SEC client with conservative request pacing."""

    TICKER_URL = "https://www.sec.gov/files/company_tickers.json"
    FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"

    def __init__(
        self,
        user_agent: str,
        cache_dir: str | Path = ".cache/sec",
        requests_per_second: float = 4.0,
        timeout: int = 30,
    ) -> None:
        if not user_agent or "example.com" in user_agent:
            raise ValueError(
                "SEC_USER_AGENT must identify the requester with a real contact address."
            )
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.min_interval = 1.0 / requests_per_second
        self.timeout = timeout
        self._last_request = 0.0
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": user_agent,
                "Accept-Encoding": "gzip, deflate",
                "Accept": "application/json",
            }
        )

    def _pace(self) -> None:
        elapsed = time.monotonic() - self._last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)

    def _get_json(self, url: str, cache_file: Path, refresh: bool = False) -> Any:
        if cache_file.exists() and not refresh:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        self._pace()
        response = self.session.get(url, timeout=self.timeout)
        self._last_request = time.monotonic()
        response.raise_for_status()
        data = response.json()
        cache_file.write_text(json.dumps(data), encoding="utf-8")
        return data

    def ticker_map_raw(self, refresh: bool = False) -> dict[str, Any]:
        return self._get_json(
            self.TICKER_URL, self.cache_dir / "company_tickers.json", refresh=refresh
        )

    def companyfacts(self, cik: int, refresh: bool = False) -> dict[str, Any]:
        return self._get_json(
            self.FACTS_URL.format(cik=cik),
            self.cache_dir / f"CIK{cik:010d}.json",
            refresh=refresh,
        )
