---
title: "Remembered: Dil Stratejisi (DIL-001)"
created: 2026-08-29
updated: 2026-09-06
type: reference
tags:
  - remembered
  - language
  - i18n
  - strategy
  - dil
sources:
  - global-lansman-stratejisi.md
  - is-tanimi-veritabani.md
  - Uğur handoff (2026-08-26)
base_confidence: high
lifecycle: active
lifecycle_changed: 2026-08-29
provenance: synthesized
summary: "DIL-001 Dil stratejisi: EN+TR çıkış, DE/ES/FR genişleme kriterleri, global hesap İngilizce, TR tek uzantı, lokalizasyon ilkeleri. hreflang teknik brief Ozan'a ayrı dokümanda."
---

# Remembered: Dil Stratejisi (DIL-001)

> Görev sahibi: Alleksenes / İ. Mert · Destek: Doğa · Deadline: hafta sonu (entegre/dil mevzusu) + yarın/cuma toplantı

## 1. Stratejik İlkeler

1. **"Architecture multilingual from day one; content does not have to be."**, Yazılım mimarisi ilk günden çok dilli; içerik kademeli dolar. (PRD'den)
2. **EN = global/default dil.** İngilizce evrensel erişim + "global hesap yabancı olmalı" hissi (Uğur).
3. **TR = ilk güçlü lokalizasyon.** Tek TR uzantı sayfa; uzun vadede her yerden oturur.
4. **Genişleme sırası (veriye göre):** DE → ES → FR → diğerleri. Ülke hesabı açmak traction sonucudur, teknik karar değil.
5. **Gerçek lokalizasyon, makine çevirisi değil.** Google çok dilli yapılarda içeriğin gerçekten lokalize edilmesini ayırır; makine çevirisi tek başına yetmez.
6. **Kullanıcı kontrollü dil değiştirici.** IP'den tahmin edip zorla yönlendirme yok; kullanıcı dili kendi seçebilir.

## 2. Dil Mimari Kararları (Ozan'a brief'in özeti)

| Karar | Değer | Gerekçe |
|---|---|---|
| URL yapısı | `/en/` + `/tr/` subdirectory | Google önerisi; tek domain otoritesi; kolay hreflang |
| hreflang | Her dil + `x-default` | Çok dilli indexleme; doğru dil eşleşmesi |
| sitemap | Ayrı dil girişleri | Google'ın dil değişkenlerini görmesi |
| canonical | Self-referencing + dil alternatifi | Otorite dağılmasın |
| Dil değiştirici | UI'da görünür (header/footer) | Kullanıcı kontrolü; IP zorlaması yok |
| Default | `en` (global default) | Kullanıcı dilini belirleyemezse EN |

## 3. DE/ES/FR Genişleme Kriterleri (veriye dayalı)

Bir sonraki dil NE ZAMAN açılır:

| Kriter | Eşik (öneri) | Kaynak |
|---|---|---|
| Organik trafik | İlgili dilde aylık 5.000+ oturum | GSC per-property |
| Arama hacmi | Hedef dilde "memorial/obituary" niş kelimelerde aylık 10.000+ toplam arama | Keyword araştırması |
| Kayıt/oluşturma | İlgili ülkeden kayıtlı kullanıcı sayısı anlamlı eşiğe ulaştı | Analitik |
| Talep | Topluluk/PR'den gelen dil talebi | Sosyal dinleme |

**Sıra önerisi:** DE (büyük pazar, kültürel miras duyarlılığı) → ES (Latin Amerika + İspanya, yas kültürü güçlü) → FR (Fransa, "droit à l'oubli" tartışmaları, dikkatli) → diğerleri.

## 4. Global Hesap = İngilizce (sosyal)

- Tek global hesap (IG/TikTok/YT/FB) **İngilizce** içerik üretir.
- TR içerik, TR uzantı hesapta/sayfada paralel yürür.
- Ülke hesapları (Remembered Deutschland vb.) traction sonucu açılır.

## 5. İçerik Lokalizasyonu İlkeleri

1. **Her dilde aynı editoryal mimari** (Portrait→Identity→Life→Timeline→Legacy→Places→Quotes→Archive→Sources→Remember)
2. **Çeviri = editör onaylı.** AI çevirisi ham çıktıdır; editör (Doğa + ekip) onaylar.
3. **Kültürel hassasiyet:** ölüm/yas ritüelleri dile göre değişir (TR'de mevlit, DE'de Trauerfeier, FR'de hommage). İçerik yerelleşirken ritüel dili de yerelleşir.
4. **Antik Yunanca/şiir/motto gibi sabit ifadeler** (∞, "Unutulmak ikinci ölümdür") tüm dillerde aynı kalır veya kültürel karşılığıyla verilir, marka sabitleri.

## 6. Makine Çevirisi Yasağı (teknik gerekçe)

Google, makine çevirisiyle üretilmiş düşük kalite içeriği ayrı tutar ve cezalandırabilir. Bu yüzden:
- Teknik altyapı hazır (hreflang, subdirectory) ama içerik **insan/editor onaylı** akar.
- AI çevirisi kullanılırsa: editör onayı + kalite kontrol + dil uzmanı review (bizde filoloji uzmanlığı var).

## 7. Teslimatlar (DIL-001)

- [x] Strateji dokümanı (bu dosya)
- [ ] hreflang teknik brief → **SEO uzmanı alanı** (SEO-001; Ozan'a teknik uygulama uzmanla birlikte gidecek)
- [ ] Dil değiştirici UX notu → tasarım (TS-001)
- [ ] DE/ES/FR kriter eşikleri → PR/analitik kararları (SEO teknik analizi değil)

## 8. Sachphilologie dönüşü (2026-09-06)

Owner dönüşü: yapacağımız filoloji Wortphilologie'den Sachphilologie'ye intikal etmiştir. Antik yazıt, çömlek ya da tiyatro oyunu gibi kültüre aracılık eden bir nesne olarak okunur; alınmasının amacı, ölüyü yad etmenin ve anmanın bir medium olarak nasıl dillendirildiği ve ritüelleştirildiğidir. Bu notun teknik mimarisi (EN+TR, hreflang, editör onayı) aynen kalır; korpus katmanının amacı ve alıcısı bu dönüşle açılır: Courtney örneklemi, üretim otomasyonunun eğitimi, RAG'ı ve kanonlaştırması içindir. Scipio'lar dahil tekil metin işin sahibi değildir; davranış sahiptir. ^[inferred]

Uygulama hattı: örneklem ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]]) davranış etiketiyle okunur, otomasyonu besler, otomasyonun çıktısı palinode döngüsünden ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/palinodie-yontem-notu|palinode yöntem notu]]) geçmeden kanonlaşmaz. Çerçevenin tam metni [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]] içinde.

## İlgili

- [[global-lansman-stratejisi|Global Lansman Stratejisi]]
- [[is-tanimi-ve-gorev-konumlanmasi|İş Tanımı Master Derleme]]
- [[kurumsal-kimlik-briefi|Remembered Manifesto]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|DIL-001 Revizyon: Filologun Kalemi]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma Biçimleri Denemesi]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/palinodie-yontem-notu|Palinode Yöntem Notu]]

## 9. Semantik alan kararları (2026-09-06)

Owner'ın dil kararları tek kelime yerine semantik alan olarak kurulur; tam kayıtlar [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]]ndadır (SEM-01..13+). Bu stratejinin ürün yüzeyine giren kararları: temel anma eylemi "mum yakmak" (kandil kültürel işaretli alternatif, SEM-03); kapsül değil "Sandık" (SEM-07); "Miras" alan adı + "emanet" bağlam fiili (SEM-08); EN açılış "Who are you remembering?" + "Whose memory do you carry?" (SEM-09); Pulse Board adı owner seçimi bekliyor (SEM-06). Kural: owner seçmeden hiçbir kavram siteye yazılmaz; genişleme sırasındaki her yeni dil bu alanların kendi dilindeki karşılığıyla kurulur.

