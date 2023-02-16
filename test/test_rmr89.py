import unittest
from geotekppu.rmr.rmr__bieniawski1989 import r1, r2, r3, r4, r5, rmr89

class TestRMR89(unittest.TestCase):
    # Test function r1
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
    
    # assertNotEqual
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

    # Test function r2
    def test_r2_1(self):
        self.assertEqual(r2(100),20)

    def test_r2_2(self):
        self.assertEqual(r2(90),20)

    def test_r2_3(self):
        self.assertEqual(r2(89),17)

    def test_r2_4(self):
        self.assertEqual(r2(75),17)

    def test_r2_5(self):
        self.assertEqual(r2(74),13)

    def test_r2_6(self):
        self.assertEqual(r2(50),13)

    def test_r2_7(self):
        self.assertEqual(r2(49),8)

    def test_r2_8(self):
        self.assertEqual(r2(25),8)

    def test_r2_9(self):
        self.assertEqual(r2(25),8)

    def test_r2_10(self):
        self.assertEqual(r2(24),3)
    
    # assertNotEqual
    def test_r2_11(self):
        self.assertNotEqual(r2(100),3)

    def test_r2_12(self):
        self.assertNotEqual(r2(90),8)

    def test_r2_13(self):
        self.assertNotEqual(r2(89),20)

    def test_r2_14(self):
        self.assertNotEqual(r2(75),20)

    def test_r2_15(self):
        self.assertNotEqual(r2(74),8)

    def test_r2_16(self):
        self.assertNotEqual(r2(50),8)

    def test_r2_17(self):
        self.assertNotEqual(r2(49),3)

    def test_r2_18(self):
        self.assertNotEqual(r2(25),17)

    def test_r2_19(self):
        self.assertNotEqual(r2(25),20)

    def test_r2_20(self):
        self.assertNotEqual(r2(24),17)

    # Test function r3
    def test_r3_1(self):
        self.assertEqual(r3(2.1),20)

    def test_r3_2(self):
        self.assertEqual(r3(2.0),15)

    def test_r3_3(self):
        self.assertEqual(r3(1.7),15)

    def test_r3_4(self):
        self.assertEqual(r3(0.6),15)

    def test_r3_5(self):
        self.assertEqual(r3(0.55),10)

    def test_r3_6(self):
        self.assertEqual(r3(0.2),10)

    def test_r3_7(self):
        self.assertEqual(r3(0.19),8)

    def test_r3_8(self):
        self.assertEqual(r3(0.06),8)

    def test_r3_9(self):
        self.assertEqual(r3(0.055),5)
    
    # assertNotEqual
    def test_r3_10(self):
        self.assertNotEqual(r3(2.1),15)

    def test_r3_11(self):
        self.assertNotEqual(r3(2.0),20)

    def test_r3_12(self):
        self.assertNotEqual(r3(1.7),20)

    def test_r3_13(self):
        self.assertNotEqual(r3(0.6),10)

    def test_r3_14(self):
        self.assertNotEqual(r3(0.55),15)

    def test_r3_15(self):
        self.assertNotEqual(r3(0.2),15)

    def test_r3_16(self):
        self.assertNotEqual(r3(0.19),20)

    def test_r3_17(self):
        self.assertNotEqual(r3(0.06),15)

    def test_r3_18(self):
        self.assertNotEqual(r3(0.055),10)
    

if __name__ == '__main__':
    unittest.main()