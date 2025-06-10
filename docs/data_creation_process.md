# How were the AEDG datasets made?

Here’s a look at each step that went into building the datasets – so you can trust the foundation behind the insights.

## Targeting Datasets

The AESTF State Energy Data Subcommittee Report defines energy data as “Information about how electricity, heat, and transportation fuels are sourced, generated, stored, distributed, used, and governed; and the impacts on the built, natural, and socioeconomic environments.” Previous versions of the Alaska Energy Data Gateway were valuable to a wide audience because of the broad range of data it contained. Therefore, we needed to consider these contexts as we chose the data to include.

We started with the datasets used by previous versions of AEDG. Then we held internal brainstorming meetings and consulted with subject matter experts via user interviews to determine which datasets were still available and to find newly published ones. With this list of possible datasets and using user stories, we established priorities for which datasets to incorporate in the first year of the project.

## Data Sourcing

To enable quick development of dashboards with up-to-date, relevant data, our sources needed to be available online from government agencies or previously compiled by ACEP and ISER. We cataloged data server URLs for each dataset and established a data pipeline that downloads from all sources at the push of a button. These downloaded data sets are copied into a local archive and then loaded into a database for processing. The flexibility of our pipeline will allow us to incorporate data from other sources and research projects in future iterations of this work.

## Data Standardization

To allow the merging of disparate datasets that characterizes AEDG, data were standardized and normalized. Column names were standardized, values were calculated and converted to established units, and data tests were written in order to ensure we serve the best available data. Code also subsets, aggregates, and transforms the tables into the datasets loaded into the AEDG database.

## Data Enrichment

This iteration of AEDG, like previous versions, displays data at the community level. However, some data are only available in aggregates of communities (electrical grids connecting communities, reporting by utilities that serve multiple communities). And other data apply to subsets of communities (some Alaska legislative districts, census tracts) Therefore the subtleties of this display needed to be identified and described to make the dashboards understandable. Additionally the context of relationships between data sources and credit to the data originators needed to be established.

Merging data tables within the processing database enriches the original sources. Additional context is provided by metadata displayed in the Data Explorer which includes descriptions of the data and sources, units, publication year, authors, and licenses. Together, these operations provide a unique glimpse into energy data in Alaska.
