import sys
import os
import time
start = time.perf_counter()
def ValueCheck(): #function to check the input values
    for i in lst:
        for t in i:
            if t in '+-1234567890':
                if t == '+' or t =='-':
                    print('The values are not correct.')
                    exit()
                else:
                    pass
            else:
                print('The values are not correct.')
                exit()
def binary_search(input_array, item_to_be_found): #Binary Search
    input_array.sort()
    left_index = 0  
    right_index = len(input_array) - 1
    while right_index >= left_index:
        middle = (left_index + right_index) // 2
        if input_array[middle] < item_to_be_found:
            left_index = middle + 1
        elif input_array[middle] > item_to_be_found:
            right_index = middle - 1
        else:
            print(middle)
            return middle 
#main program
VarTF=False 
if len(sys.argv)==2: #check for number of inputs
    for i in sys.argv:  #input file exists or not
        if os.path.isfile(i) == True: 
            VarTF = True
        else:
            print(f"{i} is not available\n")
            print('The entered files doesnot exist please enter correct files')
            exit()

    if VarTF==True:
        lst=[]
        #reading input file
        with open(sys.argv[1], encoding='utf-8') as file:
            for i in file.readlines():
                for j in i.split():
                    lst.append(j)
            ValueCheck()
            if len(lst[0].split())!=1:
                print('The values are not correct.')
                exit()
            target=int(lst[0])
            data=[int(item) for item in lst[1:]]

        binary_search(data, target)  
else:
    print("Please enter correct number of files in the terminal.")
    exit()

end = time.perf_counter()
print(f'time taken={end-start}')