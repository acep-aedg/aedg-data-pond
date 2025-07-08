# Lookup tables for Alaska Energy Statistics (Neil McMahon, DOWL)

The Alaska Energy Statistics is a long-running collection of data and reports about energy production, consumption, and related topics specific to the state of Alaska. This is a continuation of a 40+ year effort to create and maintain high level views of the state’s energy profile that are useful for policy makers, businesses, researchers, and others interested in Alaska’s energy sector. Data are derived from community Power Cost Equalization (PCE) reports collated by the Alaska Energy Authority and power plant reporting to the U.S. Energy Information Administration (EIA).

The most recent version of Alaska Energy Statistics was produced by Neil McMahon, DOWL, under contract to the Alaska Center for Energy and Power (ACEP), University of Alaska Fairbanks. The resulting datasets are posted at [Alaska Energy Statistics, 2011 - 2021](https://acep-uaf.github.io/ak-energy-statistics-2011_2021/) and displayed in the [2024 Alaska Electricity Trends Report](https://acep-uaf.github.io/aetr-web-book-2024/). In order to connect EIA and PCE data, Neil developed a series of lookup tables that cross-references the codes these two datasets use to refer to power plants and to connect communities into grids. In 2025, ACEP asked Neil to create an update to these tables in preparation for the next generation of Alaska Energy Statistics.

## Data Deliveries

The first data delivery was `Tables_Operators&Plants_2025-03-10.xlsx` in March 2025. It contained only 2 lookup tables, Operator and Plants, and data dictionaries for both - so 4 sheets altogether. It was not stored in GitHub; it is [in Google Drive](https://docs.google.com/spreadsheets/d/1lBdR9TbwQvxDV1LUW2HGDvdd1C5UQ7mq/edit?usp=drive_link&ouid=112418087891577909150&rtpof=true&sd=true), if you have access to that. Information from the data dictionary was transferred to `raw_dowl_data_dictionary.csv`

A second data delivery occurred in April, 2025. `AEDG LOOKUP TABLES_FINAL.xlsx` includes Operator, Plants, Communities, Interties, and Sales. It is stored here in this repo with CSV files derived from its sheets.

Two additional lookup tables - EIA fuel codes and prime mover codes - were not included in these deliveries. Instead, they were scraped from the Alaska Energy Statistics Workbooks, specifically `Energy_Stats_Generation_Tables.xlsx` posted in [Alaska Energy Statistics, 2011 - 2021](https://acep-uaf.github.io/ak-energy-statistics-2011_2021/).

## Data Processing

Python scripts using pandas were developed in `src/dowl` to create individual CSV files from the incoming Excel workbooks. The results of this were mixed because many of the IDs in the sheets are integers or integers with leading zeros. The missing data in these columns caused these numbers to convert to floats. With more time to fine-tune the code, this problem could have been avoided.

The CSV files became the basis for the accompanying metadata. Those files were generated using the [AEDG metadata generator](https://github.com/acep-aedg/aedg-metadata/tree/main).
