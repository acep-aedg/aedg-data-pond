#!/bin/bash

# A script to pull generated metadata from its repository and put each in place
# to accompany the data file it describes. Metadata is in the metadata project's
# object store so each file must be accessed individually.
#
# call with `bash pull_metadata.sh` from the `src` directory.
#
# ELD
# 6/6/2025


repo_root="https://github.com/acep-aedg/aedg-metadata/raw/refs/heads/main"

# Pull metadata for data explorer files in `public`
# URLS like https://raw.githubusercontent.com/acep-aedg/aedg-metadata/refs/heads/main/metadata/public/public_capacity.json

subdir=public

for file in data/$subdir/*.csv; do
  [ -e "$file" ] || continue

  base="${file##*/}"                     
  metadata="${base%.csv}.json"           
  url="$repo_root/metadata/$subdir/$metadata"
  out="data/$metadata"

  if wget -q -O "$out" "$url"; then
    printf '%s: Success\n' "${base%.csv}"
  else
    rc=$?
    printf >&2 '%s: Error (wget exit %d) — %s\n' "$metadata" "$rc" "$url"
  fi
done
