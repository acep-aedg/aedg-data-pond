# Heating Degree Days by Communities

## Description
This dataset provides monthly counts of Heating Degree Days (HDD) for Alaska communities identified by name and Census FIPS code. Heating degree days quantify the daily thermal deficit below a 65 degree Fahrenheit baseline, serving as a primary metric for estimating building heating fuel consumption, analyzing seasonal energy demand, and supporting rural energy planning across Alaska.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_heating_degree_days/public_heating_degree_days.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_heating_degree_days/public_heating_degree_days.csv)
* **Reference Date:** 2025

### Sources
* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Heating Degree Days** (2025)
  https://daymet.ornl.gov
 This is a CSV derived from ORNL's Daymet API, queried for each community in AEDG. Max and min daily temperature values were averaged and subtracted from 65F to calculate heating degree days. Data contains total annual cumulative heating degree days at a spatial resolution of 1 km. Units are degree days Fahrenheit (°F⋅days).
Heating degree days (HDD), defined in the U.S. as degrees F below 65 multiplied by duration in days, quantifies energy needed to heat a building over a year's time. This information helps AEDG users to understand building energy needs amongst different Alaskan communities.

* **Heating Degree Days** (2024)
  https://earthmaps.io/degree_days/
 This is a CSV derived from SNAP's heating degree day API, queried for each community in AEDG. Data contains total annual cumulative heating degree days at a spatial resolution of 12 km. Units are degree days Fahrenheit (°F⋅days). Modeled baseline data were derived from a Daymet dataset and are available for years 1980–2017. Modeled data were derived from bias corrected and downscaled CMIP5 climate models using RCP 4.5 and RCP 8.5 emissions scenarios.
Heating degree days (HDD), defined in the U.S. as degrees F below 65 multiplied by duration in days, quantifies energy needed to heat a building over a year's time. This information helps AEDG users to understand building energy needs amongst different Alaskan communities.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Community FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places, assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Year | integer | None | Four digit year as Common Era (CE) |
| Month | integer | None | Month as 1-12 for the reported observation |
| Heating Degree Days | integer | HDD | Heating degree days (HDD), defined in the U.S. as degrees F below 65 multiplied by duration in days, quanitifies energy needed to heat a building over a year's time |

### Comments
> **2025**: 1. Identified climate data sources and integrated it into the data pipeline.
> 2. Compiled community names and FIPS identifiers for AEDG.
> 3. Joined heating degree day data with AEDG communities to create this dataset.
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

