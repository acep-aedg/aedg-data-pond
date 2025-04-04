"""Quickie script to read Operators and Plants from Excel file and write to CSV files

source .venv/bin/activate 
python operators2csv.py
"""

from pathlib import Path

import pandas as pd

def main():
    print("Hello from dowl!")

    filename = "Tables_Operators&Plants_2025-03-10.xlsx"
    data_dir = Path(__file__).parents[2] / "data" / "raw" / "dowl"
    sheets = {
        "LOOKUP OPERATOR 2025-03-07": "lookup_operator_2025-03-07.csv",
        "LOOKUP PLANTS 2025-03-10": "lookup_plants_2025-03-10.csv"
    }
    # standardize column names
    renames ={
        "AK_operator Id": "ak_operator_id",
        "PCE_utility_code": "pce_utility_code",	
        "CPCN": "cpcn",
        "Operator_name": "operator_name",
        "EIA_sector__name": "eia_sector_name",
        "EIA_sector__number": "eia_sector_number", # we don't know what this is
        "operator__utility_type_name": "operator_utility_type_name",
        "Power Generation End Use": "power_generation_end_use",
        "AK Plant ID": "ak_plant_id",
        "PCE reporting ID": "pce_reporting_id",
        "OPERATOR_AK_operator Id": "operator_ak_operator_id",
        "OPERATOR_Operator_name": "operator_operator_name",
        "INTERTIE_Current Intertie ID": "intertie_current_intertie_id",
        "INTERTIE_Current Intertie name": "intertie_current_intertie_name",
        "Grid Primary voltage (kV)": "grid_primary_voltage_kv",
        "Grid Primary voltage 2 (kV)": "grid_primary_voltage2_kv",
        "Phases": "phases",
        "Latitude": "latitude",
        "Notes": "notes"
    }
    
    # operators
    for sheet, outname in sheets.items():

        # read
        df = pd.read_excel(
            data_dir / filename,
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
