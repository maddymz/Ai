#algorithm to find maximum sub array in linear time
import numpy as np
from numpy import asarray
import timeit as timeit

#function to calculate max  subarray
def find_max_subarray(array):
    max_sum=0
    sum_so_far = 0
    for i in range(len(array)):
        if(sum_so_far + array[i] > 0 ):
            sum_so_far += array[i]
        else:
            sum_so_far = 0
        if(max_sum < sum_so_far):
            max_sum = sum_so_far
        
    return max_sum

#variable intialization and function call
array = [1,3,-5,-9,4,9,3,5,7,0,-7,-4,-6]
Start = timeit.default_timer()
subarray_max_sum = find_max_subarray(array)
End = timeit.default_timer()
print("Max subarray is {}".format(subarray_max_sum))
print("RUn time : ", End - Start)