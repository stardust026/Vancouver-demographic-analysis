'''
CS 5001 Milestone1
Fall 2022
Steven
Test_functions.py
'''

import unittest
from data_functions import *

TESTURL = "https://gist.githubusercontent.com/LoganWS/b944ee355fdef4d1df9d3e1a26227233/raw/083e5f9afc6eeaed9c859ae3faacfd0dfd3aed9e/parks_name_neighbourhood.txt"
BADURL = "http://www.example.com/page-not-found"

class Test_fuctions(unittest.TestCase):
    def test_read_url(self):
        text = read_url(TESTURL)
        self.assertEqual(text[0:4],"Name")
    
    def test_bad_read_url(self):
        with self.assertRaises(HTTPError):
            read_url(BADURL)
        
    def test_split_rows(self):
        string = "hello\nhi"
        self.assertEqual(split_rows(string),["hello","hi"])
    
    def test_bad_split_rows(self):
        with self.assertRaises(TypeError):
            split_rows(90)
    
    def test_clean_data(self):
        case1 = ["data1,data2,data3\"\'","\'data4,data5,data6"]
        actual = clean_data(case1,0,2)
        expected = [["data1","data2","data3"],["data4","data5","data6"]]
        self.assertEqual(actual,expected)
    
    def test_bad_clean_data(self):
        with self.assertRaises(TypeError):
            clean_data("hello")

    def test_import_to_2016class(self):
        list1 = [["","Chinese","","123","","123","","123"]]
        objectlst = import_to_2016class(list1)
        self.assertEqual(objectlst[0],Census2016("Chinese",123,123,123))
    
    def test_bad_import_to_2016class(self):
        with self.assertRaises(TypeError):
            import_to_2016class("hello")
            import_to_2016class(123)
    
    def test_import_to_2021class(self):
        list1 = [["","Chinese","","123","","123","","123"]]
        objectlst = import_to_2021class(list1)
        self.assertEqual(objectlst[0],Census2021("Chinese",123,123,123))
    
    def test_bad_import_to_2016class(self):
        with self.assertRaises(TypeError):
            import_to_2021class("hello")
            import_to_2021class(123)

    def test_analyze_data(self):
        objectlst2016 = [Census2016("Chinese",1000,600,400)]
        objectlst2021 = [Census2021("Chinese",2000,1200,800)]
        returnlst = analyze_data(objectlst2016,objectlst2021)
        self.assertEqual(returnlst[0][0],"Chinese")
        self.assertEqual(returnlst[1][0],1000)
        self.assertEqual(returnlst[2][0],600)
        self.assertEqual(returnlst[3][0],400)
        self.assertEqual(returnlst[4][0],1)
        self.assertEqual(returnlst[5][0],1)
        self.assertEqual(returnlst[6][0],1)

    def test_bad_analyze_data(self):
        with self.assertRaises(TypeError):
            analyze_data("hello","hi")
            analyze_data([1,12],[12,1])
    
    def test_create_dictionary(self):
        lst = [["Chinese"],[1000],[600],[400],[1],[1],[1]]
        dictionary = create_dictionary(lst)
        self.assertEqual(dictionary["Minority Name"],["Chinese"])
        self.assertEqual(dictionary["Total Counts"],[1000])
        self.assertEqual(dictionary["Male Growth Rate"],[1])

    def test_bad_create_dictionary(self):
        lst1 = ["Chinese",[1000],[600],[400],[1],[1],[1]]
        lst2 = [["Chinese"],[1000],[600],[400],[1],[1]]
        with self.assertRaises(TypeError):
            create_dictionary("hello")
            create_dictionary(lst1)
        with self.assertRaises(IndexError):
            create_dictionary(lst2)
    
    def test_create_panda_dataframe(self):
        dictionary = {"Minority Name":["Chinese"]}
        actual = create_panda_dataframe(dictionary) 
        expected = pandas.DataFrame(dictionary)
        pandas.testing.assert_frame_equal(actual,expected)

    def test_bad_create_panda_dataframe(self):
        with self.assertRaises(TypeError):
            create_dictionary("hello")

def main():

     unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()