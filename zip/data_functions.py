'''
CS 5001 Milestone1
Fall 2022
Steven
data_functions.py
'''

import requests
import pandas
from requests.exceptions import HTTPError
from Census2016 import *
from Census2021 import *

SPLIT_ROWS = "\n"
SPLIT_COLUMNS = ","
STRIP = " \"\'"
START_ROW_2016 = 1327
END_ROW_2016 = 1337
START_ROW_2021 = 1688
END_ROW_2021 = 1698
MINORITY_NAME_COLUMN_INDEX = 1
TOTAL_POPULATION_COLUMN_INDEX = 3
MALE_POPULATION_COLUMN_INDEX = 5
FEMALE_POPULATION_COLUMN_INDEX = 7
DECIMAL_DIGITS = 4
HEADERS = ("Minority Name","Total Counts","Male Counts","Female Counts","Total Growth Rate","Male Growth Rate","Female Growth Rate")

def read_url(url):
    '''
    Name -- read_url
        purpose: to open url, read content from it and return such content.
    Parameters:
        url -- a string, web address
    Returns:
        a string, the content from website
    Raises:
        HTTPError
        OtherError
    '''
    try:
        response = requests.get(url) # get or retrieve data from a specified resource
        response.raise_for_status() # if request successfully, program will proceed without exception raised
        text = response.text
        return text # return content from url
    except HTTPError as http_err:
        raise HTTPError(f'HTTP error occurred{http_err}')
    except ConnectionError as conn_err:
        raise ConnectionError(f'Connection error occurred: {conn_err}') 

def split_rows(content):
    '''
    Name/Purpose: split_rows, spilt the content into rows and add them to a list
    Parameters: content, a string, the content read from the website
    Returns: rows, a list of all rows
    Raises: TypeError
    '''
    if not isinstance(content,str):
        raise TypeError("This function takes string")
    rows = content.split(SPLIT_ROWS) # split by new line character '\n'
    return rows
    
def clean_data(rows,start_row,end_row):
    '''
    Name/Purpose: clean2016data -- Clean the data in Census2016, split into columns and strip punctuation
    Parameters: rows -- a list, which include all the rows of Census 2016
    Returns: new_list, a list that have been cleaned, which is a table from row 1327 to row 1337
    Raises: TypeError
    '''
    if not isinstance(rows,list):
        raise TypeError("This function takes list")
    new_list = []
    for i in rows[start_row:end_row]: # extract the rows we need
        column = i.split(SPLIT_COLUMNS) # split by comma ','
        new_row = []
        for j in column:
            new_row.append(j.strip(STRIP)) # strip quote
        new_list.append(new_row)
    return new_list
    

def import_to_2016class(cleaned_data):
    '''
    Name/Purpose: import_to_2016class, for each list in the list, create an object in Census2016 class
    Parameters: cleaned_data, a list of list, the list in the list are attributes we need to set in the class
    Returns: new_list, a list of objects, we append the object we created into a list
    Raises:TypeError
    '''
    if not isinstance(cleaned_data,list):
        raise TypeError("This function takes list")
    new_list = []
    for lst in cleaned_data: # extract the columns we need (1,3,5,7), remove the blank space columns，convert string into integer
        new_list.append(Census2016(lst[MINORITY_NAME_COLUMN_INDEX],int(lst[TOTAL_POPULATION_COLUMN_INDEX]),int(lst[MALE_POPULATION_COLUMN_INDEX]),int(lst[FEMALE_POPULATION_COLUMN_INDEX])))
    return new_list

def import_to_2021class(cleaned_data):
    '''
    Name/Purpose: import_to_2021class, for each list in the list, create an object in Census2021 class
    Parameters: cleaned_data, a list of list, the list in the list are attributes we need to set in the class
    Returns: new_list, a list of objects, we append the object we created into a list
    Raises:TypeError
    '''
    if not isinstance(cleaned_data,list):
        raise TypeError("This function takes list")
    new_list = []
    for lst in cleaned_data: # extract the columns we need (1,3,5,7), remove the blank space columns
        new_list.append(Census2021(lst[MINORITY_NAME_COLUMN_INDEX],int(lst[TOTAL_POPULATION_COLUMN_INDEX]),int(lst[MALE_POPULATION_COLUMN_INDEX]),int(lst[FEMALE_POPULATION_COLUMN_INDEX])))
    return new_list

def analyze_data(objectlst2016,objectlst2021):
    '''
    Name/Purpose: analyze_data -- calculate the minority population counts and percentage change in Vancouver from 2016 to 2021. and add each kind of results to a seperate list
    Parameters: 
        objectlst2016 -- list of Census2016 objects
        objectlst2021 -- list of Census2021 objects
    Returns: a list, contains seven lists: minority_name,total_counts,male_counts,female_counts,total_percentages,male_percentages,female_percentages
    Raises: TypeError
    '''
    if not (isinstance(objectlst2016,list) and isinstance(objectlst2021,list)):
        raise TypeError("This function takes list")
    minority_name = []
    total_counts = []
    male_counts = []
    female_counts = []
    total_percentages = []
    male_percentages = []
    female_percentages = []
    for i in range(len(objectlst2016)):
        if not(isinstance(objectlst2016[i],Census2016) and isinstance(objectlst2021[i],Census2021)):
            raise TypeError("the element in the list must be Census2016 or Census2021")
        # append minority name in a list
        minority_name.append(objectlst2021[i].minority_name)
        # calculate counts change
        total_counts.append(objectlst2021[i].total_population - objectlst2016[i].total_population) 
        male_counts.append(objectlst2021[i].male_population - objectlst2016[i].male_population)
        female_counts.append(objectlst2021[i].female_population - objectlst2016[i].female_population)
        # calculate growth rate
        total_percentages.append(round(objectlst2021[i].total_population / objectlst2016[i].total_population - 1,DECIMAL_DIGITS)) #round to 4 digits
        male_percentages.append(round(objectlst2021[i].male_population / objectlst2016[i].male_population - 1,DECIMAL_DIGITS))
        female_percentages.append(round(objectlst2021[i].female_population / objectlst2016[i].female_population - 1,DECIMAL_DIGITS))
    return [minority_name,total_counts,male_counts,female_counts,total_percentages,male_percentages,female_percentages]

def create_dictionary(lst):
    '''
    Name/Purpose: create_dictionary -- connect lists with headers, which help create panda dataframe.
    Parameters: lst -- a list created in analysis step
    Returns: dictionanry -- a dictionary, keys are headers, values are lists.
    Raises: TypeError
    '''
    if not isinstance(lst,list):
        raise TypeError("This function takes list")
    if len(lst) != 7:
        raise IndexError("The list should have 7 elements")
    dictionary = {}
    for i in range(len(HEADERS)): # add header to each list
        if not isinstance(lst[i],list):
            raise TypeError("The element should be list")
        dictionary[HEADERS[i]] = lst[i] #create a dictionary, keys are headers, values are lists 
    return dictionary

def create_panda_dataframe(dictionary):
    '''
    Name/Purpose: dataframe, create a panda dataframe
    Parameters: dictionary, a dictionary, headers are keys, lists are values. 
    Returns: dataframe, a panda dataframe 
    Raises: TypeError
    '''
    if not isinstance(dictionary,dict):
        raise TypeError("This function takes dictionary")
    dataframe = pandas.DataFrame(dictionary)
    return dataframe
    
