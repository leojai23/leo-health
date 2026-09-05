# -*- coding: utf-8 -*-
"""Build the Leo-Health single-file PWA (index.html + manifest.json + sw.js).

Run:  python build.py [output_dir]
Default output_dir = ../../../../Leo-Health  is NOT assumed; pass it explicitly,
or it writes ./dist next to this script.
"""
import json
import os
import re
import sys
import hashlib

from content_food import SUBJECT as FOOD
from content_kids import SUBJECT as KIDS
from content_juice import SUBJECT as JUICE

SUBJECTS = [FOOD, KIDS, JUICE]

SITE_TITLE = "Leo-Health"
SITE_SUB = "Satvic Movement reference — Food, Kids & Juice"

# --------------------------------------------------------------------- utils ---
_tag = re.compile(r"<[^>]+>")
_ws = re.compile(r"\s+")


def strip_tags(s):
    return _ws.sub(" ", _tag.sub(" ", s)).strip()


def headings(body):
    out = []
    for m in re.finditer(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S):
        out.append(strip_tags(m.group(1)))
    for m in re.finditer(r"<dt>(.*?)</dt>", body, re.S):
        out.append(strip_tags(m.group(1)))
    return out


def page_slug(subject, page):
    return "%s-%s" % (subject["id"], page["id"])


# ------------------------------------------------------------------ assemble ---
def build_pages_html():
    parts = []
    for sub in SUBJECTS:
        for sec in sub["sections"]:
            for pg in sec["pages"]:
                sid = page_slug(sub, pg)
                parts.append(
                    '<article class="page" id="%s" data-subject="%s" '
                    'data-section="%s" hidden>\n'
                    '    <div class="page-crumb">%s <span>&rsaquo;</span> %s</div>\n'
                    '    <h1>%s</h1>\n'
                    '    <div class="prevnext" data-for="%s"></div>\n'
                    '%s\n'
                    '</article>' % (
                        sid, sub["id"], sec["id"],
                        sub["name"], _ws.sub(" ", strip_tags(sec["name"])),
                        pg["title"], sid, pg["body"],
                    )
                )
    return "\n\n".join(parts)


def build_home_html():
    cards = []
    for sub in SUBJECTS:
        npages = sum(len(s["pages"]) for s in sub["sections"])
        first = page_slug(sub, sub["sections"][0]["pages"][0])
        cards.append(
            '      <a class="subj-card" href="#%s" style="--accent:%s">\n'
            '        <span class="subj-tag">%s</span>\n'
            '        <h3>%s</h3>\n'
            '        <p>%s</p>\n'
            '        <span class="subj-meta"><span class="sc-count">%d pages</span>'
            '<span class="sc-prog" data-subject="%s"></span></span>\n'
            '      </a>' % (
                first, sub["accent"], sub["tag"], sub["name"], sub["blurb"],
                npages, sub["id"],
            )
        )
    return (
        '  <section class="home-hero">\n'
        '    <h1>%s</h1>\n'
        '    <p class="home-sub">%s</p>\n'
        '    <div class="home-progress"><div class="hp-bar"><span id="hpFill"></span></div>'
        '<span id="hpText"></span></div>\n'
        '  </section>\n'
        '  <div id="continueCard"></div>\n'
        '  <section class="subj-grid">\n%s\n  </section>\n'
        '  <p class="home-foot">A private reference notebook. Content from the Satvic '
        'Movement books by Subah Jain / Subah Saraf. Not medical advice.</p>'
        % (SITE_TITLE, SITE_SUB, "\n".join(cards))
    )


def build_nav_json():
    nav = []
    for sub in SUBJECTS:
        s = {"id": sub["id"], "name": sub["name"], "accent": sub["accent"], "sections": []}
        for sec in sub["sections"]:
            s["sections"].append({
                "id": sec["id"], "name": sec["name"],
                "pages": [{"id": page_slug(sub, p), "title": p["title"]} for p in sec["pages"]],
            })
        nav.append(s)
    return nav


def build_search_json():
    idx = []
    for sub in SUBJECTS:
        for sec in sub["sections"]:
            for pg in sec["pages"]:
                idx.append({
                    "id": page_slug(sub, pg),
                    "t": strip_tags(pg["title"]),
                    "s": sub["name"],
                    "sec": _ws.sub(" ", strip_tags(sec["name"])),
                    "h": headings(pg["body"])[:40],
                })
    return idx


def build_seq_json():
    """Flat ordered list of page ids per subject, for prev/next."""
    seq = {}
    for sub in SUBJECTS:
        seq[sub["id"]] = [page_slug(sub, p) for s in sub["sections"] for p in s["pages"]]
    return seq


# ----------------------------------------------------------------------- CSS ---
CSS = r"""
:root{
  --bg:#f6f4ef; --bg-2:#fffdf8; --panel:#ffffff; --ink:#2b2a26; --ink-soft:#5f5c54;
  --line:#e4dfd3; --accent:#4f7bb0; --accent-ink:#fff;
  --chip:#eef2f7; --chip-ink:#42607f; --quote:#f0ede4; --shadow:0 1px 3px rgba(40,35,25,.08),0 8px 24px rgba(40,35,25,.06);
  --maxw:52rem;
}
[data-theme="sepia"]{
  --bg:#efe6d4; --bg-2:#f7efdf; --panel:#f9f2e4; --ink:#43382a; --ink-soft:#6c5c46;
  --line:#ddceb2; --chip:#e8dcc3; --chip-ink:#6b573a; --quote:#e7dcc4;
  --shadow:0 1px 3px rgba(90,70,40,.1),0 8px 22px rgba(90,70,40,.08);
}
[data-theme="dark"]{
  --bg:#181a1d; --bg-2:#1f2226; --panel:#23272c; --ink:#e6e4df; --ink-soft:#a7a49c;
  --line:#333941; --accent:#79a7d8; --chip:#2b333d; --chip-ink:#9fc2e6; --quote:#20242a;
  --shadow:0 1px 3px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}
[data-theme="night"]{
  --bg:#0b0d12; --bg-2:#0f1218; --panel:#12151c; --ink:#c9d1dc; --ink-soft:#7f8794;
  --line:#20242e; --accent:#6ea8e6; --chip:#182030; --chip-ink:#8fb6e0; --quote:#0f1218;
  --shadow:0 1px 2px rgba(0,0,0,.6),0 12px 32px rgba(0,0,0,.5);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  background:var(--bg); color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  -webkit-text-size-adjust:100%;
}
a{color:var(--accent); text-decoration:none}
a:hover{text-decoration:underline}

/* ---- layout ---- */
.app{display:flex; min-height:100vh}
.sidebar{
  width:19rem; flex:0 0 19rem; background:var(--bg-2); border-right:1px solid var(--line);
  position:sticky; top:0; height:100vh; overflow-y:auto; padding:1rem .5rem 4rem;
}
.side-head{display:flex; align-items:center; gap:.6rem; padding:.4rem .6rem 1rem}
.side-head .logo{
  width:2rem;height:2rem;border-radius:.55rem;flex:0 0 2rem;display:grid;place-items:center;
  background:var(--accent); color:#fff; font-weight:800; font-size:1.05rem;
}
.side-head b{font-size:1.02rem}
.side-head small{display:block; color:var(--ink-soft); font-size:.74rem; font-weight:500}
.progress-mini{padding:.1rem .7rem 1rem}
.progress-mini .pm-bar{height:6px;border-radius:99px;background:var(--line);overflow:hidden}
.progress-mini .pm-bar span{display:block;height:100%;background:var(--accent);width:0}
.progress-mini small{color:var(--ink-soft);font-size:.72rem;display:block;margin-top:.35rem}

nav.tree{font-size:.9rem}
.tree .subj{margin:.15rem 0 .5rem}
.tree .subj>button{
  width:100%;text-align:left;background:none;border:0;color:var(--ink);font:inherit;font-weight:700;
  padding:.5rem .6rem;border-radius:.5rem;cursor:pointer;display:flex;align-items:center;gap:.5rem;
}
.tree .subj>button:hover{background:var(--chip)}
.tree .subj>button .dot{width:.6rem;height:.6rem;border-radius:99px;flex:0 0 .6rem}
.tree .subj>button .caret{margin-left:auto;transition:transform .15s;color:var(--ink-soft)}
.tree .subj.collapsed>button .caret{transform:rotate(-90deg)}
.tree .subj.collapsed .sec-list{display:none}
.sec{margin:.15rem 0 .3rem .35rem}
.sec>.sec-name{
  color:var(--ink-soft);font-weight:600;font-size:.76rem;text-transform:uppercase;
  letter-spacing:.03em;padding:.5rem .6rem .25rem;
}
.sec a{
  display:flex;gap:.5rem;align-items:baseline;padding:.34rem .6rem;border-radius:.45rem;
  color:var(--ink);
}
.sec a:hover{background:var(--chip);text-decoration:none}
.sec a.active{background:var(--accent);color:var(--accent-ink)}
.sec a.active .tick{color:var(--accent-ink)}
.sec a .tick{flex:0 0 1rem;color:var(--accent);font-size:.8rem;opacity:0}
.sec a.read .tick{opacity:1}
.sec a .lbl{flex:1}

/* ---- main ---- */
.main{flex:1; min-width:0; display:flex; flex-direction:column}
.topbar{
  position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:.5rem;
  padding:.5rem .9rem; background:color-mix(in srgb,var(--bg-2) 90%,transparent);
  backdrop-filter:blur(8px); border-bottom:1px solid var(--line);
}
.topbar .menu-btn{display:none}
.topbar .spacer{flex:1}
.icon-btn{
  border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer;
  width:2.2rem;height:2.2rem;border-radius:.6rem;display:grid;place-items:center;font-size:1rem;
}
.icon-btn:hover{border-color:var(--accent);color:var(--accent)}
.seg{display:flex;border:1px solid var(--line);border-radius:.6rem;overflow:hidden;background:var(--panel)}
.seg button{
  border:0;background:none;color:var(--ink-soft);cursor:pointer;padding:.4rem .55rem;font:inherit;font-size:.82rem;
}
.seg button.on{background:var(--accent);color:#fff}

.wrap{max-width:var(--maxw); margin:0 auto; padding:2rem 1.4rem 6rem; width:100%}
.page-crumb{color:var(--ink-soft);font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.03em;margin-bottom:.4rem}
.page-crumb span{opacity:.5;margin:0 .15rem}
.page h1{font-size:1.9rem;line-height:1.2;margin:.1rem 0 .2rem;letter-spacing:-.01em}
.page h2{font-size:1.22rem;margin:2rem 0 .5rem;padding-top:.3rem}
.page h3{font-size:1rem;margin:1.4rem 0 .4rem;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-soft)}
.page p{margin:.7rem 0}
.page ul,.page ol{margin:.6rem 0 .9rem;padding-left:1.35rem}
.page li{margin:.3rem 0}
.page ul{list-style:disc}

blockquote{
  margin:1rem 0;padding:.8rem 1.1rem;background:var(--quote);border-left:3px solid var(--accent);
  border-radius:.3rem;font-style:italic;color:var(--ink-soft)
}
blockquote cite{display:block;margin-top:.4rem;font-style:normal;font-weight:600;font-size:.82rem;color:var(--ink-soft)}

.callout{margin:1rem 0;padding:.8rem 1rem;border-radius:.55rem;background:var(--bg-2);border:1px solid var(--line);font-size:.94rem}
.callout p{margin:.35rem 0}
.callout p:first-child{margin-top:0}.callout p:last-child{margin-bottom:0}
.callout-label{display:inline-block;font-weight:700;font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--accent);margin-bottom:.25rem}
.callout.tip{border-left:3px solid #57a05a}.callout.tip .callout-label{color:#57a05a}
.callout.prep{border-left:3px solid #b0863f}.callout.prep .callout-label{color:#b0863f}

dl.term-list{margin:1rem 0;display:grid;gap:.1rem}
dl.term-list dt{font-weight:700;margin-top:.7rem}
dl.term-list dd{margin:.1rem 0 .2rem;color:var(--ink-soft)}

.tbl-wrap{overflow-x:auto;margin:1rem 0;border:1px solid var(--line);border-radius:.5rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;min-width:30rem}
th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--bg-2);font-size:.76rem;text-transform:uppercase;letter-spacing:.03em;color:var(--ink-soft)}
tr:last-child td{border-bottom:0}

/* ---- recipe ---- */
.recipe-sub{display:inline-block;font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;
  color:var(--chip-ink);background:var(--chip);padding:.2rem .55rem;border-radius:99px;margin:.2rem 0 .4rem}
.recipe-meta{color:var(--ink-soft);font-weight:600;font-size:.9rem;margin:.2rem 0 .6rem}
.recipe-cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:1.6rem;margin:1rem 0;align-items:start}
.recipe-ing{background:var(--bg-2);border:1px solid var(--line);border-radius:.6rem;padding:.9rem 1rem}
.recipe-ing h3,.recipe-method h3{margin:.1rem 0 .5rem}
.recipe-ing ul{list-style:none;padding-left:0;margin:.2rem 0 .6rem}
.recipe-ing li{padding-left:1rem;position:relative;margin:.35rem 0;font-size:.92rem}
.recipe-ing li:before{content:"";position:absolute;left:0;top:.62rem;width:.32rem;height:.32rem;border-radius:99px;background:var(--accent)}
.ing-group{font-weight:700;font-size:.8rem;text-transform:uppercase;letter-spacing:.03em;color:var(--ink-soft);margin:.7rem 0 .1rem}
.recipe-method ol{padding-left:1.2rem}
.recipe-method li{margin:.45rem 0}
.bestfor{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;margin:1rem 0}
.bf-label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-soft)}
.bf-chip{background:var(--chip);color:var(--chip-ink);border-radius:99px;padding:.2rem .6rem;font-size:.8rem;font-weight:600}

.prevnext{display:flex;justify-content:space-between;gap:.6rem;margin:1rem 0 1.6rem}
.prevnext a{
  flex:1;border:1px solid var(--line);border-radius:.55rem;padding:.5rem .7rem;font-size:.82rem;
  color:var(--ink-soft);background:var(--panel);max-width:48%;
}
.prevnext a:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.prevnext a.nx{text-align:right}
.prevnext a b{display:block;color:var(--ink);font-size:.9rem;margin-top:.1rem}
.prevnext a .dir{font-size:.7rem;text-transform:uppercase;letter-spacing:.05em}

/* ---- home ---- */
.home-hero h1{font-size:2.1rem;margin:.2rem 0 .2rem}
.home-sub{color:var(--ink-soft);margin:0 0 1rem}
.home-progress{display:flex;align-items:center;gap:.7rem;max-width:24rem}
.home-progress .hp-bar{flex:1;height:8px;border-radius:99px;background:var(--line);overflow:hidden}
.home-progress .hp-bar span{display:block;height:100%;background:var(--accent);width:0}
.home-progress #hpText{font-size:.8rem;color:var(--ink-soft);font-weight:600;white-space:nowrap}
.subj-grid{display:grid;grid-template-columns:1fr;gap:1rem;margin:1.6rem 0}
@media(min-width:40rem){.subj-grid{grid-template-columns:1fr 1fr 1fr}}
.subj-card{
  display:block;border:1px solid var(--line);border-radius:.8rem;padding:1.1rem 1.15rem;background:var(--panel);
  box-shadow:var(--shadow);border-top:3px solid var(--accent);color:var(--ink);
}
.subj-card:hover{text-decoration:none;transform:translateY(-2px);transition:transform .12s}
.subj-tag{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--accent)}
.subj-card h3{margin:.3rem 0 .4rem;font-size:1.15rem}
.subj-card p{margin:0;color:var(--ink-soft);font-size:.88rem;line-height:1.55}
.subj-meta{display:flex;justify-content:space-between;margin-top:.8rem;font-size:.76rem;color:var(--ink-soft);font-weight:600}
#continueCard a{
  display:flex;gap:.8rem;align-items:center;border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:.6rem;padding:.8rem 1rem;background:var(--bg-2);color:var(--ink);margin:.4rem 0 0
}
#continueCard a:hover{text-decoration:none;border-color:var(--accent)}
#continueCard .cc-k{font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-soft);font-weight:700}
#continueCard b{display:block}
.home-foot{color:var(--ink-soft);font-size:.8rem;margin-top:2.5rem;border-top:1px solid var(--line);padding-top:1rem}

/* ---- search overlay ---- */
.ov{position:fixed;inset:0;z-index:50;display:none;background:rgba(20,18,12,.4)}
.ov.on{display:block}
.ov-box{max-width:40rem;margin:8vh auto 0;background:var(--panel);border:1px solid var(--line);border-radius:.8rem;
  box-shadow:var(--shadow);overflow:hidden}
.ov-box input{
  width:100%;border:0;border-bottom:1px solid var(--line);background:none;color:var(--ink);
  font:inherit;font-size:1.05rem;padding:1rem 1.1rem;outline:none
}
.ov-res{max-height:60vh;overflow-y:auto}
.ov-res a{display:block;padding:.7rem 1.1rem;border-bottom:1px solid var(--line);color:var(--ink)}
.ov-res a:hover,.ov-res a.sel{background:var(--chip);text-decoration:none}
.ov-res .r-t{font-weight:600}
.ov-res .r-c{font-size:.78rem;color:var(--ink-soft)}
.ov-res .r-h{font-size:.78rem;color:var(--ink-soft);margin-top:.15rem}
.ov-empty{padding:1.2rem 1.1rem;color:var(--ink-soft)}
mark{background:color-mix(in srgb,var(--accent) 30%,transparent);color:inherit;border-radius:.15rem}

/* ---- fabs ---- */
.fabs{position:fixed;right:1rem;bottom:1rem;z-index:30;display:flex;flex-direction:column;gap:.5rem}
.fabs button{
  width:2.8rem;height:2.8rem;border-radius:99px;border:1px solid var(--line);background:var(--panel);
  color:var(--ink);cursor:pointer;box-shadow:var(--shadow);font-size:1.05rem
}
.fabs button:hover{color:var(--accent);border-color:var(--accent)}

.backdrop{display:none}
@media(max-width:60rem){
  .sidebar{position:fixed;left:0;top:0;z-index:60;transform:translateX(-100%);transition:transform .2s;box-shadow:var(--shadow)}
  .app.nav-open .sidebar{transform:none}
  .app.nav-open .backdrop{display:block;position:fixed;inset:0;z-index:55;background:rgba(0,0,0,.35)}
  .topbar .menu-btn{display:grid}
  .recipe-cols{grid-template-columns:1fr;gap:1rem}
}

@media print{
  .sidebar,.topbar,.fabs,.prevnext,.ov,.backdrop,#continueCard,.home-progress{display:none !important}
  .app{display:block}.wrap{max-width:none;padding:0}
  .page[hidden]{display:none}
  body{background:#fff;color:#000;font-size:11pt}
  .recipe-cols{grid-template-columns:1fr 1.4fr}
  blockquote,.callout,.recipe-ing{border-color:#bbb}
  a{color:#000;text-decoration:none}
}
"""

# ------------------------------------------------------------------------ JS ---
JS = r"""
(function(){
"use strict";
var NAV = __NAV__;
var SEARCH = __SEARCH__;
var SEQ = __SEQ__;
var PKEY = "leo-health-progress";
var TKEY = "leo-health-theme";

var $ = function(s,r){return (r||document).querySelector(s);};
var $$ = function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));};

/* ---------- progress ---------- */
function readProg(){ try{ return JSON.parse(localStorage.getItem(PKEY)||"{}")||{}; }catch(e){ return {}; } }
function writeProg(p){ try{ localStorage.setItem(PKEY, JSON.stringify(p)); }catch(e){} }
function markRead(id){ var p=readProg(); if(!p[id]){ p[id]=Date.now(); writeProg(p); } paintProgress(); }

var TOTAL = SEARCH.length;
var TITLES = {}; SEARCH.forEach(function(r){ TITLES[r.id]=r.t; });

function paintProgress(){
  var p=readProg(), n=Object.keys(p).length;
  var pct = TOTAL? Math.round(n/TOTAL*100):0;
  var pm=$("#pmFill"); if(pm) pm.style.width=pct+"%";
  var pmt=$("#pmText"); if(pmt) pmt.textContent = n+" / "+TOTAL+" pages read";
  var hf=$("#hpFill"); if(hf) hf.style.width=pct+"%";
  var ht=$("#hpText"); if(ht) ht.textContent = pct+"% · "+n+"/"+TOTAL;
  $$(".sec a").forEach(function(a){
    a.classList.toggle("read", !!p[a.dataset.id]);
  });
  NAV.forEach(function(s){
    var ids=[]; s.sections.forEach(function(sec){ sec.pages.forEach(function(pg){ ids.push(pg.id); }); });
    var done=ids.filter(function(i){return p[i];}).length;
    $$('.sc-prog[data-subject="'+s.id+'"]').forEach(function(el){ el.textContent = done+"/"+ids.length+" read"; });
  });
  paintContinue();
}

function paintContinue(){
  var host=$("#continueCard"); if(!host) return;
  var p=readProg(), best=null,bt=0;
  Object.keys(p).forEach(function(k){ if(p[k]>bt){bt=p[k];best=k;} });
  if(!best || !TITLES[best]){ host.innerHTML=""; return; }
  // suggest the NEXT unread page in that subject's sequence
  var subj=best.split("-")[0], list=SEQ[subj]||[], i=list.indexOf(best), target=best, k="Continue reading";
  for(var j=i+1;j<list.length;j++){ if(!p[list[j]]){ target=list[j]; k="Up next"; break; } }
  host.innerHTML='<a href="#'+target+'"><span>→</span><span><span class="cc-k">'+k+
    '</span><b>'+TITLES[target]+'</b></span></a>';
}

/* ---------- theme ---------- */
function setTheme(t){
  document.documentElement.setAttribute("data-theme", t);
  try{ localStorage.setItem(TKEY, t); }catch(e){}
  $$("#themeSeg button").forEach(function(b){ b.classList.toggle("on", b.dataset.t===t); });
}
(function initTheme(){
  var t; try{ t=localStorage.getItem(TKEY); }catch(e){}
  setTheme(t||"day");
})();

/* ---------- sidebar ---------- */
function buildNav(){
  var tree=$("#tree"); tree.innerHTML="";
  NAV.forEach(function(s){
    var subj=document.createElement("div"); subj.className="subj collapsed"; subj.dataset.id=s.id;
    var btn=document.createElement("button");
    btn.innerHTML='<span class="dot" style="background:'+s.accent+'"></span><span>'+s.name+
      '</span><span class="caret">▾</span>';
    btn.onclick=function(){ subj.classList.toggle("collapsed"); };
    subj.appendChild(btn);
    var list=document.createElement("div"); list.className="sec-list";
    s.sections.forEach(function(sec){
      var wrap=document.createElement("div"); wrap.className="sec";
      var nm=document.createElement("div"); nm.className="sec-name"; nm.innerHTML=sec.name;
      wrap.appendChild(nm);
      sec.pages.forEach(function(pg){
        var a=document.createElement("a");
        a.href="#"+pg.id; a.dataset.id=pg.id;
        a.innerHTML='<span class="tick">✓</span><span class="lbl">'+pg.title+'</span>';
        wrap.appendChild(a);
      });
      list.appendChild(wrap);
    });
    subj.appendChild(list);
    tree.appendChild(subj);
  });
}

/* ---------- routing ---------- */
function show(id){
  var pages=$$(".page"), home=$("#home"), target=id&&$("#"+CSS.escape(id));
  if(id==="home" || !target){
    home.hidden=false; pages.forEach(function(p){ p.hidden=true; });
    document.title="Leo-Health";
  }else{
    home.hidden=true;
    pages.forEach(function(p){ p.hidden = (p.id!==id); });
    document.title = (TITLES[id]||"Leo-Health") + " — Leo-Health";
    fillPrevNext(id);
    markRead(id);
  }
  $$(".sec a").forEach(function(a){ a.classList.toggle("active", a.dataset.id===id); });
  // expand only the subject that owns this page
  if(id && id!=="home"){
    var subj=id.split("-")[0];
    $$(".subj").forEach(function(d){ d.classList.toggle("collapsed", d.dataset.id!==subj); });
    var active=$(".sec a.active"); if(active) active.scrollIntoView({block:"nearest"});
  }
  $("#app").classList.remove("nav-open");
  window.scrollTo(0,0);
}
function route(){
  var h=(location.hash||"#home").slice(1);
  show(h||"home");
}
function fillPrevNext(id){
  var subj=id.split("-")[0], list=SEQ[subj]||[], i=list.indexOf(id);
  var box=$('.prevnext[data-for="'+id+'"]'); if(!box) return;
  var prev=i>0?list[i-1]:null, next=i>=0&&i<list.length-1?list[i+1]:null, html="";
  html += prev ? '<a class="pv" href="#'+prev+'"><span class="dir">← Prev</span><b>'+TITLES[prev]+'</b></a>' : '<span></span>';
  html += next ? '<a class="nx" href="#'+next+'"><span class="dir">Next →</span><b>'+TITLES[next]+'</b></a>' : '<span></span>';
  box.innerHTML=html;
}

/* ---------- search ---------- */
var ov=$("#ov"), ovIn=$("#ovIn"), ovRes=$("#ovRes"), selIdx=-1, curRes=[];
function openSearch(){ ov.classList.add("on"); ovIn.value=""; ovRes.innerHTML=""; selIdx=-1; curRes=[]; setTimeout(function(){ ovIn.focus(); },30); }
function closeSearch(){ ov.classList.remove("on"); }
function esc(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"); }
function hl(text,q){ if(!q) return text; try{ return text.replace(new RegExp("("+esc(q)+")","ig"),"<mark>$1</mark>"); }catch(e){ return text; } }
function runSearch(){
  var q=ovIn.value.trim(); if(!q){ ovRes.innerHTML=""; curRes=[]; return; }
  var ql=q.toLowerCase(), out=[];
  SEARCH.forEach(function(r){
    var score=0, hHit="";
    if(r.t.toLowerCase().indexOf(ql)>=0) score+=10;
    if(r.s.toLowerCase().indexOf(ql)>=0) score+=2;
    if(r.sec.toLowerCase().indexOf(ql)>=0) score+=2;
    for(var i=0;i<r.h.length;i++){ if(r.h[i].toLowerCase().indexOf(ql)>=0){ score+=4; if(!hHit) hHit=r.h[i]; } }
    if(score>0) out.push({r:r,score:score,h:hHit});
  });
  out.sort(function(a,b){ return b.score-a.score; });
  curRes=out.slice(0,40); selIdx=curRes.length?0:-1;
  if(!curRes.length){ ovRes.innerHTML='<div class="ov-empty">No matches for &ldquo;'+q+'&rdquo;</div>'; return; }
  ovRes.innerHTML=curRes.map(function(o,i){
    return '<a href="#'+o.r.id+'" data-i="'+i+'" class="'+(i===0?"sel":"")+'">'+
      '<div class="r-t">'+hl(o.r.t,q)+'</div>'+
      '<div class="r-c">'+o.r.s+' · '+o.r.sec+'</div>'+
      (o.h?'<div class="r-h">'+hl(o.h,q)+'</div>':'')+'</a>';
  }).join("");
}
function moveSel(d){
  var links=$$("a",ovRes); if(!links.length) return;
  selIdx=(selIdx+d+links.length)%links.length;
  links.forEach(function(a,i){ a.classList.toggle("sel", i===selIdx); if(i===selIdx) a.scrollIntoView({block:"nearest"}); });
}

/* ---------- events ---------- */
window.addEventListener("hashchange", route);
document.addEventListener("DOMContentLoaded", function(){
  buildNav();
  route();
  paintProgress();

  $("#menuBtn").onclick=function(){ $("#app").classList.toggle("nav-open"); };
  $("#backdrop").onclick=function(){ $("#app").classList.remove("nav-open"); };
  $("#homeFab").onclick=function(){ location.hash="#home"; };
  $("#searchFab").onclick=openSearch;
  $("#printFab").onclick=function(){ window.print(); };
  $("#searchBtn").onclick=openSearch;
  $("#printBtn").onclick=function(){ window.print(); };
  $$("#themeSeg button").forEach(function(b){ b.onclick=function(){ setTheme(b.dataset.t); }; });

  ovIn.addEventListener("input", runSearch);
  ov.addEventListener("click", function(e){ if(e.target===ov) closeSearch(); });
  ovRes.addEventListener("click", function(e){ var a=e.target.closest("a"); if(a){ closeSearch(); } });
  document.addEventListener("keydown", function(e){
    if(e.key==="/" && !/input|textarea/i.test((e.target.tagName||"")) && !ov.classList.contains("on")){
      e.preventDefault(); openSearch(); return;
    }
    if(ov.classList.contains("on")){
      if(e.key==="Escape") closeSearch();
      else if(e.key==="ArrowDown"){ e.preventDefault(); moveSel(1); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); moveSel(-1); }
      else if(e.key==="Enter"){ var a=$$("a",ovRes)[selIdx]; if(a){ location.hash=a.getAttribute("href"); closeSearch(); } }
      return;
    }
    if(/input|textarea/i.test((e.target.tagName||""))) return;
    var cur=(location.hash||"#home").slice(1);
    if(cur==="home") return;
    var subj=cur.split("-")[0], list=SEQ[subj]||[], i=list.indexOf(cur);
    if(e.key==="ArrowLeft" && i>0) location.hash="#"+list[i-1];
    else if(e.key==="ArrowRight" && i>=0 && i<list.length-1) location.hash="#"+list[i+1];
  });

  if("serviceWorker" in navigator){
    navigator.serviceWorker.register("sw.js").catch(function(){});
  }
});
})();
"""


# ------------------------------------------------------------------- render ---
def render_index():
    nav = json.dumps(build_nav_json(), ensure_ascii=False, separators=(",", ":"))
    search = json.dumps(build_search_json(), ensure_ascii=False, separators=(",", ":"))
    seq = json.dumps(build_seq_json(), ensure_ascii=False, separators=(",", ":"))
    js = (JS.replace("__NAV__", nav).replace("__SEARCH__", search).replace("__SEQ__", seq))

    html = """<!DOCTYPE html>
<html lang="en" data-theme="day">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#4f7bb0">
<meta name="description" content="Leo-Health — a private Satvic Movement reference notebook: Satvic Food, Satvic Kids and the 3-Day Juice Diet.">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-192.png">
<title>Leo-Health</title>
<style>%s</style>
</head>
<body>
<div class="app" id="app">
  <div class="backdrop" id="backdrop"></div>
  <aside class="sidebar" id="sidebar">
    <div class="side-head">
      <span class="logo">☘</span>
      <span><b>Leo-Health</b><small>Satvic reference</small></span>
    </div>
    <div class="progress-mini">
      <div class="pm-bar"><span id="pmFill"></span></div>
      <small id="pmText"></small>
    </div>
    <nav class="tree" id="tree"></nav>
  </aside>

  <div class="main">
    <div class="topbar">
      <button class="icon-btn menu-btn" id="menuBtn" title="Menu">☰</button>
      <a class="icon-btn" href="#home" title="Home">⌂</a>
      <div class="spacer"></div>
      <div class="seg" id="themeSeg" title="Reading theme">
        <button data-t="day">Day</button>
        <button data-t="sepia">Sepia</button>
        <button data-t="dark">Dark</button>
        <button data-t="night">Night</button>
      </div>
      <button class="icon-btn" id="searchBtn" title="Search  ( / )">⚲</button>
      <button class="icon-btn" id="printBtn" title="Print">⎙</button>
    </div>

    <div class="wrap">
      <section id="home">
%s
      </section>
%s
    </div>
  </div>
</div>

<div class="fabs">
  <button id="homeFab" title="Home">⌂</button>
  <button id="searchFab" title="Search">⚲</button>
  <button id="printFab" title="Print">⎙</button>
</div>

<div class="ov" id="ov">
  <div class="ov-box">
    <input id="ovIn" type="text" placeholder="Search all pages…" autocomplete="off" spellcheck="false">
    <div class="ov-res" id="ovRes"></div>
  </div>
</div>

<script>%s</script>
</body>
</html>
""" % (CSS, build_home_html(), build_pages_html(), js)
    return html


MANIFEST = {
    "name": "Leo-Health — Satvic Reference",
    "short_name": "Leo-Health",
    "description": "Private Satvic Movement reference: Satvic Food, Satvic Kids and the 3-Day Juice Diet.",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "background_color": "#f6f4ef",
    "theme_color": "#4f7bb0",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
    ],
}

SW_TMPL = """/* Leo-Health service worker — cache-first, versioned by content hash */
var CACHE = "leo-health-%s";
var ASSETS = ["./", "./index.html", "./manifest.json", "./icon-192.png", "./icon-512.png"];
self.addEventListener("install", function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){ return c.addAll(ASSETS); }));
});
self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.map(function(k){ if(k!==CACHE) return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});
self.addEventListener("fetch", function(e){
  if(e.request.method!=="GET") return;
  e.respondWith(
    caches.match(e.request).then(function(hit){
      return hit || fetch(e.request).then(function(res){
        var copy=res.clone();
        caches.open(CACHE).then(function(c){ c.put(e.request, copy); });
        return res;
      }).catch(function(){ return caches.match("./index.html"); });
    })
  );
});
"""


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "dist")
    out = os.path.abspath(out)
    os.makedirs(out, exist_ok=True)

    html = render_index()
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(MANIFEST, f, ensure_ascii=False, indent=2)

    digest = hashlib.sha1(html.encode("utf-8")).hexdigest()[:12]
    with open(os.path.join(out, "sw.js"), "w", encoding="utf-8") as f:
        f.write(SW_TMPL % digest)

    npages = sum(len(s["pages"]) for sub in SUBJECTS for s in sub["sections"])
    print("wrote %s" % out)
    print("  index.html  %.1f KB" % (len(html.encode("utf-8")) / 1024))
    print("  %d subjects, %d pages, sw hash %s" % (len(SUBJECTS), npages, digest))


if __name__ == "__main__":
    main()
