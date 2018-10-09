#Brute force approach to solve a max subarray problem 

#function to find max sub-array
def max_subarray (array):
    max_sum = 0
    for i in range(len(array)):
        sum_so_far = 0                                                  #variable to keep track of teh total sum
        for j in range( i, len(array)):
           current_sum = sum_so_far + array[j]                          #current sum calculation 
           if (sum_so_far < current_sum and max_sum < current_sum):               
               max_sum = current_sum                                    #storing max sum
               index_low = i                                            #storing lower index of max subarray
               index_high = j                                           #storing higher index of max subarray
           sum_so_far = current_sum                                    

    return index_low, index_high, max_sum

#variable intialization and function call
array = [1,3,-5,-9,4,9]
low_index,high_index,subarray_max_sum = max_subarray(array)
print("Max subarray is array[{},{}] with sum {}".format(low_index, high_index, subarray_max_sum))


