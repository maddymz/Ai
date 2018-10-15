#Algorithm to find max subarray using divide and conqure
import numpy as np
from sysconfig import sys
from numpy import asarray
import timeit as timeit


#function to calculate array of energy difference
def find_array_energy_difference(array):
    array_diff = []
    for i in range(1, len(array)):
        energy_difference = array[i] - array[i-1]
        array_diff.append(energy_difference)
    return asarray(array_diff)

#function to find the max_cross_subarray
def find_max_crossing_subarray(array, low, mid, high):
    left_sum = -sys.maxsize -1                                        #intialize left_sum as maximum negative number
    sum_so_far = 0                                                    #so that it can never be equal to a negative sum intially
    for i in range(mid, low-1, -1):
        sum_so_far = sum_so_far + array[i]
        if(sum_so_far > left_sum):
            left_sum = sum_so_far
            max_left = i

    right_sum = -sys.maxsize -1
    sum_so_far = 0
    for j in range( mid+1, high+1):
        sum_so_far += array[j]
        if (sum_so_far > right_sum):
            right_sum = sum_so_far
            max_right = j
            
    return max_left, max_right+1, left_sum + right_sum
    
#function to find the maximum subarray
def find_max_subarray(array, low, high):
    if(low == high):
        return low, high, array[low]
    else:
        mid = (low + high)//2                                                               #// for absolute value of mid point
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid+1, high)
        cros_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)

        print(left_low,left_high)
        print(right_low, right_high)
        print(cros_low, cross_high)
        if(left_sum > right_sum and left_sum > cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum > left_sum and right_sum > cross_sum):
            return right_low, right_high, right_sum
        else:
            return cros_low, cross_high, cross_sum

# variable intialization and function call
array_list =[100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
array_diff = find_array_energy_difference(array_list)
array = asarray(array_list)
array_size = len(array_diff)
Start = timeit.default_timer()
low, high, max_sum = find_max_subarray(array_diff, 0, array_size-1)
End = timeit.default_timer()
print("The maximum subarray is subarray[{},{}] with sum {}".format(low,high,max_sum))
print("run time: ", End - Start)


        

        