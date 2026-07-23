#!/usr/bin/env node
/**
 * fetch-citations.mjs — refresh data/citations.json from OpenAlex.
 * Node built-ins only. Run: node scripts/fetch-citations.mjs
 * Resolve-mode (to re-verify the author id): node scripts/fetch-citations.mjs --resolve
 *
 * Matching order per paper: journal DOI → SSRN-derived DOI (10.2139/ssrn.N) →
 * normalized title. When several OpenAlex works match one paper (e.g. the SSRN
 * preprint and the journal version), the highest citation count wins.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const MAILTO = 'john.m.barrios@yale.edu';

// John Manuel Barrios (Yale SOM / NBER; previously U Chicago Booth, WashU Olin).
// Verified 2026-07-23 via api.openalex.org/authors?search=John%20Barrios:
// A5054886175 = "John Manuel Barrios", last known institutions NBER + Yale
// University, 86 works, ~1,900 citations (the JAR/JFE/JPubE accounting author).
// Re-check any time with: node scripts/fetch-citations.mjs --resolve
const AUTHOR_ID = 'A5054886175';

const get = async (url) => {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`OpenAlex ${res.status}: ${(await res.text()).slice(0, 200)}`);
  return res.json();
};

if (process.argv.includes('--resolve')) {
  const d = await get(`https://api.openalex.org/authors?search=John%20Barrios&per-page=10&mailto=${MAILTO}`);
  for (const a of d.results) {
    const inst = (a.last_known_institutions || []).map(i => i.display_name).join(', ');
    console.log(`${a.id.replace('https://openalex.org/', '')} | ${a.display_name} | ${a.works_count} works | ${a.cited_by_count} cites | ${inst}`);
  }
  process.exit(0);
}

const { papers } = JSON.parse(readFileSync(join(ROOT, 'data', 'papers.json'), 'utf8'));

// Fetch all works for the author (cursor paging, defensive).
const works = [];
let cursor = '*';
while (cursor) {
  const d = await get(
    `https://api.openalex.org/works?filter=authorships.author.id:${AUTHOR_ID}` +
    `&per-page=100&cursor=${encodeURIComponent(cursor)}&select=id,doi,title,cited_by_count&mailto=${MAILTO}`);
  works.push(...d.results);
  cursor = d.meta?.next_cursor && d.results.length ? d.meta.next_cursor : null;
}

const normDoi = (s) => s ? s.toLowerCase().replace(/^https?:\/\/doi\.org\//, '').trim() : null;
const normTitle = (s) => s ? s.toLowerCase().replace(/[^a-z0-9]+/g, '') : '';

const byDoi = new Map();
for (const w of works) { const d = normDoi(w.doi); if (d) byDoi.set(d, w); }

const counts = {};
const matched = [], unmatched = [];
const prefixLen = (a, b) => { let i = 0; while (i < a.length && i < b.length && a[i] === b[i]) i++; return i; };

for (const p of papers) {
  const candidates = [];
  if (p.doi && byDoi.has(normDoi(p.doi))) candidates.push(byDoi.get(normDoi(p.doi)));
  const ssrnId = p.links?.ssrn?.match(/abstract_id=(\d+)/)?.[1];
  if (ssrnId && byDoi.has(`10.2139/ssrn.${ssrnId}`)) candidates.push(byDoi.get(`10.2139/ssrn.${ssrnId}`));
  const nberId = p.links?.nber?.match(/papers\/(w\d+)/i)?.[1];
  if (nberId && byDoi.has(`10.3386/${nberId.toLowerCase()}`)) candidates.push(byDoi.get(`10.3386/${nberId.toLowerCase()}`));
  const t = normTitle(p.title);
  for (const w of works) {
    const wt = normTitle(w.title);
    if (!wt || wt.length < 15) continue;
    // exact match, containment, or a long shared prefix (catches retitled
    // journal versions, e.g. "…Entrepreneurial Entry" vs "…New Business Formation")
    if (wt === t
      || (t.length >= 20 && (wt.startsWith(t) || t.startsWith(wt)))
      || (t.length >= 25 && wt.length >= 25 && prefixLen(t, wt) >= 25)) candidates.push(w);
  }
  if (candidates.length) {
    const best = candidates.reduce((a, b) => (b.cited_by_count > a.cited_by_count ? b : a));
    counts[p.id] = best.cited_by_count;
    matched.push(`${p.id} -> ${best.cited_by_count} (${best.id.replace('https://openalex.org/', '')})`);
  } else {
    unmatched.push(p.id);
  }
}

writeFileSync(join(ROOT, 'data', 'citations.json'),
  JSON.stringify({ updated: new Date().toISOString().slice(0, 10), counts }, null, 2) + '\n');

console.log(`OpenAlex works fetched: ${works.length}`);
console.log('matched:\n  ' + matched.join('\n  '));
console.log('unmatched: ' + (unmatched.join(', ') || 'none'));
console.log(`total citations (matched): ${Object.values(counts).reduce((a, b) => a + b, 0)}`);
