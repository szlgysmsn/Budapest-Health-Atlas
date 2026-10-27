# Public-health research protocol — Budapest Health Atlas

**Project focus:** Examine spatial variation in environmental conditions relevant to population health across Budapest's 23 districts; ultimately investigate whether these conditions overlap with barriers to access to health care.

**Study type and current status (October 2026):** Exploratory ecological, secondary-data atlas with a planned primary observational pilot. Published vegetation-cover and climate-model outputs are presently available for district comparison. Verified district-specific PM2.5/NO₂ exposure surfaces, pedestrian park access, and validated care-access indices are **not yet** available. No clinical outcomes, patient data, interviews, or primary field observations have been collected.

## Four research questions and appropriate indicators

| Theme | Proposed indicator | Current state | Medical relevance | Essential caveat |
|---|---|---|---|---|
| Urban heat | Modeled threshold-frequency days/year under RCP4.5 and RCP8.5 for 2041–2070; later independently observed daytime/overnight temperature | Published district modeled values available | Heat stress, heatstroke, cardiovascular and kidney disease | Not observed heat days, illness, or a resident-level exposure |
| Air pollution | PM2.5 and NO₂ annual or seasonal exposure at a common year, spatially modeled across districts using adequately validated measurements | Official monitoring source identified; no defensible 23-district surface computed | Respiratory and cardiovascular disease | A monitoring station does not characterize an entire district |
| Green-space accessibility | Share of residential locations within **walking-network distance** of a public park entrance, using consistent rules for entrances, barriers and public access | Land-cover vegetation available; park access not measured | Physical activity, heat mitigation, mental health | Vegetated land per resident is NOT accessible public park area |
| Health care access | Distance or travel time from small population centroids to validated contracted general practitioner/clinic sites, plus facility-to-population ratios where legitimate | Official NEAK register identified; exploratory OSM location lookups only | Care availability for prevention, diagnosis and treatment | A point's proximity is not proof of eligibility, staffing, appointment availability, or travel access |

## Testable, noncausal hypotheses

H1. Published lower vegetation coverage and higher modeled heat-threshold frequency co-occur across districts. Note that land cover contributes to the model, making this partly mechanical.

H2. In a future independently sourced street audit, lower tree-shade observations co-occur with more extensively built-up street sections. Collect weather/time-matched repeats.

H3. A future walking-network analysis identifies neighborhoods farther from verified publicly accessible parks, even when district-level vegetation coverage is high.

H4. A future population-weighted analysis using NEAK-validated provider locations identifies variation in travel time to primary care across residential areas. Report access obstacles, not the quality of care or actual individual utilization.

## Methods roadmap

1. **Geography and data:** Use real 23-district boundaries credited to the upstream creators and OpenStreetMap; record the geometry vintage. Prefer consistent subdistrict grid cells for exposure comparisons.
2. **Temporal alignment:** Do not pool vegetation data from 2015–2017 with measured pollution for a different year as if contemporaneous. Projection periods must be visibly identified.
3. **Air-pollution assessment:** Download station metadata and hourly/daily measures from the National Air Pollution Monitoring Network (OLM). Document data completeness, units (µg/m³), instrumentation and missing values. Choose a consistent year; do not interpolate from sparse monitors without validation. Optionally use a justified gridded product and compare it with station measurements.
4. **Park accessibility:** Verify that parks are publicly accessible and map entrances, including barriers. Compute shortest **walking-network** routes from residential address or census-grid centroids; never substitute area of woodland, private gardens, or generic polygons for accessible recreation.
5. **Health care:** Download the relevant NEAK provider directories (general practice, specialist outpatient, inpatient). De-duplicate sites, verify addresses, classify service types; where possible model public transit and walking time from population-weighted origin points. Distinguish the legally responsible GP catchment and actual physician vacancies from mere straight-line distance.
6. **Comparative analysis:** Report medians, interquartile ranges, spatial distributions and (where justified) covariate-adjusted associations. Consider neighborhood density, age structure, socioeconomic conditions and housing. Ecological associations never show effects on an individual.
7. **Primary observations:** Seek teacher review of a standardized 100-meter sidewalk shade protocol, choose nonconvenience sampling where possible, observe at matched times, repeat observations, report uncertainty and avoid photographing identifiable people.
8. **Validation:** Keep dataset citations, methods version history and actual external feedback. Do not imply that a university, hospital or city institution endorses the project unless it confirms that.

## Safety and research ethics

Only use public, aggregated, non-identifying information in the public atlas. Any proposed survey involving students, patient information, or health conditions needs school/institutional guidance, appropriate consent and potentially ethics review before collection. Do not publish personally identifying information or identifiable photos. Maps cannot diagnose anyone or predict an individual's medical risks.

## Core source links

- Vegetation and modeled climate data: https://masfelfok.hu/2023/07/18/hosegnap-hohullam-budapest-klimavaltozas-varosi-hosziget-zoldfeluletek-fak/
- Hungarian National Air Pollution Monitoring Network (OLM): https://legszennyezettseg.met.hu/
- NEAK contracted care services: https://neak.gov.hu/letoltheto/altfin_dok/szerzodott_szolgaltatok
- KSH Budapest district statistics (BP-STAR): https://www.ksh.hu/regional-data
- WHO heat and health: https://www.who.int/en/news-room/fact-sheets/detail/climate-change-heat-and-health
- WHO ambient air quality and health: https://www.who.int/en/news-room/fact-sheets/detail/ambient-%28outdoor%29-air-quality-and-health
- WHO urban green spaces and health: https://www.who.int/europe/publications/i/item/WHO-EURO-2016-3352-43111-60341
- WHO primary health care: https://www.who.int/news-room/fact-sheets/detail/primary-health-care
- Boundaries derived from https://github.com/integralvision/geo-data-hungary (CC BY-SA 3.0) and OpenStreetMap contributors (ODbL).
