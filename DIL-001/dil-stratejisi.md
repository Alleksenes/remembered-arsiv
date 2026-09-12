---
title: "DIL-001: Dil stratejisi (EN+TR mimarisi)"
created: "2026-08-28"
updated: "2026-09-07"
type: project
tags: [remembered, task, language]
sources: []
base_confidence: high
lifecycle: active
lifecycle_changed: "2026-09-07"
provenance: "synthesized"
summary: "DIL-001 görev yüzeyi: Uğur'un F8 tanımıyla uyumlanan dört teslimat (strateji omurgası, teknik brief, TR kavram çekirdeği, ses disiplini); fazlalık katmanı deprecated."
---
# Dil stratejisi (EN+TR mimarisi)

## Nitelikler

| Alan | Değer |
|---|---|
| Task ID (primary key) | `DIL-001` |
| Owner (asli sorumlu) | alleksenes |
| Supporters (destek/denetmen) | ozan, doga |
| Preceding (öncül) | yazilim-cok-dilli-mimari |
| Next (ardıl) | editoryal-ilk-30-profil, global-pr-basin |
| Work area | language |
| Priority | high |
| Due date | entegre/dil mevzusu hafta sonu + cuma toplantı (strateji notu başlığındaki owner kaydı) |

> Görev notu adı, ID değil görevin kendi adıdır. ID (`DIL-001`) yalnızca database mantığında birincil anahtardır; Notion'da relation'larla diğer DB'lere foreign key olarak bağlanır.

## Açıklama

Uğur'un ilk planındaki tanım (F8, [[projects/remembered/02-ekip-gorev/gorev-dagilimi-v3-ugur-revizyonu|gorev-dagilimi-v3-ugur-revizyonu]]): "EN+TR; global hesap İngilizce; TR tek uzantı; DE→ES→FR; Architecture multilingual from day one; content does not have to be." 2026-09-07 uyumlanma kararıyla DIL-001'in kapsamı bu tanımla sınırlandı; 2026-09-08 düzeltmesi: semantik alan veritabanı (SEM-01..40) deprecated'tan ÇIKARILDI, gövde karar deposu olarak geri alındı (owner: "semantik alan kurmuşsun... bu deprecated olursa çalıştığımızın ne anlamı kalır"). Korpus/yöntem/otomasyon katmanı deprecated kenara durur. Kıyaslama ve karar: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|dil-001-uyumlanma-sentezi-20260907]].

## Alt Adımlar / Aşamalar (uyumlanan beş teslimat)

### 0. Semantik alan veritabanı (karar deposu, 2026-09-08 gövdeye geri alındı)
**Nasıl:** Owner'ın tek kelime kararı yerine semantik alan tutan kayıt sistemi: SEM-01..40. Her alan: adaylar + gerekçeli redler + owner işaretleri + kullanım yüzeyleri. İki alıcısı: (1) üretim otomasyonu/RAG ana başvuru kaynağı, (2) basın kiti, PR ve dijital pazarlama dili deposu. Kural: tek kelime finalize edilmez; bir aday yalnız reddetme gerekçesi belli olduğunda düşer. Tam kayıtlar: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]].
**Araç:** gövde karar deposu; kapalı kararlar SEM numarasıyla gövde notlarına bağlanır

### 1. Dil stratejisi omurgası
**Nasıl:** EN global default, TR ilk güçlü lokalizasyon, DE→ES→FR genişleme sırası, kullanıcı kontrollü dil değiştirici, makine çevirisi yasağı. Tam metin: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-notu|DIL-001 Dil Stratejisi]].
**Açık maddeler:** dil değiştirici UX kararı (tasarım), DE/ES/FR eşik kararları (traction verisi gelince).

### 2. Ozan'a teknik brief (hreflang, x-default, subdirectory)
**Nasıl:** /en/ + /tr/ subdirectory, her dil + x-default hreflang, ayrı dil sitemap girişleri, self-referencing canonical, IP zorlaması yok. Strateji notu bölüm 2 tablosu brief'in kendisidir.
**Kaynak:** [DigitalApplied, Hreflang Guide](https://www.digitalapplied.com/blog/international-seo-hreflang-multilingual-guide)

### 3. TR içerik çekirdeği
**Nasıl:** /tr sayfalarının kavram seti ve site yazı planı: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]. Lokalizasyon kuralı: makine çevirisi yasak, editör onaylı akış.

### 4. Ses disiplini
**Nasıl:** Hem TR hem EN hem basın metinlerinin ses kaynağı: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] (altı neşter kuralı, kesilmiş TR/EN cümleler). Açık owner kararları: yasak kelime listesi, ses klonu çerçevesi (rıza, sınırlar, dil katmanı).

## Deprecated katman (2026-09-07, düzeltildi 2026-09-08)

Epigrafik anma laboratuvarı, Courtney 206 şiir hattı, Sachphilologie, Palinode, Ritüel mozaik, Ölüm cümlesi akışı, Anma biçimleri denemesi, session briefleri, HOMONOIA briefi, Luna arşivi: `archived` işlendi; (SEMANTİK ALAN VERİTABANI bu listeden 2026-09-08'de çıkarıldı; artık gövde teslimi, aşağıya bkz.) içerik silinmedi, başka işe dönerse lifeline geri açılır. Tam liste ve gerekçeler: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|dil-001-uyumlanma-sentezi-20260907]] bölüm 4. Archived notlardaki owner onaylı dil kararlarının (SEM kayıtları, ekran cümleleri, davranış REC'leri) teslimat 3 ve 4'e taşınması [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/gorev-briefi-dil001-govde-sentezi|gorev-briefi-dil001-govde-sentezi]] paketiyle yapılır.


## Şematik: DIL-001 bağlantı haritası (2026-09-08)

Neyin neye bağlandığı tek bakışta:

```text
KARAR KAYNAĞI
semantik-alan-veritabani (SEM-01..40, AKTİF karar deposu)
  ├─ owner cümleleri + gerekçeli redler + kullanım yüzeyleri
  └─> kapalı kararlar SEM no ile gövdeye bağlanır

TESLİMAT 1 · Strateji omurgası
dil-stratejisi-notu
  ├─ EN default + TR lokalizasyon, hreflang/x-default, dil değiştirici
  ├─ DE→ES→FR eşikleri (traction bekler)
  └─> Ozan'a teknik brief (hreflang) — açık

TESLİMAT 3 · TR içerik çekirdeği
tr-retorik-kavram-notu
  ├─ kavram seti + site yazı planı
  ├─ 2026-09-08'de SEM-03/06/07/08 kararlarıyla senkron
  └─> canlı site TR sözlüğü ile hizalama (Uğur paketi K9)

TESLİMAT 4 · Ses disiplini
dil-stratejisi-filolog-kalemi
  ├─ altı neşter kuralı + ekran cümleleri (§4) + karar yüzeyi (§8, §8.1)
  ├─ kaynak: olum-cumlesi-ve-akis-kurgusu (İŞ B), anma-bicimleri (İŞ C)
  └─> ürün gereksinimi briefi (Ozan) — açık

İŞ PAKETİ (gövde sentez briefi: İŞ A/B/C)
  ├─ İŞ A: SEM owner kayıtlarından tr-not tablosu (senkron)
  ├─ İŞ B: ekran cümleleri filolog-kalemi'ne
  └─ İŞ C: davranış REC'leri (d.7 hayvan hariç)

ARCHIVED LİFLİNE (beklemede, silinmedi)
  ├─ epigrafik lab, palinode, sachphilologie, ritüel mozaik, olum-cumlesi
  ├─ anma-bicimleri, courtney hattı, luna hattı, session briefleri, homonoia
  └─> ihtiyaç olursa kartı geri açılır (karar deposu SEM artık burada değil)

PR-001 (bu hattın müşterisi)
  ├─ basin-kiti-20260911/ (TR + EN master) ← üretim devam ediyor
  ├─ dil hattından: ses kuralları (filolog kalemi), kavramlar (tr-not + SEM)
  └─> kilit: Uğur karar oturumu (9 madde) + Ozan ürün yanıtları
```

## PR-001 öncesi DIL-001 kapanış defteri (2026-09-08)

PR işine temiz girmek için DIL-001 tarafında kapatılacaklar; kapanınca -- ile işaretlenir:

- [x] Semantik alan veritabanı gövdeye geri alındı (2026-09-08 owner kararı)
- [x] DIL-001 dosya düzeni: dil001-docs / dil001-deprecated / dil001-raporlar altında toplandı
- [x] Şematik bu nota işlendi
- [ ] Gövde sentez briefi koşturulacak (İŞ A/B/C; SEM artık senkron kaynağı, archived üç not taşınır)
- [ ] Uğur karar oturumu: paket 9 madde (kütük adı, Pulse Board, dinî ritüel, ziyaret kartı, Yad Etti, ses klonu, alt başlık, iletişim kişisi, canlı site sözlüğü 5 açık karar)
- [ ] Ozan'a hreflang teknik briefi (teslimat 1 açık maddesi)
- [ ] Ozan'a ürün gereksinimi briefi: ekran cümleleri + ses klonu çerçevesi (İŞ B sonrası)
- [ ] Canlı site TR sözlük hizalaması: IMMORTALIZE, "ebedi" politikası, kütük tam adı, Sessiz Saygı/tribute, dossier=kütük (Uğur paketi K9)
- [ ] Yasak kelime listesi kararı (B8 ertelendi; PR metinlerinde filolog kuralları zaten uygulanıyor)
- [ ] TR/EN eşleşme turu (basın kiti kapanış ölçütü)

## Bağlı Kuram (Obsidian)

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|DIL-001 Uyumlanma Sentezi ve Revizyon]]
- [[projects/remembered/01-strateji/global-lansman-stratejisi|Global Lansman Stratejisi]]
- [[projects/remembered/06-arastirma/pazar-arastirmasi-ve-intikal|Pazar Araştırması ve İntikal]]

## Dış Kaynaklar

- [DigitalApplied, Hreflang Guide](https://www.digitalapplied.com/blog/international-seo-hreflang-multilingual-guide)

## Not

Bu görev notu, CRM database şemasındaki tasks satırının Obsidian karşılığıdır ve DIL-001'in Obsidian yüzeyidir. Detaylı durum yüzeyi Notion DIL-001 kanban sayfasında tutulur.
