#!/bin/bash

METADATA_FILES=$(find "data" -type f -name "*.json")

echo ""

for METADATA_FILE in $METADATA_FILES; do
    REPORT_PATH="${METADATA_FILE%.json}.md"
    
    # single jq command to build the doc
    jq -r '
      .resources[0] | 
      (
        "# " + .title + "\n\n" +
        "## Description\n" + .description + "\n\n" +
        
        "## Responsible Party\n" +
        "* **Publisher:** " + .context.publisher + "\n" +
        "* **Funding Agency:** " + .context.fundingAgency + "\n\n" +
        
        "## Data Lineage\n" +
        "* **URL:** [" + .path + "](" + .path + ")\n" +
        "* **Reference Date:** " + .temporal.referenceDate + "\n\n" +
        
        "### Sources\n" +
        ([.sources[] | "* **" + .title + "** (" + .publicationYear + ")\n  " + .path + "\n " + .description] | join("\n")) + "\n\n" +
        
        "### Data Dictionary\n" +
        "| Column Name | Type | Unit | Description |\n" +
        "| :--- | :--- | :--- | :--- |\n" +
        ([.schema.fields[] | "| " + .long_name + " | " + .type + " | " + (.unit // "None") + " | " + .description + " |"] | join("\n")) + "\n\n" +

        "## License\n" +
        .licenses[].name + "\n" +
        .licenses[].title + "\n" +
        .licenses[].path + "\n"
      )
    ' "$METADATA_FILE" > "$REPORT_PATH"

    printf "Converted: %s\n" "$REPORT_PATH"
done



