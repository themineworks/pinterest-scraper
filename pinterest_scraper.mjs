#!/usr/bin/env node
// pinterest-profile — Apify actor client.
// Node.js client for the themineworks/pinterest-profile Apify actor: runs it, waits, saves results.json.
// Free Apify account + API token: https://console.apify.com/sign-up
import { ApifyClient } from 'apify-client';
import { writeFileSync } from 'node:fs';

const ACTOR = 'themineworks/pinterest-profile';

// Flags map 1:1 to the actor's input schema. Run: node pinterest_scraper.mjs --token YOUR_TOKEN --usernames "nasa"
function parseArgs(argv) {
    const out = {};
    for (let i = 0; i < argv.length; i++) {
        if (!argv[i].startsWith('--')) continue;
        const key = argv[i].slice(2);
        const val = (argv[i + 1] && !argv[i + 1].startsWith('--')) ? argv[++i] : true;
        out[key] = val;
    }
    return out;
}

const args = parseArgs(process.argv.slice(2));
const token = args.token || process.env.APIFY_TOKEN;
if (!token) {
    console.error('Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up');
    process.exit(1);
}

const runInput = {};
if (args['usernames'] !== undefined) runInput.usernames = String(args['usernames']).split(',').map(s => s.trim());
if (args['username'] !== undefined) runInput.username = args['username'];
if (args['board-urls'] !== undefined) runInput.boardUrls = String(args['board-urls']).split(',').map(s => s.trim());
if (args['seed-pins'] !== undefined) runInput.seedPins = String(args['seed-pins']).split(',').map(s => s.trim());
if (args['search-queries'] !== undefined) runInput.searchQueries = String(args['search-queries']).split(',').map(s => s.trim());
if (args['max-items'] !== undefined) runInput.maxItems = parseInt(args['max-items'], 10);
if (args['include-pins'] !== undefined) runInput.includePins = args['include-pins'] === true || args['include-pins'] === 'true';
if (args['max-pins'] !== undefined) runInput.maxPins = parseInt(args['max-pins'], 10);

const client = new ApifyClient({ token });
console.log(`Running ${ACTOR} ...`);
const run = await client.actor(ACTOR).call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
writeFileSync('results.json', JSON.stringify(items, null, 2));
console.log(`Saved ${items.length} results to results.json`);
