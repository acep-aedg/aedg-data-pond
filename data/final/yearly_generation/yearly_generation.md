# Yearly Electrical Generation by Grid

## Description
This dataset is yearly electrical generation aggregated by grid. It summarizes the amount of electrical power produced for a grid and the fuels that were used to generate it. Two factors complicate this simple seeming dataset. First, there is no single state or federal agency that collects data on all the generation sources in Alaska. Second, some communities have isolated microgrids where generation sources are easy to identify, but other communities are interconnected with interties into grids where generation sources are shared. In those cases, it is therefore impossible to pair a community with individual power stations (called plants) or the operators/utilities for which generation is recorded even if the plant is physically located within a community.
To address the first issue, this dataset derives from the Alaska Energy Statistics workbooks, which in turn compiles data from multiple sources including community Power Cost Equalization reports collated by the Alaska Energy Authority and reporting to the U.S. Energy Information Administration (EIA). Source data was harmonized to account for differences in reporting through a combination of subject matter expertise and transformations.
To address the second issue, generation is summed over all the generators with different fuels - diesel and natural gas boilers, solar installations, wind turbines - that are connected to a grid. Grids were defined as an element of the Alaska Energy Statistics workbooks and implemented with a lookup table that joins them to individual plants. The same values for total generation will be reported for all the communities on a grid.


## Responsible Party
* **Publisher:** Alaska Center for Energy and Power (ACEP) at the University of Alaska Fairbanks (UAF)
* **Funding Agency:** State of Alaska

## Data Lineage
* **Path:** [https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/final/yearly_generation/yearly_generation.csv](https://raw.githubusercontent.com/acep-aedg/aedg-data-pond/refs/heads/main/data/final/yearly_generation/yearly_generation.csv)
* **Publication Date:** 2025-12-15

### Sources
* **Alaska Energy Statistics Electrical Generation Tables** (2024)
  The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. The workbooks were developed to provide community and utility level datasets that support regional and statewide aggregations for use in the 2024 Alaska Electricity Trends Report. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA). These sources are supplemented by annual filings to the Regulatory Commission of Alaska (RCA), village and powerhouse assessments, and direct communications with utilities and hydro/wind program managers.
Additional funding was contributed by Office of Naval Research (ONR) funded Alaska Regional Collaboration for Technology Innovation and Commercialization (ARCTIC) program, the Denali Commission, and the State of Alaska.
AEDG uses this dataset as the best available compilation of electrical generation, incorporating data from multiple sources into a single source.


### Data Dictionary
| Column Name | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| Alaska Energy Authority Plant ID | number | None |  |
| Energy Information Administration Plant ID | number | None |  |
| Net Generation (MWh) | number | MWh | Net electrical generation as Megawatt Hour aggregated by grid |
| Fuel Type Code | string | None | Code indicating generation fuel as defined by the U.S. Energy Information Administration (EIA) |
| Fuel Type | string | None | Generation fuel |
| Year | integer | None | Four digit year as Common Era (CE) for which monthly reported generation was summed |
