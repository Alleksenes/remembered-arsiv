---
title: "DIL-001 Gövde Sentezi Briefi: dört archived nottan owner kararlı dil hukukunun gövdeye promosyonu"
created: "2026-09-07"
updated: "2026-09-07"
type: reference
tags: [remembered, dil, gorev, brief, sentez]
sources:
  - "Alleksenes direktifi (2026-09-07): 'gövdeye sentezlenebilecek yerler varsa katalım, tamamen kendi çabamızı da çöpe atmayalım'"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|DIL-001 Uyumlanma Sentezi]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|Semantik Alan Veritabanı]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm Cümlesi ve Akış Kurgusu]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma Biçimleri Denemesi]]"
base_confidence: high
lifecycle: active
lifecycle_changed: "2026-09-07"
provenance: "synthesized"
summary: "Archived dört DIL-001 notundaki owner kararlı dil kararlarını gövde notlarına taşıyan tek session'lık kapalı görev paketi."
---

# DIL-001 Gövde Sentezi Briefi

> Kullanım: yeni bir agent session aç, tek satır bırak: "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/gorev-briefi-dil001-govde-sentezi|gorev-briefi-dil001-govde-sentezi]] dosyasını oku, İŞ A'dan başlayarak tüm işleri baştan sona tamamla." Model-agnostic yazıldı; Hermes olmayan agent da koşabilir. Tek session'lık iş; iki ayrı session'a bölünmez.

## 0. Durum ve amaç

DIL-001 uyumlanma kararı ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|dil-001-uyumlanma-sentezi-20260907]]) ile korpus, yöntem ve otomasyon katmanı `lifecycle: archived` oldu. 2026-09-08 owner düzeltmesi: semantik alan veritabanı GÖVDEYE GERİ ALINDI (aktif, teslimat 0); bu brief artık ondan archived depo olarak değil AKTİF KAYNAK olarak yararlanır. Bu brief'in işi: gövdeye taşınacak owner onaylı dil kararlarını aktarmak. Kaynaklar:

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|Semantik Alan Veritabanı]] (SEM-01..40; AKTİF, taşıma değil senkron: İŞ A tablo, kaynağın güncel haliyle kurulur)
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm Cümlesi ve Akış Kurgusu]] (archived, taşınır)
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma Biçimleri Denemesi]] (archived, taşınır)

Hedef gövde notları iki tanedir:

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] (TR içerik çekirdeği, DIL-001 teslimat 3)
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] (ses disiplini, DIL-001 teslimat 4)

Sentez ölçütü: bir kayıt yalnızca owner cümlesiyle işaretliyse (kaynakta aynen alıntı) ya da gövde notundaki açık bir §8 maddesini karşılıyorsa taşınır. SEM artık aktif olduğu için İŞ A ondan 'taşıma' değil 'senkron' yapar: tablo, SEM-01..40'ın owner işaretli kayıtlarından güncel haliyle kurulur ve kaynak gövdede kalır.

## 1. Ortak kurallar (her işte şart)

- Frontmatter'sız değişiklik yok: hedef notların SCHEMA'nın 11 zorunlu alanı korunur; `updated: "2026-09-07"`, `lifecycle: active`, `lifecycle_changed: "2026-09-07"` güncellenir.
- Em-dash yasaktır. Paragraf tek satır; hard-wrap yok.
- Wikilink: `[[tam-yol-dosya|gorunen-ad]]` biciminde tam yol ve alias; düz `.md` referansı yok. (Bu satır örnektir, gerçek link değildir.)
- Uydurma yok: emin olunmayan yer `[?]`; karar gereken yer `KARAR-BEKLIYOR` etiketiyle işaretlenir ve iş durmaz.
- Genellemeler `^[inferred]`; owner'ın çıplak söylediği işaretsiz (SOURCE).
- Türkçe yazım: Latinleştirme ve Türkçeleştirme yasaktır.
- Notion'a hiçbir şey yazılmaz; Notion yüzeyleri (DIL-001 ve PR-001) zaten günceldir.
- `.obsidian/` altına dokunma.

## 2. İŞ A: TR Retorik Kavram Notu'na "Owner kararlı semantik alanlar" bölümü

Hedef: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]].

Yeni bölüm başlığı: `## Owner kararlı semantik alanlar (2026-09-06 itibarıyla)`. Bölümün giriş cümlesi: bu tablo, DIL-001'in semantik alan veritabanındaki owner işaretli dil kararlarının güncel özetidir; tam kayıtlar ve gerekçeli redler [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]]ndadır.

Tablo kolonları: `Alan` | `Karar / adaylar` | `Durum` | `Kaynak SEM`.

Kayıtlar (veritabanını tamamen oku, owner işaretli olanları tabloya taşı; aşağıdaki liste kontrol listesidir, tahmin değil):

| Alan | Karar / adaylar | Durum |
|---|---|---|
| Create Memorial açılışı | Tek default yok; A (owner'ın verdiği cümle), B (dilek kullanıcı seçimi), C (anma biçimi paketine bağlı) adayları semantik alanda | KARARLI (owner: "varsayılan olmaz, seçilen cümleler") |
| Ölüm cümlesi ifade edişleri | Platform sesinde çıplak "öldü" YOK; "vefat etti" (duyuru), "aramızdan ayrıldı" (yalnız topluluk), "kaybettik" (yalnız aile), "hayata veda etti" (duyuru) sahiplikle kullanılır | KARARLI (owner: "farklı ifade edişleri kullanmak değerli; dokunaklı bir iş yapıyoruz") |
| Mum ve kandil | Temel eylem "mum yakmak"; "kandil yak" kültürel işaretli alternatif; kandil default değil | KARARLI |
| Yad şeridi fiilleri | "Kandil yak. Dilek tut. Dua oku. Çiçek bırak. Mektup yaz. Kalbininde yaşat." + üst satır "Her dil ve dinde ölüyü yad etmek mümkün." (EN: "Remember the dead in every language and every faith.") | KARARLI (liste açık; üst satır owner cümlesi) |
| Kütük adı | "Dijital Vefat Kütüğü" + "Yad Etme Kütüğü" ikisi birden | KARAR-BEKLIYOR (owner: "her ikisi, uğur'la bakarız buna") |
| Pulse Board alanı | Adaylar: "Hatırat Kürsüsü", "Merhumun Huzuru", "Anma Divanı"; reddedilenler: "Canlı Anma Meclisi", "dergâh", "canlı" | KARAR-BEKLIYOR |
| Kapsül ve sandık | "Sandık"; "kapsül" reddedildi; mektup kartı "Mektup" kalır | KARARLI |
| Miras ve emanet | Alan adı "Miras"; "emanet" devir ve muhafaza cümlelerinde fiil; tek kelimeye sıkıştırma yok | KARARLI (owner: alternate kullanım daha zengin alan) |
| EN açılış | "Who are you remembering?" + "Whose memory do you carry?" her ikisi | KARARLI |
| Ortak laht | İki kişilik sayfa kurgusu (iki ad, iki tarih yan yana; katkılar sahiplikle işaretli) | KARARLI (owner: "Ortak laht antropolojisi tam da Remembered'ın yaratacağı bir unsur") |
| Yoldan geçene sesleniş | "Bu sayfada onun hayatından bir iz var." + soru biçimli davet; emir yığını ve zorunlu katkı reddedildi | KISMEN KARARLI (filolog §8 açık maddesine bağlı) |
| Boş sayfa dili | "Bu sayfa bir hayatın başlangıcı. İlk cümleyi sen yaz." | KARAR-BEKLIYOR (filolog §8 "kesilmiş cümleler örnek kabul" maddesi açık) |
| Anı daveti sahnesi | "Onunla geçen bir akşamı anlat." / "En son ne zaman güldünüz birlikte?" + sade karşılıklar "Ondan sana ne kaldı?" / "What do you keep of them?" | Aday olarak kayıtlı; örnek kabul maddesi açık |

Kural: tablodaki her satırın kaynağı SEM numarasıdır; tabloya veritabanında olmayan hiçbir şey eklenmez. Veritabanında owner işaretli ek kayıt varsa (SEM-13 ve sonrası) aynı biçimde eklenir.

## 3. İŞ B: filolog kalemi'ne ekran katmanı ve kural 6 amendmanı

Hedef: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|DIL-001 Revizyon: Filologun Kalemi]]. Üç ekleme:

### 3.1 Kural 6 amendmanı (bölüm 6'nın altına, içeriği silmeden)

Bölüm 6'daki "Bir hayatı pazarlama" kuralının platform uygulaması owner tarafından 2026-09-06'da amendmanlandı: platform sesinde çıplak "öldü" yoktur; "dokunaklı bir iş yapıyoruz, ana haber bülteni veya istihbarat raporu hazırlamıyoruz" (owner). Ölüm cümlesi haritası sahiplik ayrımı olarak kalır: "kaybettik" yalnız aile, "aramızdan ayrıldı" yalnız topluluk, "vefat etti" ve "hayata veda etti" duyuru dili; hepsi kullanıcının tercih listesinde, varsayılan olmaz. Kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]] SEM-02.

Bu eklemenin ardından bölüm 8'deki ilgili satır güncellenir: "[ ] Yasak kelime listesi (bölüm 6)" maddesine "kural 6'nın platform uygulaması owner amendmanıyla kesinleşti (SEM-02)" notu eklenir; satırın checkbox'ı yalnızca kalan açık kısım (ebediyet vaadi vb.) için açık kalır.

### 3.2 Ekran cümle katmanı (bölüm 4'ün sonuna yeni alt bölüm: "Ekran bazında derinleştirme (2026-09-06 turları)")

[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm cümlesi ve akış kurgusu]] bölüm 5'ten, Create Memorial akışının ekran ekran cümleleri TR/EN olarak taşınır. Her cümle yüksek sesle okunur stilindedir; taşınanlar:

- Ekran 1 (ad): "Kimi anıyorsunuz?" + alt satır "Adı, doğduğu yıl, öldüğü yıl. Bilmediğini boş bırak; soru işareti de bir cevaptır." EN: "Who are you remembering?" / "Name, year of birth, year of death. Leave blank what you do not know; a question mark is an answer too."
- Ekran 1b (iki kişilik sayfa): "Bu sayfa iki kişiyi taşır. Anne ve kız; karı ve koca; ana ve baba." EN: "This page can hold two people. A mother and a daughter. A husband and a wife. A mother and a father."
- Ekran 2 (hatırat): owner sorusu aynen "Sizdeki hatıratı nasıldır?"; sade karşılık "Ondan sana ne kaldı?" EN: "What do you keep of them?"
- Ekran 3 (sahne): owner sorusu aynen "Nasıldı bir akşamı, hüznü, neşesi..?"; sade karşılıklar "Onunla geçen bir akşamı anlat." / "En son ne zaman güldünüz birlikte?" EN: "Tell us one evening you spent with them." / "When did you last laugh together?"
- Kapanış: "Bu sayfa bir hayatın başlangıcı. İlk cümleyi sen yaz." (zaten §4'te var; eklenmez, çapız referans verilir)
- Ölüm cümlesi haritası: sahiplik tablosu ("kaybettik" aile, "aramızdan ayrıldı" topluluk, "vefat etti"/"hayata veda etti" duyuru; platform sesinde çıplak "öldü" yok) ve iki tarih altındaki satır: TR "Bu iki tarih arasında bir hayat var. Aşağıda onu anlatanlar var." EN "Between these two dates, a life. Below are the people who remember it." Bilinmeyen tarih "1940-?" olarak işaretlenir.

Kaynak işareti her satırda: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 5 ve [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|semantik-alan-veritabani]] SEM kayıtları.

### 3.3 İki tarih satırı ve davranış REC'lerinin ürün gereksinimi hanesi (bölüm 8'e)

Bölüm 8'deki "[ ] 'Kayıp ses' ve 'zaman kapsülü' cümleleri ürün gereksinimine işlenecek" maddesine ikinci bir madde eklenir: "[ ] Create Memorial üç sorusu ve ekran cümleleri ürün gereksinimine işlenecek (Ozan); kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] ekran katmanı."

## 4. İŞ C: anma biçimleri denemesi'nden davranış REC'lerinin taşınması

Hedef: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] ekran katmanı bölümüne (İŞ B'de açılan) ikinci bir alt bölüm: "Anma davranışları: taşınan REC'ler (2026-09-06)".

[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma biçimleri denemesi]]nin 12 davranışından yalnızca ürün diline doğrudan giren REC'ler, şiir numarası kaynak işaretiyle taşınır (SOURCE/INT katmanı archived kalır, taşınmaz):

1. Boş sayfa yetkisi: "Bu sayfa bir hayatın başlangıcı. İlk cümlede sen yaz." daveti; emir yığını kurma. (taş 1, 8, 17, 70)
2. Ritüel sahnesi: kandil, mezar başı anı gibi törenlerde yalnız metni değil sahneyi kaydetme daveti ("o gün kim vardı, hangi şarkı çaldı"). (taş 1)
3. İtiraf alanı: "Söylemediklerin mi var? Buraya bırak."; ödenmemiş borç metaforu ekrana yazılmaz. (taş 6, 7)
4. Sahne daveti: "Onunla geçen bir akşamı anlat."; hayat özeti alanı istenmez, üç fiillik anı üç sıfatlı övgüden ağır basar. (taş 16, 17, 109)
5. Sağkayken yazılan yüzey: zaman kapsülü ve son irade "sağkayken yazılır" konumlaması; "Sen yazarsın. Biz açarız."; haleflik bu yüzeye bağlanır. (taş 130, 59, 28)
6. Çocuk sesi ayrımı: "Bunu ailesi yazdı" ile "bunlar onun sözleri" etiketleri ayrı; çocuk adına platform ağzından teselli kurulmaz. (taş 70, 113, 179, 178)
7. Evcil hayvan sayfası: İŞLENMEZ (2026-09-07 owner revizyonu). Uğur evcil hayvanlar için ayrı bir alan açıyor; eski "aynı kandil, aynı anı daveti" REC'i geri alındı. Bu madde İŞ C taşımalarına DAHİL EDİLMEZ; sadece [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 7'deki REVİZE notuyla uyum için burada işaretlidir. (taş 200, 203, 204)
8. Kayıp ses boşluğu: "Onun sesi burada yok. Belki bir kaset, bir telesekreter kaydı vardır. Bulursan ekle."; boşluk gizlenmez. (taş 76, 75)
9. Ton: defter, matem panayırı değil; "Bu iki tarih arasında bir hayat var." satırı; yas kaynakları yıl dönümlerinde de sunulur. (taş 21, 199, 61)
10. Kalıcılık: vaat kelimesi yerine yapılmış iş gösterilir: dışa aktarım dosyası, haleflik planı, yıllık durum sayfası. (taş 199A)
11. İtirafın yayını: anı yayınlanmadan önce sahibine "Bu akşamı onun adına yayımlamama izin verir misin?" sorusu. (taş 25)
12. Keşif katmanı: seçilmiş fotoğrafların ilk harfleri, yıl dönümünde açılan küçük not; oyun zorunlu değildir. (taş 28)

"Taşınmayanlar" listesi de özetle taşınır (formül kopyalanmaz; ölümle övünme dili girmez; ölüm nedeni suçlayıcı isim yazılmaz; adak kelimesi ekranda kullanılmaz; "en çok anılan" sıralaması yok).

## 5. Kapanış protokolü

1. Doğrulama: iki hedef notun tüm wikilink'lerini vault çapında çözümle (script veya manuel); ölü link 0 olmalı. Em-dash taraması 0 olmalı.
2. `log.md` (vault kökü) append-only tek satır: `- [2026-09-07] DIL001_GOVDE_SENTEZ | owner kararlı semantik alanlar + ekran katmanı + davranış REC'leri gövdeye taşındı`.
3. `index.md` (vault kökü) Remembered bölümüne tek satır.
4. `git add -A && git commit -m "wiki-dil001: govde sentezi (semantik alanlar + ekran katmanı + davranış REC'leri)"`.
5. Rapor: `projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-raporlar/is-govde-sentezi-raporu.md` (taşınan kayıt listesi, SEM numaraları, atlanan içerik ve gerekçesi).

## 6. Bu briefin işlemediği şeyler (bilinçli olarak archived kalanlar)

- Üretim otomasyonu hattı: davranış etiketlerinin otomasyon şablonuna dönüşmesi, 72 kayıtlık pilot, RAG beslemesi, palinode döngüsü (Sachphilologie notuyla birlikte archived).
- İŞ 5 (tasnif ikinci tur) ve Courtney metin notları üretimi: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/gorev-briefi-courtney-metinleri-obsidiana|Courtney görev briefi]] kendi içinde durur; istenirse bağımsız koşturulur.
- Luna arşivi kuyruğu: envanter archived; iş açılırsa oradan devam edilir.

## İlgili

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-001-uyumlanma-sentezi-20260907|DIL-001 Uyumlanma Sentezi ve Revizyon]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/semantik-alan-veritabani|Semantik Alan Veritabanı]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm Cümlesi ve Akış Kurgusu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|Anma Biçimleri Denemesi]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-001-session-briefleri-20260905|DIL-001 Session Briefleri (eski 9 işlik sistem, archived)]]
