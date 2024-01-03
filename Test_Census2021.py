'''
CS 5001 Milestone1
Fall 2022
Steven
Test_Census2021.py
'''

import unittest
from Census2021 import *

class Test_Census2021(unittest.TestCase):
    def test_init(self):
        mycensus2021 = Census2021("Chinese",5000,2600,2400)
        self.assertEqual(mycensus2021.minority_name,"Chinese")
        self.assertEqual(mycensus2021.total_population,5000)
        self.assertEqual(mycensus2021.male_population,2600)
        self.assertEqual(mycensus2021.female_population,2400)
        
    def test_bad_init(self):
        with self.assertRaises(TypeError):
            mycensus2021_1 = Census2021(201,21,12,21)
            mycensus2021_2 = Census2021("Chinese","121",21,21)
            mycensus2021_3 = Census2021("Chinese",21,21,21.12)

    def test_str(self):
        mycensus2021 = Census2021("Chinese",5000,2600,2400)
        self.assertEqual(str(mycensus2021),"Chinese has population of 5000 in 2021, with 2600 males and 2400 females")
    
    def test_bad_str(self):
        with self.assertRaises(TypeError):
            Census2021.__str__("hello")
    
    def test_eq(self):
        mycensus2021_1 = Census2021("Chinese",6000,3000,3000)
        mycensus2021_2 = Census2021("Chinese",5000,2600,2400)
        mycensus2021_3 = Census2021("Arab",4000,2000,2000)
        self.assertEqual(mycensus2021_1 == mycensus2021_2, True)
        self.assertEqual(mycensus2021_2 == mycensus2021_3, False)

    def test_bad_eq(self):
        mycensus2021_1 = Census2021("Chinese",6000,3000,3000)
        with self.assertRaises(TypeError):
            mycensus2021_1.__eq__("Hello")
            
def main():

     unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()