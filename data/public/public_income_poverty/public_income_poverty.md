# Income Poverty by Community

## Description
This dataset contains community-level per capita income and poverty status estimates for communities in Alaska derived from U.S. Census Bureau American Community Survey (ACS) 5-year data. It provides estimated per capita income alongside population counts for individuals living below the federal poverty level and total individuals evaluated for poverty status (determined using reported income from the preceding 12 months of the ACD 5-year interval end year), with associated margins of error for each metric. All monetary metrics are inflation-adjusted to the period end year and are organized by community FIPS code, community name and ACS survey time period.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_income_poverty/public_income_poverty.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_income_poverty/public_income_poverty.csv)
* **Reference Date:** 2023

### Sources
* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **American Community Survey Income and Poverty** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Demographics/Alaska_American_Community_Survey/MapServer/2
 Population counts in Alaskan communities that fall under poverty status measures for the last 12 months of the most recent ACS 5-year interval. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see US Census Bureau, Poverty Data and Alaska American Community Survey Data


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Community FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places, assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Per Capita Income | integer | USD | Estimated per capita income (adjusted for inflation to survey end year) |
| Per Capita Income Margin of Error | integer | USD | Margin of error for estimated per capita income |
| Population Below Poverty Level | integer | persons | Estimated population with income below the federal poverty level |
| Population Below Poverty Level Margin of Error | integer | persons | Margin of error for estimated population with income below the federal poverty level |
| Population Evaluated for Poverty Status | integer | persons | Estimated total population for whom poverty status is determined |
| Population Evaluated for Poverty Status Margin of Error | integer | persons | Margin of error for estimated population for whom poverty status is determined |
| ACS Start Year | integer | year | Start year of the 5-year ACS survey observation window |
| ACS End Year | integer | year | End year (vintage) of the 5-year ACS survey observation window |

### Comments
> **2025**: 1. Identified data source and integrated it into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Joined income poverty data with AEDG communities to create this dataset

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

