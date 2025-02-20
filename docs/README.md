# Documentation

## Data Model

The data model of AEDG is documented by Entity Relation Diagram (ERD) and these were built in https://dbdiagram.io/.  This tool uses a markup language of their own design called DBML. These are text files that will be version controled here by manually copying the DBML from the web-based tool.

There are two diagrams that were split, not for technical reasons, but for convenience to avoid showing too many tables on a single image. The division is roughly the tables that will appear in the data explorer and those that crosswalk between different geospatial entities.

Note: we have attempted to use FIPS code as the foreign key common to most tables, but for energy data, the grid id is the most common basic unit. More on this later.
