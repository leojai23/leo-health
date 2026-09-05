# Leo-Health

A private, offline-capable **reference notebook** for the Satvic Movement material —
not a course, just something to look things up in. Built as a single-file PWA in the
same style as the MBA / Leo-Interview notebooks.

**Live:** https://leojai23.github.io/leo-health/

## Subjects

| Subject | Source book | What's in it |
|---|---|---|
| **Satvic Food** | *The Food Book* (Subah Jain) | Food philosophy (what Satvic means, the 4 principles, 21 food laws, digestion, food combining, how you eat), setting up a Satvic kitchen, the meal plans, and the full recipe collection (pre-breakfast → occasional) + skin care. |
| **Satvic Kids** | *Satvic Kids Book* (Subah Saraf) | Basics (nut milks, butters, curd, cheese, hummus) and kid-friendly recipes — smoothies, smoothie bowls, salads, juices, snacks and desserts. |
| **Satvic Juice** | *Satvic 3-Day Juice Diet* manual | The 3-day juice fast — how to prepare, shopping list, the three juices, the daily schedule and FAQs. |

111 pages total.

## The app

Single `index.html` (everything inlined) + `manifest.json` + `sw.js` + two icons.
No build step needed to *run* it — just open `index.html` or visit the live URL.

Features (reference-only — deliberately **no quizzes, exams, flashcards or case studies**):

- Collapsible **sidebar** grouped by subject → section → page
- Client-side **search** overlay (floating button or the `/` key; ↑/↓/Enter to pick)
- 4-way **reading theme** switcher — Day / Sepia / Dark / Night (persisted in `localStorage`)
- **Reading progress** — visited pages get a ✓ in the sidebar, a per-subject count on
  the home cards, an overall bar, and an "Up next" card on the home page
  (`localStorage['leo-health-progress']`)
- **Prev / next** bar under each page heading + keyboard ← / →
- **Print** button (clean `@media print` stylesheet)
- Installable **PWA**, offline via a cache-first service worker whose cache name is
  stamped with a hash of the built page (so a new deploy can't serve a stale copy)

## Rebuilding after editing content

Content lives in `build-scripts/content_{food,kids,juice}.py` as plain Python data
structures (helpers in `helpers.py`). To regenerate:

```
cd build-scripts
python build.py ..            # rewrites ../index.html, ../manifest.json, ../sw.js
python make_icons.py ..       # only needed if you change the icon
```

Then commit and push — GitHub Pages redeploys in ~1–3 min.

## Disclaimer

Personal study notes transcribed from the Satvic Movement books by Subah Jain /
Subah Saraf. Not medical advice.
