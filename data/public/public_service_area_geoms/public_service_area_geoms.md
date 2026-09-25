# Electric Service Areas of Alaska (Individual Geometries)

## Description
Spatial file of electric service area polygons in Alaska, used in AEDG (Alaska Energy Data Gateway) to associate communities with infrastructure and sales reporting. Non-contiguous service boundaries assigned to a single utility CPCN are split into separate feature records.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_service_area_geoms/public_service_area_geoms.geojson](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_service_area_geoms/public_service_area_geoms.geojson)
* **Reference Date:** 2026-01-01

### Sources
* **ACEP Electric Service Areas** (2025)
  https://acep-uaf.github.io/utility-service-areas/
 The Regulatory Commission of Alaska (RCA) associates every regulated electric utility with a service area in which they are allowed to operate. Using the individual service area files provided by the RCA, the Alaska Center for Energy and Power (ACEP) assembled a single geospatial file in GeoJSON format which contains the service area boundaries of every active electric utility in Alaska. AEDG uses these service area polygons to identify the utility/utilities serving each community across the state.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Name | string | None | Official name of the electric utility holding the CPCN certificate for the polygon (e.g., 'Alaska Village Electric Cooperative, Inc.'). |
| Service Area Geometry ID | string | None | Unique composite identifier for each individual spatial polygon. Formatted as '{cpcn_id}_{geom_index}' (e.g., '169_1'). |
| Uniform Resource Locator | string | None | Internet address to the official Certificate Details page on the Regulatory Commission of Alaska (RCA) portal. |

### Comments
> **2025**: Shapefiles of individual electric service areas were collected from RCA, cleaned and validated, then combined into a singular geojson file.
> 

> **2025**: Identified data source and integrated it into the data pipeline.
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

