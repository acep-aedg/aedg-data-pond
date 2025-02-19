# Welcome

Welcome to the data repository for the Alaska Energy Data Gateway (AEDG). This repo is intended to provide long-term public access to the data used in AEDG. 

## Interacting with this repository
If you are interested in accessing the data used in AEDG Community Dashboard, please direct your attention to `data/final` where you will find files in CSV and GeoJSON formats. 

CSV files may be opened using graphical programs such as Excel, or opened using programming lanugages such as R and python. 

GeoJSON files cannot be opened using Excel, but may be opened graphically using QGIS and ArcGIS or opened programatically using R (package `sf`) and python (library `geopandas`). 

The organization of these files is best explained using an Entity Relationship Diagram (ERD), a visual representation of how the tables are connected and which columns may be used to join the data together. In order to answer questions such as "What is the electrical capacity of the grid that serves Ketchikan?", we would need to connect `communities.geojson` to `capacity.csv`. This is done using the field `grid_id`, information that we would glean from an Entity Relationship Diagram.

## How this repository works
As part of the AEDG effort, a series of programming scripts were run to ingest data from external sources, load the data into a database, then clean and reorganize the data. The result 



<br>
<br>
<br>
<br>
<br>

##### TODO:
* Add license