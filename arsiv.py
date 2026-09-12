# -*- coding: utf-8 -*-
"""Remembered iş arşivi paketleyici (Alleksenes / İ. Mert paketleri).
Obsidian'dan DIL-001 ve PR-001 teslim dosyalarını kopyalar, site metadata'sıyla
(kanonik · canlı site) tasarlanmış embed HTML readme üretir, her paketi zip'ler.
Off-record / süreç içi / deprecated / ham oturum dosyaları pakete GİRMEZ."""
import os
import shutil
import sys
from pathlib import Path

from PIL import Image  # kullanılmıyor; font css'i doğrudan gömülecek

VAULT = Path.home() / ".llm-wiki/wiki/projects/remembered"
OUT = Path(__file__).resolve().parent
GEN3 = Path.home() / "Documents/GitHub/remembered-pitchdecks-gen3"
FONTS = GEN3 / "fonts.css"

#: site-kanonik tasarım tokenları (remembered-design-tokens.md)
SITE = {
    "paper": "#FAF8F5", "paper2": "#F8F8F5", "paper3": "#F7F3EA",
    "ink": "#111111", "ink2": "#1E1B18", "ink3": "#2B2724",
    "sec": "#787163", "bord": "#DCD3C1",
    "bronze": "#855327", "bronze2": "#8C6239", "amber": "#C29B38",
    "gold": "#C5A059", "mono": "'JetBrains Mono',monospace",
    "serif": "'Playfair Display','Bodoni Moda',Georgia,serif",
    "body": "'Newsreader',Georgia,serif",
    "sans": "'Inter',system-ui,sans-serif",
}

TASKS = {
    "DIL-001": {
        "name": "Dil Stratejisi (EN+TR mimarisi)",
        "tagline": "Remembered dil disiplini: ses kuralları, retorik, semantik alan, karar envanteri ve Uğur karar paketleri.",
        "notion": "https://www.notion.so/Buraya-DIL-001-is-notu-linki",
        "notion_label": "DIL-001 · Dil Stratejisi (Notion iş notu)",
        "files": [
            ("dil-stratejisi.md", "Dil Stratejisi (EN+TR mimarisi)", "Görev yüzeyi; dört teslimat omurgası.", "dil001-docs"),
            ("dil-stratejisi-notu.md", "Dil Stratejisi Notu", "EN+TR çıkış, DE/ES/FR genişleme kriterleri, global hesap.", "dil001-docs"),
            ("dil-stratejisi-filolog-kalemi.md", "Filologun Kalemi", "Ses disiplini: stratejiyi değil sesi düzeltir; altı kural, AI reglajı.", "dil001-docs"),
            ("tr-retorik-kavram-notu.md", "TR Retorik & Kavram Kurulumu", "Türkçede farklı kılacak kavram seti ve tasnif disiplini.", "dil001-docs"),
            ("semantik-alan-veritabani.md", "Semantik Alan Veritabanı", "40 kayıt; formül aileleri ve sahiplik kuralı.", "dil001-docs"),
            ("rakip-dil-denetimi-20260908.md", "Rakip Dil Denetimi", "Beş açık karar için rakip dili kanıt taraması.", "dil001-docs"),
            ("canli-site-dil-denetimi-20260908.md", "Canlı Site Dil Denetimi", "TR lokalizasyon, 71 string, canlı sözlük.", "dil001-docs"),
            ("dil-karar-envanteri-ve-yonerge-taslagi-20260908.md", "Karar Envanteri & Yönerge Taslağı", "Açık kararlar ve üretim yönergesi.", "dil001-docs"),
            ("arsiv-adaleti-on-iki-ilke-taslak-20260908.md", "Arşiv Adaleti · 12 İlke (taslak)", "Arşiv adaleti ilke taslağı.", "dil001-docs"),
            ("is-10-semantik-veritabani-briefi.md", "Semantik Veritabanı Briefi", "Çalışma briefi.", "dil001-docs"),
            ("gorev-briefi-dil001-govde-sentezi.md", "Gövde Sentezi Briefi", "Arşivlenen notlardan owner kararlı dil hattı özeti.", "dil001-docs"),
            ("dil-001-uyumlanma-sentezi-20260907.md", "Uyumlanma Sentezi", "Hat hizalaması ve kapsam.", "dil001-docs"),
            ("ugur-gorusme-paketi-20260908.md", "Uğur Görüşme Paketi (2026-09-08)", "Açık kararların toplantı paketi.", "dil001-docs"),
            ("ugur-karar-paketi-tek-sayfa-20260910.md", "Uğur Karar Paketi (Tek Sayfa, 2026-09-10)", "Tokalaşılan karar paketi.", "dil001-docs"),
            ("is-govde-sentezi-raporu.md", "Gövde Sentezi Raporu (İŞ A/B/C)", "40 kayıtlık SEM tablosu dahil sentez raporu.", "dil001-raporlar"),
        ],
    },
    "PR-001": {
        "name": "Global PR & Basın Rezervasyonu",
        "tagline": "Basın kiti (TR/EN), üretim notları, iş planı ve sosyal içerik motoru.",
        "notion": "https://www.notion.so/Buraya-PR-001-is-notu-linki",
        "notion_label": "PR-001 · Global PR & Basın (Notion iş notu)",
        "files": [
            ("TR-basin-kiti.md", "Basın Kiti (TR)", "Master TR dosya.", "basin-kiti"),
            ("EN-press-kit.md", "Press Kit (EN)", "Master EN dosya.", "basin-kiti"),
            ("global-pr-basin.md", "Görev Notu: Global PR & Basın", "Sorumlu, ardıl, alt adımlar, kaynaklar.", "task"),
            ("pr-001-basin-kiti-is-plani.md", "Basın Kiti İş Planı", "Deadline, sorumlu, kapanış ölçütleri.", "task"),
            ("01-basin-kiti-uretim-notu.md", "Uğur · Basın Kiti Üretim Notu (verbatim)", "8 bölümlük üretim şartnamesi.", "ugur-briefleri"),
            ("02-ilk-tanitim-metinleri-ve-ekip-dagilimi.md", "Uğur · İlk Tanıtım Metinleri + Ekip Dağılımı", "Ana mesaj, TR/EN giriş, gönderiler.", "ugur-briefleri"),
            ("03-icerik-paketi-devami.md", "Uğur · İçerik Paketi Devamı", "06-09 gönderiler, video, story seti, yayın sırası.", "ugur-briefleri"),
            ("04-ozan-otomasyon-briefi-ve-buffer-arastirmasi.md", "Uğur · Ozan Otomasyon Briefi + Buffer Araştırması", "Günlük profil otomasyonu ve takvim araç karşılaştırması.", "ugur-briefleri"),
            ("05-kalite-denetimi.md", "Kalite Denetimi", "PR hattı dil kuralları doğrulaması.", "ugur-briefleri"),
            ("sosyal-medya-icerik-motoru.md", "Sosyal Medya & İçerik Motoru", "Lansman kampanyaları, haftalık takvim.", "icerik"),
        ],
    },
}

#: kaynak: dil001 raporların retros (is-1-5.. is-10) + tüm deprecated + oturum/JSONL DIŞARI


def font_css():
    return FONTS.read_text(encoding="utf-8") if FONTS.exists() else ""


def rel_src(taskid, fname, group):
    if taskid == "DIL-001":
        return VAULT / "02-ekip-gorev/gorevler/DIL-001" / group / fname
    # PR-001
    return {
        "basin-kiti": VAULT / "04-icerik/basin-kiti-20260911",
        "task": VAULT / "02-ekip-gorev" if fname.startswith("pr-001") else VAULT / "02-ekip-gorev/gorevler",
        "ugur-briefleri": VAULT / "04-icerik/ugur-briefleri-20260907",
        "icerik": VAULT / "04-icerik",
    }[group] / fname


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render_css():
    s = CSS
    for k, v in SITE.items():
        s = s.replace("%(" + k + ")s", v)
    return s


def readme(tid, meta):
    rows = []
    for i, (fname, label, desc, group) in enumerate(meta["files"], start=1):
        rows.append(
            '<tr><td class="num">%02d</td>'
            '<td class="f"><a href="%s" class="fname">%s</a>'
            '<span class="fdesc">%s</span></td></tr>'
            % (i, esc(fname), esc(label), esc(desc)))
    files_html = "".join(rows)
    return """<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Remembered · {tid} — {name}</title>
<style>{css}</style></head><body>
<header><span class="brand">THE REMEMBERED CHRONICLE · ARŞİV</span><span class="sec">{tid}</span></header>
<main>
  <div class="kicker">ÖZET PAKET · {tid}</div>
  <h1>{tid}&nbsp;·&nbsp;{name}</h1>
  <p class="lede">{tagline}</p>
  <dl class="meta">
    <dt>Asli sorumlu</dt><dd>Alleksenes / İ. Mert · Büyüme &amp; Operasyon</dd>
    <dt>Durum</dt><dd>Notion iş notuyla eş · paketlenmiş teslim</dd>
    <dt>İçerik</dt><dd>{n} dosya · markdown</dd>
  </dl>
  <a class="notion" href="{notion}">{notion_label} ↗</a>
  <section>
    <h2>Paket Dosyaları</h2>
    <table>{files_html}</table>
  </section>
  <p class="foot">Bu paket, siteden alınan kanonik tasarım metadatasıyla hazırlandı (krem + mürekkep + bronz; Newsreader / Playfair / Inter / JetBrains Mono). İçerik Obsidian arşivinden, off-record ve süreç içi dosyalar dışarıda bırakılarak toplandı.</p>
</main>
</body></html>""".format(
        tid=tid, name=esc(meta["name"]), tagline=esc(meta["tagline"]),
        notion=esc(meta["notion"]), notion_label=esc(meta["notion_label"]),
        n=len(meta["files"]), files_html=files_html,
        css=render_css())


CSS = """
:root{--paper:%(paper)s;--paper2:%(paper2)s;--ink:%(ink)s;--ink2:%(ink2)s;
 --sec:%(sec)s;--bord:%(bord)s;--bronze:%(bronze)s;--bronze2:%(bronze2)s;
 --amber:%(amber)s;--mono:%(mono)s;--serif:%(serif)s;--body:%(body)s;--sans:%(sans)s;
  --grain:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.55;-webkit-font-smoothing:antialiased}
body:before{content:"";position:fixed;inset:0;background-image:var(--grain);opacity:.05;mix-blend-mode:multiply;pointer-events:none;z-index:0}
header{padding:34px 64px 22px;border-bottom:1px solid var(--bord);display:flex;justify-content:space-between;align-items:baseline;position:relative;z-index:1}
.brand{font-family:var(--body);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--ink2)}
.sec{font-family:var(--mono);font-size:12px;letter-spacing:.28em;color:var(--bronze);text-transform:uppercase}
main{max-width:1080px;margin:0 auto;padding:56px 64px 40px;position:relative;z-index:1}
.kicker{font-family:var(--mono);font-size:12px;letter-spacing:.3em;color:var(--bronze);text-transform:uppercase;margin-bottom:20px}
h1{font-family:var(--serif);font-size:46px;font-weight:500;line-height:1.12;letter-spacing:-.01em;margin-bottom:18px}
.lede{font-size:21px;color:var(--ink2);max-width:64ch;margin-bottom:30px}
.meta{display:grid;grid-template-columns:160px 1fr;gap:6px 20px;margin-bottom:30px;border-top:1px solid var(--bord);border-bottom:1px solid var(--bord);padding:18px 0}
.meta dt{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;color:var(--sec);text-transform:uppercase}
.meta dd{font-size:16px;color:var(--ink2)}
.notion{display:inline-block;font-family:var(--mono);font-size:13px;letter-spacing:.12em;color:var(--paper);background:var(--bronze);padding:12px 20px;text-decoration:none;margin-bottom:44px}
.notion:hover{background:var(--bronze2)}
section h2{font-family:var(--serif);font-size:28px;font-weight:500;margin-bottom:14px}
table{width:100%;border-collapse:collapse}
tr{border-top:1px solid var(--bord)}
tr:last-child{border-bottom:1px solid var(--bord)}
td{padding:14px 6px;vertical-align:top}
.num{font-family:var(--mono);font-size:12px;color:var(--amber);white-space:nowrap}
.fname{font-family:var(--serif);font-size:19px;color:var(--bronze2);text-decoration:none;font-weight:500}
.fname:hover{text-decoration:underline}
.fdesc{display:block;font-size:15px;color:var(--sec);margin-top:3px}
.foot{margin-top:48px;font-size:13px;color:var(--sec);max-width:76ch;padding-top:18px;border-top:1px solid var(--bord)}
@media(max-width:720px){main{padding:34px 22px}header{padding:24px 22px 16px}h1{font-size:34px}.meta{grid-template-columns:110px 1fr}}
""" + "%s"


def build():
    assert FONTS.exists(), "fonts.css yok: önce gen3 fonts.py çalıştır"
    fc = font_css()
    for tid, meta in TASKS.items():
        pkg = OUT / tid
        if pkg.exists():
            shutil.rmtree(pkg)
        pkg.mkdir(parents=True, exist_ok=True)
        for fname, _label, _desc, group in meta["files"]:
            src = rel_src(tid, fname, group)
            dst = pkg / fname
            if not src.exists():
                print("  UYARI eksik:", src)
                continue
            shutil.copy2(src, dst)
        readme_html = readme(tid, meta)
        (pkg / ("README-%s.html" % tid)).write_text(readme_html, encoding="utf-8")
        shutil.make_archive(str(pkg), "zip", OUT, tid)
        print(tid, "->", len(meta["files"]), "dosya + readme + zip")
    # index
    index = _index()
    (OUT / "INDEX.html").write_text(index, encoding="utf-8")
    print("INDEX.html yazıldı; hedef:", OUT)


def _index():
    cards = []
    for tid, meta in TASKS.items():
        cards.append('<div class="card"><div class="tag">%s</div>'
                     '<h2>%s</h2><p>%s</p>'
                     '<a class="open" href="%s/README-%s.html" target="_blank">AÇ ▶</a></div>'
                     % (tid, esc(meta["name"]), esc(meta["tagline"]), tid, tid))
    return """<!doctype html><html lang="tr"><head><meta charset="utf-8">
<title>Remembered · İş Arşivi (Alleksenes / İ. Mert)</title>
<style>body{margin:0;background:%(paper)s;color:%(ink)s;font-family:%(serif)s}
header{padding:50px 64px 26px;border-bottom:1px solid %(bord)s}
h1{font-size:40px;font-weight:500;margin:0 0 8px}
.sub{font-family:%(mono)s;font-size:11.5px;letter-spacing:.28em;color:%(bronze)s;text-transform:uppercase}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:26px;padding:44px 64px}
.card{border:1px solid %(bord)s;background:%(paper2)s;padding:26px 24px;display:flex;flex-direction:column;gap:12px}
.tag{font-family:%(mono)s;font-size:11px;letter-spacing:.24em;color:%(bronze)s}
h2{font-family:%(serif)s;font-size:24px;font-weight:500;margin:0}
p{font-family:%(body)s;color:%(ink2)s;font-size:15px;line-height:1.5}
.open{font-family:%(mono)s;font-size:12.5px;letter-spacing:.16em;color:%(ink)s;text-decoration:none;border-bottom:1px solid %(bronze)s;align-self:flex-start;padding-bottom:3px}
@media(max-width:700px){main{padding:24px}header{padding:28px 24px}}</style></head>
<body><header><div class="sub">REMEMBERED · ARŞİV · ALLEKSENES / İ. MERT</div>
<h1>İş Arşivi</h1></header><main>""" + "".join(cards) + "</main></body></html>" % SITE


if __name__ == "__main__":
    build()