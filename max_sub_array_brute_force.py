#Brute force approach to solve a max subarray problem 
import time
from sysconfig import sys
#function to find max sub-array

def max_subarray (array):
    max_sum = -sys.maxsize -1
    for i in range(len(array)):
        sum_so_far = 0                                                  #variable to keep track of teh total sum
        for j in range( i, len(array)):
           sum_so_far = sum_so_far + array[j]                          #current sum calculation 
           if (max_sum < sum_so_far):               
               max_sum = sum_so_far                                    #storing max sum
               index_low = i                                            #storing lower index of max subarray
               index_high = j                                           #storing higher index of max subarray
                                             
    return index_low, index_high, max_sum

#variable intialization and function call
array = [1,3,-5,-9,4,9,3,5,7,0,-7,-4,-6]

low_index,high_index,subarray_max_sum = max_subarray(array)
print("Max subarray is array[{},{}] with sum {}".format(low_index, high_index, subarray_max_sum))


