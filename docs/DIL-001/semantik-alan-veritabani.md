---
title: >-
    DIL-001 Semantik Alan Veritabanı
created: "2026-09-06"
updated: "2026-09-06"
type: reference
tags: [remembered, dil, semantik, otomasyon, rag]
sources:
  - "Alleksenes direktifi (2026-09-06): 'benim dil kullanımımdan, bakış açılarımdan, getirdiğim kaynaklardan derleyerek bir semantik veritabanı kurgulayacağız, sonra da bunu dil stratejimizle rag'e verip eğittireceğiz'"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm Cümlesi ve Akış Kurgusu]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|Ritüel Mozaik ve Kavram Revizeleri]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]]"
  - "[[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/is-10-semantik-veritabani-briefi|İŞ 10 Semantik Veritabanı Briefi]]"
base_confidence: high
lifecycle: active
lifecycle_changed: "2026-09-08"
provenance: "synthesized"
tier: core
summary: >-
    Owner dilinden derlenen semantik alan kayıtları: adaylar, gerekçeli redler ve owner işaretleri;
    otomasyon RAG'ının ana başvuru kaynağı (2026-09-08: gövdeye geri alındı, owner kararı) ve PR/pazarlama dilinin deposu.
---

# DIL-001 Semantik Alan Veritabanı

## Amaç ve iki alıcı

Bu veritabanı tek kelime kararı tutmaz; semantik alan tutar. Her alan, bir kavramın etrafındaki adayları, gerekçesiyle reddedilenleri ve owner işaretlerini bir arada taşır. İki alıcısı vardır: (1) RAG yoluyla üretim otomasyonunun (tarihi şahsiyet üretimleri dahil) ana başvuru kaynağı; (2) basın kiti, pitch deck, PR ve dijital pazarlama dilinin deposu. Ürün ekranı adayları da buradan süzer. (SOURCE)

## Kurallar

1. Tek kelime finalize edilmez; bir aday yalnız reddetme gerekçesi belli olduğunda alandan düşer.
2. Her kaydın kaynağı wikilink ya da owner cümlesidir; uydurma yok, emin olunmayan yer [?].
3. Reddiler gerekçesiz kaydedilmez; gerekçe, otomasyonun aynı hataya düşmesini önler.
4. Owner'ın kişisel kanon dosyaları (USER.md, SOUL.md) bu veritabanına kopyalanmaz; yalnız ses kalibrasyonu içindir.
5. Alan zenginliği kusur değil mallardır: alternate kullanım alanı zenginleştirir (owner, SEM-08 üzerinde). (SOURCE)

## Kayıt şablonu

```text
SEM-XX: alan adı
adaylar: ...
reddedilen: ... (gerekçe: ...)
owner işareti: ...
kullanım yüzeyleri: ... (otomasyon RAG / PR / ürün ekranı)
kaynak: [[...]]
```

## Kayıtlar

### SEM-01: Create Memorial açılışı
adaylar: "Ruhu şad olsun, kimi anıyorsunuz?" (owner taslağı); "Kimi anıyorsunuz?"; dilek kalıpları kullanıcı seçimi olarak ("Ruhu şad olsun", "Rahmetle anıyorum", "Çok özledim").
reddedilen: tek default açılış (gerekçe: varsayılan olmaz; dileğin sahipliği platformda olamaz).
owner işareti: "varsayılan olmaz, seçilen cümleler; daha doğrusu semantik alanlar olur." (SOURCE)
kullanım yüzeyleri: Create Memorial ekranı; otomasyon açılış üretimi.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 3 ve 6.1.
owner işareti: "varsayılan olmaz, seçilen cümleler; daha doğrusu semantik alanlar olur." (SOURCE)
karar (2026-09-08): B+C kırması. Çıplak soru "Kimi anıyorsunuz?" ana açılış; dilek katmanı kullanıcı seçimi ("Ruhu şad olsun", "Rahmetle anıyorum", "Çok özledim" öneri listesi). A seçeneği (dilek önerisi) listede korunur, varsayılan değil. KARAR-KAPANDI.
### SEM-02: Ölüm cümlesi ifade edişleri
adaylar: "vefat etti" (duyuru dili); "aramızdan ayrıldı" (topluluk); "hayata veda etti"; "kaybettik" (yalnız aile); "hakkın rahmetine kavuştu" [?].
reddedilen: platform sesinde çıplak "öldü" (gerekçe: dokunaklı bir iş yapılıyor; ana haber bülteni veya istihbarat raporu değil).
owner işareti: "ölümün etrafında dans etmek, yani farklı ifade edişleri kullanmak değerli." (SOURCE)
kullanım yüzeyleri: tüm ürün yüzeyleri; otomasyon ölüm cümlesi üretimi; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 4 ve 6.1.

### SEM-03: Mum ve kandil
adaylar: temel eylem "mum yakmak" ("Mum Yaktı", EN "Lit a candle"); "kandil yak" kültürel işaretli alternatif.
reddedilen: kandil'in default anma eylemi oluşu (gerekçe: kandil eşit değil mum; mum yakma Rum/Ortodoks geleneğidir, karışım hata üretir).
owner işareti: "kandil default anma eylemi değil, mum yakmak olsun." (SOURCE)
kullanım yüzeyleri: anma kartları; şerit.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 6 ve 7.

### SEM-04: Yad şeridi fiilleri
adaylar: "Kandil yak. Dilek tut. Dua oku. Çiçek bırak. Mektup yaz. Kalbinde yaşat." Üst satır: "Her dil ve dinde ölüyü yad etmek mümkün." EN eşlik: "Remember the dead in every language and every faith."
reddedilen: yok (liste owner ifadesiyle açık; "gibi" der).
owner işareti: koyu turuncu kavuniçi ton, sağdan sola akış. (SOURCE)
kullanım yüzeyleri: anma eylem yüzeyi; PR görsel dili.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 6.

### SEM-05: Kütük adı
adaylar: "Dijital Vefat Kütüğü"; "Yad Etme Kütüğü".
reddedilen: yok.
owner işareti: "her ikisi, uğur'la bakarız buna." (SOURCE)
kullanım yüzeyleri: marka kavramı; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 7.

### SEM-06: Pulse Board alanı
adaylar: "Hatırat Kürsüsü"; "Merhumun Huzuru" (huzuruna çıkmak, ziyaret etmek semantiği); "Anma Divanı" gibi; liste kapalı değil.
reddedilen: "Canlı Anma Meclisi" (gerekçe: meclis vurgusu garip); "dergâh" (owner reddi); "canlı" (owner reddi; teknolojik ses).
owner işareti: yukarıdaki aday listesi. (SOURCE)
kullanım yüzeyleri: ürün ekranı; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 7.
owner işareti: yukarıdaki aday listesi. (SOURCE)
karar (2026-09-08): "Merhumun Huzuru" seçildi (ziyaret semantiği: huzuruna çıkmak). "Hatırat Kürsüsü" ve "Anma Divanı" yedek aday. Uğur onayına gidecek (KARAR-KAPANDI-OWNER-ONAYINA-BAGLI).
### SEM-07: Kapsül ve sandık
adaylar: "Sandık".
reddedilen: "kapsül" (gerekçe: çok AI, çok dijital; naftalinli sandık imgesi istenir).
owner işareti: "kapsül değil sandık." (SOURCE) Mektup kartı "Mektup" olarak kalır.
kullanım yüzeyleri: ürün ekranı (zaman mektubu yüzeyi).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 7.

### SEM-08: Miras ve emanet
adaylar: alan adı "Miras"; "emanet" bağlam fiili (devir ve muhafaza cümlelerinde).
reddedilen: tek kelimeye sıkıştırma (gerekçe: alternate kullanım daha zengin semantik alana oturtur).
owner işareti: "işte bu alternate kullanım bizi daha zengin bir semantik alana oturtacak." (SOURCE)
kullanım yüzeyleri: profil alanları; otomasyon; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 7.

### SEM-09: EN açılış
adaylar: "Who are you remembering?"; "Whose memory do you carry?".
reddedilen: yok.
owner işareti: "her ikisi." (SOURCE)
kullanım yüzeyleri: EN Create Memorial; otomasyon.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 6.1.

### SEM-10: Ortak laht
adaylar: iki kişilik sayfa: "Bu sayfa iki kişiyi taşır."; iki ad ve iki tarih yan yana; katkılar kime ait olduğuyla işaretlenir.
reddedilen: yok.
owner işareti: "Ortak laht antropolojisi tam da Remembered'ın yaratacağı bir unsur." Ekran kurgusunun owner'a adım adım anlatılması beklenir. (SOURCE)
kullanım yüzeyleri: Create Memorial akışı; profil; PR anlatısı.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 5 ve 6.1.

### SEM-11: Yoldan geçene sesleniş
adaylar: ziyaretçiye tek cümlelik yetki verilmesi ("Bu sayfa bir hayatın başlangıcı. İlk cümleyi sen yaz." ailesi); "dur, oku, geç" küçük işi; yabancı ziyaretçinin saygılı tanık olması; "Bu sayfada onun hayatından bir iz var." + "Bir anı bırakmak ister misiniz?" soru biçimli davet (QR plaket dili).
reddedilen: emir yığını ve zorunlu katkı (gerekçe: sesleniş talep değil davettir; yabancıyla kurulan bağ küçük bir iş verir; ziyaretçiye suçluluk, ritüel borcu ve etkileşim baskısı yüklenmez; katkı zorunlu değildir).
owner işareti: "yedi yüzey için kesilmiş cümleler örnek kabul edilecek; ekran bazında derinleştirilecek" maddesi açık (filolog §8, 2026-09-04). (SOURCE)
kullanım yüzeyleri: ürün ekranı (anma sayfası ziyaret daveti); PR (QR plaket dili); otomasyon RAG.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 1; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 6 (yoldan geçene hitap satırı); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] bölüm 12 (güvenli örnek) ve 13.1; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 8.

### SEM-12: Boş sayfa dili
adaylar: "Bu sayfa bir hayatın başlangıcı. İlk cümleyi sen yaz." / "This page is where a life begins to be told. Write the first sentence."
reddedilen: "Henüz anı eklenmemiş. İlk anıyı ekleyerek bu değerli hayatı onurlandırın." (gerekçe: "değerli hayat" kimin adına söyleniyor belli değildir; "onurlandırın" emir kipi yaslı insana iş buyurur; cümle form doldurma daveti gibidir).
owner işareti: kesilmiş cümleler örnek kabul edilecek maddesi açık (filolog §8); kapanış ekranı cümlesi anma biçimleri denemesi 1. davranış REC'iyle aynıdır, çelişki yok (İŞ 8 çelişki denetimi). (SOURCE)
kullanım yüzeyleri: ürün ekranı (Create Memorial kapanışı, boş profil); otomasyon RAG.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 3, 4 (boş durum) ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 5 (kapanış ekranı).

### SEM-13: Anı daveti sahnesi
adaylar: "Onunla geçen bir akşamı anlat." / "En son ne zaman güldünüz birlikte?" / "Tell us one evening you spent with them." / "When did you last laugh together?"; owner sorusunun sade karşılıkları "Ondan sana ne kaldı?" / "What do you keep of them?"; "En çok ne yaparken hatırlıyorsun?" temel soru adayı (Luna).
reddedilen: "Bu değerli insanla ilgili bir anınızı paylaşın." (gerekçe: "anı paylaş" bürokratik bir fiildir; somut davet kapıyı tek sahneye açar; herkesin bir akşamı vardır, herkesin "anısı" yoktur); hayat özeti alanı isteme (gerekçe: üç fiillik anı, üç sıfatlı övgüden ağır basar; "o kimdi" sorusunun cevabı anılardan derlenir, platform yazmaz).
owner işareti: ekran 3'te owner sorusu aynen durur ("Nasıldı bir akşamı, hüznü, neşesi..?"); sade karşılıkların owner sorusunun yanına konması KARAR-BEKLIYOR (İŞ 8 karar yüzeyi 5). (SOURCE)
kullanım yüzeyleri: ürün ekranı (Create Memorial ekran 3, anı ekleme); otomasyon RAG.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 3 ve 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 2 (Adım 3) ve 5; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] 13.4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 4.
owner işareti: ekran 3'te owner sorusu aynen durur ("Nasıldı bir akşamı, hüznü, neşesi..?"); sade karşılıkların owner sorusunun yanına konması KARAR-BEKLIYOR (İ...
karar (2026-09-08): İkisi birden durur: owner sorusu ana, sade karşılık yardımcı ("Sizdeki hatıratı nasıldır?" + "Ondan sana ne kaldı?"). KARAR-KAPANDI.
### SEM-14: Kayıp ses ve ses daveti
adaylar: "Onun sesi burada yok. Belki bir kaset, bir telesekreter kaydı, bir video vardır. Bulursan ekle." / "Their voice is missing here. Maybe an old tape, an answering machine, a home video. If you find one, add it."; "O gün kim vardı, hangi şarkı çaldı" sorularının kayda girmesi; profil Voice bölümü.
reddedilen: kayıt eklenmeden önce boşluğu gizlemek veya doldurmak (gerekçe: eksiklik yapay kesinlikle doldurulmaz; "Burada bir ses vardı, henüz kaydedilmedi" demek boşluğu yok saymaktan bin kat iyidir; boşluk cümlesi, ses klonu kararını beklemeden doğru olanı yapar).
owner işareti: "Kayıp ses ve zaman kapsülü cümleleri ürün gereksinimine işlenecek" maddesi açık (filolog §8); ses klonu kararı owner'dadır (SEM-37). (SOURCE)
kullanım yüzeyleri: ürün ekranı (profil Voice, kayıt öncesi boşluk metni); otomasyon RAG.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 2, 4 (kayıp ses) ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 2 ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] Katman 3 (Voice sekmesi).

### SEM-15: Taziye ve dilek formül ailesi
adaylar: "Ruhu şad olsun" (eski İstanbul/Rum dili saygın dileği; Alevi-Bektaşi kullanımda belirgin; "Allah" adını anmadığı için "Allah rahmet eylesin"e göre dinî yükü hafiftir); "Allah rahmet eylesin", "toprağı bol olsun", "ruhuna fatiha" (Sünni gündelik sözvarlığı); Rum/Ortodoks'un ruha değil anıya yönelen formül ailesi (aynen durur, reddedilmez); EN "May they rest in peace" yalnız kullanıcı cümlesi olarak.
reddedilen: platform ağzından kurulan dilek (gerekçe: taş dilek kurmaz, dilek söyleyene aittir; platform dileği sevenler adına konuşmak olur; üç ses kuralına ve aile adına teselli yasağına takılır).
owner işareti: "Ruhu şad olsun" owner taslağı SEM-01'de dilek seçim listesine girdi; formül ailesi analizi (kim söylüyor, hangi gelenek, hangi grupta yabancı) İŞ 8 §3'te karar yüzeyindedir (KARAR-BEKLIYOR). (SOURCE)
kullanım yüzeyleri: ürün ekranı (dilek seçim listesi); otomasyon RAG (tarihi şahsiyet üretiminde taziye dili); PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 6. SEM-01 ile ilişki: dilek seçim listesi orada; bu kayıt formül ailesinin sözvarlığını ve sahiplik kuralını tutar.

### SEM-16: Mezar ziyareti ve bakım
adaylar: "Bugün onu ziyaret ettim" kaydı; ziyaretle gelen bakım davranışı (temizleme, su dökme); "Kabir ziyareti artık mesafeyle sınırlı değil." köprü cümlesi.
reddedilen: yok; kart adı formülü belirsiz ("Mezar Ziyareti Etti" ya da başka bir formül [?]), eşlik cümlesi owner'dadır (KARAR-BEKLIYOR).
owner işareti: alternatif, brief'in üç testini (gerçek ritüel, dil doğallığı, platform cümlesine dönüşüm) geçen ve din bağlamayan aday olarak önerildi. (SOURCE)
kullanım yüzeyleri: ürün ekranı (anma kartı); otomasyon RAG; diaspora PR anlatısı.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 2.4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] giriş (terra levis dileğinin davranış çevirisi).

### SEM-17: İcra ritüellerinin kayıt dili (mevlit, fatiha, lokma, helva)
adaylar: "Ailesi bugün onun için mevlit okuttu."; "Bugün onun için fatiha okundu."; "Ailesi bugün lokma döktü."; helva, lokma ile aynı sınır ve aynı dönüşümdedir.
reddedilen: platformun icranın yapımcısı olması ve dinî metnin platform ağzından sunulması (gerekçe: platform bu icranın yapımcısı olamaz, yalnız kaydını tutabilir; dinî yük kullanıcının geleneğine göre değişir; her alternatif tek seçenek değil eşlik eden seçenektir).
owner işareti: kart adları ve kayıt cümleleri owner'dadır (İŞ 7, her biri KARAR-BEKLIYOR); mevlit köprü cümlesi ("Mevlit okutmak gibi, dijitalde de bir hatıra bırakmak vefa işidir.") owner'da "rewrite - edgy" işaretlidir, yeniden kuruluş bekliyor. (SOURCE)
kullanım yüzeyleri: ürün ekranı (anma kartları); otomasyon RAG; TR pazarlama.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 2.1, 2.2, 2.5 ve 2.6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 3 (C1 işareti).

### SEM-18: Çiçek bırakma ve gönderim ayrımı
adaylar: "Çiçek bıraktı" kartı; çiçek bırakma dinî olmayan ve herkese açık eylemdir; bırakılan çiçek sözsüz bir cümledir, dil gerektirmez.
reddedilen: yok. Koşul (red değil): sembolik kayıt ile paketlerde fiziksel çiçek gönderiminin ayrımı çözülmeden kart kurulmaz (kavram karmaşası riski, owner işareti).
owner işareti: "çiçek bırak" kararı sembolik kayıt ve fiziksel gönderim ayrımının çözümüne bağlıdır (İŞ 7 §2.3, KARAR-BEKLIYOR). (SOURCE)
kullanım yüzeyleri: ürün ekranı (anma kartı); otomasyon RAG.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 2.3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 2 (A5 işareti).
owner işareti: "çiçek bırak" kararı sembolik kayıt ve fiziksel gönderim ayrımının çözümüne bağlıdır (İŞ 7 §2.3, KARAR-BEKLIYOR). (SOURCE)
karar (2026-09-08): İki katman ayrı. Sembolik kayıt şimdi kurulur ("Çiçek bıraktı"); fiziksel gönderim ileride ayrı paket, bugün kapsam dışı. KARAR-KAPANDI.
### SEM-19: Adlandırma davranışı
adaylar: isim + kimin söylediği + neyle anıldığı üçlüsü; ekran satırı "Adı, doğduğu yıl, öldüğü yıl. Bilmediğini boş bırak; soru işareti de bir cevaptır." / "Name, year of birth, year of death. Leave blank what you do not know; a question mark is an answer too."; "Bu anmayı kime adıyorsun?" eski plan adayı (KARAR-BEKLIYOR, owner üçlüsüne bağlı).
reddedilen: unvan ve biyografi listesi isteme (gerekçe: adlandırma davranışı üç parçadır; ad, onu anan ağzın seçimiyle sayfaya girer; övgüyü sıfat değil fiil taşır).
owner işareti: owner üç sorusunun ilk halkası ("Ruhu şad olsun, kimi anıyorsunuz?") aynen malzemedir; akışın ilk adımı adı sorar, unvan listesi istemez (İŞ 8 REC). (SOURCE)
kullanım yüzeyleri: ürün ekranı (Create Memorial ekran 1); otomasyon RAG (tarihi şahsiyet üretiminde adlandırma bloğu).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 2 (Adım 1) ve 5; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 4 (B5 işareti).

### SEM-20: Ses sahipliği ve üç ses
adaylar: üç ses ayrımı (merhumun doğrulanmış kendi sözü, yaşayanların tanıklığı, platformun cümlesi); "Bunu ailesi yazdı" ile "bunlar onun sözleri" etiket ayrımı (çocuk sayfası dahil); her katkının sahibiyle işaretlenmesi; etiketsiz cümlenin akışa girmemesi.
reddedilen: seslerin birbirine karışması (gerekçe: üç ses birbirine karıştığı anda metin yalan söyler; tek yüzey üç ses taşıyabilir ama her ses kendi satırında tanınır).
owner işareti: altı kuralın genel çerçevesi onaylandı (2026-09-04); emir bazında "2 (üç ses ayrımı) şimdilik ertelendi: teknolojik kararlar ötelenecek" kaydıyla teknoloji katmanı bekletildi; ürün dilindeki etiket uygulaması İŞ 8'de REC olarak durur. (SOURCE)
kullanım yüzeyleri: ürün ekranı (katkı etiketleri); otomasyon RAG (otomasyon çıktısında ses sahipliği etiketi).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] kural 3 ve bölüm 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 2 (62 numaralı taşın üç ses kanıtı).

### SEM-21: Övgüde fiil ve itiraf
adaylar: sıfat yerine tek sahne ve tek fiil ("güldürdü, yün eğirdi, hasadı öncü kesti"); itirafın anıların içinde serbest bırakılması; editoryal kural "övgüyü silme, çirkinliği düzeltme"; yayın öncesi rıza sorusu "Bu akşamı onun adına yayımlamama izin verir misin?"
reddedilen: hazır sıfatlar "değerli", "kıymetli", "saygıdeğer" (gerekçe: bir insanın değeri sıfatla değil anlatılan sahneyle kurulur); sayfanın "onur listesi" bölümünün yanına ayrı "itiraf" bölümü konması (gerekçe: hayatın pürüzsüz anlatısı, taşın gözünden düşük kalan anlatıdır; itiraf ayrı kutuya değil anıların içine bırakılır).
owner işareti: altı kuralın genel çerçevesi onaylandı (2026-09-04); itiraf REC'i SOURCE kanıtıyla durur (25 numaralı taş, "libertinus eram, fateor"). (SOURCE)
kullanım yüzeyleri: ürün ekranı (anı akışı, profil); otomasyon RAG (övgü üretiminde sıfat yasağı); PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] kural 1 ve 2, bölüm 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 4 ve 11; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] bölüm 12 (meslek ve emek övgüsü).

### SEM-22: Kalıcılık vaadi ve yasak süs kelimeleri
adaylar: kalıcılığın vaat değil yapılmış iş olarak gösterilmesi: dışa aktarma dosyası, haleflik planı, yıllık durum sayfası; "Verilerinizi yılda bir dışa aktarabilirsiniz." cümlesi; "Hafızayı, bakım ve ortak sorumlulukla koruruz." / "We preserve memory through care, stewardship and shared responsibility."
reddedilen: "unutulmaz", "ölümsüz", "ebedi", "sonsuza dek" kelimeleri (gerekçe: kalıcılık vaat değil teknik gerçektir; teknik gerçek kanıtlanmadan o kelimeler ağza alınmaz); alt başlıktaki "ebediyen" (gerekçe: platformun kalıcılık vaadi sunmama ilkesiyle ters düşer; owner "ilintili ilerlenebilir" notuyla rewrite istedi).
owner işareti: "Yasak kelime listesi (bölüm 6): editoryal geçide alınacak; ancak bölüm 6'nın tamamı owner onayından geçmedi" (filolog §8, açık madde, KARAR-BEKLIYOR). (SOURCE)
kullanım yüzeyleri: tüm ürün yüzeyleri; PR; basın kiti ve pitch deck (kalıcılık sorusunun cevabı).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] kural 6, bölüm 6 ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.5 (B2 işareti); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 10; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] ilke 5.

### SEM-23: Ölçme ve yarışma yasağı
adaylar: sayfa ziyaretinin ölçülmesi ama ölçünün ziyaretçinin yüzüne yığınmaması kuralı (iç metrik, yüzeyde yok).
reddedilen: beğeni, streak, skor, liderlik tablosu, "en çok anılanlar" sıralaması ve etkileşim baskısı (gerekçe: yası ölçmek; sayı sayma yarışı ortaklığı rekabete çevirir; 112 numaralı taşın yandaş sesi ortaklığa örnektir, rekabete değil).
owner işareti: bölüm 6'nın tamamı owner onayından geçmedi notuyla bağlıdır (filolog §8); güvensiz adaylar listesi epigrafik laboratuvar review yüzeyindedir. (SOURCE)
kullanım yüzeyleri: tüm ürün yüzeyleri (etkileşim tasarımı); PR (yas metrikleri sorularının cevabı).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 1 (REC) ve Taşınmayanlar; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 8 (güvensiz adaylar).

### SEM-24: Mahremiyet, vasiyet ve haleflik
adaylar: "Bu sayfa, hayattayken verdiğin kararlarla yönetilir. Hesabın kime devredileceğini sen seçersin; biz sormadan kimseye açmayız." / "This page follows the choices you made while alive. You choose who takes over your account; we show it to no one unasked."; hesap halefliyetinin sağkayken yazılan yüzeye bağlanması.
reddedilen: ailenin yasını kamusal varsaymak (gerekçe: güvensiz aday; kamusal görünürlük açık, isteğe bağlı ve geri alınabilir olmalıdır).
owner işareti: yüzey cümlesi filolog §4 setinden; §8'deki "kesilmiş cümleler örnek kabul edilecek" maddesine bağlıdır; yasal satır (KVKK/GDPR) uzmanla (tr-retorik §4). (SOURCE)
kullanım yüzeyleri: ürün ekranı (mahremiyet ve vasiyet yüzeyi); PR (gizlilik anlatısı); yasal metin.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 4 (mahremiyet ve vasiyet) ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 5.

### SEM-25: Silme, arşivleme ve gizleme fiilleri
adaylar: "Gizle / arşivle / kaldır"ın üç farklı eylem olarak ayrılması; katkıyı silebilme, bölümü gizleyebilme, sayfayı dondurabilme, kamusal profili özel yapabilme, yanlış veya incitici hatıraya itiraz edebilme.
reddedilen: yok (Luna katman 2 önerisi; owner işareti bekliyor).
owner işareti: yok (öneri statüsü; "silme de bir anma hakkıdır" ilkesi iki katmanlı arşiv modeliyle owner review'dadır, DIL-EP-004). (SOURCE)
kullanım yüzeyleri: ürün ekranı (katkı ve profil yönetimi); otomasyon RAG; yasal metin.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] Katman 2 tablosu ve ilke 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 7 ve DIL-EP-004.

### SEM-26: İki tarih satırı ve boşluk işareti
adaylar: "Bu iki tarih arasında bir hayat var. Aşağıda onu anlatanlar var." / "Between these two dates, a life. Below are the people who remember it."; bilinmeyen tarihte "1940-?" biçimi; "soru işareti bir kusur değil, dürüstlük işaretidir" ilkesi.
reddedilen: "Bir ömür, mezar taşındaki iki tarihten ibaret değildir." iddia cümlesinin tarih altına konması (gerekçe: iddia cümlesi yerine davet cümlesi; "ibaret değildir" öğretmen gibi konuşur; cümle manifesto ailesinde kalır, SEM-33).
owner işareti: iki tarih satırı filolog §3'ten aynen alındı (İŞ 8); anma biçimleri denemesi 9. davranış REC'iyle aynı cümledir, çelişki yok (İŞ 8 çelişki denetimi). (SOURCE)
kullanım yüzeyleri: ürün ekranı (iki tarih altı satır, ekran 1); otomasyon RAG (tarih doldurma yasağı).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 3 ve kural 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 4 ve 5; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 9.

### SEM-27: Kanıt ve kaynak dürüstlük dili
adaylar: "Bu bilgi aile arşivinden aktarılmıştır."; "Tarih doğrulanmayı bekliyor."; "Bu anlatının farklı bir versiyonu da bulunmaktadır."; "Kaynak belirtilmedi."; SOURCE/INT/REC etiket sistemi; kırık işareti, [?] ve ^[inferred] işaretlerinin otomasyona aynen taşınması.
reddedilen: "AI bunu doğruladı.", "Kesin olarak böyleydi.", "Herkes onu böyle hatırlıyordu." (gerekçe: otomasyon kesinlik süsü veremez; belirsizlik işaretleri örneklemden otomasyona taşınmak zorundadır; Sachphilologie'nin metin filolojisinden devraldığı şey yorum yetkisi değil dürüstlük rejimidir).
owner işareti: owner Sachphilologie dönüşü: yazıt, dillendirme ve ritüelleştirme davranışı taşıyan kültürel nesnedir; otomasyonun çıktıları da aynı dürüstlük rejimine tabidir. (SOURCE)
kullanım yüzeyleri: tüm ürün yüzeyleri (provenance etiketleri); otomasyon RAG (kanıt etiketi şartı); PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] ilke 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]] bölüm 3 ve 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 5.

### SEM-28: Göç, uzaklık ve çok dillilik
adaylar: "Uzaklardaki bir evlat, babasının sesini burada duyar."; sayfada aile dili, kişinin konuştuğu diller, farklı dillerde anılar ve her dil için ayrı çeviri notu; göç, savaş veya görev sırasında ölüm, fiziksel vedanın gerçekleşmemiş olması alanları; ritüel terimlerinin beş bağlamda (dinî, seküler, ailevi, kamusal, diasporik) değerlendirilmesi.
reddedilen: her katkıyı İngilizceye çevirip orijinal dili saklamak (gerekçe: güvensiz aktarım; özgün dil ve yazı sistemi çeviriyle birlikte korunur).
owner işareti: EN/diaspora tarafındaki beş bağlamlı değerlendirme kuyruktadır (envanter A12, DIL-001D protokolü); owner işareti bekliyor. (SOURCE)
kullanım yüzeyleri: ürün ekranı (dil katmanları, diaspora akışı); otomasyon RAG; diaspora PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] bölüm 12 (çok dilli aidiyet), 13.5 ve Katman 4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-arsivi-yazilmamis-isler-envanteri|Luna envanteri]] A12.

### SEM-29: Seçilmiş aile ve ilişki dili
adaylar: "Aile"nin yalnızca soy bağı olmaması; bakıcıların, öğretmenlerin, komşuların, evlatlık ilişkilerin, dostlukların ve seçilmiş ailelerin profilin asli unsuru olması; ilişkilerin etiket listesi değil açık cümleler ve katkı rolleri olarak modellenmesi; "Aileni davet et" satırı.
reddedilen: biyolojik ailenin, dinin, cinsiyetin veya statünün tek geçerli ilişki modeli yapılması (gerekçe: epigrafik matrisin aktarılmayacak tarafı; Melitta örneği statü sınırlarını aşan sevgiyi görünür kılar).
owner işareti: yok (ilişki ve katkıcı dili standardizasyonu DIL-EP-031'de owner onayına bağlı). (SOURCE)
kullanım yüzeyleri: ürün ekranı (profil ilişkileri); otomasyon RAG (akrabalık çıkarımı yerine rol etiketi); PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] 13.3 ve Katman 2; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 6 (adlandırma ve ilişki satırı) ve DIL-EP-031.

### SEM-30: Çocuk sesi ve erken ölüm
adaylar: çocuk sayfasında iki sesin ayrı durması ("Bunu ailesi yazdı" / "bunlar onun sözleri"); ailenin kendi cümlesine yer açılması; gül ve menekşe dileğinin anne-baba sesinden gelmesi.
reddedilen: erken ölümün otomatik olarak eksiklik, ders veya dönüşüm anlatısına çevrilmesi (gerekçe: aktarılmayacak taraf; yaş isteğe bağlı tutulur, yaşam uzunluğu ideal başarı ölçüsü yapılmaz); çocuk adına platform ağzından teselli cümlesi kurulması (gerekçe: ses sahipliği kuralı; ailenin kendi cümlesine yer açılır).
owner işareti: yok (davranış çevirisi; kanıt Courtney 70, 113, 178, 179). (SOURCE)
kullanım yüzeyleri: ürün ekranı (çocuk sayfası); otomasyon RAG; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 6 (yaşam, yaş ve kesilmiş biyografi satırı); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|ölüm cümlesi ve akış kurgusu]] bölüm 3.

### SEM-31: Evcil hayvan anma dili (REVİZE 2026-09-07)
adaylar: (geri alındı) ilk aday "hayvan sayfasında aynı kandil, aynı anı daveti, aynı fotoğraf alanı" idi.
REVİZE: Owner kararıyla Uğur evcil hayvanlar için ayrı bir alan açıyor; hayvan anması insan sayfası şablonunun çeşidi değil, kendi işleyişi olan ayrı bir yüzeydir. Antik taşların öğrettiği davranış (yabancılaşmadan yaslanma, sahneyi anlatma; kanıt Courtney 200, 203, 204) o alanın tasarımına girdi olarak işaretlidir. (SOURCE: owner kararı 2026-09-07)
kullanım yüzeyleri: ürün ekranı (ayrı hayvan alanı); otomasyon RAG (durur).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 7.

### SEM-32: Üçlü konumlandırma ve çekirdek kavram çevirisi
adaylar: üçlü yapı: anma sayfası (genel kullanıcı dili), hatıra kütüğü (markasal kavram), yaşayan hafıza arşivi (üst düzey konumlandırma); owner çeviri düzeltmesi "İnsan Belleğinin Yaşayan Arşivi" [?] / "İnsan Hafızasının Yaşayan Arşivi" [?]; CTA "İlk kütüğü aç" / "Bir anı bırak"; "Kütük aç" yalnızca belirli bağlamda.
reddedilen: bütün ürünün kütük üzerine kurulması (gerekçe: kütük bazı kullanıcılarda kaba, bazı bağlamlarda nüfus kaydı ya da ağaç gövdesi duygusu yaratabilir; üçlü yapı daha sağlamdır); "Yaşayan İnsan Hafızası Arşivi" birebir çevirisi (gerekçe: owner çeviri yanlışlığı işareti; "İnsan Hafızasının/Belleğinin(?) Yaşayan Arşivi" olmalıdır).
owner işareti: K3 ^[ambiguous]: Luna üçlüsü ile "Dijital Vefat Kütüğü" owner kararı (SEM-05) aynı alanda ve tam örtüşmüyor; karar owner yüzeyindedir; çekirdek kavram çevirisi KARAR-BEKLIYOR. (SOURCE)
kullanım yüzeyleri: marka konumlandırma; PR; pitch deck; site üst konumu.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] Katman 2 ("Kütük" kararı); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 2 (A1 işareti) ve 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-arsivi-yazilmamis-isler-envanteri|Luna envanteri]] A5 ve K3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.4. SEM-05 ile ilişki: kütük ad adayları orada; bu kayıt konumlandırma katmanını tutar.

### SEM-33: Manifesto ve hero dili
adaylar: "İnsan iki kez ölür: Biri kalbinin durduğu gün, biri adının son kez anıldığı gün."; "Unutulmak, ikinci ölümdür."; "Bir hayat sonludur. Bıraktığı iz değil."; hero çifti: TR "Bir insan iki kez ölür. İkincisi, adının son kez anıldığı gündür. Biz birinciyi yas tutar, ikinciyi geciktiririz." ve EN eşlik; "Her hayat hatırlanmayı hak eder." (sitenin EN başlığının birebir TR karşılığı).
reddedilen: alt başlığın mevcut hali ("...tek bir yerde, ebediyen.") (gerekçe: platformun kalıcılık vaadi sunmama ilkesiyle ters düşer; SEM-22 ile aynı gerekçe; owner "ilintili ilerlenebilir" notuyla rewrite istedi).
owner işareti: hero başlık "rewrite" (B1); manifesto "revize halleriyle" (B7); ikisi de KARAR-BEKLIYOR; hero malzemesi filolog §4 kesilmiş cümlelerinde hazır durur. (SOURCE)
kullanım yüzeyleri: PR; basın kiti; pitch deck; site hero ve manifesto.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 3 ve 4 (B1, B2, B7 işaretleri); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 4 (hero); [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.5.
owner işareti: hero başlık "rewrite" (B1); manifesto "revize halleriyle" (B7); ikisi de KARAR-BEKLIYOR; hero malzemesi filolog §4 kesilmiş cümlelerinde hazır durur. (SOURCE)
karar (2026-09-08): Manifesto revize hali Uğur'un bulk'undan yazılır (ana mesaj + "Every life deserves" çerçevesi); "İnsan iki kez ölür" hikâyesi korunur. Hero alt başlığı Uğur onayına gidecek. KARAR-KAPANDI (hero tek cümle "Her hayat hatırlanmayı hak eder" kesin).
### SEM-34: Fidan ve hatıra ormanı
adaylar: "Fidan Dikti" / "Plant a tree"; "Adına bir fidan dikilsin." / "Plant a tree in their name."; "Hatıra Ormanı"; TEMA ve vefa ormanı bağlantısı.
reddedilen: gerçek bağış veya eylem olmadan fidan dilinin kullanılması (gerekçe: owner işareti "olumlu, gerçekten ifa edilecek" yönündedir; Luna satırı "gerçek bağış/eylem varsa kullanılmalı" der).
owner işareti: olumlu; kartların siteye yazılma onayı bekliyor (İŞ 7 §3.4, KARAR-BEKLIYOR). (SOURCE)
kullanım yüzeyleri: ürün ekranı (anma kartı); PR; kurumsal sponsorluk anlatısı.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 1, 2 (A6 ve A9 işaretleri) ve 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.4; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] Katman 2 tablosu.
owner işareti: olumlu; kartların siteye yazılma onayı bekliyor (İŞ 7 §3.4, KARAR-BEKLIYOR). (SOURCE)
karar (2026-09-08): ERTELENDİ. TEMA anlaşması netleşmeden fidan/orman kartları kurulmaz. Beklemede.
### SEM-35: Bırakılan söz ve itiraf alanı
adaylar: "Söyleyeceklerin varsa, bırak." / "Söylemediklerin mi var? Buraya bırak." / "Is there something you never said? Leave it here."; isimsiz itiraf için açık alan; eşlik cümlesinin kart adından bağımsız durabilmesi.
reddedilen: "ödenmemiş borç" metaforunun ekrana yazılması (gerekçe: davet yazılır, metafor yazılmaz; adak kelimesi ekranda kullanılmaz); moderasyonun itirafın içeriğine dokunması (gerekçe: metin moderasyonu gündelik kaba dili süzer, itirafın içeriğine dokunmaz).
owner işareti: kart adı owner'dadır: "Mektup bıraktı" / "anıt" [?] / "lahit" [?] (İŞ 7 §3.2, KARAR-BEKLIYOR); eşlik cümlesi adı beklemeden durabilir. (SOURCE)
kullanım yüzeyleri: ürün ekranı (bırakma yüzeyi); otomasyon RAG; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]] bölüm 2 (A5 işareti) ve 3; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 3 ve 11; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.2.
owner işareti: kart adı owner'dadır: "Mektup bıraktı" / "anıt" [?] / "lahit" [?] (İŞ 7 §3.2, KARAR-BEKLIYOR); eşlik cümlesi adı beklemeden durabilir. (SOURCE)
karar (2026-09-08): "Mektup Bıraktı" EN "Left a letter" ile eşleşir; TR kart davet cümlesiyle kurulur: "Söylemediklerin mi var? Buraya bırak." KARAR-KAPANDI.
### SEM-36: Mühürlü mektup ve sağkayken yazma
adaylar: "Bu mektup, seçtiğin güne kadar mühürlü kalır. Biz açarız; sen yazarsın." / "This letter stays sealed until the day you choose. You write it. We open it."; zaman kapsülü ve son irade bölümünün "sağkayken yazılır" konumlanışı; "O gün kim vardı, hangi şarkı çaldı" sorularının kayda girmesi.
reddedilen: yok (davranış katmanı; nesne adı kararı SEM-07'de sandık olarak kapandı).
owner işareti: "Kayıp ses ve zaman kapsülü cümleleri ürün gereksinimine işlenecek" maddesi açık (filolog §8); davranış kaynağı 5. davranıştır ("kendi taşını sağkayken döşemek", Vitalis 130); hesap halefliyeti bu yüzeye bağlanır (SEM-24). (SOURCE)
kullanım yüzeyleri: ürün ekranı (zaman mektubu yüzeyi); otomasyon RAG; PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 4 (zaman kapsülü) ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 2 ve 5; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 3.1. SEM-07 ile ilişki: ad kararı orada; bu kayıt davranış katmanını tutar.

### SEM-37: Merhum adına konuşma sınırı ve ses klonu
adaylar: merhumun doğrulanmış kendi sözünün üç sesten biri olarak durması (SEM-20); ses klonu owner yönü: "anısını yaşatmak" adına kullanılacak; çerçevesinin (kim rızasıyla, hangi sınırla, hangi dille) kurgulanacak olması.
reddedilen: "Bu kişi sizinle konuşuyor" iddiası, merhum adına yeni cümle, tahminî kişilik, otomatik yas mesajı ve "onun söyleyeceği" varsayılan cevaplar (gerekçe: antik yazıtı analiz etmek başka, ölmüş bir kişiyi simüle etmek başkadır; merhumun ağzından cümle uydurmak, sesini taklit etmek filolojik cinayettir).
owner işareti: "Ses klonu kararı owner'da. Owner yönü: ses klonu KULLANILACAK, 'anısını yaşatmak' adına. Notun ilk taslağındaki 'kapı dışarı' hükmü geçerli değil." (filolog §8, açık madde, KARAR-BEKLIYOR); ürün içi AI görevleri (düzenleme, gruplama, tarih çıkarma, çeviri taslağı) simülasyondan ayrıdır. (SOURCE)
kullanım yüzeyleri: ürün ekranı (Voice); otomasyon RAG (üretim sınırı); PR (soru-cevap hazırlığı).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]] bölüm 6 ve 8; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] bölüm 17; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] bölüm 8 ve DIL-EP-044.

### SEM-38: Yas görev değil davet
adaylar: her eylemin davet olması; "kalbinde yaşat"ın hiçbir ritüel yapmayan kullanıcıya görev yüklemediği; "Bir anı bırakmak ister misiniz?" soru biçimli davet; ritüelin şablonlaştırılmaması, kaydın bırakılıp biçimi ailenin seçmesi.
reddedilen: "Onu unutma. Şimdi bir mum yak. Ailenin görevini tamamla." tipi dil (gerekçe: suçluluk üretir, yas sürecini ölçer, platformu ritüel otoriteye dönüştürür); "Her merhumun bir miras bırakması gerekir." (gerekçe: hayatı başarı ve etki zorunluluğuna indirger; miras alanı SEM-08'dedir, zorunluluk yoktur).
owner işareti: şerit fiilleri owner'ın kendi listesidir (SEM-04); davet kuralı filolog kalemi ses disiplininin ürün yüzeyidir. (SOURCE)
kullanım yüzeyleri: tüm ürün yüzeyleri; otomasyon RAG (çağrı cümlesi üretimi); PR.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] ilke 7 ve bölüm 12; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|ritüel mozaik]] bölüm 6; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi|anma biçimleri denemesi]] davranış 2.

### SEM-39: Hürmet ve ücret duvarı
adaylar: temel anma eylemleri (anma sayfası açma, temel metin ekleme, anı bırakma, aile katkısı, erişim ve silme kontrolü) ücret duvarı arkasına konmaz; premium olabilecekler: profesyonel tasarım, baskı, fiziksel plaket, arşiv danışmanlığı, ek depolama, kurumsal hizmetler.
reddedilen: hürmetin kendisinin ürün özelliği olarak satılması (gerekçe: antik yazıtların sosyal eşitsizlikleri tasarıma aktarılmaz).
owner işareti: yok (Luna ilkesi; fiyatlandırma ve paket kararı owner'dadır). (SOURCE)
kullanım yüzeyleri: fiyatlandırma sayfası dili; PR; pitch deck.
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] ilke 8.

### SEM-40: Arşiv adaleti ve belgelenmemiş hayat
adaylar: "Bir insanın yazıt bırakmamış olması, hatırlanmaya değmediği anlamına gelmez." (ahlaki merkez adayı); belgelenmiş ve belgelenmemiş hayatın eşit saygınlığı; fotoğrafı olmayan profilin eksik değerli sayılmaması; aile içi görünmeyen emeğin ayrı kategori olması; göçmen, azınlık, kölelik, yoksulluk, hastalık ve intihar deneyimlerinin otomatik sansürlenmemesi, ama aile yetkisi ve mahremiyetle korunması.
reddedilen: yok.
owner işareti: yok (Luna ilkesi; on iki ilkenin tek liste hâli ve arşiv adaleti bölümünün etik karar bloğuna eklenmesi kuyruktadır, envanter A14). (SOURCE)
kullanım yüzeyleri: ürün ekranı (boş profil, görünmeyen emek kategorisi); PR; pitch deck (etik anlatı).
kaynak: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904|Luna arşivi]] bölüm 18; [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-arsivi-yazilmamis-isler-envanteri|Luna envanteri]] A14.

## Durum

İlk tur 10 kayıt: 2026-09-06 sabahı owner kararlarından derlendi. İkinci tur (İŞ 10, 2026-09-06): [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/is-10-semantik-veritabani-briefi|İŞ 10 briefi]] yürütüldü; SEM-11'den SEM-40'a 30 kayıt eklendi, toplam 40. Kaynak seti: tr-retorik allek işaretleri (17 madde), filolog-kalemi karar yüzeyi, İŞ 6-9 çıktı ve raporları, Courtney anma biçimleri denemesi, Luna arşivi ve Sachphilologie dönüşü. Owner'ın deneme değerlendirmesi ("bu başlangıç fena değil, ancak yeterli de değil; daha tumturaklı, metodik bir yaklaşım gerekiyor") ikinci turun derinlik ölçütü olarak alındı. ^[inferred] Luna kaynaklı kayıtlarda (SEM-25, SEM-39, SEM-40) owner işareti yoktur; öneri statüsündedir. Çift sayım noktaları kayıt içine not edildi (SEM-15 ile SEM-01; SEM-32 ile SEM-05; SEM-36 ile SEM-07).

## KARAR-BEKLIYOR (owner taraması)

1. Açılış ve dilek: A/B/C seçimi ve dilek formül ailesinin yüzeyleri (SEM-01, SEM-15).
2. Sandığın tam adı ve mektup kartının adı: "Mektup bıraktı" / "anıt" [?] / "lahit" [?] (SEM-07, SEM-35, SEM-36).
3. Mezar ziyareti, mevlit, fatiha, lokma, helva kart adları ve kayıt cümleleri; mevlit köprü cümlesinin rewrite'ı (SEM-16, SEM-17).
4. Çiçeğin sembolik kayıt ile fiziksel gönderim ayrımı (SEM-18).
5. Çekirdek kavram çevirisi ("Belleğin" / "Hafızasının" [?]) ve üçlü konumlandırmanın onayı (SEM-32; K3 ^[ambiguous]).
6. Kütük adı seçimi: "Dijital Vefat Kütüğü" / "Yad Etme Kütüğü" (SEM-05).
7. Yasak kelime listesinin editoryal geçide alınması; bölüm 6'nın tamamı owner onayından geçmedi (SEM-22, SEM-23).
8. Hero, alt başlık ve manifesto rewrite halleri (SEM-33).
9. Fidan ve orman kartlarının siteye yazılma onayı (SEM-34).
10. Sade karşılıkların owner sorularının yanına konması (SEM-13).
11. Ses klonu çerçevesi: kim rızasıyla, hangi sınırla, hangi dille (SEM-37).
12. Üç ses ayrımının teknoloji katmanı (SEM-20).
13. Kayıp ses ve zaman kapsülü cümlelerinin ürün gereksinimine işlenmesi (SEM-14, SEM-36).
14. On iki ilkenin tek liste hâli ve arşiv adaleti bölümü (SEM-40).

## İlgili

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri|Ritüel Mozaik ve Kavram Revizeleri]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu|Ölüm Cümlesi ve Akış Kurgusu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu|Sachphilologie Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/palinodie-yontem-notu|Palinode Yöntem Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/is-10-semantik-veritabani-briefi|İŞ 10 Semantik Veritabanı Briefi]]
- [[is-10-raporu|İŞ 10 Raporu]]

