## Overview of the dataframe
# %%
import pandas

data = pandas.read_csv('reviews.csv')
print(data.hist('Rating'))
# %%
data['Rating'] #selecting one column
# data['Rating'].mean() #average
# %%
# to select multiple columns you pass a list in the df
data[['Rating', 'Course Name']]
# %%
data['Timestamp'].iloc[2] #is like a slice
# %%
# Filtering based on conditions
data[data['Rating'] > 4]

# Multiple conditions
data[(data['Rating'] > 4) & (data['Course Name'] == 
'The Complete Python Course: Build 10 Professional OOP Apps')]
# %%
