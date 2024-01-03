'''
CS 5001 Milestone1
Fall 2022
Steven
data_view.py
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

def make_bar_graph_from_data_frame(df1, xticklabels, title, ylabel, xlabel,ispercentage = False):
    '''
    Name/Purpose: make_bar_graph_from_data_frame
    Parameters: df1 -- a panda dataframe
                xticklabels -- list of x axis tick labels
                title -- a string, title for axes
                ylabel -- a string, label for y axis
                xlabel -- a string, label for x axis
                ispercentage -- a boolean, check if to convert y tick label into percent format, default value is False
    Returns: None
    Raises: None
    '''
    figure1, ax1 = plt.subplots()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xticklabels(xticklabels)
    ax1.set_title(title)
    ax1.set_ylabel(ylabel)
    ax1.set_xlabel(xlabel)
    if ispercentage:
        ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    figure1.autofmt_xdate()
    plt.show()

