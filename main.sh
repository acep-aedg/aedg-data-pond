#!/bin/bash

# Start Time
start_time=$(date +%s.%N)


# Set PostgreSQL credentials and target database name (password stored in .pgpass)
export PG_HOST="localhost"      
export PG_PORT="5432"           
export PG_USER="aedg"     
export PG_DB="aedg_etl_dev"    # Database name to delete tables from

# Ensure the .pgpass file exists and has correct permissions
if [ ! -f "$HOME/.pgpass" ]; then
  echo "Error: .pgpass file not found in your home directory."
  exit 1
fi


# Define an array of directories and file types to remove
declare -a dirs=("intermediate" "final" "public")
declare -a types=("csv" "geojson" "json")

# Remove files
for dir in "${dirs[@]}"; do
  for type in "${types[@]}"; do
    rm ./data/$dir/*/*.$type
  done
done


# run data dump script
source ./src/file_dump.sh
 
# run metadata pull script
source ./src/pull_metadata.sh




# End time
end_time=$(date +%s.%N)
# Elapsed time
elapsed_time=$(echo "$end_time - $start_time" | bc)

echo "Execution time: $elapsed_time seconds"