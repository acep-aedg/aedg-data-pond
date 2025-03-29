# Scripts for files from DOWL (Neil McMahon)

## operator2.csv.py

Script to convert the March 2025 delivery of Operator and Plant tables from
Neil's Excel workbook to separate CSV files.

The incoming file is stored locally on Liz's drive and not uploaded to GitHub because it is a binary file. It contains 2 lookup tables and data dictionaries for both - so 4 sheets altogether. (It is also stashed in the AEDG Google Drive under "AEDG Data")

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
