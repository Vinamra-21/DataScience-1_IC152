#q4 part a
#defining rows and colums
row=int(input('q4 part a input (number of rows):'))
column=int(input('q4 part a input (number of columns):'))

#creating matrix
matrix=[]
print('Enter elements rowwise')

#iterating the elements
for i in range(row):
    a=[]
    for j in range(column):
        a.append(int(input('q4 part a input (elements of matrix):')))
    matrix.append(a)
print(matrix)

#printing as matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end = " ")
    print()

k=int(input('q4 part a input (elements of matrix whose index is to be found):'))

#printing the index(row and column) of the element      
count=0
for i in range(0,row):
    for j in range(0,column):
        if matrix[i][j]==k:
            print('row=',i+1,'column=',j+1)
            count+=1
        else:
            pass
if count==0:
    print("The element is not in the matrix")
    
##################################################################################

#q4 part b
#matrix is symmmetric or skew-symmetric

#Define for symmetric matrix
def symmetry(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]!=matrix[j][i]:
                return False
    return True

#Define for skew-symmetric matrix
def skewSymmetry(matrix):
    sym=None
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==-matrix[j][i] and matrix[i][i]==0:
                sym=True
            else:
                sym=False
                break
    if sym==True:
        return True
    else:
        return False

n=int(input('q4 part b input (number of rows and number of columns):'))

#creating matrix
matrix=[]
print('Enter elements rowwise')

#iterating the elements
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input('q4 part a input (elements of matrix):')))
    matrix.append(a)
print(matrix)

#printing as matrix
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()

#output statements
if symmetry(matrix):
    print('The matrix is symmetric')

if skewSymmetry(matrix):
    print('The matrix is skew-symmetric')

if symmetry(matrix)==False and skewSymmetry(matrix)==False:
    print('The matrix is neither symmetric nor skew-symmetric')

     