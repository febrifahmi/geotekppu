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

if __name__ == '__main__':
    unittest.main()