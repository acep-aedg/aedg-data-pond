# Community Employment

## Description
The number of employed residents and the number of unemployment insurance claimants for each community. Data are available for 2001 to 2016.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_employment/public_employment.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_employment/public_employment.csv)
* **Reference Date:** 2016

### Sources
* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Employment and Wages, All Locations** (2016)
  https://maps.commerce.alaska.gov/server/rest/services/Economics_Related/Economics_Employment_Wages/MapServer/0
 Current monthly employment data for Alaska is available at https://live.laborstats.alaska.gov/labforce/000000/01/ces.html, but only at the regional level. This data is at the community level and has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data.
AEDG uses this dataset to provide employment figures for communities. However, these data have not been updated since 2016, and there is very little metadata. Previous versions of AEDG used the publicly accessible ALARI database, but that is no longer available.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Residents Employed | integer | None | Number of residents  |
| Unemployment Insurance Claimants | integer | None | Number of people who claimed unimployment insurance |
| Year | integer | None | Four digit year as Common Era (CE) |

### Comments
> **2025**: 1. Identified data source and integrated it into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Joined employment data with AEDG communities to create this dataset
> 

> **2026-01-12**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

