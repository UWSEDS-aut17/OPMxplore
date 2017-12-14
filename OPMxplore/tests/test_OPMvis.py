"""
Unit test for OPMvis.py module
Checks to see whether the plot functions  work as expected
"""
import os
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import OPMxplore.OPMvis as vis
import pandas as pd

df_test = pd.DataFrame(d = {'Transmembrane': [1, 2],
                            'thickness': [3, 4],
                            'membrane':[5, 6],
                            'title':[7, 8],
                            'gibbs':[9,10]})

# Define a class in which the tests will run
class UtilsTest(unittest.TestCase):

    def test_stat_plot(self):
        return

    def test_brill_3d(self):
        #brill_3d(high_type, df, x, y, z)
        #self.assertRaises(URLError, utils.get_data, BAD_URL, DUMMY_FILENAME)
        return

    # test whether a non-URL string throws an exception
    def test_swarm_plot(self):
        #swarm_plot(df, xvar, yvar, title)
        #self.assertRaises(ValueError, utils.get_data, 'junk', DUMMY_FILENAME)
        return

    def test_scatter_plot(self):
        #swarm_plot(df, xvar, yvar, title)
        #self.assertTrue(os.path.getsize(DUMMY_FILENAME) == 0)
        return

    def test_stat_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.stat_plot,
                          [],
                          'thickness',
                          'membrane',
                          'title'))

    def test_brill_3d_no_df(self):
        self.assertRaises(AttributeError,
                          vis.brill_3d,
                          'Transmembrane',
                          [],
                          'thickness',
                          'membrane',
                          'gibbs'))

    def test_swarm_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.swarm_plot,
                          [],
                          'thickness',
                          'membrane',
                          'title'))

    def test_scatter_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.scatter_plot,
                          [],
                          'thickness',
                          'membrane',
                          'title'))

