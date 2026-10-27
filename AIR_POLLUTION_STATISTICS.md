# Budapest district air pollution: descriptive statistical comparisons

**Status (October 27, 2026):** A reproducible, original **spatial aggregation and secondary statistical comparison** of published gridded values. Environmental Health Atlas presents its PM2.5 and NO₂ capital-city map sources as EEA (2023). The ArcGIS map-service layer's own data vintage has not been separately verified and is therefore **provisionally attributed to 2023**. It would be inaccurate to call these directly measured district air-quality readings.

## Methods

- Source: European Environment Agency (EEA), Environmental Health Atlas capital-city 1 × 1 km pollution surfaces for PM2.5 and NO₂.
- Downloaded cell polygons: PM2.5 layer 0, NO₂ layer 5, from EEA Environmental Health Atlas / European_Capitals_2D MapServer.
- Overlay: Intersect raster-cell polygons with all 23 Budapest district boundaries, project both in equal-area EPSG:3035, and compute **intersection-area-weighted concentration mean per district**, in µg/m³.
- Coverage: All 23 districts satisfy the pipeline's ≥85% area coverage cutoff; coverage and number of map cells for each district are published in the CSV. The coastal-boundary percentage is not a measurement-data uncertainty estimate.
- Statistics: Districts are then treated as 23 equally weighted spatial units; Pearson *r*, Spearman ρ, and top/bottom six vegetation-group means are derived from the calculated pollution values and previously published district vegetation cover. Calculations: [pollution_statistics.py](analysis/pollution_statistics.py).

## Key results

| Descriptive statistic | PM2.5, µg/m³ | NO₂, µg/m³ |
|---|---:|---:|
| District-unweighted mean, all 23 | 15.417 | 23.791 |
| Minimum district estimate | 14.134 (II) | 16.122 (XXIII) |
| Maximum district estimate | 15.978 (XIII) | 31.741 (V) |
| Six least-vegetated districts, district-unweighted mean | 15.895 | 29.574 |
| Six most-vegetated districts, district-unweighted mean | 14.777 | 19.549 |
| Group difference (least minus most vegetation) | **+1.117** | **+10.025** |
| Pearson correlation with district vegetation cover | **−0.868** | **−0.869** |
| Spearman rank correlation with district vegetation cover | **−0.920** | **−0.864** |

Six least-vegetated districts by the vegetation dataset: VII, V, VI, XIII, VIII, XIX.
Six most-vegetated districts: XII, II, XXII, III, XVII, XVIII.

PM2.5 and NO₂ district-mean estimates have Pearson *r* ≈ +0.821 in this sample.

## Medical context

The World Health Organization's 2021 **annual** air-quality guideline levels are **5 µg/m³ for PM2.5** and **10 µg/m³ for NO₂**. All 23 of these mapped district area-means exceed both guideline concentrations, but this is an *exploratory model-based comparison*, **not** a legal compliance assessment, measure of disease rates, population-weighted exposure, or proof of individual risk. The WHO guidelines are health-based recommendations, not identical to EU enforceable limits.

## What can and cannot be concluded

The district patterns are compatible with a contrast between dense central districts and less densely built peripheral or hilly districts. They do **not** establish that vegetation itself caused lower pollution. Traffic intensity, land use, topography, population density, heating patterns, urban form and meteorology are possible confounders; neighboring districts are not independent statistical samples.

**Critical temporal mismatch:** The vegetation estimates date to approximately 2015–2017, whereas the EEA map display is labeled 2023. The observed association joins different-year datasets. Pearson and Spearman values are descriptive, not formal hypothesis tests adjusted for spatial autocorrelation or uncertainty. Exact PM2.5 distinctions of a few tenths of µg/m³ should not be overinterpreted.

The map is 1-km modeled/interpolated ambient concentration, missing local street-canyon variability, peaks near roads, indoors and residents' actual movements. No information about illness, patient records, mortality, or healthcare use was included.

## Data and source credits

- **Derived district table:** [air_pollution_by_district.csv](data/air_pollution_by_district.csv)
- **Source extraction and geometry method:** [district_air_pollution.py](analysis/district_air_pollution.py)
- **Exploratory statistics:** [pollution_statistics.py](analysis/pollution_statistics.py)
- **EEA Environmental Health Atlas:** https://discomap.eea.europa.eu/atlas/?page=Air-pollution
- **EEA ArcGIS map service:** https://trial.discomap.eea.europa.eu/arcgis/rest/services/EnvHealthAtlas/European_Capitals_2D/MapServer
- **EEA PM2.5 2023 metadata and 1-km methodology:** https://sdi.eea.europa.eu/catalogue/datahub/api/records/57807f24-25dc-4df3-9468-dcff8cee5468
- **EEA validated 2023 spatial mapping report (ETC HE 2025/5):** https://www.eionet.europa.eu/etcs/etc-he/products/etc-he-products/etc-he-reports/etc-he-report-2025-5-air-quality-maps-of-eea-member-and-cooperating-countries-for-2023-pm10-pm2-5-o3-no2-nox-and-bap-spatial-estimates-and-their-uncertainties
- **WHO 2021 guideline table:** https://www.ncbi.nlm.nih.gov/books/NBK574591/table/ch3.tab26/
- **District boundaries:** https://github.com/integralvision/geo-data-hungary, CC BY-SA 3.0, based on OpenStreetMap contributors.

Recheck current upstream map service metadata before treating any derived numbers as permanently stable.
