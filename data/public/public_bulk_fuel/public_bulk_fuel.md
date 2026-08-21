# Bulk Fuel Facilities

## Description
This dataset derived from the Bulk Fuel Inventory, a list of bulk fuel facilities in Alaska including assessments and tank details provided by the Alaska Energy Authority, the U.S. Coast Guard, and Division of Community and Regional Affairs.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_bulk_fuel/public_bulk_fuel.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_bulk_fuel/public_bulk_fuel.csv)
* **Reference Date:** 2026

### Sources
* **Bulk Fuel Inventory** (2015)
  https://maps.commerce.alaska.gov/server/rest/services/Services/CDO_Utilities/MapServer/48
 A list of bulk fuel facilities in Alaska including photos, assessments, and tank details provided by the Alaska Energy Authority, the U.S. Coast Guard, and Division of Community and Regional Affairs.

* **Bulk Fuel Tanks** (2024)
  https://github.com/acep-aedg/aedg-bulk-fuel/blob/main/data/l0/l0_bulk_fuel_survey.xlsx
 A list of bulk fuel tank details provided by the Alaska Energy Authority.

* **Bulk Fuel Facilities** (2024)
  https://github.com/acep-aedg/aedg-bulk-fuel/blob/main/data/l0/l0_bulk_fuel_survey.xlsx
 A list of bulk fuel facility details provided by the Alaska Energy Authority.

* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Tank Farm ID | string | None |  |
| USCG ID | string | None | Identification number given by United States Coast Guard |
| Alaska Energy Authority ID | string | None | Identification number given by Alaska Energy Authority |
| Entity Name | string | None |  |
| Number of Tanks | number | None | Number of tanks in the facility |
| Total Capacity | number | gallons | Total capacity of tank farm |
| Gasoline Capacity | number | gallons | Capacity of gasoline in gallons |
| Diesel Capacity | number | gallons | Capacity of diesel in gallons |
| Aviation Gas Capacity | number | gallons | Capacity of aviation gas (avgas) in gallons |
| Jet Fuel Capacity | number | gallons | Capacity of jet fuel in gallons |
| Other Fuel Capacity | number | gallons | Capacity of other fuel (non diesel; jet fuel; gasoline; or avgas) in gallons |
| Barge Delivery | boolean | None | Does this community receive fuel via barge? |
| Plane Delivery | boolean | None | Does this community receive fuel via airplane? |
| Road Delivery | boolean | None | Does this community recieve fuel via road? |
| Inspected by USCG | boolean | None | Is this facility inspected by United States Coast Guard? |
| Fuel Supplier | string | None |  |
| Recommendations by AEA | string | None |  |
| Distance to Barge Mooring | number | None |  |
| Tank Farm Evaluation ID | string | None |  |
| Source | string | None | Source of data |
| Report | string | None | Title, type, or classification of the source document or reference report associated with the record |
| Start Year | integer | None | Beginning of the data collection period |
| End Year | integer | None | End of the data collection period |
| Latitude | number | degrees N | Latitude |
| Longitude | number | degrees E | Longitude |

### Comments
> **2025**: 1. Identified data source and integrated it into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Joined bulk fuel, bulk fuel tanks and bulk fuel facilities with AEDG communities to create this dataset.
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

