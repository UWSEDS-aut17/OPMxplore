import pandas as pd
import numpy as np
import pypdb as pdb
import os


def get_file_path(filename):
    return os.path.dirname(os.getcwd())+"\\pdb-search\\data\\"+filename


# load the data from excel files located in this directory
def load_data():
    """
    Load the OPM database into memory as a pandas data frame.
    The protein data was downloaded from the OPM database
    as a MySQL dump file:
    http://opm.phar.umich.edu/OPM-2016-10-10.sql
    
    The data is stored locally as an excel file:
    "pdb-search/data/OPM_data_from_MySQL.xlsx"
    
    Returns
    -------
    df : pandas.DataFrame
        The data from the OPM database, including protein types,
        classes, superfamilies, families, species, and localization
    """
    return pd.read_excel(get_file_path("OPM_data_from_MySQL.xlsx"), "Sheet1")

# 
def find_matches(query, df):
    """
    search the PDB database for matches to a give query
    and return a subset of a given dataframe
    which contains matching 'PDB_ID's
    make a PDB database query and perform a search,
    then convert the results to lower case
    """
    # make a PDB database query and perform a search,
    # then convert the results to lower case
    search_results = [x.lower() for x in pdb.do_search(pdb.make_query(query))]
    return df[df['pdbid'].isin(search_results)]
    
    