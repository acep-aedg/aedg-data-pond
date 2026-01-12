# Taxes for Communities and Boroughs

## Description
Sales, property, and special tax revenue for communities and boroughs, 2017-2024.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_taxes/public_taxes.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_taxes/public_taxes.csv)
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

* **Taxes, All Locations** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Economics_Related/Economics_Taxes/MapServer/0
 This dataset is a summary of property and sales taxes assessed at both the community and borough levels from 2015 to present. Note from DCRA on use for analysis: This data set mixes scale. It includes rows for boroughs, which contain multiple census designated places (CDP's) and cities from this same data set in many cases. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data.
AEDG includes tax data as a measure of economic activity. From our analysis, this tax data for "All Locations" includes records/rows for both individual cities and boroughs. The tax revenue values for a city are not included in the borough the city is geographically part of. For example, in 2023 the city of Fairbanks reported $4,279,586.00 in bed tax revenue but the Fairbanks North Star borough only reported $2,933,702.00 in bed tax revenue. When providing tax data for a borough as a geographic whole using this dataset, both the borough and any individual city listed separate from the borough but within the physical bounds of the borough will need to be aggregated.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Tax Year | integer | None | Four digit tax year as Common Era (CE) |
| Total Tax Revenue | integer | USD | Total tax revenue in U.S. Dollars (USD) for either the community or the borough |
| Total Sales Tax Revenue | integer | USD | Total sales tax revenue in U.S. Dollars (USD) for either the community or the borough |
| Property Tax Revenue | integer | USD | Propery tax revenue in U.S. Dollars (USD) for either the community or the borough |
| Total Special Tax Revenue | integer | USD | Total special tax revenue in U.S. Dollars (USD) for either the community or the borough |
| Community Report | boolean | USD | Answers the question: Did the community report these taxes?  ("t" for yes, and "f" for no) |
| Most Recent Taxes | boolean | USD | Answers the question: Are these the most recent values for these taxes?  ("t" for yes, and "f" for no) |

### Comments
> **2025**: 1. Identified data source and integrated it into the data pipeline.
> 2. Complied community names, locations, and FIPS identifiers for AEDG
> 3. Joined tax data with AEDG communities to create this dataset
> 

> **2026-01-12**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

