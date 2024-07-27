#Roots of polynomial

# import numpy library
import numpy as np
  
lst = []

# number of elements as input
print('please enter the numbers starting from constant term')
n = int(input('q1 part b input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q1 part b input (elements): '))
    lst.append(element)

# Enter the coefficients of the poly in the array
for i in np.roots(lst):
    print(i)


  

     
     
