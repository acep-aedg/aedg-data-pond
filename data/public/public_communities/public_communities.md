# Alaska Energy Data Gateway Communities

## Description
List of the communities displayed in the Alaska Energy Data Gateway (AEDG), cross-walked to other regional energy, governmental, governmental and Indigenous organizations.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_communities/public_communities.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_communities/public_communities.csv)
* **Reference Date:** 

### Sources
* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Geographic Names Information System (GNIS) Federal Codes for AK** (2025)
  https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data
 The Geographic Names Information System (GNIS) is the Federal standard for geographic nomenclature. The U.S. Geological Survey developed the GNIS for the U.S. Board on Geographic Names, a Federal inter-agency body chartered by public law to maintain uniform feature name usage throughout the Government and to promulgate standard names to the public. The GNIS is the official repository of domestic geographic names data; the official vehicle for geographic names use by all departments of the Federal Government; and the source for applying geographic names to Federal electronic and printed products of all types.
AEDG includes GNIS code as a community attribute for purposes of cross referencing data from different sources.

* **Alaska Native Regional Corporations** (2024)
  https://www.arcgis.com/home/item.html?id=c78df0004ab845a9a32697d9c20d09e0
 This feature layer, utilizing National Geospatial Data Asset (NGDA) data from the U.S. Census Bureau (USCB), displays the twelve territories that make up the Alaska Native Regional Corporations (ANRC). Per the Bureau, each ANRC is defined "as a ’Regional Corporation’ organized under the laws of the State of Alaska to conduct both the for-profit and non-profit affairs of Alaska Natives within a defined region of Alaska. Twelve Regional Corporations cover the entire state of Alaska except for the area within the Annette Island Reserve (a federally recognized American Indian reservation under the governmental authority of the Metlakatla Indian Community). A thirteenth represents Alaska Natives who do not live in Alaska and do not identify with any of the twelve corporations.”
Regional Corporations were created by the Alaska Native Claims Settlement Act (ANCSA) and are organized around geographic areas defined by the common heritage and shared interests of the indigenous peoples. The boundaries of these areas do not directly represent land ownership, but instead define the areas in which each regional corporation could select lands to be conveyed under the provisions of ANCSA.
AEDG includes Regional Corporations in the description of communities.

* **Boroughs and Census Areas** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/3
 Boroughs are analogous to a counties in other states. Organized boroughs were formed in those areas where economies were better developed. The remaining areas are the unorganized borough, which is divided into census areas; these areas exist for statistical analysis and do not have a government of their own. There are also consolidated city-borough governments. The Division of Community and Regional Affairs (DCRA) provides these boundaries as part of their Community Database Online (CDO), a source of information to aid in advising and assisting local governments, including for research purposes.
AEDG includes borough or census area as a community attribute to identify governing entities.

* **Alaska Energy Statistics Infrastructure Tables** (2024)
  https://acep-uaf.github.io/ak-energy-statistics-2011_2021/
 The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. The workbooks were developed to provide community and utility level datasets that support regional and statewide aggregations for use in the 2024 Alaska Electricity Trends Report. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA). These sources are supplemented by annual filings to the Regulatory Commission of Alaska (RCA), village and powerhouse assessments, and direct communications with utilities and hydro/wind program managers.
Additional funding was contributed by Office of Naval Research (ONR) funded Alaska Regional Collaboration for Technology Innovation and Commercialization (ARCTIC) program, the Denali Commission, and the State of Alaska.
AEDG uses this dataset as the best available compilation of electrical generation capacity, incorporating data from multiple sources into a single source.

* **Alaska Energy Statistics Financial Tables** (2024)
  https://acep-uaf.github.io/ak-energy-statistics-2011_2021/
 The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. The workbooks were developed to provide community and utility level datasets that support regional and statewide aggregations for use in the 2024 Alaska Electricity Trends Report. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA). These sources are supplemented by annual filings to the Regulatory Commission of Alaska (RCA), village and powerhouse assessments, and direct communications with utilities and hydro/wind program managers.
Additional funding was contributed by Office of Naval Research (ONR) funded Alaska Regional Collaboration for Technology Innovation and Commercialization (ARCTIC) program, the Denali Commission, and the State of Alaska.
AEDG uses this dataset as the best available compilation of electricity sales, incorporating data from multiple sources into a single source.

* **Public Use Microdata Areas (PUMA)** (2023)
  https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2010/MapServer/0
 Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state or equivalent entity into geographic areas containing no fewer than 100,000 people each. They cover the entirety of the United States, Puerto Rico, and Guam. The Census Bureau defines PUMAs for the tabulation and dissemination of decennial census and American Community Survey (ACS) Public Use Microdata Sample (PUMS) data. Additionally, the ACS and Puerto Rico Community Survey use them to disseminate their respective period estimates.
AEDG uses PUMA to identify communities in Alaskan subsistence areas.

* **Alaska Economic Regions** (2024)
  https://maps.commerce.alaska.gov/server/rest/services/Boundaries/CDO_Economic_Regions/MapServer/0
 Alaska economic regions based on 2013 borough and census area geography. Boundaries are determined by the Alaska Department of Labor & Workforce Development. For more information, see Alaska Department of Labor Maps & GIS. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see: Alaska Local and Regional Information
AEDG uses this dataset to add the economic region spatial polygon to Anchorage gas prices.

* **Power Cost Equalization (PCE) Program Eligible Entities** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Services/CDO_Utilities/MapServer/3
 The Power Cost Equalization (PCE) program supports rural Alaskans who live in areas where energy costs are significantly higher than urban areas in meeting the cost of electricity. Eligibility is determined by the Regulatory Commission of Alaska under Alaska Statutes 42.45.100-170. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data.
AEDG includes PCE eligibility as an essential element of energy costs in Alaska.

* **Heating Degree Days** (2024)
  https://earthmaps.io/degree_days/
 This is a CSV derived from SNAP's heating degree day API, queried for each community in AEDG. Data contains total annual cumulative heating degree days at a spatial resolution of 12 km. Units are degree days Fahrenheit (°F⋅days). Modeled baseline data were derived from a Daymet dataset and are available for years 1980–2017. Modeled data were derived from bias corrected and downscaled CMIP5 climate models using RCP 4.5 and RCP 8.5 emissions scenarios.
Heating degree days (HDD), defined in the U.S. as degrees F below 65 multiplied by duration in days, quantifies energy needed to heat a building over a year's time. This information helps AEDG users to understand building energy needs amongst different Alaskan communities.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| GNIS Code | integer | None | The GNIS contains information about physical geographic features of many types in the United States, associated areas, and Antarctica, current and historical, but not including roads and highways or cultural features. The database holds the Federally recognized name of each feature and defines the feature location by state, county, USGS topographic map, and geographic coordinates. |
| Community Name | string | None | Name of the community |
| Alaska Native Regional Corporation | string | None | Alaska Native regional corporations were created by the Alaska Native Claims Settlement Act (ANCSA) |
| Borough or Census Area Name | string | None | Boroughs are analagous to a county in other places. Census areas are statistical subdivisions of the  the Unorganized Borough, which does not have a government. |
| Grid Name | string | None | The unique grid name, which is based on the primary Alaskan community in the grid |
| Public Use Microdata Area | string | None | Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state or equivalent entity into geographic areas containing no fewer than 100,000 people each. |
| DCRA Economic Region | string | None | Alaska Division of Community and Regional Affairs (DCRA) economic regions were determined based on 2013 borough and census area geography by the Alaska Department of Labor & Workforce Development. |
| PCE Eligibility | boolean | None | Answers the question: Is this community eligible for the Alaska Energy Authority's Power Cost Equalization program? ("t" for yes, and "f" for no) Eligibility is determined by the Regulatory Commission of Alaska under Alaska Statutes 42.45.100-170. |
| Latitude | number | degrees N | Latitude |
| Longitude | number | degrees E | Longitude |

### Comments
> **2025**: 1. Identified data sources and integrated them into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Used spatial joins to crosswalk AEDG communities with other organizations to create this dataset
> 

> **2026-01-12**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

