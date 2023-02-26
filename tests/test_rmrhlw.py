import unittest
from src.geotekppu.rmr.rmr_hlw_tong_etal2022 import AdjustedR1ucs, AdjustedR2, AdjustedR3, CalcR7, CalcR8


class TestRMRhlw(unittest.TestCase):
    
    # Test function AdjustedR1ucs
    def test_AdjustedR1_1(self):
        self.assertEqual(AdjustedR1ucs(200),12.4981)

    def test_AdjustedR1_2(self):
        self.assertEqual(AdjustedR1ucs(245),14.215)

    def test_AdjustedR1_3(self):
        self.assertEqual(AdjustedR1ucs(25),3.3421)
    
    def test_AdjustedR1_2(self):
        self.assertEqual(AdjustedR1ucs(251),15)

    # Test function AdjustedR2
    def test_adjustedR2_1(self):
        self.assertEqual(AdjustedR2(245),48.6194)

    # Test function AdjustedR3
    def test_adjustedR3_1(self):
        self.assertEqual(AdjustedR3(2.0),20)

    def test_adjustedR3_1(self):
        self.assertEqual(AdjustedR3(1.9),19.1897)
    
    # Test function CalcR7
    def test_adjustedR7_1(self):
        self.assertEqual(CalcR7(-4,80),-320)


    # Test function CalcR8
    def test_adjustedR8_1(self):
        self.assertEqual(CalcR8(0.6),-4.80)

if __name__ == '__main__':
    unittest.main()