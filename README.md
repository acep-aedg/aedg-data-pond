# Welcome

Welcome to the data repository for the Alaska Energy Data Gateway (AEDG). Energy-related data are stored here in multiple directories for use in AEDG. The unifying hub is the PostGIS data that AEDG's [Extract-Load-Transform (ELT) pipeline](https://github.com/acep-aedg/aedg-etl-2024) (permissions may be required) has created. A script in this repository pulls normalized tables and denormalized views from that database and writes the files found here. Formats and uses are described below.

The second source of files here is AEDG's [metadata generation process](https://github.com/acep-aedg/aedg-metadata). That system uses Python code to generate JSON metadata files conforming to the [OEMetadata standard](https://openenergyplatform.github.io/oemetadata/latest/). The resulting metadata files are then copied here to create documentation for individual data files.

## Serving multiple purposes

This repository currently serves two distinct purposes.

1. This repository is a transfer point between the [Extract-Load-Transform (ELT) pipeline](https://github.com/acep-aedg/aedg-etl-2024) (permissions may be required) and the Rails web app that displays data at the community level. [TODO: add link when it is available]. These files are for **internal** development work.
2. This repository is also intended to provide long-term public access to the data available via the AEDG. This includes storage of the original (or slightly corrected) source files and user-friendly versions of data that can be applied to other purposes. These files are designed to face **external** users.

As the system matures, we will develop an alternative method of transfering internal files. However, for the time being, these are CSV and GeoJSON versions of normalized database tables; these files will not be intuitively accessible by humans. 

The best form for the external files adhere to the Findable-Accessible-Interoperable-Reuseable (FAIR) principles, a goal not required for our internal development work.

## File formats

We have chosen widely accessible file formats for these data. Some data is geospatial in nature (a new developement for the AEDG) so is distributed as GeoJSON. Otherwise, files are comma delimited CSV files.

* CSV files may be opened using graphical programs such as Excel, or opened using programming lanugages such as R and python. 

* GeoJSON files cannot be opened using Excel, but may be opened graphically using QGIS and ArcGIS or accessed programatically using R (package `sf`) and python (library `geopandas`). 

It is our intention to document all these files with Frictionless data package metadata. These files are currently under development. 

## Repository Structure

### `docs/`

This directory contains documentation of the data model for the internal files as Entity Relationship Diagrams (ERD), visual representations of how the tables are connected. These show  which columns may be used to join the data in the normalized tables together. Files here were developed in https://dbdiagram.io/ and uses their DBML syntax. They are also avalable as PNG files.

### `data/`

As part of the AEDG effort, a series of programming scripts were run to ingest data from external sources, load the data into a database, then clean and reorganize the data. Output from various steps in this process are available in the `data/` directory


#### `raw/`

These are files from the original sources with as little modification as possible.

#### `intermediate/`

These are manually created look-up tables that create the relationships between primary and foreign keys in the database. These files took some effort to create, but the information contained in them is generally contained in the derived tables.

#### `final/`

These are the normalized internal files. Connections between files are described in the ERDs, but we do not expect users to recreate a new database from scratch.

For instance, in order to answer questions such as "What is the electrical capacity of the grid that serves Ketchikan?", a user would need to connect `communities.geojson` to `capacity.csv`,using the field `grid_id`, information that could be gleaned from the ERDs.

#### `public/`

These are denormalized versions of the internal database tables - joined in ways to make the data more user friendly. These files are available via the Data Explorer portion of the AEDG. [TODO: add link when it goes into production.] These files are accompanied by OEMetadata files that document the schema (i.e. data dictionary) and sources of the data.

Using these files, to answer questions such as "What is the electrical capacity of the grid that serves Ketchikan?", a user would download `public_capacity.csv` and filter to "Ketchikan" using their favorite tool.

## Workflow

We have adopted tagged releases to structure integration into the Rails app. Tags are prefixed with the letter "v" and have 2 digits - i.e. v[major].[minor].

- Prior to the v1.0 release, minor releases will include schemas changes as required for development; tables will be added as data types are available.
- Post v1.0, schema changes and revisions that would break the Rails app will constitute major revisions, and minor revisions will consist of table updates with new data

To add or revise data, utilize a branch and PR with review. When the data are consistent enough to integrate into Rails, tag a release. These releases are intended to correspond to Jira versions and should consist of needed, identified, and documented changes.

Data should be validated for internal consistency prior to posting. For instance, community id is required in all applicable tables and cannot be Null because it is the basic building block of AEDG. The full list of validation steps is currently being developed and will be posted when it is available.

Additional data quality guidelines are also being developed.

##### TODO:
* Add license