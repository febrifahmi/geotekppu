import unittest
from src.geotekppu.rmr.rmr_b_geocontrol2012 import rmr_ucs, rmr_rqd_spacing, rmrb
from src.geotekppu.rmr.rmr__bieniawski1989 import discontinuity_class, r5


class TestRMRb(unittest.TestCase):
    # change kg/cm2 to MPa
    convfactor = 0.0980665
    # Test the rmr_ucs function 
    def test_rmr_ucs_1(self):
        self.assertEqual(rmr_ucs(2501*self.convfactor), 15)

    def test_rmr_ucs_2(self):
        self.assertEqual(rmr_ucs(1000*self.convfactor), 12)

    def test_rmr_ucs_3(self):
        self.assertEqual(rmr_ucs(2500*self.convfactor), 12)

    def test_rmr_ucs_4(self):
        self.assertEqual(rmr_ucs(500*self.convfactor), 7)

    def test_rmr_ucs_5(self):
        self.assertEqual(rmr_ucs(999*self.convfactor), 7)

    def test_rmr_ucs_6(self):
        self.assertEqual(rmr_ucs(250*self.convfactor), 4)

    def test_rmr_ucs_7(self):
        self.assertEqual(rmr_ucs(50*self.convfactor), 2)

    def test_rmr_ucs_8(self):
        self.assertEqual(rmr_ucs(249*self.convfactor), 2)

    def test_rmr_ucs_9(self):
        self.assertEqual(rmr_ucs(10*self.convfactor), 1)

    def test_rmr_ucs_10(self):
        self.assertEqual(rmr_ucs(49*self.convfactor), 1)

    def test_rmr_ucs_11(self):
        self.assertEqual(rmr_ucs(9*self.convfactor), 0)
    
    # Test the rmr_rqd_spacing function
    def test_rmr_rqd_1(self):
        self.assertEqual(rmr_rqd_spacing(5),27)

    def test_rmr_rqd_2(self):
        self.assertEqual(rmr_rqd_spacing(21),13)

    def test_rmr_rqd_3(self):
        self.assertEqual(rmr_rqd_spacing(32),8)

    def test_rmr_rqd_4(self):
        self.assertEqual(rmr_rqd_spacing(50),0)

    def test_rmr_rqd_5(self):
        self.assertEqual(rmr_rqd_spacing(9),23)

    def test_rmr_rqd_6(self):
        self.assertEqual(rmr_rqd_spacing(46),1.5)
    
    # Test rmrb function
    def test_rmrb_1(self):
        self.assertEqual(rmrb(
            rmr_ucs(2501),
            rmr_rqd_spacing(5),
            discontinuity_class(0.5,0.1,"rough","hl<5","decomposed"),
            r5(None,0,"dry")),
            76)
        
    def test_rmrb_1(self):
        self.assertNotEqual(rmrb(
            rmr_ucs(2501),
            rmr_rqd_spacing(5),
            discontinuity_class(0.5,0.1,"rough","hl<5","decomposed"),
            r5(None,0,"dry")),
            0)

if __name__ == '__main__':
    unittest.main()