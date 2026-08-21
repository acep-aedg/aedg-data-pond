# Household Income by Community

## Description
This dataset contains community-level household income and benefits estimates for Alaska derived from U.S. Census Bureau American Community Survey (ACS) 5-year data. It provides total household counts, median household income, and household distributions across income brackets ranging from under $10,000 to $200,000 or more. All income categories and monetary metrics include both household income and benefits, inflation-adjusted to the period end year and are organized by FIPS code, community name, and ACS survey time period.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_household_income/public_household_income.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_household_income/public_household_income.csv)
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

* **American Community Survey Household Income and Benefits** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Demographics/Alaska_American_Community_Survey/MapServer/3
 Population counts by household income in Alaskan communities for the last 12 months of the most recent ACS 5-year interval. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see: US Census Bureau, Household Income and Alaska American Community Survey Data


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Total Households | integer | households | Estimated total number of households |
| Median Household Income | integer | USD | Estimated median household income (including benefits, adjusted for inflation to survey end year) |
| Household Income Under $10k | integer | households | Estimated households with income under $10,000 (including benefits, adjusted for inflation to survey end year) |
| Household Income $10,000–$14,999 | integer | households | Estimated households with income of $10,000 to $14,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $15,000–$24,999 | integer | households | Estimated households with income of $15,000 to $24,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $25,000–$34,999 | integer | households | Estimated households with income of $25,000 to $34,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $35,000–$49,999 | integer | households | Estimated households with income of $35,000 to $49,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $50,000–$74,999 | integer | households | Estimated households with income of $50,000 to $74,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $75,000–$99,999 | integer | households | Estimated households with income of $75,000 to $99,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $100,000–$149,999 | integer | households | Estimated households with income of $100,000 to $149,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $150,000–$199,999 | integer | households | Estimated households with income of $150,000 to $199,999 (including benefits, adjusted for inflation to survey end year) |
| Household Income $200,000+ | integer | households | Estimated households with income of $200,000 or more (including benefits, adjusted for inflation to survey end year) |
| ACS Start Year | integer | year | Start year of the 5-year ACS survey observation window |
| ACS End Year | integer | year | End year (vintage) of the 5-year ACS survey observation window |

### Comments
> **2025**: 1. Identified data source and integrated it into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Joined household_income data with AEDG communities to create this dataset
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

