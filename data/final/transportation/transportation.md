# Community Transportation Summary

## Description
Summary of the types of transportation available to each community. Includes information on airports, roads, the state ferry, harbors and docks, coastal status, and cargo barge. The price a community pays for energy depends significantly on the transportation options available for fuel and construction materials.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **Path:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/final/transportation/transportation.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/final/transportation/transportation.csv)
* **Publication Date:** 2025-12-15

### Sources
* **Community Transportation Overview** (2024)
  Summary of the types of transportation available to each community. Includes information on airports, roads, the state ferry, harbors and docks, coastal status, and cargo barge. Most communities in Alaska typically have an unmanned general aviation airport of which Alaska DOT P&F owns and operates 237 airports. This data is relatively static.
AEDG uses these data to display transportation options because these greatly influence the prices paid for fuel and other energy sources. Communities who rely only on air freight will likely pay a much higher amount for energy.

* **2024 US Census Place Gazetteer File, Alaska** (2024)
  The U.S. Gazetteer File provide a listing of all geographic areas in Alaska. The files include geographic identifier codes, names, area measurements, and representative latitude and longitude coordinates.
AEDG used to use the ANSI codes in this dataset as an identifier of communities but this was discontinued.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Community FIPS Code | string | None | 5-digit Federal Information Processing Series (FIPS) code identifier for places, assigned and maintained by the Census Bureau |
| Airport | boolean | None | Answers the question: Does the Community have an airport? ("t" for yes, and "f" for no) |
| Harbor Dock | boolean | None | Answers the question: Does the Community have a harbor with a dock? ("t" for yes, and "f" for no) |
| State Ferry | boolean | None | Answers the question: Is the Community served by a state ferry? ("t" for yes, and "f" for no) |
| Cargo Barge | boolean | None | Answers the question: Is the Community served by a cargo barge? ("t" for yes, and "f" for no) |
| Road Connection | boolean | None | Answers the question: Is the Community connected to a road system to other communities? ("t" for yes, and "f" for no) |
| Coastal | boolean | None | Answers the question: Is the Community located on the coast? ("t" for yes, and "f" for no) |
| Road or Ferry | boolean | None | Answers the question: Is the Community served by a state ferry or a road? ("t" for yes, and "f" for no) |
| Description | string | None | Narrative description |
| As of Date | string | None | When the transportation dataset last updated |
