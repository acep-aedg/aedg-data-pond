#!/bin/bash

# This quick shell script sorts the data dictionary alphabetically by name, which keeps things tidy

DATA_DICTIONARY=registry/fields.csv

# First part pulls the header, second part pulls the rest, third part sorts by first column (-k1), which is 'name'
(head -n 1 $DATA_DICTIONARY && tail -n +2 $DATA_DICTIONARY | sort -t, -k1) > tmp.csv
# For safety (otherwise input file will get deleted), output results to tmp.csv then immediately rename to data_dictionary input name
mv tmp.csv $DATA_DICTIONARY