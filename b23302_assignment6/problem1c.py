#importing required modules
import sys
import os

#using command line argument accept the files otherwise throw error
errorMsg='''Input file not provided.
          Example:Follow the next 5 steps to run “samplescript.py” on the terminal with command line arguments.
                  1.Click on properties where your assignment folder is located.
                  2.Copy the path under attribute “Parent folder:”
                  3.Click on “Activities” in top right of Ubuntu (Linux) and type terminal.
                  4.write “cd ” (cd followed by a space) and then paste the copied path using “Shift + Ctrl + V” keys.
                  5.Now you can “cd Assignment6/” and then write “python3 samplescript.py problem1b_i_xy problem1b_ii_xy” (note: sampleScriptOutput.csv will be created in /Assignment6)'''

   
#main program

#final list contains final answer        
final_lst=[]

#input files
def main():
    result=False 
    if len(sys.argv) <= 1:
        print("Please enter the file names in the terminal as well")
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
            for k in range(1,len(sys.argv)):          
                #opening and reading the files
                with open(sys.argv[k]) as x:
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
                    
                    #number of x or y values
                    n=len(xList)
                    
                    #summation x_i into y_i
                    sum_XintoY=0
                    for i in range(n):
                        sum_XintoY+=xList[i]*yList[i]

                    # summation x_i into x_i    
                    sum_XintoX=0
                    for i in range(n):
                        sum_XintoX+=xList[i]*xList[i]

                    # summation y_i into y_i
                    sum_YintoY=0
                    for i in range(n):
                        sum_YintoY+=yList[i]*yList[i]

                    num=(n*sum_XintoY)-(sum(xList)*sum(yList))
                    den=((n*sum_XintoX)-(sum(xList)**2))**(1/2)*((n*sum_YintoY)-(sum(yList)**2))**(1/2)
                    
                    #final answer to be appended to list
                    r=num/den
                    final_r=f"r for problem1b_{'i'*k}_xy = {r}"
                    
                    final_lst.append(final_r)
            for i in sys.argv[1::]:
                #printing if the 'r' is computed
                print(f"The answer of {i} is computed successfully!!!")
        else:
            print(errorMsg)
                

main()

#opening csv as write        
with open('Output1c.txt', 'w')as f:
            #writing the answers
            f.write('\n'.join(final_lst))
            #closing the file
            f.close()       


        
            


