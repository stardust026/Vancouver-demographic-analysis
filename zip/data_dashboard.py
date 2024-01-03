'''
CS 5001 Milestone1
Fall 2022
Steven
data_dashboard.py
'''

from data_functions import *
from Census2016 import *
from Census2021 import *
from data_view import *
from data_controller import *

URL2016 = "https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/current-actuelle.cfm?Lang=E&Geo1=CSD&Code1=5915022&Geo2=PR&Code2=01&B1=All&type=0&FILETYPE=CSV"
URL2021 = "https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/current-actuelle.cfm?Lang=E&SearchText=vancouver&DGUIDlist=2021A00055915022&GENDERlist=1,2,3&STATISTIClist=1&HEADERlist=0&FILETYPE=CSV"


def main():
    try:
        #Request
        text2016 = read_url(URL2016)
        text2021 = read_url(URL2021)

        #Clean data
        data2016 = split_rows(text2016)
        data2021 = split_rows(text2021)
        data2016 = clean_data(data2016,START_ROW_2016,END_ROW_2016)
        data2021 = clean_data(data2021,START_ROW_2021,END_ROW_2021)
        data2016.sort()
        data2021.sort()

        #Import to class
        objectlst2016 = import_to_2016class(data2016)
        objectlst2021 = import_to_2021class(data2021)

        #Analyze
        result = analyze_data(objectlst2016,objectlst2021)
        
        #Create dictionary and data frame
        dictionary = create_dictionary(result)      
        dataframe = create_panda_dataframe(dictionary)
        print(dataframe)

        #User interaction and visualization
        root = Tk() #create a top level tk window
        app = Controller(root,dataframe)
        root.mainloop() #enter tk event loop, wait to react to the button presses

    
    except ValueError:
        print("Please check the arguments you are passing.")
    except TypeError:
        print("Please check the arguments you are passing.")
    except HTTPError:
        print("HTTP error occurred.")
    except ConnectionError:
        print("Connection error occurred.")
    except IndexError:
        print("IndexError occured.")
    

if __name__ == "__main__":
    main()
