# Final Data

This repository is a transfer point between the [Extract-Load-Transform (ELT) pipeline](https://github.com/acep-aedg/aedg-etl-2024) and the Rails web app that displays data at the community level. [TODO: add link when it goes into production.] These files are normalized for efficient access in the Rails database and are not intuitively accessible by humans; they are for **internal** development work.

These are the normalized internal files. Connections between files are described in the ERDs, but we do not expect users to recreate a new database from scratch.

For instance, in order to answer questions such as "What is the electrical capacity of the grid that serves Ketchikan?", a user would need to connect `communities.geojson` to `capacity.csv`, using the field `grid_id`, information that could be gleaned from the ERDs.
