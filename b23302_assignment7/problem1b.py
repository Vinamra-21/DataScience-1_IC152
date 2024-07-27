#importing required modules
import numpy as np
import sys
import os

VarTF= False #variable
def ValueCheck(): #function to check the input values
    for i in lst:
        for t in i:
            if t in '+-1234567890':
                if t == '+' or t =='-':
                    print('The values in the matrix are not correct ')
                    exit()
                else:
                    pass
            else:
                print('The values in the matrix are not correct ')
                exit()
#checking the input file in terminal
if len(sys.argv)>3 or len(sys.argv)<=1:
  print("Please enter correct number of arguments as 'python file_name in_file1 in_file2'")
  exit()
else:
    for i in sys.argv:
        if os.path.isfile(i) == True: #input file exists or not
            VarTF = True
        else:
            print(f"{sys.argv[0]} is not available\n") #check if valid input in file
            print('The entered files doesnot exist please enter correct files')
            exit()
if VarTF==True:
    matrix1=[]
    matrix2=[]

    #reading the input files
    with open(sys.argv[1],encoding='utf-8') as in1:
        for line in in1.readlines()[1:]:
            lst=line.split()
            ValueCheck()
            lst=[int(i) for i in lst]
            matrix1.append(lst)
        matrix1=np.array(matrix1) #matrix1

    with open(sys.argv[2],encoding='utf-8') as in2:
        for line in in2.readlines()[1:]:
            lst=line.split()
            ValueCheck()
            lst=[int(i) for i in lst]
            matrix2.append(lst)
        matrix2=np.array(matrix2) #matrix2

    if np.shape(matrix1)[1]==np.shape(matrix2)[0]:
        multi_sol=np.matmul(matrix1,matrix2) #multiplication of the two matrices
        #writing output in output file
        with open('multOp.txt','w',encoding='utf-8') as out2:
            out2.writelines(f'{np.shape(multi_sol)[0]} {np.shape(multi_sol)[1]}')  #shape of matrix
            str_list=list(multi_sol)
            for i in str_list:
                str2m=' '.join(map(str,i))
                out2.write('\n')
                out2.write(str2m)
    else:
        print('The matrices are not compatible for multiplication')

    if np.shape(matrix1)==np.shape(matrix2):
        addition_sol=np.add(matrix1,matrix2) #addition of the two matrices
        #writing output in output file
        with open('addOp.txt','w',encoding='utf-8') as out1:
            out1.writelines(f'{np.shape(addition_sol)[0]} {np.shape(addition_sol)[1]}') #shape of matrix
            str_list=list(addition_sol)
            for i in str_list:
                str1m=' '.join(map(str,i))
                out1.write('\n')
                out1.write(str1m)  
    else:
        print("The matrices are not compatible for addition")
        
        
  

            
            
    





















