# Exploration Notebook to 
#  - find and correct the idiosyncrasies of the Interties lookup table as it came from Neil
#  - test chunks of code before they were formalized in interties2grids.py
#  - test the final output to ensure it is doing expected things
# run with "uv run --with jupyter jupyter lab" with the venv activated

from pathlib import Path

import numpy as np
import pandas as pd

infile = "../../data/raw/dowl/lookup_interties_2023-11-08.csv"
outfile = "lookup_grids_2025-03-31.csv"

# read
df = pd.read_csv(infile)

# some columns we don't need
df.drop(columns=[
    "month_of_intertie",   # mostly unknown
    "source", # awkward. maybe add later
    "aea_energy_region",  # in the crosswalk or maybe we aren't using
], inplace=True)
# Railbelt and Copper Valley have blank placeholders. Can't deal with that
df.dropna(subset=['communities_intertied'], inplace=True)

# Standardize the grid names - some have spaces or punctuation
print(len(df['intertie_unique_id_name'].unique()))
df['intertie_unique_id_name'] = df['intertie_unique_id_name'].str.replace(' ', '').str.replace('.', '').str.replace('-', '').str.replace('\'', '')
df['intertie_unique_id_name'] = df['intertie_unique_id_name'].str.replace('_grid', '').str.replace('_', '')
df['intertie_unique_id_name'] = df['intertie_unique_id_name'] + '_grid'
print(len(df['intertie_unique_id_name'].unique()))

# reformat the id
df['intertie_id'] = df['intertie_id'].str.replace('_', '-')
df[['grid_id', 'connection_year']] = df['intertie_id'].str.split('-', expand=True)
df['ak_grid_id'] = 'AK-GR-' + df['grid_id']
df['grid_id'] = df['grid_id'].astype(int)
df['connection_year'] = df['connection_year'].astype(int)

# to separate communities into rows, first standardize delimiters (including dash in "Wrangell-Petersburg"
df['communities_intertied'] = df['communities_intertied'].str.replace(';', ',').str.replace('-', ',')
df['communities_intertied'] = df['communities_intertied'].map(lambda x: [y.strip() for y in x.split(',')])

df

# sometimes grids start with many communities. Prince_of_Wales_Is_grid added 2 communities at a time
# so cann't assume building up one by one
number_changed = {}
for grid_name in df['intertie_unique_id_name'].unique():
    list_lens = []
    grid = df.loc[grid_name == df['intertie_unique_id_name']]
    for index, community_list in grid['communities_intertied'].items():
        if grid_name == 'Prince_of_Wales_Is_grid':
            print(grid_name, community_list)
        #print(grid_name, len(value))
        list_lens.append(len(community_list))
    if list_lens[0] != 1 or len(list_lens) > 1:
        print(grid_name, list_lens)
    if len(list_lens) > 1:
        number_changed[grid_name] = list_lens


# list of all communities mentioned
all_communities = []
for index, community_list in df['communities_intertied'].items():
    all_communities = all_communities + community_list

all_communities = list(set(all_communities))
all_communities.sort()
print(f"{len(all_communities)} communities")

# sometimes grids are not named after a community in the list (or punctuation is different)
all_grid_names = df['intertie_unique_id_name'].unique()
print(f"{len(all_grid_names)} grids")

for gn in all_grid_names:
    match = False
    gn_clean = gn.replace('_grid', '')
    for cn in all_communities:
        if cn.replace(' ', '') in gn:
            match = True
            break
        elif gn_clean in cn.replace(' ', '').replace('\'', ''):
            match = True
            break    
    if not match:
        print(gn)
        

# how many grids is each community mentioned in?
comcount = {}
for community in all_communities:
    count = 0
    for grid_name in df['intertie_unique_id_name'].unique():
        grid = df.loc[grid_name == df['intertie_unique_id_name']]
        for index, community_list in grid['communities_intertied'].items():
            if community in community_list:
                count = count + 1
    if count > 1:
        print(community, count)
        comcount[community] = count


# associate the community name with the year it was added to a grid
print(number_changed)
events = pd.DataFrame({})
for key, counts in number_changed.items():
    grid = df.loc[key== df['intertie_unique_id_name']]
    previous = grid['communities_intertied'].values[0]
    for index, row in grid.iloc[1:, :].iterrows():
        event = {}
        event['to_grid_name'] = key
        event['to_grid_id'] = row['ak_grid_id']
        event['year'] = row['connection_year']
        event['added'] = list( set(row['communities_intertied']) - set(previous) )
        previous = row['communities_intertied']
        events = pd.concat([events, pd.DataFrame(event)], ignore_index=True)
events.set_index('added', inplace=True)
print(events)
print(events.loc['Tetlin'])


# Not all added communities have their own grid to start with in the Intertie table
from_grid = []
for community, row in events.iterrows():
    alone = False
    for index2, row2 in df.iterrows():
        if [community] == row2['communities_intertied']:
            #from_grid.append(row2['intertie_unique_id_name'])
            events.loc[community, 'from_grid_name'] = row2['intertie_unique_id_name']
            events.loc[community, 'from_grid_id'] = row2['ak_grid_id']

events

len(events)

## Exploration is done
# ready to build the Grids table

grids = pd.DataFrame({})
for grid_id in df['ak_grid_id'].unique():
    chunk = df.loc[grid_id == df['ak_grid_id']]
    record = chunk.loc[chunk['connection_year'] == chunk['connection_year'].min(), :]
    grids = pd.concat([grids, record], ignore_index=True)

grids = grids.explode(column='communities_intertied', ignore_index=True)
grids['termination_year'] = np.nan
print(grids.shape)

for index, row in events.iterrows():
    # add the connection info
    joining_grid = row['to_grid_id']
    year = row['year']
    record = df.loc[(df['ak_grid_id'] == joining_grid) & (df['connection_year'] == year), :]
    record.loc[:,'communities_intertied'] = index
    grids = pd.concat([grids, record], ignore_index=True)

    # alter existing record to show termination info
    leaving_grid = row['from_grid_id']
    grids.loc[grids['ak_grid_id'] == leaving_grid, 'termination_year'] = year

# assume if no termination year, then it is still operating
grids['termination_year'] = grids['termination_year'].fillna(9999)
grids['termination_year'] = grids['termination_year'].astype(int)


# clear out last vestiges
grids.drop(columns=[
    'intertie_id',
    'current_id',
    'year_of_intertie'
], inplace=True)
grids.rename(columns={'communities_intertied': 'community', 'intertie_unique_id_name': 'grid_name'}, inplace=True)

grids = grids[['community', 'grid_id', 'ak_grid_id', 'grid_name', 'connection_year', 'termination_year']]
grids.sort_values(by=['grid_id', 'connection_year'], inplace=True)

grids

grids.loc[grids['community'] == 'Mountain Village']

grids.loc[grids['grid_name'] == 'SaintMarys_grid']

grids.loc[grids['ak_grid_id'] == 'AK-GR-023']