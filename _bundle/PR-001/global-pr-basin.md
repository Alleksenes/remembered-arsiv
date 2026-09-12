---
title: "PR-001: Global PR & basın rezervasyonu"
created: "2026-08-28"
updated: "2026-08-28"
type: project
tags: [remembered, task, pr]
sources: []
base_confidence: medium
lifecycle: draft
lifecycle_changed: "2026-08-28"
provenance: "synthesized"
summary: "PR-001 görev tanımı: sorumlu, destek, öncül/ardıl, alt adımlar, kaynaklar."
---
# Global PR & basın rezervasyonu

## Nitelikler

| Alan | Değer |
|---|---|
| Task ID (primary key) | `PR-001` |
| Owner (asli sorumlu) | alleksenes |
| Supporters (destek/denetmen) | doga |
| Preceding (öncül) | crm-kurulumu, editoryal-ilk-30-profil |
| Next (ardıl) | intikal-listing, marketing-growth |
| Work area | pr |
| Priority | high |
| Due date | 2026-09-04 |

> Görev notu adı, ID değil görevin kendi adıdır. ID (`PR-001`) yalnızca database mantığında birincil anahtardır; Notion'da relation'larla diğer DB'lere foreign key olarak bağlanır.

## Açıklama

Yurt dışı tanıtımı AI ile: İngilizce basın/STK tanıtım yazıları, DeathTech medyası + AI sorgu görünürlüğü hedefli.

## Alt Adımlar / Aşamalar (derinleştirilmiş know-how)

### 1. İngilizce tanıtım yazısı taslağı (Manifesto sesiyle)
**Nasıl:** Kurumsal kimlik briefindeki ses/ton kuralları: saygılı, editoryal, 'living archive of human memory'. 400-600 kelime, CTA www.remembered8.com. ✅ TAMAMLANDI → [[ingilizce-tanitim-yazisi]]
**Araç:** write_file → taslak
**Kaynak:** [[kurumsal-kimlik-briefi|Remembered Manifesto]] (ses/ton §3), [[marka-manifestosu|Marka Manifestosu]]

### 2. DeathTech medyası + kültür mirası hedef listesi
**Nasıl:** ✅ TAMAMLANDI → [[pr-medya-listesi]] (18 genel + 7 DeathTech + 8 trend, iletişim formatlarıyla). Her medya CRM'e işlenecek: organizations satırı (org-type: media, pipeline-stage: lead, expectation: pitch).
**Araç:** web araştırması → CRM
**Kaynak:** [[pr-medya-listesi|Global PR Medya Listesi]]

### 3. Basın kiti üretimi (2026-09-07 güncel odak)
**Nasıl:** Uğur'un 8 bölümlük basın kiti notu ve sosyal medya paketi iş planına çevrildi: bölüm planı, sorumlular, cuma (11 Eylül) teslim sırası ve kapanış kontrol listesi: [[projects/remembered/02-ekip-gorev/pr-001-basin-kiti-is-plani|PR-001 Basın Kiti İş Planı]]. DIL-001 uyumlanma sentezinden gelen ses kaynağı: [[projects/remembered/02-ekip-gorev/gorevler/DIL-001/dil001-docs/dil-stratejisi-filolog-kalemi|Filologun Kalemi]].
**Araç:** iş planı → ekip dağıtımı

### 4. Structured data + otoriter kaynaklarla AI alıntı yüzeyi
**Nasıl:** Schema.org Person/DeathPlace; güvenilir kaynaklardan alıntı yapılabilir olmak (AI sorgu görünürlüğü).
**Araç:** Ozan'a schema brief
**Kaynak:** [https://schema.org/Person](https://schema.org/Person)

### 4. Basın/STK temaslarını CRM'e işle
**Nasıl:** Her temas: people/orgs satırı + pipeline-stage + beklenti + meetings kaydı.
**Araç:** Notion CRM

### 5. Nezaketli 'bizi haber yapabilir misiniz' çerçevesi
**Nasıl:** Alçakgönüllü, bilgi veren, bağ kurma amaçlı ilk temas; satış dili yok.
**Araç:** e-posta şablonu

### 6. Gönderim + takip
**Nasıl:** Gönderilen her e-posta için meetings satırı + next-step; takip 5-7 gün.
**Araç:** Notion CRM

## Bağlı Kuram (Obsidian)

- [[kurumsal-kimlik-briefi]]
- [[marka-manifestosu]]
- [[pazar-arastirmasi-ve-intikal]]

## Dış Kaynaklar

- [5WPR AI Visibility Index 2026](https://www.5wpr.com/research/funeral-services-ai-visibility-index-2026/)
- [North America Outlook, DeathTech](https://www.northamericaoutlookmag.com/industry-insights/trend-report-the-rise-of-deathtech)

## Not

Bu görev notu, CRM database şemasındaki tasks satırının Obsidian karşılığıdır. Alt adımlar know-how ile derinleştirildi; ilişkisellik ağına (tasks DB) işlenecek.
