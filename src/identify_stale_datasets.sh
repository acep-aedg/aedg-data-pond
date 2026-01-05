#!/bin/bash

# default stale threshold to 2023
THRESHOLD=${1:-2023}
OUTPUT_FILE="registry/stale_datasets.md"
METADATA_FILES=$(find "data" -type f -name "*.json")

# clear output file
: > "$OUTPUT_FILE"

echo ""
echo "Finding stale data using $THRESHOLD as staleness threshold"

for METADATA_FILE in $METADATA_FILES; do
    # dig in the JSON for referenceDate, extract year, extract basename
    DATE=$(jq -r '.resources[0].temporal.referenceDate' "$METADATA_FILE" 2>/dev/null)
    YEAR=${DATE:0:4}
    FILE=$(basename $METADATA_FILE .json)

    # check year is numeric, write to file if over stale threshold
    if [[ "$YEAR" =~ ^[0-9]{4}$ ]]; then
        if ((YEAR < THRESHOLD)); then
            echo -e "\t$FILE is stale ($YEAR)"
            echo "$FILE $YEAR" >> $OUTPUT_FILE
        fi
    fi

done
