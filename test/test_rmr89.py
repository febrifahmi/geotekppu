import unittest
from geotekppu.rmr.rmr__bieniawski1989 import r1, r2, r3, r4, r5, rmr89

class TestRMR89(unittest.TestCase):

    def test_r1_1(self):
        self.assertEqual(r1("pls", 16), 15)
    
    def test_r1_2(self):
        self.assertEqual(r1("pls", 5), 12)
    
    def test_r1_3(self):
        self.assertEqual(r1("pls", 3), 7)

    def test_r1_4(self):
        self.assertEqual(r1("pls", 1.5), 4)

    def test_r1_5(self):
        self.assertEqual(r1("pls", 0), "For value lower than 1 MPa, please proceed with Uniaxial Compressive Strength Test")
    
    def test_r1_6(self):
        self.assertNotEqual(r1("pls", 16), 12)
    
    def test_r1_7(self):
        self.assertNotEqual(r1("pls", 5), 15)

    def test_r1_8(self):
        self.assertNotEqual(r1("pls", 3), 4)

    def test_r1_9(self):
        self.assertNotEqual(r1("pls", 1.5), 7)

    def test_r1_10(self):
        self.assertNotEqual(r1("pls", 0), "Please choose ucs")
    
    def test_r1_11(self):
        self.assertEqual(r1("ucs", 251), 15)
    
    def test_r1_12(self):
        self.assertEqual(r1("ucs", 165), 12)
    
    def test_r1_13(self):
        self.assertEqual(r1("ucs", 67), 7)

    def test_r1_14(self):
        self.assertEqual(r1("ucs", 33), 4)

    def test_r1_15(self):
        self.assertEqual(r1("ucs", 19), 2)

    def test_r1_16(self):
        self.assertEqual(r1("ucs", 3), 1)

    def test_r1_17(self):
        self.assertEqual(r1("ucs", 0.73), 0)

    def test_r1_18(self):
        self.assertNotEqual(r1("ucs", 251), 7)

    def test_r1_19(self):
        self.assertNotEqual(r1("ucs", 165), 15)

    def test_r1_20(self):
        self.assertNotEqual(r1("ucs", 67), 12)

    def test_r1_21(self):
        self.assertNotEqual(r1("ucs", 33), 2)

    def test_r1_22(self):
        self.assertNotEqual(r1("ucs", 19), 1)

    def test_r1_23(self):
        self.assertNotEqual(r1("ucs", 3), 4)

    def test_r1_24(self):
        self.assertNotEqual(r1("ucs", 0.73), 14)

    

if __name__ == '__main__':
    unittest.main()