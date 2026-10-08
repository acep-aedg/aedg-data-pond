# Alaska Native Regional Corporations

## Description
This dataset provides spatial boundary polygons, FIPS codes, and area measurements (land and water) for Alaska Native Regional Corporations.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_regional_corporations/public_regional_corporations.geojson](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_regional_corporations/public_regional_corporations.geojson)
* **Reference Date:** 2026-09-18

### Sources
* **Alaska Native Regional Corporations** (2024)
  https://www.arcgis.com/home/item.html?id=c78df0004ab845a9a32697d9c20d09e0
 This feature layer, utilizing National Geospatial Data Asset (NGDA) data from the U.S. Census Bureau (USCB), displays the twelve territories that make up the Alaska Native Regional Corporations (ANRC). Per the Bureau, each ANRC is defined "as a ’Regional Corporation’ organized under the laws of the State of Alaska to conduct both the for-profit and non-profit affairs of Alaska Natives within a defined region of Alaska. Twelve Regional Corporations cover the entire state of Alaska except for the area within the Annette Island Reserve (a federally recognized American Indian reservation under the governmental authority of the Metlakatla Indian Community). A thirteenth represents Alaska Natives who do not live in Alaska and do not identify with any of the twelve corporations.”
Regional Corporations were created by the Alaska Native Claims Settlement Act (ANCSA) and are organized around geographic areas defined by the common heritage and shared interests of the indigenous peoples. The boundaries of these areas do not directly represent land ownership, but instead define the areas in which each regional corporation could select lands to be conveyed under the provisions of ANCSA.
AEDG includes Regional Corporations in the description of communities.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Standards (FIPS) code identifier for geographic entities, assigned and maintained by the Census Bureau |
| Land Area | number | sq m | Total land area |
| Name | string | None | Name of the regional corporation |
| Water Area | number | sq m | Total water area |

### Comments
> **2025**: Identified data source and integrated it into the data pipeline.
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

