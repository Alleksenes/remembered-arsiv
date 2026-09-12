# -*- coding: utf-8 -*-
"""Obsidian markdown → NOCTURNE (koyu) temalı, iç-bağlantılı HTML.
- Ön temizlik: [[..\\|alias]] → [[..|alias]]; satır-sonunda "\\" devamını yapıştır.
- Wikilink: hedef paket içindeyse GERÇEK <a href="x.html">; değilse sessiz metin.
- deprecated/archived yolu hedeflerse bağlantı düşer, yalnız etiket kalır (editöryel).
"""
import re
from pathlib import Path

GEN3FONTS = Path.home() / "Documents/GitHub/remembered-pitchdecks-gen3/fonts.css"

#: NOCTURNE paleti (deck-b esas alındı; site bronz/altın ailesi)
T = {
    "paper": "#0C0C0C", "paper2": "#181818", "paper3": "#111111",
    "ink": "#F5F2E8", "ink2": "#E4D2B4", "ink3": "#B4A284",
    "sec": "#8A7A5F", "bord": "#3A2F22", "bronze": "#DEBA84",
    "bronze2": "#E4C08A", "amber": "#78603C", "gold": "#DEBA84",
    "mono": "'JetBrains Mono',monospace", "serif": "'Playfair Display','Bodoni Moda',Georgia,serif",
    "body": "'Newsreader',Georgia,serif", "sans": "'Inter',system-ui,sans-serif",
}


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def clean_md(t):
    # Obsidian bozuk atıf kaliplari: çift/tek tersbölü+pipe -> pipe
    t = t.replace("\\\\|", "|")
    t = t.replace("\\|", "|")
    # satır sonunda "\" devamını satıra yapıştır
    t = re.sub(r"\\\n", "", t)
    # iki satıra bölünmüş wikilink:  [[...\n...]] -> [[......]]
    t = re.sub(r"\[\[([^\]\n]*)\n([^\]\]\n]*)\]\]", lambda m: "[[%s%s]]" % (m.group(1), m.group(2)), t)
    return t


def _basename(w):
    w = w.strip().rstrip(".md")
    if "|" in w:
        w = w.split("|")[0]
    w = w.split("/")[-1].split("\\")[-1]
    for sep in ("#", "^"):
        if sep in w:
            w = w.split(sep)[0]
    return w.strip()


class R:
    def __init__(self, iwl=None, deprecated_words=("deprecated", "archived", "session", "homonoia",
                                                   "palinodie", "sachphilologie", "rituel", "courtney",
                                                   "luna", "briefleri")):
        self.iwl = iwl or {}
        self.gag = tuple(deprecated_words)

    def _linkw(self, target, alias):
        base = _basename(target)
        if any(w in target.lower() for w in self.gag) or any(w in base.lower() for w in self.gag):
            return '<span class="ref">%s</span>' % esc(alias if alias else base)
        if base in self.iwl:
            return '<a class="inpk" href="%s">%s</a>' % (esc(self.iwl[base]), esc(alias if alias else base))
        return '<span class="ref">%s</span>' % esc(alias if alias else base)

    def inline(self, t):
        t = esc(t)
        t = _WL.sub(lambda m: self._linkw(m.group(1), m.group(2)), t)
        t = _LINK.sub(lambda m: '<a href="%s" %s>%s</a>' % (
            esc(m.group(2)), 'target="_blank" rel="noopener"' if m.group(2).startswith("http") else "",
            esc(m.group(1))), t)
        t = re.sub(r"`([^`]+)`", lambda m: "<code>%s</code>" % esc(m.group(1)), t)
        t = re.sub(r"\*\*(.+?)\*\*", lambda m: "<strong>%s</strong>" % m.group(1), t)
        t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", lambda m: "<em>%s</em>" % m.group(1), t)
        return t


_WL = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_FENCE = re.compile(r"```([a-zA-Z0-9-]*)")
_HEAD = re.compile(r"^(#{1,4})\s+(.*)$")
_UL = re.compile(r"^(\s*)[-*+]\s+(.*)$")
_OL = re.compile(r"^(\s*)\d+[.)]\s+(.*)$")
_QUOTE = re.compile(r"^>\s*(.*)$")
_TBL_ROW = re.compile(r"^\s*\|")


def _parse_fm(lines, i):
    meta = {}
    j = i
    while j < len(lines):
        if lines[j].strip() == "---" and j != i:
            break
        m = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", lines[j])
        if m:
            k = m.group(1)
            v = m.group(2).strip().strip('"')
            meta[k] = meta[k] + " " + v if k in meta else v
        j += 1
    return meta, (j + 1 if j < len(lines) else i + 1)


def _split(row):
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def render_md(md_text, r):
    lines = clean_md(md_text).split("\n")
    meta = {}
    i = 0
    if len(lines) > 1 and lines[0].strip() == "---":
        meta, i = _parse_fm(lines, 0)
    out, blk, fenced = [], [], False

    def flush():
        if blk:
            out.append("<p>%s</p>" % r.inline(" ".join(blk)))
            del blk[:]

    def list_blk(start):
        tag = None
        pieces, k = [], start
        while k < len(lines):
            m = _UL.match(lines[k]); o = _OL.match(lines[k])
            if not (m or o) or lines[k].strip() in ("",):
                if (m or o) and lines[k].strip() == "":
                    k += 1
                    continue
                break
            is_ol = bool(o); t = (o or m).group(2)
            if tag is None:
                tag = "ol" if is_ol else "ul"
            elif (is_ol and tag != "ol") or (not is_ol and tag != "ul"):
                break
            pieces.append("<li>%s</li>" % r.inline(t))
            k += 1
        if pieces:
            out.append("<%s>%s</%s>" % (tag, "".join(pieces), tag))
        return k

    while i < len(lines):
        ln = lines[i]
        if fenced:
            if _FENCE.match(ln.strip()):
                out.append("</code></pre>")
                fenced = False
            else:
                out.append(esc(ln))
            i += 1
            continue
        mf = _FENCE.match(ln.strip())
        if mf:
            flush()
            out.append("<pre><code class=\"%s\">" % esc(mf.group(1)))
            fenced = True
            i += 1
            continue
        if ln.strip() in ("---", "***"):
            flush()
            out.append("<hr>")
            i += 1
            continue
        mh = _HEAD.match(ln)
        if mh:
            flush()
            out.append("<h%d>%s</h%d>" % (len(mh.group(1)), r.inline(mh.group(2).strip()), len(mh.group(1))))
            i += 1
            continue
        if _TBL_ROW.match(ln):
            rows, hdr = [], None
            while i < len(lines) and _TBL_ROW.match(lines[i]):
                cells = _split(lines[i])
                if cells and all(re.fullmatch(r":?-+:?", c) for c in cells):
                    pass
                elif hdr is None:
                    hdr = cells
                else:
                    rows.append(cells)
                i += 1
            th = "".join("<th>%s</th>" % r.inline(c) for c in (hdr or []))
            tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % r.inline(c) for c in row) for row in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, tb))
            continue
        mq = _QUOTE.match(ln)
        if mq:
            q = []
            while i < len(lines) and _QUOTE.match(lines[i]):
                q.append(_QUOTE.match(lines[i]).group(1))
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % r.inline(" ".join(q)))
            continue
        if _UL.match(ln) or _OL.match(ln):
            flush()
            i = list_blk(i)
            continue
        if ln.strip() == "":
            flush()
            i += 1
            continue
        blk.append(ln.strip())
        i += 1
    flush()
    return meta, "\n".join(out)


def render_page(md_text, package_label=None, iwl=None, is_index=False):
    r = R(iwl=iwl or {})
    meta, body = render_md(md_text, r)
    title = meta.get("title", "").strip('"') or (meta.get("name", "") or "Belge")
    created, updated = meta.get("created", ""), meta.get("updated", "")
    summary = meta.get("summary", "")
    chips = []
    if created:
        chips.append('<span class=chip><b>Oluşturma</b> · %s</span>' % esc(created))
    if updated and updated != created:
        chips.append('<span class=chip><b>Güncel</b> · %s</span>' % esc(updated))
    if meta.get("type"):
        chips.append('<span class=chip><b>Tür</b> · %s</span>' % esc(meta["type"]))
    if meta.get("tags"):
        chips.append('<span class=chip><b>Etiket</b> · %s</span>' % esc(meta["tags"]))
    sumh = '<p class=summary>%s</p>' % r.inline(summary) if summary else ""
    sec = package_label or "REMEMBERED · ARŞİV"
    return ("<!doctype html><html lang=tr><head><meta charset=utf-8>"
            "<meta name=viewport content=\"width=device-width,initial-scale=1\">"
            "<title>%s · Remembered Arşiv</title><style>%s%s</style></head><body>"
            "<div class=page><header><span class=brand>THE REMEMBERED CHRONICLE · ARŞİV</span>"
            "<span class=sec>%s</span></header>"
            "<div class=kicker>GÖREV BELGESİ · MARKDOWN RENDER</div>"
            "<h1>%s</h1>%s<div class=meta>%s</div>%s</div></body></html>"
            % (esc(title), _fonts(), css(), esc(sec), esc(title), sumh, "".join(chips), body))


def css():
    s = _CSS
    for k, v in T.items():
        s = s.replace("@%s@" % k, v)
    return s


def _fonts():
    global _F
    if _F is None:
        _F = GEN3FONTS.read_text(encoding="utf-8") if GEN3FONTS.exists() else ""
    return _F


_F = None

_CSS = """
:root{--paper:@paper@;--paper2:@paper2@;--paper3:@paper3@;--ink:@ink@;--ink2:@ink2@;--ink3:@ink3@;
 --sec:@sec@;--bord:@bord@;--bronze:@bronze@;--bronze2:@bronze2@;--amber:@amber@;--gold:@gold@;
 --mono:@mono@;--serif:@serif@;--body:@body@;--sans:@sans@}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
body:before{content:"";position:fixed;inset:0;background:radial-gradient(1100px 420px at 78% -120px, @amber@26, transparent 62%);pointer-events:none;z-index:0}
.page{max-width:920px;margin:0 auto;padding:0 44px 90px;position:relative;z-index:1}
header{padding:36px 0 20px;border-bottom:1px solid var(--bord);display:flex;justify-content:space-between;align-items:baseline;margin-bottom:34px}
.brand{font-family:var(--body);font-size:12.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--ink2)}
.sec{font-family:var(--mono);font-size:11.5px;letter-spacing:.26em;color:var(--gold);text-transform:uppercase}
h1{font-family:var(--serif);font-size:39px;font-weight:500;line-height:1.14;letter-spacing:-.012em;margin:2px 0 6px}
.kicker{font-family:var(--mono);font-size:11.5px;letter-spacing:.3em;color:var(--gold);text-transform:uppercase;margin-bottom:14px}
.summary{font-size:19px;color:var(--ink2);max-width:64ch;margin-bottom:18px}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}
.chip{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--ink3);border:1px solid var(--bord);background:var(--paper2);padding:5px 10px}
.chip b{color:var(--ink2);font-weight:400}
h2{font-family:var(--serif);font-size:26px;font-weight:500;margin:38px 0 12px;padding-top:14px;border-top:1px solid var(--bord)}
h3{font-family:var(--serif);font-size:20px;font-weight:500;margin:24px 0 8px}
h4{font-family:var(--sans);font-size:15px;font-weight:600;margin:20px 0 6px;color:var(--ink)}
p{margin:0 0 14px;color:var(--ink2)}
strong{color:var(--ink)}
a{color:var(--bronze2);text-decoration:underline;text-underline-offset:3px}
a.inpk{color:var(--gold);text-decoration:underline;text-decoration-color:var(--amber)}
a:hover{color:var(--paper)}
code{font-family:var(--mono);font-size:.86em;color:var(--ink2);background:var(--paper2);border:1px solid var(--bord);padding:1px 5px}
pre{background:#050505;color:var(--ink);padding:16px 18px;overflow:auto;border-radius:4px;margin:0 0 16px;font-size:13px}
pre code{background:none;border:0;color:inherit;padding:0}
ul,ol{margin:0 0 16px;padding-left:24px;color:var(--ink2)}
li{margin:0 0 6px}
blockquote{border-left:3px solid var(--bronze2);padding:2px 0 2px 18px;margin:0 0 16px;color:var(--sec);font-style:italic}
blockquote p{margin:0;color:inherit}
hr{border:0;border-top:1px solid var(--bord);margin:26px 0}
table{width:100%;border-collapse:collapse;margin:0 0 20px;font-size:14.5px}
th{font-family:var(--sans);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);text-align:left;border-bottom:2px solid var(--bronze2);padding:8px 10px}
td{border-bottom:1px solid var(--bord);padding:9px 10px;vertical-align:top;color:var(--ink2)}
tr:hover td{background:var(--paper2)}
.ref{color:var(--sec);font-style:italic}
img{max-width:100%;height:auto}
@media(max-width:640px){.page{padding:0 20px 60px}h1{font-size:31px}}
"""