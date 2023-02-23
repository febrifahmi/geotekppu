import unittest
from src.geotekppu.rmr.rmr_hlw_tong_etal2022 import AdjustedR1ucs, AdjustedR2


class TestRMRhlw(unittest.TestCase):
    
    # Test function AdjustedR1ucs
    def test_AdjustedR1_1(self):
        self.assertEqual(AdjustedR1ucs(200),1.0968)
    
    def test_AdjustedR1_2(self):
        self.assertEqual(AdjustedR1ucs(251),15)

    # Test function AdjustedR2
    def test_adjustedR2_1(self):
        self.assertEqual(AdjustedR2(245),48.6194)

if __name__ == '__main__':
    unittest.main()