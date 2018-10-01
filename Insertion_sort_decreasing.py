#insertion sort algorithm to sort into decreasing order

import random 

#function to sort in decreasing order 
def insertion_sort_decreasing(array) : 
    for j in range(1, len(array)):
        key = array[j]

        i = j-1

        while i>=0 and array[i] < key:
            array[i+1]  = array[i]
            i= i-1
        array[i+1] = key

    return array

# initialization and function call

unsorted_array_list = random.sample(range(100), 9)
sorted_array_list  = insertion_sort_decreasing(unsorted_array_list)
print("Sorted array in decreasing order : ", sorted_array_list)