# Monthly Electrical Generation by Community

## Description
This dataset is monthly electrical generation aggregated by grid and associated with every community connected to the grid. It summarizes the amount of electrical power produced for a community and the fuels that were used to generate it. Two factors complicate this simple seeming dataset. First, there is no single state or federal agency that collects data on all the generation sources in Alaska. Second, some communities have isolated microgrids where generation sources are easy to identify, but other communities are interconnected with interties into grids where generation sources are shared. In those cases, it is therefore impossible to pair a community with individual power stations (called plants) or the operators/utilities for which generation is recorded even if the plant is physically located within a community.
To address the first issue, this dataset derives from the Alaska Energy Statistics workbooks, which in turn compiles data from multiple sources including community Power Cost Equalization reports collated by the Alaska Energy Authority and reporting to the U.S. Energy Information Administration (EIA). Source data was harmonized to account for differences in reporting through a combination of subject matter expertise and transformations.
To address the second issue, generation is summed over all the generators with different fuels - diesel and natural gas boilers, solar installations, wind turbines - that are connected to a grid. Grids were defined as an element of the Alaska Energy Statistics workbooks and implemented with a lookup table that joins them to individual plants. The same values for total generation are reported for all the communities on a grid, which creates multiple duplicate values in this dataset.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_monthly_generation/public_monthly_generation.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_monthly_generation/public_monthly_generation.csv)
* **Reference Date:** 2024-02-29

### Sources
* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Energy Statistics Electrical Generation Tables** (2024)
  https://acep-uaf.github.io/ak-energy-statistics-2011_2021/
 The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. The workbooks were developed to provide community and utility level datasets that support regional and statewide aggregations for use in the 2024 Alaska Electricity Trends Report. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA). These sources are supplemented by annual filings to the Regulatory Commission of Alaska (RCA), village and powerhouse assessments, and direct communications with utilities and hydro/wind program managers.
Additional funding was contributed by Office of Naval Research (ONR) funded Alaska Regional Collaboration for Technology Innovation and Commercialization (ARCTIC) program, the Denali Commission, and the State of Alaska.
AEDG uses this dataset as the best available compilation of electrical generation, incorporating data from multiple sources into a single source.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Service Area Net Generation (MWh) | number | MWh | Net generation of all plants within the service area |
| Fuel Type | string | None | Generation fuel as defined by the U.S. Energy Information Administration (EIA) |
| Year | integer | None | Four digit year as Common Era (CE) |
| Month | integer | None | Month as 1-12 for which generation was reported |

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

