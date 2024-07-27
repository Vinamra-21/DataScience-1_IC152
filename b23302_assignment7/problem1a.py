#importing required modules
import numpy as np
import sys
import os

VarTF=False   #variable

#checking the input file in terminal
if 1<len(sys.argv)>5 or len(sys.argv)<=1:
  print("Please enter correct number of arguments as 'python file_name r1 c1 r2 c2'")
  exit()
else:
   if os.path.isfile(sys.argv[0]) == True: #input file exists or not
      VarTF = True
      for i in sys.argv[1:]: #check if valid input in file
         for k in i.split():
            if k in '1234567890':
               pass
            else:
               print('The values are not correct ')
               exit()
   else:
      print(f"{sys.argv[0]} is not available\n")
      print('The entered files doesnot exist please enter correct files')
      exit()
   
   if VarTF==True:
      r1=int(sys.argv[1]) #rows in matrix 1
      c1=int(sys.argv[2]) #columns in matrix 1
      r2=int(sys.argv[3]) #rows in matrix 2
      c2=int(sys.argv[4]) #columns in matrix 2

      matrix1=np.random.randint(10,size=(r1,c1))  #generating random matrix 1
      matrix2=np.random.randint(10,size=(r2,c2))  #generating random matrix 2
      str1=f'{r1} {c1}'
      str2=f'{r2} {c2}'

      #writing in respective files
      with open('MatA.txt','w',encoding='utf-8') as file1:
         file1.writelines(str1) # writing shape of matrix
         #writing matrix content to text file 
         str_list=list(matrix1)
         for i in str_list:
            str1m=' '.join(map(str,i))
            file1.write('\n')
            file1.write(str1m)
         
      with open('MatB.txt','w',encoding='utf-8') as file2:
         file2.writelines(str2) # writing shape of matrix
         #writing matrix content to text file
         str_list=list(matrix2)
         for i in str_list:
            str2m=' '.join(map(str,i))
            file2.write('\n')
            file2.write(str2m)