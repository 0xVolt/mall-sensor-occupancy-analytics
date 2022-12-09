# This python script file generates a csv file that simulates the data that's being generated off of an Arduino sensor. We'll then import that csv file to perform some analytics so the pipeline is up and running for when we go to real-time analytics. 

# Import libraries
import pandas as pd
import numpy as np

# Number of data points to create
numberOfDataPoints = 500

# Creating a list of columns for our data frame
listOfEntryColumns = ['Store 1 - Entry', 'Store 2 - Entry', 'Store 3 - Entry']
listOfExitColumns = ['Store 1 - Exit', 'Store 2 - Exit', 'Store 3 - Exit']

# Creating our random data points in the range [-1, 1]
listOfEntryRandomNumbers = np.random.randint(0, 2, size=(numberOfDataPoints, len(listOfEntryColumns)))
listOfExitRandomNumbers = np.random.randint(-1, 1, size=(numberOfDataPoints, len(listOfExitColumns)))

# Creating a data frame of those points
entryDataFrame = pd.DataFrame(listOfEntryRandomNumbers, columns=listOfEntryColumns)
exitDataFrame = pd.DataFrame(listOfExitRandomNumbers, columns=listOfExitColumns)

# print(exitDataFrame)

df = pd.concat([entryDataFrame, exitDataFrame], axis=1)

df['Main Gate - Entry'] = df[listOfEntryColumns].sum(axis=1)
df['Main Gate - Exit'] = df[listOfExitColumns].sum(axis=1)

print(df)

# Writing the data frame to a .csv file
df.to_csv(r'./data.csv')
