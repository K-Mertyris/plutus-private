"""
    This function's purpose is to read a pipe-delimited CSV file into a
    pandas dataframe. Another part of plutus will pick up the data from the
    dataframe, this function's sole purpose is to just read and store data into
    a variable
"""

# import pandas library for dataframes
import pandas as pd

# create an empty dataframe
my_df = pd.DataFrame()

# read bank file
my_df = pd.read_csv('.\\draft-private\\bank.csv')

# print output
print(my_df)
