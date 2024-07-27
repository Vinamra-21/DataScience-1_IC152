import sys
import csv
import os
#using command line argument accept the files otherwise throw error
errorMsg='''Input file not provided.
          Example:Follow the next 5 steps to run “samplescript.py” on the terminal with command line arguments.
                  1.Click on properties where your assignment folder is located.
                  2.Copy the path under attribute “Parent folder:”
                  3.Click on “Activities” in top right of Ubuntu (Linux) and type terminal.
                  4.write “cd ” (cd followed by a space) and then paste the copied path using “Shift + Ctrl + V” keys.
                  5.Now you can “cd Assignment6/” and then write “python3 samplescript.py problem1b_i_xy problem1b_ii_xy” (note: sampleScriptOutput.csv will be created in /Assignment6)'''

#file
if len(sys.argv) <= 1 :
    print("please input the file.")
else:
    if os.path.isfile(sys.argv[1])==True:
        #new dictionary to count the frequency of words
        new_dict={}
        #opening and reading the file
        with open(sys.argv[1], encoding='utf-8') as user_data:
            text = user_data.read()
            # code to count the frequency of each word
            for i in text.split():
                if i not in new_dict:
                    new_dict[i]=1
                else:
                    new_dict[i]=int(new_dict[i])+1

        #sorting the dictionary in descending order according to values
        new_dict_sort=dict(sorted(new_dict.items(), key=lambda item: item[1] ,reverse=True))

        #list of keys
        l1=list(new_dict_sort.keys())
        #list of values
        l2=list(new_dict_sort.values())

        #final  list to contain all the dictionaries 
        list_final=[]

        for i in range(len(l1)):
            #dict_temp format = {'word':key,'frequency':value}
            dict_temp={}
            dict_temp['word']=l1[i]
            dict_temp['frequency']=l2[i]
            #append all the dictionaries to list 
            list_final.append(dict_temp)

        #opening the csv file
        with open('problem2Output.csv', 'w', encoding='utf-8') as fOut:
            #defining writer using DictWriter
            writer = csv.DictWriter(fOut,fieldnames = ['word','frequency'] )
            #heading
            fOut.write('Top 10 words(According to frequency)\n\n')
            #writing the header
            writer.writeheader()
            #writing the top 10 dictionaries from list to csv file
            writer.writerows(list_final[:10])
            
            #heading
            fOut.write('\nAll words and frequency\n\n')
            #writing the header
            writer.writeheader()
            #writing the dictionaries from list to csv file
            writer.writerows(list_final)
    else : 
        print(errorMsg)  
        exit()