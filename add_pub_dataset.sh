#!/bin/bash

# 1. Check if the user provided the required 3 arguments
if [ "$#" -ne 3 ]; then
    echo "Oops! You need to provide 3 arguments."
    echo "Usage: ./add_dataset.sh <category> <dataset_name> <extension>"
    echo "Example: ./add_dataset.sh public public_service_area_geoms geojson"
    exit 1
fi

CATEGORY=$1
DATASET_NAME=$2
EXTENSION=$3

# 2. Define our file paths based on your current project structure
METADATA_YML="src/generate_metadata.yml"
DATA_DIR="data/$CATEGORY/$DATASET_NAME"
NEW_YML_FILE="$DATA_DIR/$DATASET_NAME.yml"
TEMPLATE_FILE="registry/config_template.yml"

# 3. Check if the dataset already exists in the YAML file before appending
# We search for two spaces, the dataset name, and a colon to ensure an exact match
if grep -q "^  $DATASET_NAME:" "$METADATA_YML"; then
    echo "Looks like $DATASET_NAME is already in $METADATA_YML! Skipping append."
else
    echo "Adding $DATASET_NAME to $METADATA_YML..."
    # The <<EOF ... EOF syntax lets us write a multi-line block of text easily
    cat <<EOF >> "$METADATA_YML"
  $DATASET_NAME:
    data_path: data/$CATEGORY/$DATASET_NAME/$DATASET_NAME.$EXTENSION
    bbox: infer
    time: specify
EOF
fi

# 4. Create the new directory (the -p flag creates parent directories if they don't exist)
echo "Creating directory $DATA_DIR..."
mkdir -p "$DATA_DIR"

# 5. Copy the template file into the new directory
echo "Copying template to $NEW_YML_FILE..."
if [ -f "$TEMPLATE_FILE" ]; then
    cp "$TEMPLATE_FILE" "$NEW_YML_FILE"

    # Bonus: This automatically replaces the blank 'name' line in the template with your dataset name!
    sed -i "s/name: # Filename stub/name: $DATASET_NAME/g" "$NEW_YML_FILE"

    echo "Success! $DATASET_NAME is ready to go."
else
    echo "Warning: Template file $TEMPLATE_FILE not found. Are you running this from the aedg-data-pond root?"
fi
