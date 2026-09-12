# Remembered İş Arşivi · MANIFEST (Alleksenes / İ. Mert)

Tarih: 2026-09-12 · Kaynak: Obsidian (`.llm-wiki/wiki/projects/remembered`)
Üretici: `arsiv.py` (tekrar koş: `env -u PYTHONPATH python3 arsiv.py`)
Hedef klon: `~/Documents/GitHub/remembered-arsiv/`

Amaç: Notion iş notlarından (DIL-001, PR-001) hyperlink ile bağlanan, site metadata'sıyla
(krem + bronz + Newsreader/Playfair/Inter/JetBrains Mono) tasarlanmış embed HTML readme'ler
ve her görevin kendi zip'i. "Boş konuşmak mı, iş yapmak mı" tartışmasına somut teslim.

## Paketler

| Paket | Task | Dosya sayısı | Readme | Zip |
|---|---|---|---|---|
| DIL-001 | Dil Stratejisi (EN+TR mimarisi) | 15 | `DIL-001/README-DIL-001.html` | `DIL-001.zip` |
| PR-001 | Global PR & Basın Rezervasyonu | 10 | `PR-001/README-PR-001.html` | `PR-001.zip` |

INDEX: `INDEX.html` (iki pakete kartlı galeri).

## DIL-001 kapsamı (15 dosya)
Strategi: `dil-stratejisi`, `dil-stratejisi-notu`, `Filologun Kalemi`, `TR Retorik & Kavram`,
`Semantik Alan Veritabanı`, `Rakip Dil Denetimi`, `Canlı Site Dil Denetimi`,
`Karar Envanteri & Yönerge`, `Arşiv Adaleti · 12 İlke`, `Semantik Veritabanı Briefi`,
`Gövde Sentezi Briefi`, `Uyumlanma Sentezi`, `Uğur Görüşme Paketi`, `Uğur Karar Paketi (Tek Sayfa)`,
`Gövde Sentezi Raporu (İŞ A/B/C)`.

## PR-001 kapsamı (10 dosya)
`Basın Kiti TR`, `Press Kit EN`, `Görev Notu`, `Basın Kiti İş Planı`,
Uğur briefleri (üretim notu, ilk tanıtım metinleri, içerik paketi devamı, Ozan otomasyon + Buffer,
kalite denetimi), `Sosyal Medya & İçerik Motoru`.

## Hariç tutulanlar (gerekçe)

Süreç içi / özel / ıskartaya gitmiş içerik pakete GİRMEDİ:

- `*dil001-deprecated/*` (eski taslaklar, ıskartaya gitmiş hatlar)
- `courtney-siirler/*` (206 ham şiir transkripsiyonu; kaynak hat deprecated) ve `courtney-musa-lapidaria-tasnif-20260905.md`
- `dil001-raporlar/is-1-5..is-10-*.md` (süreç günlükleri; owner değerlendirmeleri, `^[inferred]` iç işaretleri içerir)
- `luna-session-zinciri-arsivi-20260904.md`, `06-arastirma/luna-zincir-ham-kayit-20260904.jsonl` (özel ajan oturum kayıtları, off-record)
- `homonoia-brief`, `palinodie-yontem-notu`, `sachphilologie-notu`, `rituel-mozaik-...`, `dil-001-session-briefleri-*` (süreç içi)
- `ugur-briefleri-20260907/00-uyumluluk-testi.md` (iç test)
- Off-record konumlanma/sahiplik notları (`02-ekip-gorev/*` içindeki kişi yargıları, sponsorship adı, plan notları): bunlar zaten DIL/PR teslim dosyalarında yok, ayrıca taranıp teyit edildi.

## Notion bağlantısı

`arsiv.py` içinde her task'ın `notion` URL'si placeholder: `https://www.notion.so/Buraya-X-is-notu-linki`.
Readme'deki "Notion iş notu" butonuna ilgili Notion task sayfa/veritabanı linkini girmen yeterli
(`arsiv.py`'de `TASKS[tid]["notion"]` değerini değiştirip `arsiv.py`'yi yeniden koş ya da brand doğrudan HTML'i düzenle).

## Off-record / mahremiyet

- Pakete giren 25 .md dosyası tarandı (off-record/aramızda/iç kurgu/yargı markörleri): temiz.
  Yalnızca ürün dili olan "ölüm cümlesi sahiplik ayrımı" içeriği var (o, teslimin kendisi).
- "imha" listesi ayrı: özel ajan oturum kayıtları + süreç içi artıfakt'lar vault'ta duruyor; silinmesi
  kullanıcı onayına bırakıldı (no-delete kuralı).

## Yeniden üretim
```bash
cd ~/Documents/GitHub/remembered-arsiv
env -u PYTHONPATH python3 arsiv.py   # paket + readme + zip
env -u PYTHONPATH python3 render.py  # görsel doğrulama ekranları (~/deck_check/arsiv)
```
Deck tarafının font atomları (`fonts.css`, gen3 reposundan) readme'lere gömülü; internet gerekmez.