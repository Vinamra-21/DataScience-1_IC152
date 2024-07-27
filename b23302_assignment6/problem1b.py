#importing required modules
import sys
import os
import matplotlib.pyplot as plt

#using command line argument accept the files otherwise throw error
errorMsg='''Input file not provided.
          Example:Follow the next 5 steps to run “samplescript.py” on the terminal with command line arguments.
                  1.Click on properties where your assignment folder is located.
                  2.Copy the path under attribute “Parent folder:”
                  3.Click on “Activities” in top right of Ubuntu (Linux) and type terminal.
                  4.write “cd ” (cd followed by a space) and then paste the copied path using “Shift + Ctrl + V” keys.
                  5.Now you can “cd Assignment6/” and then write “python3 samplescript.py problem1b_i_xy problem1b_ii_xy” (note: sampleScriptOutput.csv will be created in /Assignment6)'''

   
#main program
#input files
def main():
    result=False 
    if len(sys.argv) <= 1:
        print("Please enter the file names in the terminal.")
    else:
        #function to check weather the values are correct or not if not raise error
        def checkIfCorrectValue():
            x,y=[],[]

            for i in lst[0]:
                x.append(i)
            for j in lst[1]:
                y.append(j)
            
            x.remove('\n')

            #check of same number of values for x and y
            #check for variable is either x or y
            if x[0]=='x' and y[0]=='y':
                pass
            elif len(x)!=len(y):
                raise ValueError('x and y must be the same size')
            else:
                raise ValueError('Variable must be x or y')
            
            #check for only integers are there as values of x and y
            for j in range(1,len(x)):
                if x[j] in ' +-1234567890':  
                    pass
                else:
                    raise ValueError('The values for x and y are not correct.Please recheck the values')
            for j in range(1,len(y)):
                if y[j] in ' +-1234567890':
                    pass
                else:
                    raise ValueError('The values for x and y are not correct.Please recheck the values')
        for i in sys.argv:
            if os.path.isfile(i) == True:
                result = True
            else:
                print(f"{i} is not available\n")
                print(errorMsg)
                sys.argv.remove(i)
                main()
                exit()

        if result == True :
            #iteratinon on all files
            for i in range(1,len(sys.argv)):
                #opening and reading the files
                with open(sys.argv[i]) as x:
                    lst = x.readlines()
                    #check values and raise error if any
                    checkIfCorrectValue()

                    xList_temp=lst[0].split()[1:] #list of x values
                    for t in xList_temp:
                        #check for only + or only - as value
                        if t in '+-':
                            raise ValueError('The values for x and y are not correct.Please recheck the values')                 

                    yList_temp=lst[1].split()[1:]  #list of y values
                    for t in yList_temp:   
                        #check for only + or only - as value 
                        if t in '+-':
                            raise ValueError('The values for x and y are not correct.Please recheck the values')
                    
                    yList=[int(t) for t in yList_temp]
                    xList=[int(t) for t in xList_temp]

                    #scatter plot
                    plt.scatter(xList,yList)
                    plt.title(f"problem1b_{'i'*(i)}_xy")          #title for scatter plot
                    plt.grid(True)
                    #x and y labels
                    plt.xlabel('X-Values')
                    plt.ylabel('Y-values')
                    plt.savefig(f"prob1b_{'i'*i}_xy.png")         #saving the plot
                    plt.clf() #clearing!
            for i in sys.argv[1::]:
                #printing if the plot is completed
                print(f"The plotting of {i} is now complete.You can check the graph!!")
        else:
            print(errorMsg)
                

main()
