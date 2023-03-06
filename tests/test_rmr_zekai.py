import unittest
from src.geotekppu.rmr.rmr__sen_sadagah2002 import RMR02pls, RMR02ucs

class TestRMR89(unittest.TestCase):

    # Testing function RMR02pls
    def test_rmrpls_1(self):
        self.assertEqual(RMR02pls(1.2,20,5,-5,-5), 85.7223)

    # Testing function RMR02ucs
    def test_rmrucs_1(self):
        self.assertEqual(RMR02ucs(1.2,200,5,-5,-5),65.6523)

if __name__ == '__main__':
    unittest.main()