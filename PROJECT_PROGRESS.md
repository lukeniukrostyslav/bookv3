# PROJECT PROGRESS — bookv3

Дата контрольной точки: 23.09.2026

## Current master status

| Блок | Статус | Прогресс |
|---|---|---:|
| B0–B13 | завершены | 100% |
| B14 — русская финальная публикация | финальная production/Google Play цепочка | 76% |
| B15 — международная локализация и публикация | Italian edition + KDP + StreetLib | 90% |

## B0–B13

B0–B13 считаются завершёнными на основании сохранённого master progress.

**B0–B13: 100%.**

## B14 — финальная русская публикация

**Текущий master progress: 76%.**

Из сохранённых технических checkpoint-документов:

- B14.4 — структурный аудит: **85%** в последнем отдельном audit-документе.
- B14.5 — финальный подсчёт слов: **100% выполнен**, канонический корпус = **32 главы / 76 735 слов**.
- B14.6 — внутренние иллюстрации: **10%**; manifest утверждён, производство и QA изображений впереди.
- B14.7 — обложка: **40%**; исходник утверждён владельцем, технически проверен, интеграция в финальный EPUB впереди.
- B14.8 — EPUB 3.3: **100%**, базовая сборка закрыта; после интеграции финальной обложки требуется финальная пересборка.
- B14.9 — EPUBCheck: **100%** для текущей cover-independent сборки; после интеграции обложки EPUBCheck необходимо повторить.
- B14.10 — Google Play Books QA: **20%**; финальный cover-integrated EPUB ещё не загружен и визуальный QA ещё не закрыт.

### Канонический корпус

- 32 канонические главы.
- Отдельного эпилога нет.
- Глава 32 — «Человек у окна».
- Канонический объём: **76 735 слов**.

## B15 — Italian edition / international publication

**Текущий master progress: 90%.**

- B15.1 — Italian translation: **100%**
- B15.2 — Italian literary editing + QA: **100%**
- B15.3 — Italian EPUB production: **100%**
- B15.5 — Amazon KDP Italy: **100% submitted; current status observed on 23.09.2026 = PUBLISHING**
- B15.6 — Google Play Books Italy: **0% — intentionally on hold**
- B15.7 — StreetLib: **90% — publication review in progress**

## AMAZON KDP — CURRENT CHECKPOINT 23.09.2026

The owner provided a live KDP Bookshelf screenshot on 23.09.2026 at approximately 23:21 local time.

Verified from the screenshot:

- Title: **L'Hotel dell'ultimo domani**
- Author shown: **Rostislav Lukeniuk**
- Format: **Kindle eBook**
- Price shown: **€5.99 EUR**
- ASIN shown: **B0HTK8KKT**
- Current KDP status: **Publishing**
- Last modified: **September 23, 2026**
- Paperback: **Draft**
- Hardcover: not created yet

Meaning of the current status:
**IN REVIEW has progressed to PUBLISHING.** The Kindle edition is now in Amazon's publication stage. The next expected state is **Online**. Do not treat the book as fully live until KDP shows Online and the Amazon product page is confirmed.

### Amazon operating rule

Do not make unnecessary changes while the Kindle eBook is in **Publishing**. After it becomes **Online**, perform a final storefront QA: product page, title/author, cover, description, price, sample/reading, and availability.

## StreetLib S1

**Current S1 progress: 90%.**

| Sub-block | Status |
|---|---:|
| S1.1 Verify current StreetLib eBook conditions | 100% |
| S1.2 Distribution strategy | 100% |
| S1.3 Amazon/KDP conflict check | 100% |
| S1.4 Google Play timing | 100% |
| S1.5 ISBN decision — StreetLib free ISBN selected | 100% |
| S1.6 StreetLib registration / profile / billing / agreement | 100% |
| S1.7 Upload EPUB + cover | 100% |
| S1.8 Italian metadata | 100% |
| S1.9 Store/channel configuration + price/territories | 100% |
| S1.10 Final QA / publication and store-link verification | 0% |

### StreetLib technical checkpoint

- Corrected EPUB installed.
- ACE accessibility validation: **0 violations**.
- WCAG: **0** findings.
- EPUB: **0** findings.
- Best practices: **0** findings.
- Price: **€5.99 EUR**.
- Territories: **worldwide**.
- Amazon Kindle Store: **disabled** in StreetLib because the Italian edition is submitted directly through KDP.
- Google Play Store: **disabled intentionally**.
- StreetLib dashboard state at last saved checkpoint: **revisione**.
- Store links are not final until publication completes and links are verified.

## Other publication channels

- Amazon KDP Italy: **100% submitted / PUBLISHING**
- Google Play Books Italy: **0% — intentionally on hold**
- StreetLib: **90% — review in progress**
- Apple Books direct: **0%**
- Kobo Writing Life direct: **0%**

## Current next actions

1. **Amazon KDP:** wait for Kindle eBook to change from Publishing to Online; then perform storefront QA.
2. **StreetLib:** wait for review/publication; then verify actual store links.
3. **B14:** continue only the unfinished final production gates; do not rewrite the manuscript.
4. After final cover integration, rerun EPUBCheck before final Google Play QA.

## Fixed rules

1. Do not create a second StreetLib publication for the same Italian edition.
2. Do not enable StreetLib Amazon Kindle distribution for this Italian edition.
3. Do not replace the validated EPUB unless a concrete issue requires it.
4. Every completed checkpoint is saved to GitHub.
5. Percentages must reflect the actual saved state and must not be inflated.
