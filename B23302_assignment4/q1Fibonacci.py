# q1 part a
# fibonacci series

n=int (input ('q1 part a input (integer):') )
def fiboSer():
    lst= [0,1]
    if n==0:
        lst.pop()
    elif n==1:
        pass
    else:
        for i in range (0, n-1) :
         x=lst[i]+lst[i+1]
         lst.append(x)
    print(lst)
fiboSer()

##################################################################################

#q1 part b
#Find majority element else return -1

lst = []

# number of elements as input
n = int(input('q1 part b input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q1 part b input (elements): '))
    lst.append(element)

#defining funcion to find majority element
def find_majority_element(lst):
    b=0
    c=0
    for i in lst:
        a = lst.count(i)
        if b<a:
            b=a
            c=i
        else:
            pass
    #defining outputs
    if b>((len(lst))//2):
        print(c, 'is the majority element')
    else:
        print(-1)

find_majority_element(lst)

##################################################################################

#q1 part c
# find repeating elements

lst = []

# number of elements as input
n = int(input('q1 part c input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q1 part c input (elements): '))
    lst.append(element)

def find_first_repeating_element(lst):
    seen_numbers = set()
    
    for n in lst:
        if n in seen_numbers:
            return n  
        seen_numbers.add(n)
    
    return "no repeating element "  

output = find_first_repeating_element(lst)
print(output)                  

##################################################################################

#q1 part d
# number triangle

n=int(input('q1 part d input (ineger):'))
for i in range(1,n+1):
        #printing spaces
    print(' '*(n-i) ,end="")
        #printing forward series
    for j in range(1,i+1):
        print(j,end="")
        #printing back series
    for k in range(i-1,0,-1):
        print(k,end="")
    print(" ")

##################################################################################

#q1 part e
# find repeating elements

lst = []

# number of elements as input
n = int(input('q1 part e input (number of elements):'))

# iterating till the range entered
for i in range(0, n):
    element = int(input('q1 part e input (elements): '))
    lst.append(element)

new_lst=[]

def remove_repeating_element():
    for x in lst:
        if x in new_lst:
            pass
        else:
            new_lst.append(x)
    print(new_lst)



remove_repeating_element()


