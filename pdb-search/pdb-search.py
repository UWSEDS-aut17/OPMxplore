import pandas as pd
import numpy as np
import pypdb as pdb
import os


#def get_file_path(filename):
#    return os.path.dirname(os.getcwd())+"\\pdb-search\\data\\"+filename

def get_path(filename):
    """
    Locate the files in the appropriate directory relative to the current
    working directory. This assumes the current file is in
    "~/example_notebooks/", or in "~/pdb-search/"
    and that the data files are located in
    "~/pdb-search/data/sql_export/".
    
    os.path.join is used to provide cross-platform support.
    
    Returns:
    -------
    path : string
        The full path to the file
    """
    return os.path.join(os.path.dirname(os.getcwd()),
                        'pdb-search',
                        'data',
                        'sql_export',
                        filename)

def load_data():
    """
    A Function to read all of the OPM database tables from csv files
    and load it into memory as a pandas dataframe.
    'protein.csv' contains the main table of protein information
    and the rest of the tables contain specific information about
    the various categories of proteins.  These are converted to dicts,
    and used to add the appropriate columns to the proteins dataframe
    
    Returns:
    -------
    df : pandas.DataFrame
        The data from the OPM database, including protein types,
        classes, superfamilies, families, species, and localization
    """
    
    # First we load all of the csv files into memory as pandas dataframes
    # proteins is the main table we are interested in
    proteins = pd.read_csv(get_path('protein.csv'), sep=';')

    # types, classes, families, and membranes will all become
    # dicts to interpret their various id's and turn them into names
    types = pd.read_csv(get_path('type.csv'), sep=';')
    classes = pd.read_csv(get_path('class.csv'), sep=';')
    families = pd.read_csv(get_path('family.csv'), sep=';')
    membranes = pd.read_csv(get_path('membrane.csv'), sep=';')

    # any given family superfamilies and species
    classifications = pd.read_csv(get_path('classification.csv'), sep=';')
    superfamilies = pd.read_csv(get_path('superfamily.csv'), sep=';')
    species = pd.read_csv(get_path('species.csv'), sep=';')

    # Next we make a series of dictionaries to translate:
    # family id --> family name
    # family id --> class number
    # family id --> type id
    # family id --> family tcdb code
    # family id --> family pfam code
    # family id --> superfamily_id
    family_names = dict(families[['id','name']].values)
    family_tcdbs = dict(families[['id','tcdb']].values)
    family_pfams = dict(families[['id','pfam']].values)
    
    # family id --> superfamily id
    # family id --> class id
    # family id --> type id
    family_to_superfam = dict(classifications[['family_id','superfamily_id']].values)
    family_to_class = dict(classifications[['family_id','class_id']].values)
    family_to_type = dict(classifications[['family_id','type_id']].values)

    # superfamily id --> superfamily name
    # superfamily id --> superfamily tcdb code
    # superfamily id --> superfamily pfam code
    superfamily_names = dict(superfamilies[['id','name']].values)
    superfamily_tcdbs = dict(superfamilies[['id','tcdb']].values)
    superfamily_pfams = dict(superfamilies[['id','pfam']].values)
    
    # class id --> class name
    # type id --> type name
    # species id --> species name
    # membrane id --> memrane name
    # memrane id --> membran abbreviation
    class_names = dict(classes[['id','name']].values)
    type_names = dict(types[['id','name']].values)
    species_names = dict(species[['id','name']].values)
    membrane_names = dict(membranes[['id','name']].values)
    membrane_abbr = dict(membranes[['id','abbreviation']].values)

    # now we use the dics from above to create new columns in the
    # proteins data frame containing the actual names of the
    # species, membrane, family, superfamily, etc
    proteins['species'] = proteins.species_id.replace(species_names)
    proteins['membrane'] = proteins.membrane_id.replace(membrane_names)
    proteins['membrane_abbr'] = proteins.membrane_id.replace(membrane_abbr)
    proteins['family'] = proteins.family_id.replace(family_names)
    proteins['family_pfam'] = proteins.family_id.replace(family_pfams)
    proteins['family_tcdb'] = proteins.family_id.replace(family_tcdbs)
    proteins['superfamily'] = proteins.family_id.replace(family_to_superfam).replace(superfamily_names)
    proteins['superfamily_tcdb'] = proteins.family_id.replace(family_to_superfam).replace(superfamily_tcdbs)
    proteins['superfamily_pfam'] = proteins.family_id.replace(family_to_superfam).replace(superfamily_pfams)
    proteins['class'] = proteins.family_id.replace(family_to_class).replace(class_names)
    proteins['type'] = proteins.family_id.replace(family_to_type).replace(type_names)
    
    return proteins
    
# load the data from excel files located in this directory
def load_excell_data():
    """
    Deprecated: Load the OPM database into memory as a pandas data frame.
    The protein data was downloaded from the OPM database
    as a MySQL dump file:
    http://opm.phar.umich.edu/OPM-2016-10-10.sql
    
    The data is was then converted to an excel file stored locally:
    "pdb-search/data/OPM_data_from_MySQL.xlsx"
    
    Returns:
    -------
    df : pandas.DataFrame
        The data from the OPM database, including protein types,
        classes, superfamilies, families, species, and localization
    """
    return pd.read_excel(get_path("OPM_data_from_MySQL.xlsx"), "Sheet1")

def find_matches(query, df):
    """
    Search the PDB database for matches to a given query using pypdb,
    then cross-reference the results with the dataframe provided,
    and return a subset of the dataframe with matching pdbid's.
    Assumes that the provided which contains a column called 'pdbid'
    
    Returns:
    -------
    df : pandas.DataFrame
        A subset of the provided dataframe, which only includes the
        pdbid's which matched the query
    """
    # make a PDB database query and perform a search,
    # then convert the results to lower case
    search_results = [x.lower() for x in pdb.do_search(pdb.make_query(query))]
    return df[df['pdbid'].isin(search_results)]
    
    