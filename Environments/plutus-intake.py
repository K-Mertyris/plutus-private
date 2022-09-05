"""
    This function's purpose is to read a pipe-delimited CSV file into a
    pandas dataframe. Another part of plutus will pick up the data from the
    dataframe, this function's sole purpose is to just read and store data into
    a variable
"""

# import pandas library for dataframes, import re for regex
import pandas as pd
import re

# TEST: read unformatted csv file, store data, display

# create an empty dataframe
my_df = pd.DataFrame()

# read bank file
my_df = pd.read_csv('.\\draft-private\\bank.csv', sep='|')

# print output
print(my_df)
