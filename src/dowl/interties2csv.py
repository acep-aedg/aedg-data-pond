"""Quickie script to read Grids from workbook Excel file and write to CSV file

source .venv/bin/activate 
python grids2csv.py
"""

from pathlib import Path

import pandas as pd

def main():
    print("Hello from dowl!")

    url = "https://github.com/acep-uaf/ak-energy-statistics-2011_2021/raw/refs/heads/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx"
    data_dir = Path(__file__).parents[2] / "data" / "raw" / "dowl"
    sheets = {
        "LOOKUP INTERTIES 2023-11-08": "lookup_interties_2023-11-08.csv"
    }
    # standardize column names
    renames ={
        'Intertie Unique ID Name': 'intertie_unique_id_name', 
        'Current ID': 'current_id',
        'Communities Intertied': 'communities_intertied', 
        'Month of interite': 'month_of_intertie', 
        'Year of intertie': 'year_of_intertie',
        'AEA energy region': 'aea_energy_region', 
        'Source': 'source'
    }
    
    # operators
    for sheet, outname in sheets.items():

        # read
        df = pd.read_excel(
            url,
            sheet_name=sheet
        )

        # clean
        df.rename(columns=renames, inplace=True)

        # write
        df.to_csv(
            data_dir / outname,
            index=False
        )

if __name__ == "__main__":
    main()
