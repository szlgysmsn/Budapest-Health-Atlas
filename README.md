# Budapest Health Atlas

Bilingual (English/Hungarian) secondary environmental research atlas comparing vegetation cover and **modeled** urban heat exposure across Budapest's 23 districts.

## View the website

[Open index.html](./index.html). To go live, enable GitHub Pages: **Settings → Pages → Build and deployment → Deploy from a branch → main → / (root) → Save**. Once deployment succeeds, expected URL: https://szlgysmsn.github.io/Budapest-Health-Atlas/

## Sources

- [Csóka Gergely, Másfélfok (2023)](https://masfelfok.hu/2023/07/18/hosegnap-hohullam-budapest-klimavaltozas-varosi-hosziget-zoldfeluletek-fak/)
- [Budapest environmental reports](https://budapest.hu/zold-budapest/klima-es-kornyezetvedelem/budapest-kornyezetvedelmi-programja-es-kornyezeti-allapotertekelese)
- [BKK demographic context](https://bkk.hu/downloads/32854/)

## Scientific limitations

Input district-level values come from existing published analysis, not our own climate modeling or new observations. The heat variable measures modeled 30-year-average-temperature threshold exceedances, **not observed annual hot days**, health outcomes or individual exposure. Vegetation and projected heat associations are descriptive and not independent causal evidence (the climate model already uses land cover). The district tiles are a schematic visualization rather than GIS geographical boundaries.

## Research integrity

The site and comparative computations were prepared with substantial AI assistance. Independent source verification, original fieldwork, academic peer review, institutional partnerships and documented community impact have **not** occurred. Those must not be claimed before they happen. This release is not a peer-reviewed medical study.

See [methodology](./METHODOLOGY.md) and [original research roadmap](./NEXT_STEPS.md).

## Research and original fieldwork

- [Read environmental research brief](./research-report.html)
- [View bilingual observation log (local-only)](./fieldwork.html)
- [Download the source-tagged dataset](./data/district_environment.csv)
- [Download blank original fieldwork CSV](./data/fieldwork_template.csv)
- [Reproduce group statistics in Python](./analysis/analyze.py)

**Fieldwork privacy:** Entries made in the fieldwork page are stored only in the user's own browser and must be exported to CSV by the user. No observations are prefilled, transmitted to GitHub, or represented as completed. These are educational tools, not medical or epidemiological results.
