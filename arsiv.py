# -*- coding: utf-8 -*-
"""Remembered iş arşivi paketleyici (v3 · NOCTURNE).
Obsidian → her .md için koyu temalı, iç-bağlantılı HTML + readme(index) + zip.
Editöryel: süreç/deprecated notları manifestta YOK; wikilinkler paket-içi tıklanır.
Tek tık: her pakette index.html + birleşik Remembered-Arsiv.zip (kök INDEX).
"""
import shutil
from pathlib import Path

import mdrender

VAULT = Path.home() / ".llm-wiki/wiki/projects/remembered"
OUT = Path(__file__).resolve().parent
SITE = dict(mdrender.T)  # NOCTURNE koyu

TASKS = {
    "DIL-001": {
        "name": "Dil Stratejisi (EN+TR mimarisi)",
        "tagline": "Remembered dil disiplini: ses kuralları, retorik, semantik alan, karar envanteri ve Uğur karar paketleri.",
        "notion": "https://app.notion.com/p/DIL-001-Dil-3ca8e2f96dde810eba32c6b6e077a40d",
        "files": [
            ("dil-stratejisi.md", "Dil Stratejisi (EN+TR mimarisi)", "Görev yüzeyi; dört teslimat omurgası.", "dil001-docs"),
            ("dil-stratejisi-notu.md", "Dil Stratejisi Notu", "EN+TR çıkış, DE/ES/FR genişleme kriterleri, global hesap.", "dil001-docs"),
            ("dil-stratejisi-filolog-kalemi.md", "Filologun Kalemi", "Ses disiplini; altı kural, AI reglajı.", "dil001-docs"),
            ("tr-retorik-kavram-notu.md", "TR Retorik & Kavram Kurulumu", "Türkçede farklı kılacak kavram seti ve tasnif disiplini.", "dil001-docs"),
            ("semantik-alan-veritabani.md", "Semantik Alan Veritabanı", "Formül aileleri ve sahiplik kuralı.", "dil001-docs"),
            ("rakip-dil-denetimi-20260908.md", "Rakip Dil Denetimi", "Açık kararlar için rakip dili kanıt taraması.", "dil001-docs"),
            ("canli-site-dil-denetimi-20260908.md", "Canlı Site Dil Denetimi", "TR lokalizasyon, canlı sözlük.", "dil001-docs"),
            ("dil-karar-envanteri-ve-yonerge-taslagi-20260908.md", "Karar Envanteri & Yönerge Taslağı", "Açık kararlar ve üretim yönergesi.", "dil001-docs"),
            ("arsiv-adaleti-on-iki-ilke-taslak-20260908.md", "Arşiv Adaleti · 12 İlke (taslak)", "Arşiv adaleti ilke taslağı.", "dil001-docs"),
            ("ugur-gorusme-paketi-20260908.md", "Uğur Görüşme Paketi", "Açık kararların toplantı paketi.", "dil001-docs"),
            ("ugur-karar-paketi-tek-sayfa-20260910.md", "Uğur Karar Paketi (Tek Sayfa)", "Tokalaşılan karar paketi.", "dil001-docs"),
            ("is-govde-sentezi-raporu.md", "Gövde Sentezi Raporu (İŞ A/B/C)", "SEM tablosu dahil sentez raporu.", "dil001-raporlar"),
        ],
    },
    "PR-001": {
        "name": "Global PR & Basın Rezervasyonu",
        "tagline": "Basın kiti (TR/EN), üretim notları, iş planı ve sosyal içerik motoru.",
        "notion": "https://app.notion.com/p/PR-001-Global-PR-3ca8e2f96dde814ba4f2e1e9c345ebb2",
        "files": [
            ("TR-basin-kiti.md", "Basın Kiti (TR)", "Master TR dosya.", "basin-kiti"),
            ("EN-press-kit.md", "Press Kit (EN)", "Master EN dosya.", "basin-kiti"),
            ("global-pr-basin.md", "Görev Notu: Global PR & Basın", "Sorumlu, ardıl, alt adımlar.", "task"),
            ("pr-001-basin-kiti-is-plani.md", "Basın Kiti İş Planı", "Deadline, sorumlu, kapanış ölçütleri.", "task"),
            ("01-basin-kiti-uretim-notu.md", "Uğur · Basın Kiti Üretim Notu (verbatim)", "8 bölümlük üretim şartnamesi.", "ugur-briefleri"),
            ("02-ilk-tanitim-metinleri-ve-ekip-dagilimi.md", "Uğur · İlk Tanıtım Metinleri + Ekip Dağılımı", "Ana mesaj, TR/EN giriş, gönderiler.", "ugur-briefleri"),
            ("03-icerik-paketi-devami.md", "Uğur · İçerik Paketi Devamı", "Gönderiler, video, story, yayın sırası.", "ugur-briefleri"),
            ("04-ozan-otomasyon-briefi-ve-buffer-arastirmasi.md", "Uğur · Ozan Otomasyon + Buffer Araştırması", "Günlük profil otomasyonu ve takvim araç karşılaştırması.", "ugur-briefleri"),
            ("05-kalite-denetimi.md", "Kalite Denetimi", "PR hattı dil kuralları doğrulaması.", "ugur-briefleri"),
            ("sosyal-medya-icerik-motoru.md", "Sosyal Medya & İçerik Motoru", "Lansman kampanyaları, haftalık takvim.", "icerik"),
        ],
    },
}


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def rel_src(taskid, fname, group):
    if taskid == "DIL-001":
        return VAULT / "02-ekip-gorev/gorevler/DIL-001" / group / fname
    if group == "task":
        base = VAULT / ("02-ekip-gorev" if fname.startswith("pr-001")
                        else "02-ekip-gorev/gorevler")
        return base / fname
    base = {"basin-kiti": VAULT / "04-icerik/basin-kiti-20260911",
            "ugur-briefleri": VAULT / "04-icerik/ugur-briefleri-20260907",
            "icerik": VAULT / "04-icerik"}[group]
    return base / fname


_CSS = """
:root{--paper:@paper@;--paper2:@paper2@;--ink:@ink@;--ink2:@ink2@;--sec:@sec@;--bord:@bord@;
 --bronze:@bronze@;--bronze2:@bronze2@;--amber:@amber@;--gold:@gold@;--mono:@mono@;
 --serif:@serif@;--body:@body@;--sans:@sans@}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.58;-webkit-font-smoothing:antialiased}
body:before{content:"";position:fixed;inset:0;background:radial-gradient(1100px 420px at 78% -120px, @amber@30, transparent 62%);pointer-events:none;z-index:0}
.topband{height:5px;background:linear-gradient(90deg,var(--amber),var(--bronze) 45%,var(--bronze2) 90%)}
.page{max-width:960px;margin:0 auto;padding:0 44px 80px;position:relative;z-index:1}
header{padding:30px 0 18px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--bord);margin-bottom:42px}
.brand{font-family:var(--body);font-size:12.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--ink2)}
.sec{font-family:var(--mono);font-size:11.5px;letter-spacing:.28em;color:var(--gold);text-transform:uppercase}
.kicker{font-family:var(--mono);font-size:12px;letter-spacing:.32em;color:var(--gold);text-transform:uppercase;margin-bottom:14px}
h1{font-family:var(--serif);font-size:52px;font-weight:500;line-height:1.08;letter-spacing:-.014em;margin-bottom:16px;max-width:22ch}
h1 em{font-style:italic;color:var(--bronze2)}
.lede{font-size:20px;color:var(--ink2);max-width:60ch;margin-bottom:30px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--bord);border:1px solid var(--bord);margin-bottom:34px}
.stat{background:var(--paper2);padding:18px 18px 15px}
.stat .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;color:var(--ink3);text-transform:uppercase;display:block;margin-bottom:7px}
.stat .v{font-family:var(--serif);font-size:19px;color:var(--ink);line-height:1.3}
.cta{display:flex;gap:14px;align-items:center;margin-bottom:48px;flex-wrap:wrap}
.btn{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--paper);background:var(--bronze);padding:13px 22px;text-decoration:none;display:inline-flex;align-items:center;gap:9px}
.btn:hover{background:var(--bronze2)}
.ghost{font-family:var(--mono);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);text-decoration:none;border-bottom:1px solid var(--amber);padding-bottom:3px}
section h2{font-family:var(--serif);font-size:27px;font-weight:500;margin-bottom:16px}
table{width:100%;border-collapse:collapse;margin-bottom:30px}
tr{border-top:1px solid var(--bord)}
tr:last-child{border-bottom:1px solid var(--bord)}
td{padding:15px 8px;vertical-align:top}
.num{font-family:var(--mono);font-size:12px;color:var(--gold);white-space:nowrap;width:38px}
.tt{font-family:var(--serif);font-size:19px;color:var(--gold);text-decoration:none;font-weight:500}
.tt:hover{text-decoration:underline;color:var(--bronze2)}
.raw{font-family:var(--mono);font-size:10.5px;color:var(--ink3);text-decoration:none;border:1px solid var(--bord);padding:1px 6px;margin-left:8px;vertical-align:middle}
.raw:hover{border-color:var(--bronze2);color:var(--bronze2)}
.desc{display:block;font-size:14.5px;color:var(--ink3);margin-top:3px}
.callout{border-left:3px solid var(--bronze2);background:var(--paper2);padding:16px 18px;margin:34px 0;font-size:15px;color:var(--ink2)}
.callout b{color:var(--ink)}
footer{margin-top:52px;padding-top:20px;border-top:1px solid var(--bord);display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;font-family:var(--mono);font-size:11px;letter-spacing:.12em;color:var(--sec);text-transform:uppercase}
footer a{color:var(--gold);text-decoration:none}
@media(max-width:680px){.page{padding:0 20px 60px}h1{font-size:38px}.stats{grid-template-columns:repeat(2,1fr)}}
"""


def render_css():
    s = _CSS
    for k, v in SITE.items():
        s = s.replace("@" + k + "@", v)
    return s


def readme(tid, meta):
    rows = []
    for i, (fname, label, desc, group) in enumerate(meta["files"], start=1):
        html = fname[:-3] + ".html" if fname.endswith(".md") else fname
        rows.append('<tr><td class="num">%02d</td><td><a class="tt" href="%s">%s</a>'
                    '<a class="raw" href="%s">md</a>'
                    '<span class="desc">%s</span></td></tr>'
                    % (i, esc(html), esc(label), esc(fname), esc(desc)))
    files_html = "".join(rows)
    return ("<!doctype html><html lang=tr><head><meta charset=utf-8>"
            "<meta name=viewport content=\"width=device-width,initial-scale=1\">"
            "<title>Remembered · %s</title><style>%s</style></head><body>"
            "<div class=topband></div><div class=page>"
            "<header><span class=brand>THE REMEMBERED CHRONICLE · ARŞİV</span>"
            "<span class=sec>%s · ALLEKSENES / İ. MERT</span></header>"
            "<div class=kicker>GÖREV PAKETİ · %s</div>"
            "<h1>%s</h1><p class=lede>%s</p>"
            "<div class=stats>"
            "<div class=stat><span class=k>Asli sorumlu</span><span class=v>Alleksenes / İ. Mert</span></div>"
            "<div class=stat><span class=k>Kapsam</span><span class=v>%d belge</span></div>"
            "<div class=stat><span class=k>Görünüm</span><span class=v>Koyu · editoryal</span></div>"
            "<div class=stat><span class=k>Durum</span><span class=v>Teslim edilebilir</span></div></div>"
            "<div class=cta><a class=btn href=\"%s\">Notion iş notu ↗</a>"
            "<a class=ghost href=\"../INDEX.html\">Arşiv dizini ↗</a></div>"
            "<section><h2>Paket Dosyaları</h2><table>%s</table></section>"
            "<div class=callout><b>Nasıl açılır:</b> zip'i <b>çıkar</b>, bu dosyaya çift tıkla. "
            "Belge adları tıklanır ve aynı klasördeki komşu sayfalara gider; "
            "satır sonundaki <b>md</b> kaynak markdown. Zip içinden (çıkarmadan) açarsan bağlantılar çalışmaz.</div>"
            "<footer><span>%s</span><span>NOCTURNE · site bronz/altın ailesi</span></footer>"
            "</div></body></html>"
            % (esc(tid + " · " + meta["name"]), render_css(), esc(tid), esc(tid),
               esc(meta["name"]), esc(meta["tagline"]), len(meta["files"]),
               esc(meta["notion"]), files_html, esc(tid + " · " + meta["name"])))


def index():
    cards = "".join(
        '<div class="card"><div class=tag>%s</div><h2>%s</h2><p>%s</p>'
        '<a class=open href="%s/index.html" target="_blank">AÇ ▶</a></div>'
        % (esc(tid), esc(m["name"]), esc(m["tagline"]), esc(tid))
        for tid, m in TASKS.items())
    t = ("<!doctype html><html lang=tr><head><meta charset=utf-8>"
            "<meta name=viewport content=\"width=device-width,initial-scale=1\">"
            "<title>Remembered · İş Arşivi</title><style>"
            "body{margin:0;background:@paper@;color:@ink@;font-family:@serif@}"
            ".band{height:5px;background:linear-gradient(90deg,@amber@,@bronze@ 45%,@bronze2@ 90%)}"
            "header{padding:52px 64px 24px;border-bottom:1px solid @bord@}"
            ".k{font-family:@mono@;font-size:11px;letter-spacing:.3em;color:@gold@;text-transform:uppercase;display:block;margin-bottom:10px}"
            "h1{font-size:44px;font-weight:500;margin:0}"
            "main{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:26px;padding:44px 64px}"
            ".card{border:1px solid @bord@;background:@paper2@;padding:26px 24px;display:flex;flex-direction:column;gap:12px}"
            ".tag{font-family:@mono@;font-size:11px;letter-spacing:.24em;color:@gold@}"
            "h2{font-family:@serif@;font-size:24px;font-weight:500;margin:0}"
            "p{font-family:@body@;color:@ink2@;font-size:15px;line-height:1.5}"
            ".open{font-family:@mono@;font-size:12.5px;letter-spacing:.16em;color:@ink@;text-decoration:none;border-bottom:1px solid @bronze@;align-self:flex-start;padding-bottom:3px}"
            ".note{padding:0 64px 60px;max-width:780px;font-family:@body@;color:@sec@;font-size:14.5px;line-height:1.6}"
            ".note b{color:@ink2@}"
            "@media(max-width:700px){main{padding:24px}header{padding:28px 24px}.note{padding:0 24px 44px}}"
            "</style></head><body><div class=band></div><header><div class=k>REMEMBERED · ARŞİV · ALLEKSENES / İ. MERT</div>"
            "<h1>İş Arşivi</h1></header><main>" + cards +
            "</main><div class=note><b>Tek tık:</b> zip'i çıkar, <b>INDEX.html</b>'e çift tıkla; kartlardan "
            "pakete, paketten belgeye. Wikilink'ler birbirine bağlı, deprecated/dahili işlem notları pakete konmadı. "
            "Zip içinden açılırsa bağlantılar çalışmaz; önce çıkar.</div></body></html>")
    for k, v in SITE.items():
        t = t.replace("@" + k + "@", v)
    return t


def build():
    # paketler
    for tid, meta in TASKS.items():
        pkg = OUT / tid
        if pkg.exists():
            shutil.rmtree(pkg)
        pkg.mkdir(parents=True, exist_ok=True)
        iwl = {}
        for fname, label, desc, group in meta["files"]:
            stem = Path(fname).stem
            iwl[stem] = stem + ".html"
            src = rel_src(tid, fname, group)
            if not src.exists():
                print("  UYARI eksik:", src)
                continue
            md = src.read_text(encoding="utf-8")
            (pkg / fname).write_text(md, encoding="utf-8")
            if fname.endswith(".md"):
                page = mdrender.render_page(md, package_label=tid + " · " + meta["name"], iwl=iwl)
                (pkg / (Path(fname).stem + ".html")).write_text(page, encoding="utf-8")
        (pkg / "index.html").write_text(readme(tid, meta), encoding="utf-8")
        shutil.make_archive(str(pkg), "zip", OUT, tid)
        print(tid, "->", len(meta["files"]), "belge + index.html + zip")
    # birleşik zip: INDEX + paketler
    bundle = OUT / "_bundle"
    if bundle.exists():
        shutil.rmtree(bundle)
    bundle.mkdir()
    (bundle / "INDEX.html").write_text(index(), encoding="utf-8")
    for tid in TASKS:
        shutil.copytree(OUT / tid, bundle / tid)
    shutil.make_archive(str(OUT / "Remembered-Arsiv"), "zip", bundle)
    print("Remembered-Arsiv.zip yazıldı; INDEX + iki paket.")


if __name__ == "__main__":
    build()