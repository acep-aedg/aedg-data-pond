# Community Fuel Prices

## Description
Heating fuel oil and gasoline prices for Alaskan communities are a composite of three distinct datasets. The best data is for 100 communities that have been directly surveyed by the Alaska Division of Community and Regional Affairs (DCRA) since 2005. To cover communities not surveyed, DCRA computes regional averages over their economic regions, which AEDG associates with every community within that region. DCRA's survey intentionally omits the urban area of Anchorage because that area is separately surveyed by the Consumer Price Index of the U. S. Bureau of Labor Statistics (BLS). These three sources are combined into this summary dataset.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_fuel_prices/public_fuel_prices.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_fuel_prices/public_fuel_prices.csv)
* **Reference Date:** 2025-01-01

### Sources
* **Places (Cities and CDPs) Shapefile** (2020)
  https://live.laborstats.alaska.gov/article/maps-gis-data
 This is an ESRI Shapefile for use in GIS software that contains place data from the 2020 US Census for Alaska. The definition of places includes all incorporated cities as well as Census Designated Places (CDPs). Each geographic unit is identified using Federal Information Processing Standards (FIPS) numbers. Coordinate System: North American Datum 1983 Alaska Albers. Source: 2020 US Census, PL94-171 Redistricting File; 2020 US Census Tiger Shapefiles. Documentation of field names: https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.pdf. The Alaska Department of Labor and Workforce Development has had a cooperative agreement with the U.S. Census Bureau since 1981 to assist with geographic programs and help Alaskans find Census Bureau data.
AEDG uses this list to define canonical community locations to use in spatial joins and relations, to associate places with FIPS codes, and to establish total community population.

* **Alaska Communities** (2023)
  https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0
 The Alaska Communities dataset is the reference list of place locations, represented as points, used by the Alaska Division of Community and Regional Affairs (DCRA). In includes community locations but for historical reasons, it is a mix of Communities, Places of Interest, Borough/Census Area as well as Alaska centroid. DCRA uses it to link communities to their internal key GUID used elsewhere in their systems.
AEDG uses this list to define canonical community names since, as free text, these can vary in different contexts, and to establish locations to use in spatial joins and relations.

* **Community Survey of Heating Fuel Prices** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Services/CDO_Utilities/MapServer/61
 Beginning in 2005, the Division of Community and Regional Affairs began collecting prices of heating fuel and unleaded gasoline in 100 select communities. When the survey was established, the national AAA fuel survey only reported Anchorage and Mat-Su pricing so these areas were deliberately excluded from the 100 select communities. The communities have remained constant since the project’s inception. The prices for heating fuel in these 100 communities are collected via a telephone survey of each fuel retailer. Survey methodology has evolved over time; however, the reported prices should be considered representative of what a community resident would have paid for a gallon of heating fuel (including tax) on the day of contact.
AEDG uses this dataset to provide the best heating fuel prices available for the selected communities, and relies on other data sets to fill in communities that are not included in the survey.

* **Regional Gas and Heating Fuel Prices** (2025)
  https://maps.commerce.alaska.gov/server/rest/services/Services/CDO_Utilities/MapServer/45
 This data set is heating fuel and gasoline prices recorded by the Alaska Division of Community and Regional Affairs (DCRA) through their semiannual survey of 100 Alaskan communities; in this data set, surveyed prices are summarized by DCRA's economic regions. Regional price is the average of the prices of all the surveyed communities within that region, as described in page 4 of Alaska Fuel Price Report: Winter 2025, https://storymaps.arcgis.com/stories/6d6a33a3d9a74723a2f476c26ecfdf21. 
AEDG uses this dataset to provide gasoline and heating fuel prices available for communities not included in the DCRA survey.

* **Consumer Price Index Average Price Data** (2024)
  https://data.bls.gov/timeseries/APUS49G7471A?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true
 The Consumer Price Index (CPI) is a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services. Indexes are available for the U.S. and various geographic areas. Average price data for select utility, automotive fuel, and food items are also available. This dataset is Gasoline, all types, per gallon/3.785 liters in Urban Alaska, average price, not seasonally adjusted.
AEDG uses this dataset to provide the price of gasoline in Anchorage.

* **Alaska Economic Regions** (2024)
  https://maps.commerce.alaska.gov/server/rest/services/Boundaries/CDO_Economic_Regions/MapServer/0
 Alaska economic regions based on 2013 borough and census area geography. Boundaries are determined by the Alaska Department of Labor & Workforce Development. For more information, see Alaska Department of Labor Maps & GIS. This data has been visualized in a Geographic Information Systems (GIS) format and is provided as a service in the DCRA Information Portal by the Alaska Department of Commerce, Community, and Economic Development Division of Community and Regional Affairs (SOA DCCED DCRA), Research and Analysis section. SOA DCCED DCRA Research and Analysis is not the authoritative source for this data. For more information and for questions about this data, see: Alaska Local and Regional Information
AEDG uses this dataset to add the economic region spatial polygon to Anchorage gas prices.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places and boroughs (counties), assigned and maintained by the Census Bureau |
| Community Name | string | None | Name of the community |
| Fuel Price USD | number | USD/gal | Retail price of fuel, expressed as U. S. Dollars (USD) per gallon. Prices are "point in time" as reported by local vendors and contacts. |
| Fuel Type | string | None | Name of fuel type reported, either heating fuel or gasoline |
| Price Type | string | None | Type of source data for assigning price: survey of communities or regional average |
| Source of Fuel Price Data | string | None | Name of reporting entity if surveyed, or DCRA if regionally averaged |
| Reporting Season | string | None | Season for which the fuel data was reported, Winter or Summer |
| Reporting Year | integer | None | Four digit year as Common Era (CE) for which the fuel data was reported |

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

