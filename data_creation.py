
# This data set will be about the crime rates in Chicago ILL from the years of 2012 and before
# the data needs ot be cleaned, making sure there is no NAN values or if there is to make it NAN
# I will grab the top three crimes as these will be our tiles
# libraries used will be pandas
# once the crimes are grabbed they will be mapped in QGIS, and then transformed into tiles as layer maps to be used


# imports here
import pandas as pd

# read csv file
crimes_data = pd.read_csv("path/to/fle")

# We want to filter by primary type, so count the rows of primary type
crimes = (crimes_data.groupby('Primary Type').count()) # this will give the counts for all columns

#print(crimes.sort_values('ID')) # This sorts the values from low to high

# Top three types are Theft with 75464, Battery with 59137 and Criminal Damage with 35855 cases
"""
CRIMINAL DAMAGE                   35855
BATTERY                           59137
THEFT                             75464
"""


def create_table(data_set, column_name, row_wanted): # select the rows where the primary type == Theft
    """
    This function creates data frames taking in a data set, a column and the
    specific row we want from the column
    """
    new = data_set.loc[data_set[column_name] == row_wanted] 
    return new

def count_null(data_set, column_name, data_set_name):
    """
    This function prints how many null values a column has taking
    in a dataset and a column name. The column name needs to be in string
    format, I am counting how may null coordinates to report how much missing
    data the map will be missing.
    """
    counts = (data_set[column_name].isna().sum())
    return("there is "+counts+" null values in the "+column_name+" column for the "+data_set_name+"dataset")

def create_csv(data_set, filename):
    """
    this function creates a csv file to path name. Taking in a dataset
    and creating a path.
    Path name is hardcoded but it can change and submitting this code the github
    its been removed. TODO: REMOVE THE PATH PLEASE
    """
    data_set.to_csv('/path_to_desktop/'+filename+'.csv')

theft = create_table(crimes_data, 'Primary Type', 'THEFT') # 20 null
battery = create_table(crimes_data, 'Primary Type', 'BATTERY') # 12 null
criminal_damage = create_table(crimes_data, 'Primary Type', 'CRIMINAL DAMAGE') # 2 null values

# Creating CSV files from top three crimes these are filtered and ready to download by using the create_csv function
#create_csv(theft, 'theftdata') 
#create_csv(battery, 'batterydata')
#create_csv(criminal_damage, 'criminaldamage')

#TODO: move these to QGIS and export them as tiles
# edit the HTML file,

