#q2 part a
#sort list ascending and descending

# creating an empty list
lst = []

# number of elements as input
n = int(input('q2 part a input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q2 part a input (elements): '))
    lst.append(element) 

# sorting ascending
lst.sort()
print(lst)

#sorting descending
lst.sort(reverse=True)
print(lst)

##################################################################################

#q2 part b
#print list by repeating the elements x number of times

# creating an empty list
lst = []

# number of elements as input
n = int(input('q2 part b input (number of elements):'))
x= input('number of times to repeat the entered elements in the list:')

# iterating till the range entered
for i in range(0, n):
    element = int(input('q2 part b input (elements): '))
    lst.append(element)
#repeating x times
new_list=lst*int(x)
print(new_list)

##################################################################################

#q2 part c
#find max and min in list

# creating an empty list
lst = []

# number of elements as input
n = int(input('q2 part c input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q2 part c input (elements): '))
    lst.append(element)

#maximum
max=max(lst)
print(max)

#minimum
min=min(lst)
print(min)

##################################################################################

#q2 part d
#print index of the asked element

# creating an empty list
lst = []

# number of elements as input
n = int(input('q2 part d input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q2 part d input (elements): '))
    lst.append(element)
k=int(input('q2 part a input (element whose index is to be found):'))

#output is index of the entered element(k)
print(lst.index(k))

##################################################################################

#q2 part e
#printing the sum of all elements in list

# creating an empty list
lst = []

# number of elements as input
n = int(input('q2 part e input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q2 part e input (elements): '))
    lst.append(element)
print(sum(lst))




