# Electricity Rates for Communities

## Description
This dataset is sales by communities as they are recorded by reporting entities (i.e. utilities). There is no single state or federal agency that collects data on all utility sales in Alaska.
This dataset derives from the Alaska Energy Statistics workbooks, which in turn compiles data from multiple sources including community Power Cost Equalization reports collated by the Alaska Energy Authority and reporting to the U.S. Energy Information Administration (EIA). Source data was harmonized to account for differences in reporting through a combination of subject matter expertise and transformations.
To address the second issue, ... The same values for sales are reported for all the communities served by the reporting entity [even for AVEC?], which creates multiple duplicate values in this dataset.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **Path:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_rates/public_rates.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_rates/public_rates.csv)
* **Publication Date:** 2025-12-22

### Sources
* **Alaska Communities** (2023)
  The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Places (Cities and CDPs) Shapefile** (2020)
  This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Energy Statistics Financial Tables** (2024)
  The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. The workbooks were developed to provide community and utility level datasets that support regional and statewide aggregations for use in the 2024 Alaska Electricity Trends Report. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA). These sources are supplemented by annual filings to the Regulatory Commission of Alaska (RCA), village and powerhouse assessments, and direct communications with utilities and hydro/wind program managers.
Additional funding was contributed by Office of Naval Research (ONR) funded Alaska Regional Collaboration for Technology Innovation and Commercialization (ARCTIC) program, the Denali Commission, and the State of Alaska.
AEDG uses this dataset as the best available compilation of electricity sales, incorporating data from multiple sources into a single source.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Reporting Entity | string | None | The name of the electric service area providing electricity to the community |
| Residential Rate | number | USD//kWh | Price of electricity as US dollars per killowatt hour for residential customers |
| Commercial Rate | number | USD//kWh | Price of electricity as US dollars per killowatt hour for commercial customers |
| Industrial Rate | number | USD//kWh | Price of electricity as US dollars per killowatt hour for industrial customers |
| Year | integer | None | Four digit year as Common Era (CE) |
