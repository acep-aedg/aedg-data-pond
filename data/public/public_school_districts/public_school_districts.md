# School Districts

## Description
This dataset provides geographic boundary polygons and attribute data for Alaska's public school districts. It pairs spatial coordinates with key administrative metadata, including district names, unique record IDs, governance types (such as Borough or REAA), and operational status flags.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **URL:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_school_districts/public_school_districts.geojson](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/public/public_school_districts/public_school_districts.geojson)
* **Reference Date:** 2022-11-03

### Sources
* **School Districts and REAAs** (2022)
  https://maps.commerce.alaska.gov/server/rest/services/Education_Related/School_Districts_and_REAAs/MapServer/0
 This dataset describes Alaska school district boundaries and addresses. Each school district boundary (geometry, not attributes) is derived from one of three sources. 1. Borough and Census Area Boundaries (as a proxy for school districts in the organized borough). 2. Regional Educational Attendance Area Boundaries (school districts in the unorganized borough). A Regional Educational Attendance Area (REAA) is an educational area that is established in an unorganized borough of the state established by AS 14.08.031(a). REAA elections administered by the Division of Elections. This dataset is revised for recasting of REAA sections using 2020 Census data. The 2020 version is the first time REAA boundaries were fully created using Geographic Information System (GIS) technology. 3. City Boundaries - Boundaries are based on the actual certificates issued by the Local Boundary Commission. For more information, see https://education.alaska.gov/DOE_Rolodex/SchoolCalendar/DistrictAndSchoolInfo/DistrictDetails
AEDG includes information on school districts because in smaller communities, schools are often the dominant consumer of energy.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| ID | string | None | School district ID |
| Is Active | boolean | None | If the district is active or not |
| Name | string | None | Official school district name |
| Notes | string | None | Additional notes about the record |
| Type | string | None | Administrative governance type |

### Comments
> **2025**: Identified data source and integrated it into the data pipeline.
> 

> **2026**: Documented sources and defined the data dictionary using OEMetadata (Frictionless) formatted metadata https://doi.org/10.5281/zenodo.15019561.
> 

## License
CC-BY-4.0
Creative Commons Attribution 4.0 International
https://creativecommons.org/licenses/by/4.0/

