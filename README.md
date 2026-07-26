# Pinterest Scraper: Pins, Boards, Profiles & Followers

Python client for **[Pinterest Scraper: Pins, Boards, Profiles & Followers](https://apify.com/themineworks/pinterest-profile-scraper)** — scrape Pinterest pins, boards, profiles and followers — no login.

> ⚡ No login, no cookies, no ban risk · runs in the cloud on [Apify](https://apify.com/themineworks/pinterest-profile-scraper)
>
> 💸 From **$3.0 per 1,000 results** (volume discounts on paid Apify plans). You are only charged for delivered results — empty searches and failed pages are never billed.

## Quick start

```bash
pip install apify-client
python3 pinterest_scraper.py --token YOUR_APIFY_TOKEN --usernames "nasa,natgeo"
```

Get a free API token: [console.apify.com/sign-up](https://console.apify.com/sign-up) — then find it under **Settings → API & Integrations**.

## Options

| Flag | Type | Description |
|---|---|---|
| `--token` | string | Apify API token (or `APIFY_TOKEN` env var) |
| `--out` | string | Output basename — writes `results.json` + `results.csv` |
| `--usernames` | array | PROFILE MODE. Pinterest usernames (without the @) to scrape: followers, monthly views, boa |
| `--board-urls` | array | BOARD MODE. Scrape every pin in a curated board. Paste board URLs (https://www.pinterest.c |
| `--seed-pins` | array | RELATED MODE. For each seed pin, harvest Pinterest's visual-similarity "More like this" fe |
| `--search-queries` | array | SEARCH MODE. Keyword search across all public pins. Use specific brand/collection vocabula |
| `--max-items` | integer | Max pins to collect for each board, seed pin, or search query. Default 40, max 250. |
| `--include-pins` | boolean | In PROFILE mode, also collect the profile's most recent pins (image URL, save count, board |
| `--max-pins` | integer | Max recent pins per profile (profile mode only). Default 50, max 200. |

Flags map 1:1 to the actor's input schema — full reference and a live output sample on the [Store listing](https://apify.com/themineworks/pinterest-profile-scraper).

## Output

One row per result, saved as both JSON and CSV with every field the actor returns. Preview the exact fields on the [listing's output tab](https://apify.com/themineworks/pinterest-profile-scraper).

## Why this actor

- **HTTP-native** — fast, stable, no headless-browser overhead
- **No account risk** — never asks for your login or cookies
- **Fair billing** — pay per delivered result only

MIT © [The Mine Works](https://apify.com/themineworks) — part of a 69-scraper suite trusted by 450+ developers.
