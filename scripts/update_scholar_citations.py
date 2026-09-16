#!/usr/bin/env python3
"""Fetch Google Scholar profile citations and update Jekyll data."""

from __future__ import annotations

import datetime as dt
import html
import pathlib
import re
import sys
import urllib.error
import urllib.request


PROFILE_URL = "https://scholar.google.com/citations?user=PDP31hEAAAAJ&hl=en"
OUTPUT = pathlib.Path("_data/scholar.yml")


def fetch_profile() -> str:
    request = urllib.request.Request(
        PROFILE_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_citations(page: str) -> int:
    page = html.unescape(page)

    meta_match = re.search(r"Cited by\s+([0-9,]+)", page)
    if meta_match:
        return int(meta_match.group(1).replace(",", ""))

    table_match = re.search(
        r"<td[^>]*>\s*Citations\s*</td>\s*<td[^>]*class=\"gsc_rsb_std\"[^>]*>\s*([0-9,]+)",
        page,
        re.IGNORECASE,
    )
    if table_match:
        return int(table_match.group(1).replace(",", ""))

    raise ValueError("Could not find Google Scholar citation count in profile HTML.")


def write_data(citations: int) -> None:
    site_timezone = dt.timezone(dt.timedelta(hours=8))
    checked_at = dt.datetime.now(site_timezone).date().isoformat()
    OUTPUT.write_text(
        "\n".join(
            [
                f'profile_url: "{PROFILE_URL}"',
                f"citations: {citations}",
                f'checked_at: "{checked_at}"',
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    try:
        citations = extract_citations(fetch_profile())
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"Failed to update Google Scholar citations: {exc}", file=sys.stderr)
        return 1

    write_data(citations)
    print(f"Updated Google Scholar citations: {citations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
