#!/usr/bin/env python3
"""Followers, monthly views, pins, and boards without login. Python, Node.js and cURL clients for the Pinterest Profile Scraper on Apify, pay per result.

Command-line client for the themineworks/pinterest-profile-scraper actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/pinterest-profile-scraper/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/pinterest-profile-scraper"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--usernames", help="Comma-separated. PROFILE MODE")
    ap.add_argument("--username", help="Convenience field for one profile")
    ap.add_argument("--max-items", type=int, help="Max pins to collect for each board, seed pin, or search query")
    ap.add_argument("--include-pins", action=argparse.BooleanOptionalAction, help="In PROFILE mode, also collect the profile's most recent pins (image URL, save count…")
    ap.add_argument("--max-pins", type=int, help="Max recent pins per profile (profile mode only)")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.usernames: run_input["usernames"] = [s.strip() for s in a.usernames.split(",") if s.strip()]
    if a.username is not None: run_input["username"] = a.username
    if a.max_items is not None: run_input["maxItems"] = a.max_items
    if a.include_pins is not None: run_input["includePins"] = a.include_pins
    if a.max_pins is not None: run_input["maxPins"] = a.max_pins

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()
