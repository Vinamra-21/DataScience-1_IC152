#q3 part a
#input coefficients and return the coefficient of the asked degree

# creating an empty list
print('Note:Enter the elements as coefficient of higgest degree fist and then as follows')
lst = []

# number of elements as input
x = int(input('q3 part a input (number of elements):'))

# iterating till the range entered
for i in range(0, x):
    element = int(input('q3 part a input (elements): '))
    lst.append(element)
n=input('q3 part a input (degree of coefficient): ')

#reversing list
lst.reverse()


#printing the desired coefficient
print(lst[int(n)])

##################################################################################

#q3 part b
#input the value of x in polynomial
x=int(input('q3 part b input (x):'))
y=4*(x**3) - 6*(x**2) + 0*(x) - 1
print(y)

##################################################################################

#q3 part c
#input two polynomials and add them

# creating an empty list1
print('Note:Enter the elements as coefficient of higgest degree fist and then as follows and add zero if any degree coefficient is missing.')
list1 = []

# number of elements as input
x1 = int(input('q3 part c input (number of elements in list 1):'))

# iterating till the range entered
for i in range(0, x1):
    element = int(input('q3 part c input (elements): '))
    list1.append(element)

# creating an empty list2
list2 = []

# number of elements as input
x2 = int(input('q3 part c input (number of elements in list 2):'))

# iterating till the range entered
for i in range(0, x2):
    element = int(input('q3 part c input (elements): '))
    list2.append(element)

#making length of lists same
if len(list1)>len(list2):
    y=len(list1)
else:
    y=len(list2)

for i in range(0,y):
    if len(list1)==len(list2):
        pass
    elif len(list1)>len(list2):
        list2.insert(0,0)
    else:
        list1.insert(0,0)

#adding polynomial coefficients
list_final=[]
for p in range(0,y):
    list_final.append(list1[p]+list2[p])
#final answer
m=max(x1,x2)
for i in range (0,m):
    print(list_final[i],end="")
    print('x^'+str(m-i)+"+",end="")
print(list_final[-1])

#numpy can also be used to print the polynomial function
# import numpy
# print(numpy.poly1d(list_final))
