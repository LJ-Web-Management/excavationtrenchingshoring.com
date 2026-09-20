#!/usr/bin/env python3
"""
Notify IndexNow (Bing, Yandex, and other participating search engines) that
pages on excavationtrenchingshoring.com have changed.

Run this AFTER deploying, once the live site reflects your changes -
submitting before deploy just tells search engines to re-fetch stale content.

Usage:
    python3 tools/submit_indexnow.py                 # submit every URL in sitemap.xml
    python3 tools/submit_indexnow.py url1 url2 ...    # submit specific URLs only

Key file (<key>.txt at the site root, containing just the key) must already
be live at https://excavationtrenchingshoring.com/<KEY>.txt before submitting,
since IndexNow verifies ownership by fetching it.
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = "excavationtrenchingshoring.com"
KEY = "f1344c571845da0bffed3c3e4ffd8f17"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    text = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>([^<]+)</loc>", text)


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        print(f"IndexNow responded {resp.status} for {len(urls)} URL(s)")


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("No URLs to submit.")
        sys.exit(1)
    submit(urls)
