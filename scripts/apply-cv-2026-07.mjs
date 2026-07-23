// One-off: apply CV (2026 "Version Improved") statuses + new papers,
// and write data/scholar.json from the Scholar profile read on 2026-07-23.
import { readFileSync, writeFileSync } from 'node:fs';

const doc = JSON.parse(readFileSync('data/papers.json', 'utf8'));
const papers = doc.papers;
const byId = Object.fromEntries(papers.map(p => [p.id, p]));

// ── Status/title updates per CV ──
byId['informing-entrepreneurs'].title =
  'Initial Public Offering and New Business Formation: The Role of Public Firm Disclosures';
byId['informing-entrepreneurs'].note = 'Journal of Accounting Research (Accepted)';

byId['ethics-illusions'].status = 'rr';
byId['ethics-illusions'].note = 'Revision Requested: Accounting, Organizations and Society';

byId['ai-disclosures'].note = 'Under Review (2nd round): Review of Accounting Studies';
byId['regulatory-spillovers'].note = 'Under Review (2nd round): The Accounting Review';

byId['staggered-did'].status = 'working';   // CV lists as working paper, no R&R
delete byId['staggered-did'].note;

byId['taxation-venture-capital'].year = 2025; // per Scholar/Palgrave listing

// ── New papers from CV ──
const neu = [
  { id: 'imitation-innovation',
    title: 'Imitation or Innovation? Strategic Mimicry in Corporate Earnings Calls',
    authors: ['Khrystyna Bochkay', 'Roman Chychyla', 'Sundaresh Ramnath'],
    year: 2025, status: 'rr', venue: null,
    note: 'Revision Requested: Journal of Accounting and Economics',
    themes: ['reporting'], abstract: null,
    links: {}, doi: null, featured: false },
  { id: 'better-in-person',
    title: 'Better in Person? Does In-Person Screening Affect Who Gets Hired?',
    authors: ['Laura Giuliano', 'Andrew Leone'],
    year: 2021, status: 'working', venue: null,
    themes: ['labor'], abstract: null,
    links: {}, doi: null, featured: false },
  { id: 'labor-information-environment',
    title: 'Labor and the Corporate Information Environment',
    authors: ['Jung Ho Choi', 'Carolyn Deller', 'Joseph Pacelli', 'Heidi A. Packard'],
    year: 2026, status: 'working', venue: null,
    themes: ['labor', 'reporting'], abstract: null,
    links: {}, doi: null, featured: false },
  { id: 'stemming-tide',
    title: 'STEMming the Tide: The Impact of STEM Designation on Accounting Education and the Labor Market',
    authors: ['Ping Gong', 'Enshuai Yu'],
    year: 2026, status: 'working', venue: null,
    note: 'Registered Report Proposal',
    themes: ['labor'], abstract: null,
    links: {}, doi: null, featured: false },
  { id: 'stablecoins',
    title: 'One Asset, Two Financial Systems: Stablecoins and the Transmission of Runs between Decentralized and Traditional Finance',
    authors: ['Christoph Bertsch', 'Linda M. Schilling'],
    year: 2026, status: 'working', venue: null,
    themes: ['reporting'], abstract: null,
    links: {}, doi: null, featured: false },
];
for (const n of neu) if (!byId[n.id]) papers.push(n);

// Normalize themes against existing set (fall back gracefully in build if unknown).
writeFileSync('data/papers.json', JSON.stringify(doc, null, 2) + '\n');

// ── Google Scholar counts (profile yE9KwEgAAAAJ, read 2026-07-23) ──
const scholar = {
  updated: '2026-07-23',
  source: 'Google Scholar profile (total 2,772 · h-index 15 · i10 16)',
  counts: {
    'risk-politics': 839, 'civic-capital': 637, 'staggered-did': 322,
    'ridehailing': 210, 'licensing': 194, 'gig-economy': 187,
    'tax-planning': 71, 'boards-feather': 51, 'informing-entrepreneurs': 35,
    'measurement-matters': 33, 'midnight-mergers': 25, 'misaligned-control': 20,
    'ai-disclosures': 13, 'conflict-discount': 9, 'better-in-person': 9,
    'labor-information-environment': 8, 'hustling-home': 7, 'pe-accounting': 5,
    'regulatory-spillovers': 3, 'accounting-pressure': 1,
    'taxation-venture-capital': 1, 'licensing-reform': 1,
  },
};
writeFileSync('data/scholar.json', JSON.stringify(scholar, null, 2) + '\n');
console.log(`papers: ${papers.length}; scholar counts: ${Object.keys(scholar.counts).length}`);
