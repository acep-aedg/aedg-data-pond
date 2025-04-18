"""Script to read Operators and Plants from Excel file and write to CSV files

source .venv/bin/activate 
python operators2csv.py

2025-04-17 updated to use "FINAL" workbook which had more tabs (Communities and Sales
Reporting) but the same data for Operators and Plants (and Interties) 
"""

from pathlib import Path

import pandas as pd

def main():
    print("Hello from dowl!")

    filename = "AEDG LOOKUP TABLES_FINAL.xlsx"
    data_dir = Path(__file__).parents[2] / "data" / "raw" / "dowl"
    sheets = {
        "LOOKUP Communities": "lookup_communities_2024-02-23.csv",
        "LOOKUP INTERTIES 2024-02-23": "lookup_interties_2024-02-23.csv",
        "LOOKUP OPERATOR 2025-03-07": "lookup_operator_2025-03-07.csv",
        "LOOKUP PLANTS 2025-03-10": "lookup_plants_2025-03-10.csv",
        "LOOKUP SalesReport 2025-03-03": "lookup_salesreport_2025-03-03.csv",
    }
    # standardize column names
    renames ={
        # Operator
        "AK_operator Id": "ak_operator_id",
        "PCE_utility_code": "pce_utility_code",	
        "CPCN": "rca_cpcn",
        "Operator_name": "operator_name",
        "EIA_sector__name": "eia_sector_name",
        "EIA_sector__number": "eia_sector_number", # we don't know what this is
        "operator__utility_type_name": "operator_utility_type_name",
        "Power Generation End Use": "power_generation_end_use",
        # Plants
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
        "Longitude": "longitude",
        "Notes": "notes",
        # Sales
        "Sales Reporting ID": "sales_reporting_id",
        "Reporting Name": "reporting_name",
        "OPERATOR_AK-OP Operator ID": "operator_ak_operator_id",
        "OPERATOR_EIA operator Number": "eia_operator_id",	
        "OPERATOR_PCE Reporting ID": "pce_reporting_id",
        "OPERATOR_RCA CPCN": "rca_cpcn",
        "OPERATOR_Operator Name": "operator_operator_name",
        "Index Community": "index_community",
        "GNIS": "gnis_feature_id",
        "Communities reported": "communities_reported",
        # Interties
        'Intertie Unique ID Name': 'intertie_unique_id_name', 
        'Current ID': 'current_id',
        'Communities Intertied': 'communities_intertied', 
        'Month of interite': 'month_of_intertie', 
        'Year of intertie': 'year_of_intertie',
        'AEA energy region': 'aea_energy_region', 
        'Source': 'source',
        # Communities - most have right format
        "PCE ID": "pce_reporting_id",
        "census_area__id": "census_area_id",
        "census_area__census_code": "census_area_census_code",
        "census_area__county_code": "census_area_county_code",
        "census_area__gnis_feature_id": "census_area_gnis_feature_id",
        "census_area__historical": "census_area_historical",
        "census_area__name": "census_area_name",
        "census_area__notes": "census_area_notes",
        "aea_energy_region__id": "aea_energy_region_id",
        "aea_energy_region__name": "aea_energy_region",
        "alaska_native_regional_corporation__id": "alaska_native_regional_corporation_id",
        "alaska_native_regional_corporation__name": "alaska_native_regional_corporation_name",
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

        # for the data dictionary
        for col in df.columns:
            print(col, outname)


if __name__ == "__main__":
    main()
