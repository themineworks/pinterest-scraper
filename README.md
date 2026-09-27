# Pinterest Profile Scraper: Followers, Bio & Pin Counts

Scrape any public Pinterest profile without login: followers, monthly views, board count, pin count, bio, and website, plus recent pins with save counts, images, captions, and board names. No API key required.

**Run it on Apify:** [apify.com/themineworks/pinterest-profile-scraper](https://apify.com/themineworks/pinterest-profile-scraper)
**Docs, FAQ and pricing:** [themineworks.com/actors/pinterest-profile-scraper](https://themineworks.com/actors/pinterest-profile-scraper/)

**Price:** $3.00 per 1,000 profiles on Apify's free plan, down to $2.00 on higher plans, plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Follower count, monthly views, and board count
* Recent pins with save counts and images
* Bio, website, and profile metadata
* No login or Pinterest API key required
* Zero charge on empty or private profiles

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/pinterest-profile-scraper").call(run_input={
    "usernames": [
        "nasa",
        "natgeo"
    ],
    "username": "nasa"
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/pinterest-profile-scraper').call({
    "usernames": [
        "nasa",
        "natgeo"
    ],
    "username": "nasa"
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~pinterest-profile-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"usernames": ["nasa", "natgeo"], "username": "nasa"}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 pinterest_scraper.py --token YOUR_APIFY_TOKEN --usernames "nasa,natgeo" --username "nasa"
node pinterest_scraper.mjs --token YOUR_APIFY_TOKEN --usernames "nasa,natgeo" --username "nasa"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` (required) | array |  | PROFILE MODE |
| `username` | string |  | Convenience field for one profile |
| `maxItems` | integer | `40` | Max pins to collect for each board, seed pin, or search query |
| `includePins` | boolean | `false` | In PROFILE mode, also collect the profile's most recent pins (image URL, save count, board, destination link… |
| `maxPins` | integer | `50` | Max recent pins per profile (profile mode only) |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `username` | string | Pinterest username |
| `full_name` | string | Display name of the Pinterest account |
| `about` | string | Profile bio / about text |
| `followers` | integer | Number of followers |
| `following` | integer | Number of accounts followed |
| `pin_count` | integer | Total number of pins |
| `board_count` | integer | Total number of boards |
| `monthly_views` | integer | Monthly unique views on the profile |
| `is_verified` | boolean | Whether the account is verified |
| `profile_pic_url` | string | URL of the profile picture |
| `website_url` | string | Website link from the profile |
| `profile_url` | string | Full URL to the Pinterest profile |
| `source` | string | Scraping method that produced this record |
| `scraped_at` | string | ISO 8601 timestamp of when the record was scraped |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/pinterest-profile-scraper
```

## FAQ

### How much does the Pinterest Profile Scraper cost?

$3.00 per 1,000 profiles on Apify's free plan, down to $2.00 on higher plans, plus a $0.005 start fee per run. Failed and empty results are never charged. You can cap what a single run may spend with the maximum cost setting on Apify.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [Threads Scraper](https://themineworks.com/actors/threads-scraper/): Meta Threads data that returns actual data
* [Reddit Scraper](https://themineworks.com/actors/reddit-scraper/): Free Reddit data with full comment trees
* [LinkedIn Post Scraper](https://themineworks.com/actors/linkedin-post-search/): Search LinkedIn posts by keyword without login

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
