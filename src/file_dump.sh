#!/bin/bash

# Define an array of directories and file types to remove
declare -a dirs=("raw" "intermediate" "final" "public")
declare -a types=("csv" "geojson")

# Remove files
for dir in "${dirs[@]}"; do
  for type in "${types[@]}"; do
    rm ./data/$dir/*.$type
  done
done

# Function to convert Postgres table to GeoJSON
export_to_geojson() {
  local output_dir=$1
  local filename=$2
  local table_name=$3
  ogr2ogr -f "GeoJSON" ./data/$output_dir/$filename.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM $table_name"
}

# Convert tables to GeoJSON
export_to_geojson "final" "communities" "l4_communities"
export_to_geojson "final" "regional_corporations" "l2_regional_corporations"
export_to_geojson "final" "boroughs" "l2_boroughs"
export_to_geojson "final" "house_districts" "l2_house_districts"
export_to_geojson "final" "senate_districts" "l2_senate_districts"
export_to_geojson "intermediate" "pumas" "l2_pumas"

# Function to export Postgres table to CSV
export_to_csv() {
  local output_dir=$1
  local filename=$2
  local table_name=$3
  psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY $table_name TO ./data/$output_dir/$filename.csv DELIMITER ',' CSV HEADER;"
}

# Export tables to CSV
export_to_csv "final" "fuel_prices" "l3_fuel_prices"
export_to_csv "final" "populations_ages_sexes" "l2_populations_ages_sexes" 
export_to_csv "final" "populations" "l2_populations" 
export_to_csv "final" "transportation" "l2_transportation" 
export_to_csv "final" "employment" "l2_employment" 
export_to_csv "final" "taxes" "l2_taxes"
export_to_csv "final" "yearly_generation" "l2_es_yearly_generation"
export_to_csv "final" "monthly_generation" "l2_es_monthly_generation" 
export_to_csv "final" "capacity" "l2_es_capacity" 
export_to_csv "final" "grids" "l2_grids" 
export_to_csv "final" "communities_legislative_districts" "communities_legislative_districts" 
export_to_csv "final" "communities_school_districts" "communities_school_districts" 
export_to_csv "final" "communities_grids" "l2_communities_grids" 
export_to_csv "final" "reporting_entities" "l2_reporting_entities"
export_to_csv "final" "electric_rates" "l2_electric_rates"
export_to_csv "final" "sales" "l3_es_annual_sales"

export_to_csv "intermediate" "lookup_rca_electric_certificates" "lookup_rca_electric_certificates" 

# Export de-normalized views for public consumption (note: views are special, need the SELECT * query nested in the COPY command)
export_to_csv "public" "public_capacity" "(SELECT * FROM public_capacity)"
export_to_csv "public" "public_communities" "(SELECT * FROM public_communities)"
export_to_csv "public" "public_employment" "(SELECT * FROM public_employment)"
export_to_csv "public" "public_fuel_prices" "(SELECT * FROM public_fuel_prices)"
export_to_csv "public" "public_monthly_generation" "(SELECT * FROM public_monthly_generation)"
export_to_csv "public" "public_populations_ages_sexes" "(SELECT * FROM public_populations_ages_sexes)"
export_to_csv "public" "public_rates" "(SELECT * FROM public_rates)"
export_to_csv "public" "public_taxes" "(SELECT * FROM public_taxes)"
export_to_csv "public" "public_transportation" "(SELECT * FROM public_transportation)"
export_to_csv "public" "public_yearly_generation" "(SELECT * FROM public_yearly_generation)"
