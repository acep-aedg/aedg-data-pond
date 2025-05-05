"""Script to convert Neil's concept of interties to the grids concept that AEDG needs

source .venv/bin/activate 
python grids2csv.py
"""

from pathlib import Path

import numpy as np
import pandas as pd


def calc_number_changed (df): 
    """ to count the number of communities in each iteration of the intertie
    Can't assume are building the grid one community at a time
      *  sometimes grids start with many communities. 
      *  Prince_of_Wales_Is_grid added 2 communities at a time in 1999
    Return a dictionary of the grid name and a list of the lengths it has had
    (But only if it has changed. If it was always the same community list, skip it)
    """
    
    number_changed = {}
    for grid_name in df['grid_name'].unique():
        list_lens = []
        # find all the intertie variations of this grid
        grid = df.loc[grid_name == df['grid_name']]
        # each is a list of communities so count them 
        for index, community_list in grid['community'].items():
            list_lens.append(len(community_list))
        #if list_lens[0] != 1 or len(list_lens) > 1:
        #    print(grid_name, list_lens)
        # only save info on grids that changed
        if len(list_lens) > 1:
            number_changed[grid_name] = list_lens

    return number_changed


def define_connection_events(df, number_changed):
    """Define what happened each time a new community was connected
    returns a new DataFrame of connection events indexed by the community name
    """

    events = pd.DataFrame({})

    # first collect all the connection events
    for key, counts in number_changed.items():
        # find all the intertie variations of this grid
        grid = df.loc[key== df['grid_name']]
        # each is a list of communities so find what changed
        previous = grid['community'].values[0]
        for index, row in grid.iloc[1:, :].iterrows():
            event = {}
            event['to_grid_name'] = key
            event['to_grid_id'] = row['ak_grid_id']
            event['year'] = row['connection_year']
            event['added'] = list( set(row['community']) - set(previous) )
            previous = row['community']
            events = pd.concat([events, pd.DataFrame(event)], ignore_index=True)
    events.set_index('added', inplace=True)

    # then use those to check if these are new communities or if they had their own grid
    # Not all added communities have their own grid to start with in the Intertie table
    for community, row in events.iterrows():
        for index2, row2 in df.iterrows():
            if [community] == row2['community']:
                events.loc[community, 'from_grid_name'] = row2['grid_name']
                events.loc[community, 'from_grid_id'] = row2['ak_grid_id']

    return events


def build_grids(df, events):
    """ready to build the Grids table from the intertie table (knowing connection events)
    """
    # First step is to get the first configuration of the grid
    grids = pd.DataFrame({})
    for grid_id in df['ak_grid_id'].unique():
        chunk = df.loc[grid_id == df['ak_grid_id']]
        record = chunk.loc[chunk['connection_year'] == chunk['connection_year'].min(), :]
        grids = pd.concat([grids, record], ignore_index=True)

    # separate communities in rows instead of the list in a cell
    grids = grids.explode(column='community', ignore_index=True)
    grids['termination_year'] = np.nan
    print("Number of communities starting in a grid: ", len(grids))

    # add the connection info from the events table
    for index, row in events.iterrows():
        joining_grid = row['to_grid_id']
        year = row['year']
        record = df.loc[(df['ak_grid_id'] == joining_grid) & (df['connection_year'] == year), :]
        record.loc[:,'community'] = index
        grids = pd.concat([grids, record], ignore_index=True)

        # alter existing record to show termination info
        leaving_grid = row['from_grid_id']
        grids.loc[grids['ak_grid_id'] == leaving_grid, 'termination_year'] = year

    # assume if no termination year, then it is still operating
    grids['termination_year'] = grids['termination_year'].fillna(9999)
    grids['termination_year'] = grids['termination_year'].astype(int)

    grids = grids[['community', 'grid_id', 'ak_grid_id', 'grid_name', 'connection_year', 'termination_year']]
    grids.sort_values(by=['grid_id', 'connection_year'], inplace=True)

    return grids


def main():
    print("Hello from dowl!")

    data_dir = Path(__file__).parents[2] / "data" / "raw" / "dowl"
    infile = "lookup_interties_2024-02-23.csv"
    outfile = "lookup_grids_2025-04-17.csv"

    # read
    df = pd.read_csv(
        data_dir / infile,
    )

    # Railbelt and Copper Valley have blank placeholders. Can't deal with that
    df.dropna(subset=['communities_intertied'], inplace=True)

    # Standardize the grid names - some have spaces or punctuation
    print('Number of grids: ', len(df['intertie_unique_id_name'].unique()))
    df['grid_name'] = df['intertie_unique_id_name'].str.replace(' ', '').str.replace('.', '').str.replace('-', '').str.replace('\'', '')
    df['grid_name'] = df['grid_name'].str.replace('_grid', '').str.replace('_', '')
    df['grid_name'] = df['grid_name'] + '_grid'
    print('Number of grids after cleanup: ', len(df['grid_name'].unique()))

    # reformat the id
    df['intertie_id'] = df['intertie_id'].str.replace('_', '-')
    df[['grid_id', 'connection_year']] = df['intertie_id'].str.split('-', expand=True)
    df['ak_grid_id'] = 'AK-GR-' + df['grid_id']
    df['grid_id'] = df['grid_id'].astype(int)
    df['connection_year'] = df['connection_year'].astype(int)

    # to separate communities into rows, first standardize delimiters (including dash in "Wrangell-Petersburg"
    df['community'] = df['communities_intertied'].str.replace(';', ',').str.replace('-', ',')
    df['community'] = df['community'].map(lambda x: [y.strip() for y in x.split(',')])

    # some columns we don't need
    df.drop(columns=[
        "month_of_intertie",     # mostly unknown
        "source",                # awkward. maybe add later
        "aea_energy_region",     # in the crosswalk or maybe we aren't using
        'intertie_id',           # use grid_id and ak_grid_id instead
        'current_id',            # not needed in new format
        'year_of_intertie',      # use connection_year instead
        'communities_intertied', # use standardized community names instead
        'intertie_unique_id_name', # use standardized grid names instead
    ], inplace=True)

    number_changed = calc_number_changed(df)
    print("Grids where the number of communities connected increased: ", number_changed)
    events = define_connection_events(df, number_changed)
    print("Number of connection events: ", len(events))
    grids = build_grids(df, events)
    print("Number of communities with a unique connection: ", len(grids))

    # do some tests to make sure things look OK
    assert {64, 75} == set(grids.loc[grids['community'] == 'Mountain Village', 'grid_id'].values) 
    assert 4 == len(grids.loc[grids['grid_name'] == 'SaintMarys_grid'])
    assert 8 == len(grids.loc[grids['ak_grid_id'] == 'AK-GR-023'])
    assert {1987, 1999, 2004, 2006, 2011, 2015} == \
      set(grids.loc[grids['ak_grid_id'] == 'AK-GR-023', 'connection_year'].values)
    print("Passed tests.")

    # write
    grids.to_csv(
        data_dir / outfile,
        index=False
    )

if __name__ == "__main__":
    main()
