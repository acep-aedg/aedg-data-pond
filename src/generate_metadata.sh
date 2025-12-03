#!/bin/bash

SOURCE_DIR_PATH=~/repos/aedg-etl-2024/data-sources
CONFIG=src/generate_metadata.yml

DATASETS=$(yq ".datasets | keys | .[]" $CONFIG)

for DATASET in $DATASETS; do
    DATA_PATH=$(yq ".datasets.$DATASET.data_path" $CONFIG)
    DATA_DICTIONARY=$(yq ".datasets.$DATASET.data_dictionary // \"fields.csv\"" $CONFIG)
    BBOX=$(yq ".datasets.$DATASET.bbox" $CONFIG)
    TIME=$(yq ".datasets.$DATASET.time" $CONFIG)

    aedg_metadata generate \
        "$DATA_PATH" \
        "$SOURCE_DIR_PATH" \
        --data-dictionary "$DATA_DICTIONARY" \
        --bbox "$BBOX" \
        --time "$TIME"
done
