#!/bin/bash

aedg_metadata generate \
    data/final/bulk_fuel/bulk_fuel.geojson \
    ~/repos/aedg-etl-2024/data-sources \
    -dd bulk_fuel_data_dictionary.csv \
    --bbox infer \
    -t specify