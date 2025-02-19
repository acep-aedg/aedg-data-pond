#!/bin/bash

# Start Time
start_time=$(date +%s.%N)


# Set PostgreSQL credentials and target database name (password stored in .pgpass)
export PG_HOST="localhost"      
export PG_PORT="5432"           
export PG_USER="aedg_read_only"     
export PG_DB="aedg_db"    # Database name to delete tables from

# Ensure the .pgpass file exists and has correct permissions
if [ ! -f "$HOME/.pgpass" ]; then
  echo "Error: .pgpass file not found in your home directory."
  exit 1
fi




# # run data dump script
source ./src/file_dump.sh
 





# End time
end_time=$(date +%s.%N)
# Elapsed time
elapsed_time=$(echo "$end_time - $start_time" | bc)

echo "Execution time: $elapsed_time seconds"