"""
Unit test for OPMvis.py module
Checks to see whether the plot functions  work as expected
"""
import os
import unittest


# Define a class in which the tests will run
class UtilsTest(unittest.TestCase):

    """ 
    
    """
    def test_stat_plot(self):

        #stat_plot(df, xvar, yvar, title)

        #self.assertTrue(os.path.getsize(DUMMY_FILENAME) > 0)

        return

    # test whether a non-existent URL throws a correct exception
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

