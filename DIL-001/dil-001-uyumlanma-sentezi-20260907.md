# DIL-001 Uyumlanma Sentezi ve Revizyon (2026-09-07)

> Bu not iki işi tek yerde yapar: DIL-001'in üç gecelik çıktısını Uğur'un ilk planıyla (F8 Dil stratejisi + PR-001 Global PR) kıyaslar, uyumlanan katmanı DIL-001'in gövdesi yapar, uyumlanmayan fazlalığı deprecated olarak kenara alır. Karar kaynağı: Alleksenes direktifi 2026-09-07, "kendimizden kattığımız şeyleri mevcut şema, akış ve içerikle uyumlandığı ölçüde kabul edip artakalan çalışmamızı deprecated şeklinde kenara alalım".

## 1. Uğur'un ilk planı: DIL-001'in tanım kümesi

Uğur'un plan katmanı üç kaynakta durur: [[projects/remembered/02-ekip-gorev/gorev-dagilimi-v3-ugur-revizyonu|gorev-dagilimi-v3-ugur-revizyonu]] F8 satırı, [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi|DIL-001 görev notu]] ve [[projects/remembered/02-ekip-gorev/gorevler/global-pr-basin|PR-001 görev notu]]. Bu üç kaynağın dil işi için istediği şey kapalı bir liste:

1. EN+TR mimari: /en/ + /tr/ subdirectory, hreflang, x-default, sitemap, canonical. (Ozan'a teknik brief.)
2. Global hesap İngilizce; TR tek uzantı sayfa; ülke hesapları traction sonucu açılır.
3. Genişleme sırası DE→ES→FR, kriterler veriye bağlı.
4. Kullanıcı kontrollü dil değiştirici; IP zorlaması yok.
5. Makine çevirisi yasak; içerik editör onaylı akar.
6. PR-001 yüzeyi: basın kiti, tanıtım yazıları, medya listesi, TR/EN dil bütünlüğü.

Bu liste, F8'in tek satırına ("EN+TR; global hesap İngilizce; TR tek uzantı; DE→ES→FR; Architecture multilingual from day one; content does not have to be") indirgenebilir. DIL-001'in uyumlanması bu satıra göre ölçülür.

## 2. Kıyaslama: uyumlanan mı, fazlalık mı

| DIL-001 çıktısı | Uğur'un planındaki karşılığı | Hüküm |
|---|---|---|
| Dil stratejisi omurgası ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-notu\|dil-stratejisi-notu]]): EN default, TR lokalizasyon, DE→ES→FR eşikleri, dil değiştirici, makine çevirisi yasağı | F8'in birebir açılımı; görev notunun 4 alt adımının tamamlanmış hali | UYUMLANDI. DIL-001'in gövdesi bu. |
| hreflang/subdirectory teknik briefi (strateji notu bölüm 2) | F8 alt adımı 1, Ozan'a brief | UYUMLANDI. Teslim edilecek tek teknik madde. |
| TR Retorik ve Kavram Notu ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu\|tr-retorik-kavram-notu]]): TR kavram seti, site yazı planı | F8'in "TR tek uzantı" içeriği; remembered8.com /tr boşluğunun doldurulması | UYUMLANDI. TR içeriğin çekirdeği. |
| Filologun Kalemi ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi\|dil-stratejisi-filolog-kalemi]]): ses disiplini, altı kural, kesilmiş TR/EN cümleler | Uğur'un direktifiyle uyumlu: "Metinler kısa ve anlaşılır olacak... Birebir çeviri yerine doğal anlatıma bakacağız" | UYUMLANDI. PR-001'in bütün metinlerinin ses kaynağı. |
| Epigrafik anma laboratuvarı, Courtney 206 şiir, Sachphilologie, Palinode, Ritüel mozaik, Ölüm cümlesi akışı, Anma biçimleri denemesi | Uğur'un planında hiçbir karşılığı yok; plan hiçbir yerde yazıt korpusu, RAG örneklemi veya otomasyon eğitimi istemiyor | FAZLALIK. Deprecated kenara. (2026-09-08 istisnası: semantik alan veritabanı GÖVDEYE GERİ ALINDI; karar deposudur, deprecated değil.) |
| Session briefleri (İŞ 1-10) ve Homonoia briefi | Uğur'un planındaki iş akışına eşleşmiyor; briefler fazlalık katmanının üretim hattı | FAZLALIK. Deprecated kenara. |

Oran net: DIL-001'in dokuz iş paketinin dördü (strateji omurgası, teknik brief, TR kavram çekirdeği, ses disiplini) Uğur'un planının içindedir; beşi (korpus, yöntem ve otomasyon katmanı) dışındadır. Aşağıdaki kesit bunu uygulamaya koyar.

## 3. DIL-001'in yeni gövdesi (uyumlanan katman)

DIL-001 bundan sonra dört teslimattan ibarettir:

1. **Dil stratejisi omurgası:** [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-notu|DIL-001 Dil Stratejisi]]. Açık maddeler: Ozan'a hreflang briefi, dil değiştirici UX kararı, DE→ES/FR eşik kararları (traction verisi gelince).
2. **TR içerik çekirdeği:** [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]. /tr sayfalarının kavram seti ve yazı planı.
3. **Ses disiplini:** [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]]. Hem /tr hem /en hem basın metinlerinin ses kaynağı. Filologun Kalemi'nin bölüm 8'deki açık kararları (yasak kelime listesi, ses klonu çerçevesi) owner'da beklemeye devam eder.
4. **PR-001 yüzeyi:** basın kiti ve tanıtım metinleri; iş planı [[projects/remembered/02-ekip-gorev/gorevler/global-pr-basin|global-pr-basin]] notunda ve [[projects/remembered/02-ekip-gorev/pr-001-basin-kiti-is-plani|PR-001 basın kiti iş planı]]nda.

Ses klonu çerçevesi (rıza, sınırlar, dil katmanı) açık madde olarak DIL-001'de kalır; Uğur'un yönü kullanılacak tarafında, kurgu henüz yok.

## 4. Deprecated: kenara alınan katman

Kural: içerik silinmez, dosyalar yerinde durur; lifecycle `archived` olur, başına durum satırı eklenir. Bağlantılar bozulmaz; başka işe dönerse lifeline geri açılır. 2026-09-07 eki: archived üç not (ölüm cümlesi akışı, anma biçimleri denemesi, HOMONOIA briefi) içindeki owner onaylı dil kararları gövdeye taşınmak üzere; 2026-09-08 owner kararıyla semantik alan veritabanı deprecated'tan ÇIKARILDI ve gövde karar deposu olarak geri alındı (SEM kayıtları doğrudan gövdeye bağlanır) [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/gorev-briefi-dil001-govde-sentezi|gorev-briefi-dil001-govde-sentezi]] paketine bağlandı; ölçüt "owner cümlesi mi, yalnız RAG/otomasyon alıcısı mı" ayrımıdır.

| Not | İçindeki değer | Kenara alınma gerekçesi | İlerde kullanım yeri |
|---|---|---|---|
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari\|Epigrafik Anma Laboratuvarı]] | Kaynak hak mimarisi, söz-edimi matrisi, 72 kayıtlık pilot tasarımı | Ürün planı yazıt verisi istemiyor; hak geçidi işi olmadan çalıştırılamaz | Bir anma arşivi/sergi ya da akademik hat açılırsa hazır omurga |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/courtney-musa-lapidaria-tasnif-20260905\|Courtney tasnif]] + OCR çekim (json) | 206 şiir, üçlü tasnif, 22 çekirdek | Örneklemin alıcısı (otomasyon eğitimi) DIL-001 kapsamından çıktı | Şiir/filoloji çalışması; hyphantai hattı |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/gorev-briefi-courtney-metinleri-obsidiana\|Courtney görev briefi]] | Başka agent'a verilebilir kapalı görev paketi | Sıradaki işi (metin notları)Deprecated katman üretiyor | v2 briefi kendi içinde durur; istenirse koşturulur |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/sachphilologie-notu\|Sachphilologie Notu]] | Wortphilologie→Sachphilologie dönüşünün kurumsallaştırması | Yöntem katmanı, ürün planına hizmet etmiyor | Metodoloji yazısı; kişisel filoloji hattı |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/palinodie-yontem-notu\|Palinode Yöntem Notu]] | Yaz/kör ol/yad et/yeni şarkı döngüsü | Üretim hattı deprecate olan hatta bağlı | Genel editoryal kalite döngüsü olarak yeniden doğabilir |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/rituel-mozaik-ve-kavram-revizeleri\|Ritüel Mozaik ve Kavram Revizeleri]] | 22 ritüel alternatifi, kavram revizeleri (Sandık, kürsü, dergâh) | Owner kararı bekleyen kavram seti; Uğur'un planında yok | TR kavram notu revize edilirken tek tek alınabilir |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/olum-cumlesi-ve-akis-kurgusu\|Ölüm Cümlesi ve Akış Kurgusu]] | Create Memorial üç sorusu ve şiir kanıtları | Ürün akışı Ozan'ın sahası; DIL-001 kapsamı dışı | Ürün ekip redesign'a girdiğinde girdi dosyası |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/anma-bicimleri-denemesi\|Anma Biçimleri Denemesi]] | 22 şiirden davranış çıkarımı, SOURCE/INT/REC | Kanıt havuzu deprecate hatta bağlı | Deprecate Courtney setiyle birlikte döner |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-001-session-briefleri-20260905\|DIL-001 Session Briefleri]] | 9 işlik kapalı brief sistemi | Koştuğu hattın tamamı deprecate | Brief şablonu başka projeye kopyalanabilir |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/homonoia-brief-dil001-20260906\|HOMONOIA Brief]] | Üç gecenin dış yüzeyi özeti | İçerik deprecated katmanı anlatıyor | Arşiv değeri |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/luna-session-zinciri-arsivi-20260904\|Luna Arşivi]] + yazılmamış işler envanteri | 6 benzersiz Luna çıktısı, 14 işlik kuyruk | Luna hattı zaten kapalıydı; kuyruğun alıcısı DIL-001'in eski kapsamıydı | İleride iş açılırsa envantere dönülür |
| [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi\|DIL-001 görev notu]] | Alt görev tanımı (hreflang briefi, dil değiştirici, lokalizasyon kuralı, DE/ES/FR) | Bu alt görev Uğur'un planıyla DIL-001'in asıl karşılığıydı; artık sentez notası DIL-001'in yüzeyi | Ana görev notuna dönüştürüldü (aşağıda) |

Koruma notu: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-deprecated/dil-stratejisi-epigrafik-anma-laboratuvari|Epigrafik Anma Laboratuvarı]] ve [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik Kavram Notu]] arasındaki editoryal kural köprüsü (kaynak gösterimi, çeviri dürüstlüğü) deprecated olsa da ses disiplinine yararlı kalan tek parçadır; Filologun Kalemi'nin altı kuralı bunu zaten taşır.

## 4.1 Luna kararı (2026-09-08)

Luna arşivindeki notların çoğu antik epigrafinin mirasını almayı hedeflediğinden Luna hattı mecburen deprecated kalır; bu, sadece envanterin değil Luna'nın üretim yöneliminin de archived sayılması demektir. İleride bir anma arşivi/akademik hat açılırsa epigrafik laboratuvar paketiyle birlikte yeniden değerlendirilir.

## 5. Uygulanan deprecation (2026-09-07)

Yukarıdaki tablodaki 12 nota (2026-09-08 itibarıyla SEM çıkarıldı) lifecycle: `archived` işlendi; her birinin frontmatter'ına `deprecated: "2026-09-07 uyumlanma kararı; detay: dil-001-uyumlanma-sentezi-20260907"` satırı ve summary sonuna tek satır durum eklendi. İçerikte hiçbir silme yapılmadı. DIL-001 görev notu ([[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi|dil-stratejisi]]) artık DIL-001'in Obsidian yüzeyidir: alt adımları Uğur'un orijinal dörtlüsü + sentez ve revizyon referanslarıyla güncellendi.

## 6. Notion revizesi (DIL-001)

Notion DIL-001 sayfasına eklenen revize bloğu şunu söyler: uyumlanan dört katman (strateji omurgası, teknik brief maddeleri, TR kavram çekirdeği, ses disiplini) DIL-001'in gövdesi; korpus, yöntem ve otomasyon katmanı uyumlanmadığı için deprecated kenara alındı; açık işler uyumlanan katmanın açık maddelerine indirgendi (hreflang briefi, dil değiştirici UX, DE/ES/FR eşikleri, ses klonu çerçevesi). Private vault detayına yine girmiyor; karar yüzeyi konuşuyor.

## 7. PR-001'e aktarılan pay

DIL-001'in PR-001'e doğrudan giren varlıkları: Filologun Kalemi (basın metinlerinin ses kaynağı), strateji notunun dil bütünlüğü kuralları (TR/EN eşleşme, makine çevirisi yasağı; Uğur'un "birebir çeviri yerine doğal anlatım" şartıyla aynı), TR Retorik Kavram Notu'nun marka kavram seti. Uğur'un 8 bölümlük basın kiti notu, sosyal medya paketi (01-09 gönderiler, 3 video, story seti, 14 günlük yayın sırası) ve Buffer/Metricool akış sorusu PR-001 iş planına taşındı; oradaki plan bu kaynaklarla çalışır. Sentezin PR-001'e dökülen kısmı: [[projects/remembered/02-ekip-gorev/pr-001-basin-kiti-is-plani|PR-001 Basın Kiti İş Planı]].

## İlgili

- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-notu|DIL-001 Dil Stratejisi]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/tr-retorik-kavram-notu|TR Retorik ve Kavram Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]]
- [[projects/remembered/02-ekip-gorev/pr-001-basin-kiti-is-plani|PR-001 Basın Kiti İş Planı]]
- [[projects/remembered/02-ekip-gorev/gorevler/global-pr-basin|PR-001 Görev Notu]]
- [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi|DIL-001 Görev Notu]]
- [[projects/remembered/remembered|Remembered Proje Notu]]
