"""
Unit test for OPMvis.py module
Checks to see whether the plot functions  work as expected
"""
import os
import sys
import unittest
import pandas as pd
import matplotlib
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.realpath(__file__)))
import OPMxplore.OPMvis as vis

df_test = pd.DataFrame({'type': ['Transmembrane',
                                 'Peptides',
                                 'Monotopic/peripheral',
                                 'junk'],
                        'thickness': [3, 4, 5, 6],
                        'membrane': [7, 8, 9, 10],
                        'gibbs': [11, 12, 13, 14],
                        'pdbid': ['a', 'b', 'c', 'd'],
                        'name': ['alice', 'bob', 'chuck', 'dan'],
                        'class': ['x', 'y', 'z', 'zz']})


# Define a class in which the tests will run
class OPMvisTestCase(unittest.TestCase):

    def test_stat_plot(self):
        ax = vis.stat_plot(df_test,
                           'thickness',
                           'membrane',
                           'title')
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))

    def test_brill_3d(self):

        # ax = vis.brill_3d('Transmembrane',
        #                   df_test,
        #                   'thickness',
        #                   'membrane',
        #                   'title')
        # self.AssertTrue(isinstance(ax,matplotlib.axes.Axes))
        return

    # test whether a non-URL string throws an exception
    def test_swarm_plot(self):
        ax = vis.swarm_plot(df_test,
                            'thickness',
                            'membrane',
                            'title')
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        return

    def test_scatter_plot(self):
        return

    def test_stat_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.stat_plot,
                          [],
                          'thickness',
                          'membrane',
                          'title')

    def test_brill_3d_no_df(self):
        self.assertRaises(TypeError,
                          vis.brill_3d,
                          'Transmembrane',
                          [],
                          'thickness',
                          'membrane',
                          'gibbs')

    def test_swarm_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.swarm_plot,
                          [],
                          'thickness',
                          'membrane',
                          'title')

    def test_scatter_plot_no_df(self):
        self.assertRaises(AttributeError,
                          vis.scatter_plot,
                          [],
                          'thickness')
