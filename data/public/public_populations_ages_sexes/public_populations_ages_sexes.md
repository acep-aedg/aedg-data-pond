# American Community Survey Populations

## Description
Total populations were measured by the U. S. Census and associated with communities by the Alaska Division of Community and Regional Affairs (DCRA). This dataset includes population size by sex in Alaskan communities for the most recent 5-year American Community Survey (ACS) intervals. It also includes population by age. The 5-year interval data sets are published approximately 1/2 a period later than the End Year listed.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_populations_ages_sexes/public_populations_ages_sexes.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_populations_ages_sexes/public_populations_ages_sexes.csv)
* **Reference Date:** 2025-06-01

### Sources
* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **American Community Survey Population Characteristics, Age** (2022)
  https://maps.commerce.alaska.gov/server/rest/services/Demographics/Alaska_American_Community_Survey/MapServer/5
 Population by age in Alaskan communities for the most recent 5-year American Community Survey (ACS) interval. GIS data shows the median age of each community. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see: US Census - The Significance of Age and Sex Data and Alaska DOLWD ACS Data
AEDG uses this dataset to associate places (point locations) with population divided into age ranges.

* **American Community Survey Population Characteristics, Sex** (2022)
  https://maps.commerce.alaska.gov/server/rest/services/Demographics/Alaska_American_Community_Survey/MapServer/0
 Population size by sex in Alaskan communities for the most recent 5-year American Community Survey (ACS) intervals. GIS data shows the male to female ratio of each community. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see: US Census - The Significance of Age and Sex Data.
AEDG uses this dataset to associate places (point locations) with population divided into male and female.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Start Year | integer | None | Beginning of the data collection period |
| End Year | integer | None | End of the data collection period |
| Estimated Total Population | number | None | Estimated total population |
| Estimated Population Under 5 | number | None | Estimated population under 5 years old |
| Estimated Population 5-9 Years Old | number | None | Estimated population between ages 5-9 years old |
| Estimated Population 10-14 Years Old | number | None | Estimated population between ages 10-14 years old |
| Estimated Population 15-19 Years Old | number | None | Estimated population between ages 15-19 years old |
| Estimated Population 20-24 Years Old | number | None | Estimated population between ages 20-24 years old |
| Estimated Population 25-34 Years Old | number | None | Estimated population between ages 25-34 years old |
| Estimated Population 35-44 Years Old | number | None | Estimated population between ages 35-44 years old |
| Estimated Population 45-54 Years Old | number | None | Estimated population between ages 45-54 years old |
| Estimated Population 55-59 Years Old | number | None | Estimated population between ages 55-59 years old |
| Estimated Population 60-64 Years Old | number | None | Estimated population between ages 60-64 years old |
| Estimated Population 65-74 Years Old | number | None | Estimated population between ages 65-74 years old |
| Estimated Population 75-84 Years Old | number | None | Estimated population between ages 75-84 years old |
| Estimated Population 85+ Years Old | number | None | Estimated population 85+ years old |
| Estimated Population Median Age | number | None | Estimated population median age |
| Estimated Population Under 18 | number | None | Estimated population under 18 years old |
| Estimated Population 18+ Years Old | number | None | Estimated population 18+ years old |
| Estimated Population 21+ Years Old | number | None | Estimated population 21+ years old |
| Estimated Population 62+ Years Old | number | None | Estimated population 62+ years old |
| Estimated Population 65+ Years Old | number | None | Estimated population 65+ years old |
| Estimated Population All Ages | number | None | Estimated population of all ages |
| Estimated Male Population | number | None | Estimated male population |
| Estimated Female Population | number | None | Estimated female population |

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

