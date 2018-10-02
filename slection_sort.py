#selection sort algorithm using python 
"""
selection sort steps:
 - find the smallest element in the array
 - exchange it with the intial position 
 - find second smallest and exchange it with second  
"""
import random

#function to find teh smallest element of the array
def element_smallest(value, length, array, key):
    j = value -1
    for i in range(value, length):
           if(array[j] > array[i]):
                array[j] = array[i]
                array[i] = key 
                key = array[j]
    return key
           
      
#function to sort the array
def selection_sort(array):
    for j in range(len(array)):
        key = array[j]
        smallest_element = element_smallest(j+1, len(array), array, key)            # slection of the smallest element 
        array[j] = smallest_element                                                 # exchange the smallest element with a[j]

    return array       

# intializatoin and fucntion call 
unsorted_array_list = random.sample(range(50), 20)
sorted_array_list = selection_sort(unsorted_array_list)
print("Sorted array is :", sorted_array_list)

          


