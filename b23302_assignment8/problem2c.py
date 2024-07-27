import sys
import os
import time
import numpy as np

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
def search_using_for_loop(input_array,item_to_be_found):
    for item in input_array:
        if item_to_be_found == item:
            print(input_array.index(item))
            return input_array.index(item)
#main program

lst=list(np.random.randint(100000,size=10000))
target=np.random.randint(100000,size=1)
data=[int(item) for item in lst[1:]]

start_bin=time.perf_counter()
binary_search(data, target)
end_bin = time.perf_counter()
start_for=time.perf_counter()
search_using_for_loop(data, target)
end_for = time.perf_counter()

print(f'time taken in binary search method={end_bin-start_bin}')
print(f'time taken in for-loop method={end_for-start_for}')