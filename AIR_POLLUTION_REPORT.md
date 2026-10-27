# Air pollution across Budapest districts — exploratory zonal analysis

Research method: Overlay EEA Health Atlas air pollution map-cell polygons with real Budapest district boundaries and compute intersection-area weighted means in EPSG:3035. Units: µg/m³.

**Important:** Source map service vintage needs independent verification before attributing results to a calendar year. The EEA Health Atlas discusses 2023 maps, but service layer metadata need cross-checking.

These are mapped-model district **area means**, not 23 independent sets of measured station data, patient exposure, personal health risk, actual disease rates, or regulatory compliance.

## Coverage and mapped estimates

| District | PM2.5 (µg/m³) | Coverage | NO₂ (µg/m³) | Coverage |
|---|---:|---:|---:|---:|
| 1 Budapest I. kerület | 15.94 | 100.0% | 29.04 | 100.0% |
| 2 Budapest II. kerület | 14.13 | 94.7% | 18.00 | 94.7% |
| 3 Budapest III. kerület | 15.55 | 97.0% | 21.83 | 97.0% |
| 4 Budapest IV. kerület | 15.38 | 95.4% | 21.96 | 95.4% |
| 5 Budapest V. kerület | 15.93 | 100.0% | 31.74 | 100.0% |
| 6 Budapest VI. kerület | 15.95 | 100.0% | 31.18 | 100.0% |
| 7 Budapest VII. kerület | 15.95 | 100.0% | 30.89 | 100.0% |
| 8 Budapest VIII. kerület | 15.86 | 100.0% | 30.03 | 100.0% |
| 9 Budapest IX. kerület | 15.82 | 100.0% | 27.34 | 100.0% |
| 10 Budapest X. kerület | 15.46 | 100.0% | 22.38 | 100.0% |
| 11 Budapest XI. kerület | 15.52 | 99.3% | 23.76 | 99.3% |
| 12 Budapest XII. kerület | 14.32 | 95.6% | 20.00 | 95.6% |
| 13 Budapest XIII. kerület | 15.98 | 100.0% | 28.60 | 100.0% |
| 14 Budapest XIV. kerület | 15.84 | 100.0% | 27.13 | 100.0% |
| 15 Budapest XV. kerület | 15.59 | 93.6% | 19.23 | 93.6% |
| 16 Budapest XVI. kerület | 15.02 | 95.0% | 20.36 | 95.0% |
| 17 Budapest XVII. kerület | 14.63 | 97.2% | 17.91 | 97.2% |
| 18 Budapest XVIII. kerület | 14.93 | 98.5% | 19.96 | 98.5% |
| 19 Budapest XIX. kerület | 15.70 | 100.0% | 25.01 | 100.0% |
| 20 Budapest XX. kerület | 15.58 | 100.0% | 24.09 | 100.0% |
| 21 Budapest XXI. kerület | 15.65 | 95.3% | 21.02 | 95.3% |
| 22 Budapest XXII. kerület | 15.10 | 98.3% | 19.59 | 98.3% |
| 23 Budapest XXIII. kerület | 14.75 | 96.7% | 16.12 | 96.7% |

## Interpretation and limitations

Areas with lower street vegetation or higher traffic may have higher mapped concentrations, but this analysis cannot establish cause-and-effect or individual medical consequences.
Each district is a land-area aggregation of 1-km mapped source cells. Population weighting, pedestrian exposure, street canyons, fine-scale traffic, uncertainty bounds and seasonal contrasts are not computed.
Source methodology: EEA Environmental Health Atlas raster/polygon map inputs. Mapped values must not be equated to regulatory monitoring-site exceedances.
Coverage under 85% results in a missing value, not a guessed estimate. Coverage above 110% also fails as a potential overlap issue.

## Source URLs

https://trial.discomap.eea.europa.eu/arcgis/rest/services/EnvHealthAtlas/European_Capitals_2D/MapServer
https://discomap.eea.europa.eu/atlas/?page=Air-pollution
https://sdi.eea.europa.eu/catalogue/datahub/api/records/57807f24-25dc-4df3-9468-dcff8cee5468
https://github.com/integralvision/geo-data-hungary
