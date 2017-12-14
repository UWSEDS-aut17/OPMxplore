from nose import with_setup # optional
import sys 
from types import *
sys.path.append('..')
import OPMxplore 
import pandas as pd
 
class TestOPMxplore:
 
    def test_getpath(self):
        print 'test_getpath("")  <======== tests get_path function with empty string'
        test_path = OPMxplore.get_path("")
        assert (isinstance(test_path, str) == False), "get_path returned string instead of error (-1) for null filename"

        
        print 'test_getpath("randomfilename")  <======== tests get_path function with nonexistent filename'
        test_path = OPMxplore.get_path("randomfilename")
        assert (isinstance(test_path, str) == False), 'file does NOT exist.'

        print 'test_getpath("protein.csv")  <======== tests get_path function with nonexistent filename'
        test_path = OPMxplore.get_path("protein.csv")
        print OPMxplore.get_path("protein.csv")
        assert (isinstance(test_path, str) == True), 'protein.csv exists'

        print 'test_load_data()  <======== tests load_data function for empty data set'
        test_data = OPMxplore.load_data()
        #print test_data
        assert (len(test_data) != 0), "load_data returned empty data set"
 
        print 'test_load_data()  <======== tests load_data function for correct pandas dataframe'
        df = pd.DataFrame(test_data)
        if ('superfamily_tcdb' in df.columns and 
           'family_pfam' in df.columns):
           print "load_data returned valid dataframe"

        print 'test_load_data()  <======== tests load_data function for invalid pandas dataframe'
        test_data = OPMxplore.load_data()
        df = pd.DataFrame(test_data)
        if ('type1' in df.columns or 
           'class1' in df.columns):
           assert (False), "load_data returned invalid dataframe"

        print 'test_find_matches("",[])  <======== tests find_matches function using empty data set and query'
        test_data = OPMxplore.find_matches("",[])
        assert (isinstance(test_data, int) == True), "find_matches worked on empty data set"

        print 'test_find_matches("",[])  <======== tests find_matches function using empty query'
        test_data = OPMxplore.find_matches("",[])
        assert (isinstance(test_data, int) == True), "find_matches worked on empty data set"

        print 'test_sql_search([],"*","")  <======== tests sql_search function using empty data set'
        test_data = OPMxplore.sql_search([],"*","")
        assert (isinstance(test_data, int) == True), "load_data returned empty data set"
        

        print 'test_add_query(df,"channel",past_queries)  <======== tests sql_search function using empty data set'
        test_data = OPMxplore.load_data()
        df = pd.DataFrame(test_data)
        past_queries = {}
        OPMxplore.add_query(df,"channel",past_queries)
        if(past_queries):
           print "data frame added to past queries"
        else:
           assert "add_query failed..." 
        

 
