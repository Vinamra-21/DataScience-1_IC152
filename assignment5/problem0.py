import numpy
import pandas as pd
# Use pandas to read the CSV
csvData = pd.read_csv('Data.csv', sep=',')
# Convert dataframe into a numpy array into a list(of lists)
csvDataDf=pd.DataFrame(csvData)
data = csvDataDf.to_numpy().tolist()
print(data,'\n')