# Remembered · İş Arşivi (Alleksenes / İ. Mert)

Canlı görünüm: bu repo GitHub Pages'te yayınlı, kök `index.html` açılınca paketler görünür.
Paylaşım: linki WhatsApp'tan atıyorsun, notları oradan inceleyenler gezinebilir; indirenler de dosya olarak kullanabilir.

## Başlarken (insan)

- `index.html` (kök) = galeri: `DIL-001` ve `PR-001` paket kartları.
- Her pakette `index.html` = o görevin readme'si; belge adları tıklanır, komşu `.html` sayfalarına gider.
- Deprecated / iç işlem notları pakete konmadı; wikilink'ler temiz (bozuk Obsidian atıfları onarıldı).

## Başlarken (ajan / LLM)

**`AGENTS.md`**'yi oku: hangi kurallarla notları okuman ve sunman bebekten atayan yönerge. Tetik sırası: önce `AGENTS.md`, sonra `INDEX.html`/paket notları.

## Yapı

```
index.html / INDEX.html   → galeri (Pages kökü)
DIL-001/                  → 12 belge (md + html) + index.html
PR-001/                   → 10 belge (md + html) + index.html
Remembered-Arsiv.zip      → tek zip (çıkar → index.html)
AGENTS.md                 → ajan yönergesi (skill)
arsiv.py / mdrender.py    → üretici; env -u PYTHONPATH python3 arsiv.py
```

Görünüm: koyu NOCTURNE (gerçek tasarım dilinin özet belge karşılığı). Kaynak tasarım: canlı site token'ları (krem + bronz; Newsreader/Playfair/Inter/JetBrains Mono).