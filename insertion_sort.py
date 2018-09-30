# insertion sort algorithm 
import random

#sorting function 
def insertion_sort(array):
    for j in range(1, len(array)):
        key_element = array[j]
        i = j-1
        while i>0 and array[i] > key_element:
            array[i+1] = array[i]
            i = i-1                                             # places the sorted element at correct place
        array[i+1] = key_element             

    return array

#call to teh sorting function 
unsorted_array_list = random.sample(range(100), 5)              # random sample space generator
sorted_array_list = insertion_sort(unsorted_array_list)
print("The sorted array is : ", sorted_array_list)

