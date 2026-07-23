#!/usr/bin/env node
/**
 * build.mjs — generates research.html + barrios.bib from data/papers.json
 * and templates/research.tmpl.html. Node built-ins only. Run: node build.mjs
 *
 * To add a paper: edit data/papers.json, run `node build.mjs`, commit both
 * the JSON and the regenerated research.html / barrios.bib.
 */
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = dirname(fileURLToPath(import.meta.url));
const { papers } = JSON.parse(readFileSync(join(ROOT, 'data', 'papers.json'), 'utf8'));
const tmpl = readFileSync(join(ROOT, 'templates', 'research.tmpl.html'), 'utf8');

// Merge cached citation counts (data/citations.json, refreshed by
// scripts/fetch-citations.mjs / the weekly GitHub Action) when present.
let citesMeta = null;
try {
  citesMeta = JSON.parse(readFileSync(join(ROOT, 'data', 'citations.json'), 'utf8'));
  for (const p of papers) {
    if (Number.isFinite(citesMeta.counts?.[p.id])) p.citations = citesMeta.counts[p.id];
  }
} catch { /* citations.json absent — badges and Citations sort stay off */ }

// Optional Google Scholar overrides (data/scholar.json, same shape as
// citations.json: {"updated": "...", "counts": {"<paper-id>": N}}).
// Maintained manually or via a browser-assisted session — Scholar has no API.
// Scholar counts take precedence when higher (Scholar merges paper versions).
try {
  const scholar = JSON.parse(readFileSync(join(ROOT, 'data', 'scholar.json'), 'utf8'));
  for (const p of papers) {
    const s = scholar.counts?.[p.id];
    if (Number.isFinite(s) && s > (p.citations || 0)) p.citations = s;
  }
  if (scholar.updated && citesMeta) citesMeta.updated = scholar.updated;
  else if (scholar.updated && !citesMeta) citesMeta = { updated: scholar.updated };
} catch { /* scholar.json absent — OpenAlex counts only */ }

const SCHOLAR = 'https://scholar.google.com/citations?user=yE9KwEgAAAAJ&amp;hl=en';

const SITE = 'https://johnmbarrios.com/';

const themeLabels = {
  'labor': 'Labor & Professions',
  'entrepreneurship': 'Entrepreneurship',
  'political-economy': 'Political Economy',
  'governance': 'Governance',
  'taxation': 'Taxation & Regulation',
  'reporting': 'Reporting & Measurement',
  'antitrust': 'Market Structure',
  'ethics': 'Ethics & Misconduct',
};
const statusLabels = { published: 'Published', forthcoming: 'Forthcoming', rr: 'R&amp;R', working: 'Working Paper' };

const esc = (s) => String(s ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;').replaceAll("'", '&#39;');

/* ── BibTeX ── */
function bibtex(p) {
  const key = 'barrios' + p.year + p.id.replace(/-/g, '');
  const authors = ['John Manuel Barrios', ...p.authors].join(' and ');
  const lines = [`  author = {${authors}}`, `  title = {${p.title}}`, `  year = {${p.year}}`];
  let type = 'unpublished';
  if (p.type === 'chapter') {
    type = 'incollection';
    lines.push(`  booktitle = {${p.venue}}`);
    if (p.publisher) lines.push(`  publisher = {${p.publisher}}`);
  } else if (p.status === 'published' || p.status === 'forthcoming') {
    type = 'article';
    lines.push(`  journal = {${String(p.venue).replace(/&/g, '\\&')}}`);
    if (p.volume) {
      const m = String(p.volume).match(/^(\d+)(?:\((\d+)\))?$/);
      if (m) { lines.push(`  volume = {${m[1]}}`); if (m[2]) lines.push(`  number = {${m[2]}}`); }
    }
    if (p.status === 'forthcoming') lines.push(`  note = {Forthcoming}`);
  } else {
    lines.push(`  note = {Working paper${p.note && /Revision Requested/i.test(p.note) ? '; ' + p.note.replace(/Revision Requested:\s*/i, 'revision requested at ') : ''}}`);
  }
  if (p.doi) lines.push(`  doi = {${p.doi}}`);
  const url = p.doi ? `https://doi.org/${p.doi}` : (p.links?.ssrn || p.links?.nber);
  if (url) lines.push(`  url = {${url}}`);
  return `@${type}{${key},\n${lines.join(',\n')}\n}`;
}

/* ── Paper cards ── */
function kicker(p) {
  if (p.type === 'chapter') return `In ${p.venue}${p.publisher ? ', ' + p.publisher : ''} · ${p.year}`;
  if (p.status === 'published') return `${p.venue}${p.volume ? ' ' + p.volume : ''} · ${p.year}`;
  if (p.status === 'forthcoming') return p.venue; // the status pill already says "Forthcoming"
  return String(p.year); // the status pill already says "Working Paper" / "R&R"
}

function linkPills(p) {
  const L = p.links || {};
  const out = [];
  const pill = (href, label, ext = true) =>
    `<a href="${esc(href)}"${ext ? ' target="_blank" rel="noopener"' : ''}>${label}</a>`;
  if (L.page) out.push(pill(L.page, 'Paper Page', false));
  if (L.ssrn) out.push(pill(L.ssrn, 'SSRN'));
  if (L.nber) out.push(pill(L.nber, 'NBER'));
  if (p.doi) out.push(pill(`https://doi.org/${p.doi}`, 'Journal'));
  if (L.pdf) out.push(pill(L.pdf, 'PDF'));
  if (L.slides) out.push(pill(L.slides, 'Slides'));
  if (L.code) out.push(pill(L.code, 'Code &amp; Slides', /^https?:/.test(L.code) ? true : false));
  out.push(`<button type="button" class="bib-btn" data-bib="${esc(p.id)}">BibTeX</button>`);
  return out.join('\n                    ');
}

function card(p) {
  const searchBlob = [p.title, p.authors.join(' '), p.venue, p.note, p.year, p.status,
    statusLabels[p.status], ...(p.themes || []).map(t => themeLabels[t] || t), p.abstract]
    .filter(Boolean).join(' ').toLowerCase().replace(/\s+/g, ' ');
  const cites = Number.isFinite(p.citations) ? ` data-cites="${p.citations}"` : '';
  const citesBadge = Number.isFinite(p.citations) && p.citations > 0
    ? `<a class="cite-badge" href="${SCHOLAR}" target="_blank" rel="noopener" title="Citations (OpenAlex; see Google Scholar)">${p.citations.toLocaleString('en-US')} citation${p.citations === 1 ? '' : 's'}</a>` : '';
  const abstract = p.abstract
    ? `\n                <details class="paper-abstract"><summary>Abstract</summary>${p.abstract.split(/\n\n+/).map(t => `<p>${esc(t)}</p>`).join('')}</details>` : '';
  const note = p.note ? `\n                <p class="paper-note">${esc(p.note)}</p>` : '';
  const authors = p.authors.length ? `\n                <p class="paper-authors">with ${esc(p.authors.join(', ').replace(/, ([^,]*)$/, ' and $1'))}</p>` : '';
  const titleHtml = p.links?.page
    ? `<a href="${esc(p.links.page)}">${esc(p.title)}</a>` : esc(p.title);
  const body = `                <div class="paper-head">
                    <span class="paper-kicker">${esc(kicker(p))}</span>
                    <span class="status-pill status-${esc(p.status)}">${statusLabels[p.status]}</span>${citesBadge}
                </div>
                <h3>${titleHtml}</h3>${authors}${note}${abstract}
                <div class="entry-links paper-links">
                    ${linkPills(p)}
                </div>
                <script type="text/x-bibtex" id="bib-${esc(p.id)}">
${bibtex(p)}
                </script>`;
  // any paper with a figure gets a thumbnail column (desktop only)
  const hasThumb = !!p.figure;
  const inner = hasThumb
    ? `                <div class="paper-body">\n${body}\n                </div>
                <a class="paper-thumb" href="${esc(p.links?.page || p.figure)}" tabindex="-1" aria-hidden="true">
                    <img src="${esc(p.figure)}" alt="${esc(p.title)} — key figure" loading="lazy">
                </a>`
    : body;
  return `            <article class="paper${hasThumb ? ' has-thumb' : ''}" id="${esc(p.id)}" style="view-transition-name:p-${esc(p.id)}"
                data-year="${p.year}" data-status="${esc(p.status)}"${cites}
                data-themes="${esc((p.themes || []).join(' '))}"
                data-search="${esc(searchBlob)}">
${inner}
            </article>`;
}

/* ── Timeline SVG ── */
function timeline(sorted) {
  const years = sorted.map(p => p.year);
  const minY = Math.min(...years), maxY = Math.max(...years);
  const byYear = new Map();
  for (let y = minY; y <= maxY; y++) byYear.set(y, []);
  // uniform dots: the timeline shows research activity per year, with no
  // published/unpublished distinction (working papers are current work,
  // not old papers that failed to publish)
  for (const p of sorted) byYear.get(p.year).push(p);
  // each paper is a small book lying on the pile: deterministic width/offset/
  // shade from the paper id so builds are reproducible
  const hash = (str) => [...str].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 7);
  const SHADES = ['#00356b', '#1a4f8a', '#2c5f96', '#00294f'];
  const colW = 48, bh = 9, vgap = 2.5, top = 10, labelH = 22;
  const maxStack = Math.max(...[...byYear.values()].map(a => a.length));
  const W = (maxY - minY + 1) * colW, H = top + maxStack * (bh + vgap) + labelH;
  const shelfY = top + maxStack * (bh + vgap) + 1;
  let dots = '', labels = '';
  let i = 0;
  for (let y = minY; y <= maxY; y++, i++) {
    const cx = i * colW + colW / 2;
    byYear.get(y).forEach((p, j) => {
      const h = hash(p.id);
      const bw = 26 + (h % 9);                    // 26-34px wide
      const dx = ((h >> 3) % 7) - 3;              // -3..+3 lateral shift
      const x = cx - bw / 2 + dx;
      const yTop = shelfY - (j + 1) * (bh + vgap) + vgap;
      const fill = SHADES[h % SHADES.length];
      const shape =
        `<rect x="${x - 2}" y="${yTop - 1.5}" width="${bw + 4}" height="${bh + 3}" fill="transparent"/>` +
        `<rect x="${x}" y="${yTop}" width="${bw}" height="${bh}" rx="1.5" fill="${fill}"/>` +
        `<rect x="${x + bw - 3.5}" y="${yTop + 1.5}" width="2" height="${bh - 3}" rx="1" fill="#ffffff" opacity="0.55"/>`;
      dots += `<a href="#${esc(p.id)}" class="tl-dot" data-paper="${esc(p.id)}"><title>${esc(p.title)} (${p.year})</title>${shape}</a>`;
    });
    labels += `<text x="${cx}" y="${H - 5}" text-anchor="middle" class="tl-year">${y}</text>`;
  }
  return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Papers per year, ${minY} to ${maxY}" preserveAspectRatio="xMaxYMid meet">` +
    `<line x1="0" y1="${shelfY + 1}" x2="${W}" y2="${shelfY + 1}" stroke="#cfd3d9" stroke-width="1.5"/>` +
    dots + labels + `</svg>`;
}

/* ── Chips ── */
function chips() {
  const themeCounts = {}, statusCounts = {};
  for (const p of papers) {
    for (const t of p.themes || []) themeCounts[t] = (themeCounts[t] || 0) + 1;
    statusCounts[p.status] = (statusCounts[p.status] || 0) + 1;
  }
  const theme = Object.keys(themeLabels).filter(t => themeCounts[t]).map(t =>
    `                    <button type="button" class="chip" data-theme="${t}">${esc(themeLabels[t])}<span class="chip-n">${themeCounts[t]}</span></button>`
  ).join('\n');
  const status = ['published', 'forthcoming', 'rr', 'working'].filter(s => statusCounts[s]).map(s =>
    `                    <button type="button" class="chip chip-status" data-status="${s}">${statusLabels[s]}<span class="chip-n">${statusCounts[s]}</span></button>`
  ).join('\n');
  return { theme, status, statusCounts };
}

/* ── JSON-LD ── */
function jsonld() {
  const person = { '@type': 'Person', name: 'John Manuel Barrios', affiliation: 'Yale School of Management', url: SITE };
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@graph': papers.map(p => {
      const sameAs = [p.links?.ssrn, p.links?.nber, p.doi ? `https://doi.org/${p.doi}` : null].filter(Boolean);
      const o = {
        '@type': p.type === 'chapter' ? 'Chapter' : 'ScholarlyArticle',
        name: p.title,
        author: [person, ...p.authors.map(name => ({ '@type': 'Person', name }))],
        datePublished: String(p.year),
        url: p.links?.page ? SITE + p.links.page : (sameAs[0] || SITE + 'research.html#' + p.id),
      };
      if (sameAs.length) o.sameAs = sameAs;
      if (p.venue && p.type !== 'chapter') o.isPartOf = { '@type': 'Periodical', name: p.venue };
      if (p.venue && p.type === 'chapter') o.isPartOf = { '@type': 'Book', name: p.venue };
      return o;
    }),
  });
}

/* ── Assemble ── */
const sorted = [...papers].sort((a, b) => b.year - a.year || a.title.localeCompare(b.title));
const { theme, status, statusCounts } = chips();
const summaryBits = [`${papers.length} papers`];
for (const [s, label] of [['published', 'published'], ['forthcoming', 'forthcoming'], ['rr', 'R&amp;R'], ['working', 'working']]) {
  if (statusCounts[s]) summaryBits.push(`${statusCounts[s]} ${label}`);
}

const totalCites = papers.reduce((a, p) => a + (p.citations || 0), 0);
const citeLine = totalCites > 0
  ? `<div class="strip-cites">${totalCites.toLocaleString('en-US')} citations · <a href="${SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a>${citesMeta?.updated ? ` · updated ${citesMeta.updated}` : ''}</div>`
  : '';

const html = tmpl
  .replace('{{GENERATED_NOTE}}', 'GENERATED by build.mjs — edit data/papers.json or templates/research.tmpl.html, never this file.')
  .replace('{{CITE_LINE}}', citeLine)
  .replace('{{JSONLD}}', jsonld())
  .replace('{{COUNT_SUMMARY}}', summaryBits.join(' · '))
  .replace('{{THEME_CHIPS}}', theme)
  .replace('{{STATUS_CHIPS}}', status)
  .replace('{{TOTAL}}', String(papers.length))
  .replace('{{TIMELINE}}', '                ' + timeline(sorted))
  .replace('{{PAPERS}}', sorted.map(card).join('\n'));

writeFileSync(join(ROOT, 'research.html'), html);
writeFileSync(join(ROOT, 'barrios.bib'), papers.map(bibtex).join('\n\n') + '\n');

/* ── sitemap.xml + robots.txt ── */
const mainPages = ['', 'research.html', 'teaching.html', 'ai-research.html', 'labor-accounting.html', 'code.html', 'media.html', 'cv.html'];
let paperPages = [];
try {
  paperPages = readdirSync(join(ROOT, 'papers_web')).filter(f => f.endsWith('.html')).map(f => 'papers_web/' + f);
} catch { /* papers_web absent in some checkouts */ }
const today = new Date().toISOString().slice(0, 10);
const urlEntry = (path, prio) =>
  `  <url><loc>${SITE}${path}</loc><lastmod>${today}</lastmod><priority>${prio}</priority></url>`;
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n` +
  `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  mainPages.map(p => urlEntry(p, p === '' ? '1.0' : p === 'research.html' ? '0.9' : '0.7')).join('\n') + '\n' +
  paperPages.map(p => urlEntry(p, '0.5')).join('\n') + '\n</urlset>\n';
writeFileSync(join(ROOT, 'sitemap.xml'), sitemap);
writeFileSync(join(ROOT, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${SITE}sitemap.xml\n`);

console.log(`research.html: ${papers.length} papers (${summaryBits.slice(1).join(', ')}); ` +
  `citations: ${totalCites || 'n/a'}; barrios.bib, sitemap.xml (${mainPages.length + paperPages.length} urls), robots.txt written.`);
