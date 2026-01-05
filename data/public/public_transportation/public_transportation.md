# Community Transportation Summary

## Description
Summary of the types of transportation available to each community. Includes information on airports, roads, the state ferry, harbors and docks, coastal status, and cargo barge. The price a community pays for energy depends significantly on the transportation options available for fuel and construction materials.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **Path:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_transportation/public_transportation.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_transportation/public_transportation.csv)
* **Publication Date:** 2025-12-15

### Sources
* **Places (Cities and CDPs) Shapefile** (2020)
  This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Community Transportation Overview** (2024)
  Summary of the types of transportation available to each community. Includes information on airports, roads, the state ferry, harbors and docks, coastal status, and cargo barge. Most communities in Alaska typically have an unmanned general aviation airport of which Alaska DOT P&F owns and operates 237 airports. This data is relatively static.
AEDG uses these data to display transportation options because these greatly influence the prices paid for fuel and other energy sources. Communities who rely only on air freight will likely pay a much higher amount for energy.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Airport | boolean | None | Answers the question: Does the Community have an airport? ("t" for yes, and "f" for no) |
| Harbor Dock | boolean | None | Answers the question: Does the Community have a harbor with a dock? ("t" for yes, and "f" for no) |
| State Ferry | boolean | None | Answers the question: Is the Community served by a state ferry? ("t" for yes, and "f" for no) |
| Cargo Barge | boolean | None | Answers the question: Is the Community served by a cargo barge? ("t" for yes, and "f" for no) |
| Road Connection | boolean | None | Answers the question: Is the Community connected to a road system to other communities? ("t" for yes, and "f" for no) |
| Coastal | boolean | None | Answers the question: Is the Community located on the coast? ("t" for yes, and "f" for no) |
| Road or Ferry | boolean | None | Answers the question: Is the Community served by a state ferry or a road? ("t" for yes, and "f" for no) |
| Description | string | None | Narrative description |
