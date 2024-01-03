'''
CS 5001 Milestone1
Fall 2022
Steven
data_controller.py
'''

from tkinter import *
from tkinter import ttk
from data_view import *


YLABEL1 = "Counts"
YLABEL2 = "Percentages"
LABELTEXT = "Please choose a dataset"
HEADER1 = "Minority Name"
HEADER2 = "Total Counts"
HEADER3 = "Male Counts"
HEADER4 = "Female Counts"
HEADER5 = "Total Growth Rate"
HEADER6 = "Male Growth Rate"
HEADER7 = "Female Growth Rate"
TITLE1 = "Vancouver minority population change (2016-2021) (Total)"
TITLE2 = "Vancouver minority population change (2016-2021) (Male)"
TITLE3 = "Vancouver minority population change (2016-2021) (Female)"
TITLE4 = "Vancouver minority population growth rate (2016-2021) (Total)"
TITLE5 = "Vancouver minority population growth rate (2016-2021) (Male)"
TITLE6 = "Vancouver minority population growth rate (2016-2021) (Female)"


class Controller:
    '''
    Class: Controller
    Attributes: df,label,button1,button2,button3,button4,button5,button6
    Methods:click_button1,click_button2,click_button3,click_button4,click_button5,click_button6
    '''
    def __init__(self, master,dataframe):
        '''
        Name/Purpose:__init__ -- constructor
        Parameters:
            self -- the current object
            master -- root
            dataframe -- panda's dataframe
            label -- a tkinter label
            button1 -- a tkinter button
            button2 -- a tkinter button
            button3 -- a tkinter button
            button4 -- a tkinter button
            button5 -- a tkinter button
            button6 -- a tkinter button
        Returns: None
        Raises: None
        '''
        self.df = dataframe
        self.label = ttk.Label(master, text = LABELTEXT)
        self.label.grid(row = 0, column = 0,columnspan = 2)
        
        self.button1 = ttk.Button(master, text = HEADER2,
                   command = self.click_button1).grid(row = 1, column = 0)

        self.button2 = ttk.Button(master, text = HEADER3,
                   command = self.click_button2).grid(row = 2, column = 0)

        self.button3 = ttk.Button(master, text = HEADER4,
                   command = self.click_button3).grid(row = 3, column = 0)

        self.button4 = ttk.Button(master, text = HEADER5,
                   command = self.click_button4).grid(row = 1, column = 1)

        self.button5 = ttk.Button(master, text = HEADER6,
                   command = self.click_button5).grid(row = 2, column = 1)
        
        self.button6 = ttk.Button(master, text = HEADER7,
                   command = self.click_button6).grid(row = 3, column = 1)
        
        

    def click_button1(self):
        '''
        Name/Purpose: click_button1 -- make a bar graph and show it when click the button1
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL1
        title = TITLE1
        return make_bar_graph_from_data_frame(self.df[HEADER2], xticklabels, title, ylabel, xlabel)

    def click_button2(self):
        '''
        Name/Purpose: click_button2 -- make a bar graph and show it when click the button2
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL1
        title = TITLE2
        return make_bar_graph_from_data_frame(self.df[HEADER3], xticklabels, title, ylabel, xlabel)

    def click_button3(self):
        '''
        Name/Purpose: click_button3 -- make a bar graph and show it when click the button3
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL1
        title = TITLE3
        return make_bar_graph_from_data_frame(self.df[HEADER4], xticklabels, title, ylabel, xlabel)

    def click_button4(self):
        '''
        Name/Purpose: click_button4 -- make a bar graph and show it when click the button4
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL2
        title = TITLE4
        return make_bar_graph_from_data_frame(self.df[HEADER5], xticklabels, title, ylabel, xlabel,ispercentage=True)
    
    def click_button5(self):
        '''
        Name/Purpose: click_button5 -- make a bar graph and show it when click the button5
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL2
        title = TITLE5
        return make_bar_graph_from_data_frame(self.df[HEADER6], xticklabels, title, ylabel, xlabel,ispercentage=True)

    def click_button6(self):
        '''
        Name/Purpose: click_button6 -- make a bar graph and show it when click the button6
        Parameters: self -- the current object
        Returns: make_bar_graph_from_data_frame
        Raises: None
        '''
        xticklabels = self.df[HEADER1].tolist()
        xlabel = HEADER1
        ylabel = YLABEL2
        title = TITLE6
        return make_bar_graph_from_data_frame(self.df[HEADER7], xticklabels, title, ylabel, xlabel,ispercentage=True)
            
