#!/bin/bash

# A script to pull generated metadata from its repository and put each in place
# to accompany the data file it describes. Metadata is in the metadata project's
# object store so each file must be accessed individually.
#
# call with `bash pull_metadata.sh`
#
# ELD
# 6/6/2025


repo_root="https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main/metadata"

# Pull metadata for data explorer files in `public`
# URLS like https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main/metadata/public/public_capacity.json
subdir=public
cd data/$subdir
for file in *.csv
   do 
      metadata="${file/.csv/.json}"
      echo "Pulling $metadata"
      wget ${repo_root}/${subdir}/$metadata
done


