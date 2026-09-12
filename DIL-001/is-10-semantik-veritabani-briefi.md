---
title: >-
    İŞ 10 briefi: Semantik alan veritabanı madenciliği
created: "2026-09-06"
updated: "2026-09-06"
type: reference
tags: [remembered, dil, semantik, gorev, brief]
sources:
  - "Alleksenes direktifi (2026-09-06): 'benim dil kullanımımdan, bakış açılarımdan, getirdiğim kaynaklardan derleyerek bir semantik veritabanı kurgulayacağız'"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-001-session-briefleri-20260905|DIL-001 Session Briefleri]]"
base_confidence: high
lifecycle: active
lifecycle_changed: "2026-09-06"
provenance: "synthesized"
tier: core
summary: >-
    İŞ 10: vault'taki owner dili ve işaretlerinden semantik alan kayıtları çıkarıp
    semantik-alan-veritabanı.md'yi dolduran madencilik briefi.
---

# İŞ 10: Semantik Alan Veritabanı Madenciliği

> Amaç: owner'ın dil kullanımı, bakış açıları ve gerekçeli redlerinden semantik alan kayıtları çıkarmak. Veritabanı iki alıcıya hizmet eder: üretim otomasyonunun RAG'ı (tarihi şahsiyet üretimleri dahil) ve basın kiti, pitch deck, PR, dijital pazarlama dili. Owner bu sözlüğü MANUEL YAPMAZ; agent'lar madencilik yapar, owner tarama yapar.

## Ortak kurallar

[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-001-session-briefleri-20260905|DIL-001 session briefleri]] §1'deki ortak çekirdek aynen geçerlidir (okuma listesi, yazım kuralları, çalışma disiplini, kapanış). Ek kurallar:

- Tek kelime finalize edilmez; semantik alan kaydı açılır.
- Red, gerekçesiz kaydedilmez; gerekçe otomasyonun aynı hataya düşmesini önler.
- Her kaydın kaynak satırı zorunludur (wikilink ya da tırnak içinde owner cümlesi).
- Owner'ın kişisel kanon dosyalarından (USER.md, SOUL.md) hiçbir içerik kopyalanmaz; yalnız ses kalibrasyonu içindir.
- Em-dash yasak; paragraf tek satır; uydurma yok; emin olunmayan yer [?]; genellemeler ^[inferred].

## AMAÇ (GOAL)

[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]] içinde SEM-01'den itibaren numaralı kayıtların sayısı 30'u aşmış; her kayıtta adaylar, gerekçeli redler (varsa), owner işareti, kullanım yüzeyleri ve kaynak dolu.

## YAP

1. Aşağıdaki kaynakları baştan sona tara; owner cümlesi, işareti, düzeltmesi ve redlerini topla:
   - [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]: tüm allek comment'ler (17 madde).
   - [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]]: bölüm 8'deki onay satırları, altı kural, kesilmiş cümleler.
   - [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-001-session-briefleri-20260905|session briefleri]] ve [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/gorev-briefi-courtney-metinleri-obsidiana|Courtney Görev Briefi]]: owner direktifleri.
   - İŞ 6, 7, 8, 9 çıktıları ve raporları (gorevler/raporlar/): KARAR-BEKLIYOR listeleri, owner kararı bölümleri.
   - [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]]: owner feedback'leri.
   - [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]] ve [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma Biçimleri Denemesi]]: owner dönüşleri.
2. Her yeni alan için kayıt şablonunu aynen kullan; SEM numarası mevcut son numaradan devam eder.
3. Mevcut kayıtlarla (SEM-01..SEM-10) çift sayımı önle; aynı alan varsa mevcut kaydı zenginleştir, yeni açma.
4. Aranacak alan aileleri (tam liste değil): hitap ve sesleniş, dilek kalıpları, taziye dili, ritüel fiilleri, mekân ve topluluk adları, kalıcılık ve koruma dili, mahremiyet ve yetki, sayı ve ölçü yasağı, soy ve akrabalık, göç ve çok dillilik, ses ve kayıt.

## DOĞRULA (komutlarla koştur, çıktıları rapora aynen yaz)

1. Kayıt sayısı: grep -c "^### SEM-" (30 üstü olmalı).
2. Her kayıtta "kaynak:" satırı var (grep -L ile boş kalanları listele).
3. em-dash sayısı: grep -c "—" (0 olmalı).
4. Red gerekçesiz kalmamış: "reddedilen:" satırında "(gerekçe" ya da "gerekçe:" geçmeyen satır yok (elle kontrol, rapora listele).

## KAPANIŞ

1. Rapor: projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-raporlar/is-10-raporu.md (yapılan, doğrulama çıktıları, engeller, KARAR-BEKLIYOR listesi).
2. log.md, index.md ve git commit ana session'da yapılır; agent bunlara dokunmaz (sapmayı raporda not et).
3. .obsidian'a dokunma; projects/remembered/ dışına yazma.
