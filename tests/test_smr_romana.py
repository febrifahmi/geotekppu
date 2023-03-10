import unittest
from src.geotekppu.rmr.smr__romana_ts2015 import F1, F2, F3, F4, SMR2015 


class TestSMRromana(unittest.TestCase):
    
    # Test function F1
    def test_F1_1(self):
        self.assertEqual(F1("P",120,60),0.15)
    
    def test_F1_2(self):
        self.assertEqual(F1("P",90,60),0.40)
    
    def test_F1_3(self):
        self.assertEqual(F1("P",75,60),0.70)
    
    def test_F1_4(self):
        self.assertEqual(F1("P",66,60),0.85)
    
    def test_F1_5(self):
        self.assertEqual(F1("P",65,60),1.00)
    
    # Test function F2
    def test_F2_1(self):
        self.assertEqual(F2("P",55),1.0)
    
    def test_F2_2(self):
        self.assertEqual(F2("P",45),1.0)
    
    def test_F2_3(self):
        self.assertEqual(F2("P",44),0.85)
    
    def test_F2_4(self):
        self.assertEqual(F2("P",35),0.85)
    
    def test_F2_5(self):
        self.assertEqual(F2("P",34),0.70)
    
    def test_F2_6(self):
        self.assertEqual(F2("P",30),0.70)
    
    def test_F2_7(self):
        self.assertEqual(F2("P",29),0.40)
    
    def test_F2_8(self):
        self.assertEqual(F2("P",20),0.40)
    
    def test_F2_9(self):
        self.assertEqual(F2("P",19),0.15)

    # Test function F3
    def test_F3_1(self):
        self.assertEqual(F3("P",45,20),0)
    
    def test_F3_2(self):
        self.assertEqual(F3("P",25,20),-6)
    
    def test_F3_3(self):
        self.assertEqual(F3("P",20,20),-25)
    
    def test_F3_4(self):
        self.assertEqual(F3("P",11,20),-50)
    
    def test_F3_5(self):
        self.assertEqual(F3("P",1,20),-60)

    # Test function F4
    def test_F4_1(self):
        self.assertEqual(F4("pre"),10)
    
    def test_F4_2(self):
        self.assertEqual(F4("sb"),8)
    
    def test_F4_3(self):
        self.assertEqual(F4("ns"),15)
    
    def test_F4_4(self):
        self.assertEqual(F4("bm"),0)

    # Test function SMR2015
    def test_SMR2015_1(self):
        self.assertEqual(SMR2015(60,0.40,0.70,-6,15),73.32)
    
    def test_SMR2015_2(self):
        self.assertEqual(SMR2015(60,0.15,0.15,0,15),75)
    
    def test_SMR2015_3(self):
        self.assertEqual(SMR2015(45,0.15,0.15,0,15),60)
    
    def test_SMR2015_4(self):
        self.assertEqual(SMR2015(75,0.15,0.15,0,15),90)



if __name__ == '__main__':
    unittest.main()