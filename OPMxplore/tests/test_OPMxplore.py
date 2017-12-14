from nose import with_setup # optional
import sys
import os
from types import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import OPMxplore.OPMxplore as opm
import pandas as pd
import unittest

class TestOPMxplore(unittest.TestCase):
 
    def test_get_path(self):
        filename = 'protein.csv'
        print('testing get_path('+filename+')')
        test_path = opm.get_path(filename)
        print('result = '+opm.get_path(filename))
        expected_path = os.path.join(
                                    os.path.dirname(
                                    os.path.dirname(
                                    os.path.realpath(__file__))),
                                                     'data',
                                                     'sql_export',
                                                     filename)
        print('expected path = '+expected_path)
        self.assertTrue(test_path == expected_path)


    def test_load_data(self):
        print('testing load_data()')
        test_data = opm.load_data()
        #print test_data
        expected_columns=['id',
                          'family_id',
                          'species_id',
                          'membrane_id',
                          'pdbid',
                          'name',
                          'resolution',
                          'topology',
                          'thickness',
                          'thicknesserror',
                          'tilt',
                          'tilterror',
                          'gibbs',
                          'tau',
                          'numsubunits',
                          'numstrands',
                          'verification',
                          'comments',
                          'date_added',
                          'species',
                          'membrane',
                          'membrane_abbr',
                          'family',
                          'family_pfam',
                          'family_tcdb',
                          'superfamily',
                          'superfamily_tcdb',
                          'superfamily_pfam',
                          'class',
                          'type']

        print('expected columns in the dataframe: ')
        print(expected_columns)
        print('result = ' + test_data.columns)

        self.assertTrue(all(expected_columns==test_data.columns))


    def test_find_matches(self):
        # construct a minimal dataframe containing 'pdbid' column
        df = pd.DataFrame({'pdbid' : ['1xc0']})
        print('testing find_matches() with simple dataframe')
        # search for the pdbid
        matches = opm.find_matches("1xc0",df)
        # the result should be the same pdbid
        self.assertTrue(matches.equals(df))


    def test_find_matches_key_error(self):
        print('test_find_matches("",pd.DataFrame({"A" : []}))')
        print('a dataframe lacking "pdbid" column')
        # we get a key error because there is no column 'pdbid'
        df_empty = pd.DataFrame({"A" : []})
        self.assertRaises(KeyError,opm.find_matches,"",df_empty)


    # I am not sure that this test is really necessary
    # since the function expects a dataframe, not a list
    def test_find_matches_empty_list(self):
        print('test_find_matches("",[]))')
        print('an empty data set and query')
        # passing an empty list [] does not allow you to 
        # lookup by column name: df[df['pdbid']
        self.assertRaises(TypeError,opm.find_matches,"",[])


    def test_sql_search(self):
        # construct a minimal dataframe containing 'pdbid' column
        df = pd.DataFrame({'pdbid' : ['1xc0']})
        print('testing sql_search(df)')
         # search with no qualifications
        matches = opm.sql_search(df)
        # the result should be the same
        self.assertTrue(matches.equals(df))


    def test_sql_search_with_options(self):
        # load the full dataframe
        df = opm.load_data()
        print('testing sql_search(df,"*","WHERE membrane_id = 3")')
        df_m3 = df[df['membrane_id']==3]
        # search for all entries with membrane_id == 3
        matches = opm.sql_search(df,"*","WHERE membrane_id = 3")
        # the result should be the same
        self.assertTrue(df_m3.shape == matches.shape)


    def test_add_query(self):
        print('test_add_query(df,"channel",past_queries)')
        df_a = pd.DataFrame({'pdbid' : ['1xc0']})
        df_b = pd.DataFrame({'pdbid' : ['1g1z']})
        start_query = dict([('df_a',df_a)])
        end_query = opm.add_query(df_b,"df_b",start_query)
        self.assertTrue(df_a.equals(end_query['df_a']) and 
                        df_b.equals(end_query['df_b']))

 
