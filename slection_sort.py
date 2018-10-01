#selection sort algorithm using python 
import random

#function to sort the array
def selection_sort(array):
    for j in range(len(array)):
        key = array[j]
        i= j+1
        while i < len(array) and array[i] < key:
                array[i-1] = array[i]
                array[i] = key
                

    return array

# intializatoin and fucntion call 

unsorted_array_list = random.sample(range(50), 5)
sorted_array_list = selection_sort(unsorted_array_list)
print("Sorted array is :", sorted_array_list)

          


