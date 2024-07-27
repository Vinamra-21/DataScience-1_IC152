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
