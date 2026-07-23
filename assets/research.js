/* research.js — filtering, search, sort, hash state, copy-BibTeX. No deps. */
(() => {
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const papers = $$('#paper-list .paper');
  const dots = $$('.timeline .tl-dot');
  const list = document.getElementById('paper-list');
  const search = document.getElementById('rt-search');
  const count = document.getElementById('result-count');
  const none = document.getElementById('no-results');
  const themeChips = $$('#theme-chips .chip');
  const statusChips = $$('#status-chips .chip');
  const sortBtns = $$('.rt-sortbtn');
  const hasCites = papers.some(p => p.dataset.cites);
  let sort = 'year';

  if (!hasCites) {
    const b = sortBtns.find(b => b.dataset.sort === 'citations');
    if (b) { b.classList.add('off'); b.title = 'Citation counts coming soon'; }
  }

  const state = () => ({
    q: search.value.trim().toLowerCase(),
    themes: themeChips.filter(c => c.classList.contains('on')).map(c => c.dataset.theme),
    status: statusChips.filter(c => c.classList.contains('on')).map(c => c.dataset.status),
  });

  function apply(push = true) {
    const s = state();
    const vis = new Set();
    let shown = 0;
    for (const p of papers) {
      const ok = (!s.q || p.dataset.search.includes(s.q))
        && (!s.themes.length || s.themes.some(t => p.dataset.themes.split(' ').includes(t)))
        && (!s.status.length || s.status.includes(p.dataset.status));
      p.hidden = !ok;
      if (ok) { shown++; vis.add(p.id); }
    }
    for (const d of dots) d.classList.toggle('dim', !vis.has(d.dataset.paper));
    count.textContent = shown === papers.length ? papers.length + ' papers' : shown + ' of ' + papers.length + ' papers';
    none.hidden = shown > 0;
    if (push) writeHash(s);
  }

  function writeHash(s) {
    const p = new URLSearchParams();
    if (s.q) p.set('q', s.q);
    if (s.themes.length) p.set('theme', s.themes.join(','));
    if (s.status.length) p.set('status', s.status.join(','));
    if (sort !== 'year') p.set('sort', sort);
    const h = p.toString();
    history.replaceState(null, '', h ? '#' + h : location.pathname + location.search);
  }

  function readHash() {
    const h = decodeURIComponent(location.hash.slice(1));
    if (!h.includes('=')) return; // plain #paper-id anchors are not filter state
    const p = new URLSearchParams(h);
    search.value = p.get('q') || '';
    const th = (p.get('theme') || '').split(',').filter(Boolean);
    const st = (p.get('status') || '').split(',').filter(Boolean);
    themeChips.forEach(c => c.classList.toggle('on', th.includes(c.dataset.theme)));
    statusChips.forEach(c => c.classList.toggle('on', st.includes(c.dataset.status)));
    if (p.get('sort') === 'citations') setSort('citations', false);
  }

  function doSort() {
    const key = (sort === 'citations' && hasCites) ? 'cites' : 'year';
    [...papers]
      .sort((a, b) => (+b.dataset[key] || 0) - (+a.dataset[key] || 0) || (+b.dataset.year) - (+a.dataset.year))
      .forEach(p => list.appendChild(p));
  }

  function setSort(s, push = true) {
    if (s === 'citations' && !hasCites) return; // graceful no-op until citations pipeline lands
    sort = s;
    sortBtns.forEach(b => {
      const on = b.dataset.sort === s;
      b.classList.toggle('on', on);
      b.setAttribute('aria-pressed', on);
    });
    if (document.startViewTransition) {
      try {
        const t = document.startViewTransition(doSort);
        t.updateCallbackDone.catch(doSort); // never let a skipped transition swallow the sort
      } catch (e) { doSort(); }
    } else doSort();
    if (push) writeHash(state());
  }

  [...themeChips, ...statusChips].forEach(c =>
    c.addEventListener('click', () => { c.classList.toggle('on'); apply(); }));
  search.addEventListener('input', () => apply());
  sortBtns.forEach(b => b.addEventListener('click', () => setSort(b.dataset.sort)));

  $$('.bib-btn').forEach(b => b.addEventListener('click', async () => {
    const src = document.getElementById('bib-' + b.dataset.bib);
    if (!src) return;
    try { await navigator.clipboard.writeText(src.textContent.trim()); } catch (e) { return; }
    const old = b.textContent;
    b.textContent = 'Copied ✓';
    b.classList.add('copied');
    setTimeout(() => { b.textContent = old; b.classList.remove('copied'); }, 1500);
  }));

  readHash();
  apply(false);
  if (sort !== 'year') doSort();
})();

/* ── Instant timeline tooltips (native <title> is ~1s slow) ── */
(() => {
  const books = document.querySelectorAll('.tl-dot');
  if (!books.length) return;
  const tip = document.createElement('div');
  tip.className = 'tl-tip';
  document.body.appendChild(tip);
  books.forEach(b => {
    const t = b.querySelector('title');
    if (!t) return;
    const text = t.textContent;
    b.setAttribute('aria-label', text);
    t.remove(); // suppress the slow native tooltip
    b.addEventListener('mouseenter', () => { tip.textContent = text; tip.classList.add('show'); });
    b.addEventListener('mousemove', (e) => {
      const pad = 14, w = tip.offsetWidth, h = tip.offsetHeight;
      let x = e.clientX + pad, y = e.clientY - h - 10;
      if (x + w > innerWidth - 8) x = e.clientX - w - pad;
      if (y < 8) y = e.clientY + pad;
      tip.style.transform = `translate(${x}px, ${y}px)`;
    });
    b.addEventListener('mouseleave', () => tip.classList.remove('show'));
  });
})();
