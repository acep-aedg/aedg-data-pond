rm ./data/raw/*.csv
rm ./data/raw/*.geojson

rm ./data/intermediate/*.csv
rm ./data/intermediate/*.geojson

rm ./data/final/*.csv
rm ./data/final/*.geojson


# # # GeoJSONs

# communities
ogr2ogr -f "GeoJSON" ./data/final/communities.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l3_communities"

# regional_corporations
ogr2ogr -f "GeoJSON" ./data/final/regional_corporations.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_regional_corporations"

# village_corporations
ogr2ogr -f "GeoJSON" ./data/final/village_corporations.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_village_corporations"

# boroughs
ogr2ogr -f "GeoJSON" ./data/final/boroughs.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_boroughs"

# house_districts
ogr2ogr -f "GeoJSON" ./data/final/house_districts.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_house_districts"

# senate_districts
ogr2ogr -f "GeoJSON" ./data/final/senate_districts.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_senate_districts"

# places
ogr2ogr -f "GeoJSON" ./data/final/places.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l2_places"

# pumas
ogr2ogr -f "GeoJSON" ./data/final/pumas.geojson PG:"host=$PG_HOST user=$PG_USER dbname=$PG_DB" -sql "SELECT * FROM l1_pumas"





# # CSVs

# populations_ages_sexes
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY l2_populations_ages_sexes TO ./data/final/populations_ages_sexes.csv DELIMITER ',' CSV HEADER;"

# populations
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY l2_populations TO ./data/final/populations.csv DELIMITER ',' CSV HEADER;"

# transportation
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY l2_transportation TO ./data/final/transportation.csv DELIMITER ',' CSV HEADER;"

# employment
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY l2_employment TO ./data/final/employment.csv DELIMITER ',' CSV HEADER;"

# taxes
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY l2_taxes TO ./data/final/taxes.csv DELIMITER ',' CSV HEADER;"



# # relations

# # communities_districts (RENAME communities_legislative_districts)
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY communities_legislative_districts TO ./data/final/communities_legislative_districts.csv DELIMITER ',' CSV HEADER;"

# communities_school_districts
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY communities_school_districts TO ./data/final/communities_school_districts.csv DELIMITER ',' CSV HEADER;"



# # # views
# example communities generation
psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DB" -c "\COPY (SELECT * FROM example_communities_generation) TO ~/Desktop/example_communities_generation.csv DELIMITER ',' CSV HEADER;"