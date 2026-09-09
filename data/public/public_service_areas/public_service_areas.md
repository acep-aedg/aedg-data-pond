# Electric Service Areas of Alaska

## Description
Spatial file of electric service areas in Alaska, used in AEDG to associate communities with infrastructure and sales reporting.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_service_areas/public_service_areas.geojson](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_service_areas/public_service_areas.geojson)
* **Reference Date:** 2026-01-01

### Sources
* **ACEP Electric Service Areas** (2025)
  https://acep-uaf.github.io/utility-service-areas/
 The Regulatory Commission of Alaska (RCA) associates every regulated electric utility with a service area in which they are allowed to operate. Using the individual service area files provided by the RCA, the Alaska Center for Energy and Power (ACEP) assembled a single geospatial file in GeoJSON format which contains the service area boundaries of every active electric utility in Alaska. AEDG uses these service area polygons to identify the utility/utilities serving each community across the state.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Reporting Entity Certificate Number | integer | None | A CPCN (Certificate of Public Convenience & Necessity) number, also called a certificate number, denotes a unique CPCN/certificate assigned by the Regulatory Commission of Alaska to a reporting entity. |
| Community Name | string | None | Name of the community |
| Uniform Resource Locator | string | None | Internet address of resource |

### Comments
> **2025**: Shapefiles of individual electric service areas were collected from RCA, cleaned and validated, then combined into a singular geojson file.
> 

> **2026**: 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

