'''
CS 5001 Milestone1
Fall 2022
Steven
Census2016.py
'''

class Census2016:
    '''
    Class Census2016
    Attributes: minority_name,total_population,male_population,female_population
    Methods: __str__, __eq__
    '''
    def __init__(self,minority_name,total_population,male_population,female_population):
        '''
        Name/Purpose:__init__ -- constructor
        Parameters:
            self -- the current object
            minority_name -- a string, the visible minority name
            total_population -- an integer, the total population of minority in vancouver in 2016
            male_population -- an integer, the male population of minority in vancouver in 2016
            female_population -- an integer, the female population of minority in vancouver in 2016
        Returns: None
        Raises: TypeError
        '''
        if not(isinstance(minority_name,str) and isinstance(total_population,int)and isinstance(male_population,int)and isinstance(female_population,int)):
            raise TypeError
        self.minority_name = minority_name
        self.total_population = total_population
        self.male_population = male_population
        self.female_population = female_population
    
    def __str__(self):
        '''
        Name/Purpose:__str__, Returns a string representation of instance
        Parameters: self -- the current object
        Returns: string, a string representation of instance
        Raises: TypeError
        '''
        if not isinstance(self,Census2016):
            raise TypeError
        string = "{} has population of {} in 2016, with {} males and {} females".format(self.minority_name,self.total_population,self.male_population,self.female_population)
        return string
    
    def __eq__(self,other):
        '''
        Name/Purpose: __eq__ -- Compares current minority name to another one
        Parameter:
            self -- the current object
            other -- another Census2016
        Return: a boolean -- Returns True if they have same name, and False otherwise
        Raise: TypeError
        '''
        if not (isinstance(self,Census2016) and isinstance(other,Census2016)):
            raise TypeError
        return self.minority_name == other.minority_name
    

    
    
    
    
    
    



