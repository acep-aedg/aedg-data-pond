"""Script to read Prime Mover and Fuel Type codes from workbook Excel file and write to CSV file

source .venv/bin/activate 
python codes2csv.py
"""

from pathlib import Path

import pandas as pd

def main():
    print("Hello from dowl!")

    url = "https://github.com/acep-uaf/ak-energy-statistics-2011_2021/raw/refs/heads/main/workbooks/Energy_Stats_Generation_Tables.xlsx"
    # alternate name: url = "/Users/eldobbins/Desktop/projects/energy stats/Stats data gen fin infr sent 2025/Energy Stats--Generation Tables.xlsx"
    data_dir = Path(__file__).parents[2] / "data" / "raw" / "dowl"
    sheet = "LOOKUP Code tables"


    # first half of the table is prime mover. 
    outname = "lookup_primemover_2023-11-08.csv"
    df = pd.read_excel(
        url, 
        sheet_name="LOOKUP Code tables", 
        names=['prime_mover_code', 'prime_mover_definition']
    )
    # identify where the first table ends
    mover_end = df.index[df["prime_mover_code"] == "Reported Fuel Type Code"].values[0]
    df = df.iloc[:mover_end]
    # stript the whitespace from the first column
    df['prime_mover_code'] = df['prime_mover_code'].str.strip()
    # write
    df.to_csv(
        data_dir / outname,
        index=False
    )


    # second half of the table is fuel codes
    outname = "lookup_fuelcode_2023-11-08.csv"
    df = pd.read_excel(
        url, 
        sheet_name="LOOKUP Code tables", 
        names=['fuel_type_code', 'fuel_type_definition'],
        skiprows=mover_end+1
    )
    # stript the whitespace from the first column
    df['fuel_type_code'] = df['fuel_type_code'].str.strip()
    # write
    df.to_csv(
        data_dir / outname,
        index=False
    )
    
    print('Fuel codes:')
    print(df)

if __name__ == "__main__":
    main()
