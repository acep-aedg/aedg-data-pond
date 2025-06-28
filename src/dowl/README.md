# Scripts for files from DOWL (Neil McMahon)

## Data Deliveries

The first data delivery was `Tables_Operators&Plants_2025-03-10.xlsx` in March 2025. It contained only 2 lookup tables, Operator and Plants, and data dictionaries for both - so 4 sheets altogether. It was not stored in GitHub; it is [in Google Drive](https://docs.google.com/spreadsheets/d/1lBdR9TbwQvxDV1LUW2HGDvdd1C5UQ7mq/edit?usp=drive_link&ouid=112418087891577909150&rtpof=true&sd=true), if you have access to that. Information from the data dictionary was transferred to `data/raw/dowl/raw_dowl_data_dictionary.csv`

A second data delivery occurred in April, 2025. `AEDG LOOKUP TABLES_FINAL.xlsx` includes Operator, Plants, Communities, Interties, and Sales. It is stored in this repo in `data/raw/dowl` with CSV files derived from its sheets.

Two additional lookup tables - EIA fuel codes and prime mover codes - were not included in these deliveries. Instead, they were scraped from the Alaska Energy Statistics Workbooks, specifically `Energy_Stats_Generation_Tables.xlsx` posted in [Alaska Energy Statistics, 2011 - 2021](https://acep-uaf.github.io/ak-energy-statistics-2011_2021/).

## Scripts

### operator2.csv.py

This converts each tab in `AEDG LOOKUP TABLES_FINAL.xlsx` to pandas DataFrames and then outputs them to individual CSV files that where then used to generate metadata. Several ID codes in the tables were cast to floats because fields with missing values cannot be integers. But some have leading zeros so might have been better treated as strings. If these data are used in the future, it might be better to work from the original XLSX file.

### codes2csv.py

This splits a single sheet in `Energy_Stats_Generation_Tables.xlsx` into two separate CSV files. Two different types of codes - fuel and prime movers - are together originally in different rows, so to simplify future work, the code counts the rows and splits them.

### interties2grids.py

Neil organized his interties by the grids with communities as a list within a single cell. This did not work well with AEDG, so that cell was split into separate rows for each community

## Initialized

Here's how this directory was initialized

```shell
% uv init
% uv venv
% uv add pandas
% uv uv add openpyxl
% uv sync
% source .venv/bin/activate
```

Then I altered `uv`'s `hello.py` script to become `operators2csv.py`

## Installation and use

`uv sync` will create the `.venv/` directory and it can also include the optional dependencies too.

``` shell
% uv sync --all-extras  # Include all optional dependencies (which there aren't any of).
% source .venv/bin/activate
% python operators2csv.py
```
