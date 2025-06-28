#!/bin/bash

# A script to pull generated metadata from its repository and put each in place
# to accompany the data file it describes. Metadata is in the metadata project's
# object store so each file must be accessed individually.
#
# call with `bash pull_metadata.sh` from the `src` directory.
#
# ELD
# 6/6/2025


repo_root="https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main"

# Pull metadata for data explorer files in `public`
# URLS like https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main/metadata/public/public_capacity.json
subdir=public
cd ../data/$subdir
for file in *.csv
   do 
      metadata="${file/.csv/.json}"
      echo "Pulling $metadata"
      wget -O $metadata ${repo_root}/metadata/${subdir}/$metadata
done

cd ../../src

# Pull metadata to document files in `raw/dowl` (not necessarily for the Data Explorer) - only did this once.
# URLS like https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main/metadata/raw/dowl/lookup_communities_2024-02-23.json
# subdir=raw/dowl
# cd ../data/$subdir
# for file in lookup*.csv
#    do 
#       metadata="${file/.csv/.json}"
#       echo "Pulling $metadata"
#       wget -O $metadata ${repo_root}/metadata/${subdir}/$metadata
# done
# # also, there is a bespoke data dictionary. Get that too.
# wget -O raw_dowl_data_dictionary.csv ${repo_root}/src/registry/raw_dowl_data_dictionary.csv

# cd ../../../src
