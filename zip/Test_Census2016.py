'''
CS 5001 Milestone1
Fall 2022
Steven
Test_Census2016.py
'''

import unittest
from Census2016 import *

class Test_Census2016(unittest.TestCase):
    def test_init(self):
        mycensus2016 = Census2016("Chinese",5000,2600,2400)
        self.assertEqual(mycensus2016.minority_name,"Chinese")
        self.assertEqual(mycensus2016.total_population,5000)
        self.assertEqual(mycensus2016.male_population,2600)
        self.assertEqual(mycensus2016.female_population,2400)
        
    def test_bad_init(self):
        with self.assertRaises(TypeError):
            mycensus2016_1 = Census2016(201,21,12,21)
            mycensus2016_2 = Census2016("Chinese","121",21,21)
            mycensus2016_3 = Census2016("Chinese",21,21,21.12)

    def test_str(self):
        mycensus2016 = Census2016("Chinese",5000,2600,2400)
        self.assertEqual(str(mycensus2016),"Chinese has population of 5000 in 2016, with 2600 males and 2400 females")
    
    def test_bad_str(self):
        with self.assertRaises(TypeError):
            Census2016.__str__("hello")
    
    def test_eq(self):
        mycensus2016_1 = Census2016("Chinese",6000,3000,3000)
        mycensus2016_2 = Census2016("Chinese",5000,2600,2400)
        mycensus2016_3 = Census2016("Arab",4000,2000,2000)
        self.assertEqual(mycensus2016_1 == mycensus2016_2, True)
        self.assertEqual(mycensus2016_2 == mycensus2016_3, False)

    def test_bad_eq(self):
        mycensus2016_1 = Census2016("Chinese",6000,3000,3000)
        with self.assertRaises(TypeError):
            mycensus2016_1.__eq__("Hello")
            
def main():

     unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()