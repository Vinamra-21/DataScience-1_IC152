#importing required moduless
import numpy as np
import numpy.linalg as la
import sys
import os

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

def solution(): #function to print the solution for unique solution
    sol=la.solve(matA,matb)
    out.writelines(f'{np.shape(sol)[0]} {np.shape(sol)[1]}')
    str_list=list(sol)
    for i in str_list:
      str2m=' '.join(map(str,i))
      out.write('\n')
      out.write(str2m)

def MatrixCheck(mat): #function to check matrix
    a=len(mat[0])
    for i in mat:
        if len(i)==a:
            pass
        else:
            print('Entered file is incorrect')
            exit()

VarTF=False #variable
#checking the input file in terminal
if len(sys.argv)> 3 or len(sys.argv)<=1 :
    print("Please enter correct number of files in the terminal.")
    exit()

else:
    for i in sys.argv:  #input file exists or not
        if os.path.isfile(i) == True:
            VarTF = True
        else:
            print(f"{i} is not available\n")
            print('The entered files doesnot exist please enter correct files')
            exit()
    if VarTF==True:
        matA=[]
        matb=[]
      
        with open(sys.argv[1],encoding='utf-8') as in1:   #reading input file 1
            for line in in1.readlines()[1:]:
                lst=line.split()
                ValueCheck()
                lst=[int(i) for i in lst]
                matA.append(lst)
                MatrixCheck(matA)
            matA=np.array(matA) #matrix1

        with open(sys.argv[2],encoding='utf-8') as in2:   #reading input file 2
            for line in in2.readlines()[1:]:
                lst=line.split()
                ValueCheck()
                lst=[int(i) for i in lst]
                matb.append(lst)
                MatrixCheck(matb)
            matb=np.array(matb) #matrix2

        out=open('problem2bOp.txt', 'w') #output file
        

        if np.shape(matA)==(3,3) and np.shape(matb)==(3, 1):       #3X3 and 3X1
            columnA1=np.array([row[0] for row in matA]) #column 1 A
            columnA2=np.array([row[1] for row in matA]) #column 2 A
            columnA3=np.array([row[2] for row in matA]) #column 3 A
            columnb1=np.array([row[0] for row in matb]) #column 1 b

            #calculating determinants
            mat_det=la.det(matA)
            mat_det_1=la.det(np.column_stack((columnb1,columnA2,columnA3)))
            mat_det_2=la.det(np.column_stack((columnA1,columnb1,columnA3)))
            mat_det_3=la.det(np.column_stack((columnA1,columnA2,columnb1)))

            # final solution output
            if mat_det!=0:
                solution()
            elif mat_det==0 and mat_det_1==0 and mat_det_2==0 and mat_det_3==0:
                matnewA=np.delete(matA,0,1)
                matnewA=matnewA[1:]
                matnewb=matb[1:]
                ans=la.solve(matnewA,matnewb)
                final=np.array([[0],ans[0],ans[1]])
                out.writelines(f'{np.shape(final)[0]} {np.shape(final)[1]}') 
                str_list=list(final)
                for i in str_list:
                 str2m=' '.join(map(str,i))
                 out.write('\n')
                 out.write(str2m)   
            else:
                out.write("The system has no solution.")
          
        elif np.shape(matA)==(2,2) and np.shape(matb)==(2,1): #2X2 and 2X1
            columnA1=np.array([row[0] for row in matA])
            columnA2=np.array([row[1] for row in matA])
            columnb1=np.array([row[0] for row in matb])
            
            #calculating determinants
            mat_det=la.det(matA)
            mat_det_1=la.det(np.column_stack((columnb1,columnA2)))
            mat_det_2=la.det(np.column_stack((columnA1,columnb1)))
 
            # final solution output
            if mat_det!=0:
              solution()
            elif mat_det==0 and mat_det_1==0 and mat_det_2==0:
               z=matb[0][0]/matA[0][1]
               arr=np.array([[0],[z]])
               out.writelines(f'{np.shape(arr)[0]} {np.shape(arr)[1]}') 
               str_list=list(arr)
               for i in str_list:
                 str2m=' '.join(map(str,i))
                 out.write('\n')
                 out.write(str2m)   
            else:
              out.write("The system has no solution.")

        elif np.shape(matA)==(1,1) and np.shape(matb)==(1,1): #1X1 and 1X1
            ans=(matb[0][0])/(matA[0][0])
            out.writelines(f'1 1')
            out.writelines('\n')
            out.writelines(str(ans))

        else:
            print('Matrix A should be N X N matrix and Matrix b should be  N X 1 matrix with N<=3')

out.close()