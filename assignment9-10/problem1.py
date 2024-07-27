#importing required modules
import pandas as pd
import sys
import os


#1a

df = pd.read_csv("data/Cars93.csv")   #read csv file
sortModel = sorted(df['Model'].unique())   #sort model list in ascending order
result_df=pd.DataFrame({'Model Sorted': sortModel},index=list(range(1,len(df['Model'])+1))) #creates df with sorted model list
result_df.to_csv('problem1a.csv') #write result to csv file


#1b

print(df.loc[df.groupby('Type')['Price'].idxmax()]) #Print all details of the costliest car of each of the ‘Types’.


#1c

if len(sys.argv)>2 or len(sys.argv)<=1: #check input in terminal
  print("Please enter correct number of arguments as 'python problem1.py Manufacturer_name'")
  exit()
else:
    if os.path.isfile(sys.argv[0]) == True: #input file exists or not
        if (sys.argv[1] in df['Manufacturer'].unique()): #input name exists or not
            print(df[df['Manufacturer']==f'{sys.argv[1]}'])
        else:
            print('The entered manufacturer is not present in the table please recheck')
            exit()
    else:
        print(f"{sys.argv[0]} is not available\n") 
        print('The entered files doesnot exist please enter correct files')
        exit()


#1d

ManufacturerName= df['Manufacturer'].unique() #list of manufacturers
countManufacturer=[]
for i in ManufacturerName:
    countManufacturer.append(df['Manufacturer'].eq(i).sum()) #appends the number of times the name occoured to the list

result_df=pd.DataFrame({'Manufacturer': ManufacturerName, 'Count' : countManufacturer},index=list(range(1,len(ManufacturerName)+1))) #creates df with manufacturers list and count
result_df.to_csv('problem1d.csv')  #write result to csv file

