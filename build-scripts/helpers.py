# -*- coding: utf-8 -*-
"""Small helpers for authoring Leo-Health pages."""
import html as _html
import re


def slug(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def _lines(items):
    return "\n".join("      <li>%s</li>" % i for i in items)


def P(*paras):
    return "\n".join("    <p>%s</p>" % p for p in paras)


def UL(items, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return '    <ul%s>\n%s\n    </ul>' % (c, _lines(items))


def OL(items):
    return '    <ol>\n%s\n    </ol>' % _lines(items)


def H2(t):
    return "    <h2>%s</h2>" % t


def H3(t):
    return "    <h3>%s</h3>" % t


def NOTE(*paras):
    inner = "".join("<p>%s</p>" % p for p in paras)
    return '    <div class="callout note"><span class="callout-label">Note</span>%s</div>' % inner


def TIP(*paras):
    inner = "".join("<p>%s</p>" % p for p in paras)
    return '    <div class="callout tip"><span class="callout-label">Tip</span>%s</div>' % inner


def QUOTE(text, who=""):
    cite = ('<cite>%s</cite>' % who) if who else ""
    return '    <blockquote>%s%s</blockquote>' % (text, cite)


def TABLE(headers, rows):
    h = "".join("<th>%s</th>" % x for x in headers)
    body = ""
    for r in rows:
        body += "<tr>%s</tr>" % "".join("<td>%s</td>" % x for x in r)
    return ('    <div class="tbl-wrap"><table><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>') % (h, body)


def dl(pairs):
    inner = "".join("<dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in pairs)
    return '    <dl class="term-list">%s</dl>' % inner


def recipe(meta=None, intro=None, groups=None, method=None, prep=None,
           notes=None, bestfor=None, sub=None):
    """Render a recipe body.

    groups: list of (heading_or_None, [ingredient, ...])
    method: list of steps (str)  OR list of (heading, [steps])
    prep:   list of strings
    notes:  list of strings (rendered as Tip/Note callouts if prefixed 'Tip:' / 'Note:')
    bestfor: list of strings that ARE ticked
    """
    out = []
    if sub:
        out.append('    <p class="recipe-sub">%s</p>' % sub)
    if meta:
        out.append('    <p class="recipe-meta">%s</p>' % meta)
    if intro:
        for p in intro:
            out.append("    <p>%s</p>" % p)

    out.append('    <div class="recipe-cols">')
    out.append('    <div class="recipe-ing">')
    out.append("      <h3>Ingredients</h3>")
    for gname, items in (groups or []):
        if gname:
            out.append('      <p class="ing-group">%s</p>' % gname)
        out.append("      <ul>")
        for it in items:
            out.append("        <li>%s</li>" % it)
        out.append("      </ul>")
    out.append("    </div>")

    out.append('    <div class="recipe-method">')
    out.append("      <h3>Method</h3>")
    if method and isinstance(method[0], (list, tuple)):
        for mh, steps in method:
            out.append("      <p class=\"ing-group\">%s</p>" % mh)
            out.append("      <ol>")
            for s in steps:
                out.append("        <li>%s</li>" % s)
            out.append("      </ol>")
    else:
        out.append("      <ol>")
        for s in (method or []):
            out.append("        <li>%s</li>" % s)
        out.append("      </ol>")
    out.append("    </div>")
    out.append("    </div>")

    if prep:
        out.append('    <div class="callout prep"><span class="callout-label">Pre-preparation</span>'
                   + "".join("<p>%s</p>" % p for p in prep) + "</div>")

    for n in (notes or []):
        if n.startswith("Tip:"):
            out.append(TIP(n[4:].strip()))
        elif n.startswith("Note:"):
            out.append(NOTE(n[5:].strip()))
        else:
            out.append(NOTE(n))

    if bestfor:
        chips = "".join('<span class="bf-chip">%s</span>' % b for b in bestfor)
        out.append('    <div class="bestfor"><span class="bf-label">Best for</span>%s</div>' % chips)

    return "\n".join(out)
