import unittest
from src.geotekppu.rmr.rmr__celada_etal2014 import f0, f_excavation, f_stresstrain


class TestRMR14(unittest.TestCase):
    # Test f0 function
    def test_f0_1(self):
        self.assertEqual(f0("dwd",30),-2)

    def test_f0_2(self):
        self.assertEqual(f0("dwd",20),-2)

    def test_f0_3(self):
        self.assertEqual(f0("dwd",44),-2)

    def test_f0_4(self):
        self.assertEqual(f0("dwd",45),0)

    def test_f0_5(self):
        self.assertEqual(f0("dwd",90),0)
    
    # test value < 20 and > 90 with "dwd" as strike orientation ()
    def test_f0_6(self):
        self.assertEqual(f0("dwd",91),None)

    def test_f0_7(self):
        self.assertEqual(f0("dwd",19),None)

    def test_f0_8(self):
        self.assertEqual(f0("dad",91),None)

    def test_f0_9(self):
        self.assertEqual(f0("dad",19),None)

    def test_f0_10(self):
        self.assertEqual(f0("parallel",91),None)

    def test_f0_11(self):
        self.assertEqual(f0("parallel",19),None)

    def test_f0_12(self):
        self.assertEqual(f0("irrespective",21),None)
    
    # Test f_excavation function
    def test_f_excav_1(self):
        self.assertEqual(f_excavation(39),1.3042)

    def test_f_excav_2(self):
        self.assertEqual(f_excavation(41),1.28)

    def test_f_excav_3(self):
        self.assertEqual(f_excavation(40),1.32)


if __name__ == '__main__':
    unittest.main()