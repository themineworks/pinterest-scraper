#!/usr/bin/env python3
"""Scrape Pinterest pins, boards, profiles and followers — no login.
CLI for the themineworks/pinterest-profile-scraper Apify actor: runs it, waits, saves JSON + CSV.
Free Apify account + API token: https://console.apify.com/sign-up
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/pinterest-profile-scraper"

def main():
    ap = argparse.ArgumentParser(description="scrape Pinterest pins, boards, profiles and followers — no login")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"),
                    help="Apify API token (or set APIFY_TOKEN env var)")
    ap.add_argument("--out", default="results", help="Output basename (.json and .csv)")
    ap.add_argument("--usernames", help="Comma-separated. PROFILE MODE e.g. nasa,natgeo")
    ap.add_argument("--board-urls", help="Comma-separated. BOARD MODE e.g. one,two")
    ap.add_argument("--seed-pins", help="Comma-separated. RELATED MODE e.g. one,two")
    ap.add_argument("--search-queries", help="Comma-separated. SEARCH MODE e.g. one,two")
    ap.add_argument("--max-items", type=int, default=40, help="Max pins to collect for each board, seed pin, or search query")
    ap.add_argument("--include-pins", action="store_true", help="In PROFILE mode, also collect the profile's most recent pins (image URL, save count, board,…")
    ap.add_argument("--max-pins", type=int, default=50, help="Max recent pins per profile (profile mode only)")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up")

    run_input = {}
    if a.usernames is not None: run_input["usernames"] = [s.strip() for s in a.usernames.split(",") if s.strip()]
    if a.board_urls is not None: run_input["boardUrls"] = [s.strip() for s in a.board_urls.split(",") if s.strip()]
    if a.seed_pins is not None: run_input["seedPins"] = [s.strip() for s in a.seed_pins.split(",") if s.strip()]
    if a.search_queries is not None: run_input["searchQueries"] = [s.strip() for s in a.search_queries.split(",") if s.strip()]
    if a.max_items is not None: run_input["maxItems"] = a.max_items
    if a.include_pins: run_input["includePins"] = True
    if a.max_pins is not None: run_input["maxPins"] = a.max_pins

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    if items:
        keys = []
        for it in items:
            for k in it:
                if k not in keys: keys.append(k)
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: ("" if v is None else v) for k, v in it.items()})
    print(f"Done: {len(items)} results -> {a.out}.json / {a.out}.csv")

if __name__ == "__main__":
    main()
