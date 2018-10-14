# -*- coding: utf-8 -*-
import numpy as np
from sysconfig import sys
from numpy import asarray


ENERGY_LEVEL = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
#==============================================================

#function to calculate array of energy difference
def find_array_energy_difference(array):
    array_diff = []
    for i in range(1, len(array)):
        energy_difference = array[i] - array[i-1]
        array_diff.append(energy_difference)
    return asarray(array_diff)

# The brute force method to solve first problem

#function to find the max energy increase

def find_significant_energy_increase_brute(array):

    """
    Return a tuple (i,j) where A[i:j] is the most significant energy increase period.
    time complexity = O(n^2)
    """
    energy_change_max_sum = -sys.maxsize -1
    for i in range(len(array)):
        sum_so_far = 0
        for j in range(i+1, len(array)):
            sum_so_far += array[j]
            if(sum_so_far > energy_change_max_sum):
                energy_change_max_sum = sum_so_far
                index_low = i
                index_high = j
        
    return index_low+1, index_high+1
#==============================================================

# # The recursive method to solve first problem

#function to find the energy increase in cross subarrays

def find_significant_energy_increase_cross(low, high, mid, array):
    left_energy_max_sum = -sys.maxsize -1
    sum_so_far = 0
    for i in range(mid, low-1, -1):
        sum_so_far += array[i]
        if(sum_so_far > left_energy_max_sum):
            left_energy_max_sum = sum_so_far
            max_left = i
    right_energy_max_sum = -sys.maxsize -1
    sum_so_far = 0
    for j in range(mid +1, high+1):
        sum_so_far += array[j]
        if(sum_so_far > right_energy_max_sum):
            right_energy_max_sum = sum_so_far
            max_right = j
    
    return max_left, max_right+1, left_energy_max_sum + right_energy_max_sum

def find_significant_energy_increase_recursive(low, high, array):
    
    """
    Return a tuple (i,j) where A[i:j] is the most significant energy increase period.
    time complexity = O (n logn)
    """
    if(low == high):
        return low, high, array[low]
    else:
        mid = (low + high)//2
        left_low, left_high, left_sum = find_significant_energy_increase_recursive(low, mid, array)
        right_low, right_high, right_sum = find_significant_energy_increase_recursive(mid+1, high, array)
        cross_left, cross_right, cross_sum = find_significant_energy_increase_cross(low, high, mid, array)
        if(left_sum > right_sum and left_sum > cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum>left_sum and right_sum > cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_left, cross_right, cross_sum
        
# #==============================================================

# The iterative method to solve first problem

#function to find the max increase 
def find_significant_energy_increase_iterative(array):

    """
    Return a tuple (i,j) where A[i:j] is the most significant energy increase period.
    time complexity = O(n)
    """
    max_increase_sum = 0
    sum_so_far = 0
    for i in range(len(array)):
        if(sum_so_far + array[i]> 0):
            sum_so_far += array[i]
           
        else:
            sum_so_far = 0
            low_index = i
        if(sum_so_far>max_increase_sum):
            max_increase_sum = sum_so_far
            high_index = i
    
    return low_index +1, high_index+1, max_increase_sum


#variable initialization and function call
array_energy_level = np.asarray(ENERGY_LEVEL)
array_energy_diff = find_array_energy_difference(array_energy_level)                          #calculate and store array of energy differences
array_length = len(array_energy_diff)
low, high = find_significant_energy_increase_brute(array_energy_diff)
print("Most significant energy increase period: ({},{})".format(low, high))
low, high, sum = find_significant_energy_increase_recursive( 0, array_length-1, array_energy_diff)
print("Most significant energy increase period: ({},{}) ".format(low, high))
low_index,high_index, max_sum= find_significant_energy_increase_iterative(array_energy_diff)
print("Most significant energy increase period: ({},{})".format(low_index, high_index))
# #==============================================================

# # The Strassen Algorithm to do the matrix multiplication

#fucntion to recursively multiply teh matrices
def multiply_recursive(A, B):
     row_nos = A.shape[0]
    sub_marix_A = []
    sub_marix_B = []
    prod_array = []
    if(row_nos == 1):
        prod_array[1][1] = A[1][1].B[1][1]
    else:
        row_sub_matrix_A = A.shape[0]//2
        col_sub_matrix_A = A.shape[1]//2
        row_sub_matrix_B = B.shape[0]//2
        col_sub_matrix_B = B.shape[1]//2
        sub_marix_A = sub_marix_A[row_sub_matrix_A][col_sub_matrix_A]
        sub_marix_B = sub_marix_B[row_sub_matrix_B][col_sub_matrix_B]
        prod_array[0][0] = square_matrix_multiply_strassens(sub_marix_A[0][0], sub_marix_B[0][0]) + square_matrix_multiply_strassens(sub_marix_A[0][1], sub_marix_B[1][0])
        prod_array[0][1] = square_matrix_multiply_strassens(sub_marix_A[0][0], sub_marix_B[0][1]) + square_matrix_multiply_strassens(sub_marix_A[0][1], sub_marix_B[1][1])
        prod_array[1][0] = square_matrix_multiply_strassens(sub_marix_A[1][0], sub_marix_B[0][0]) + square_matrix_multiply_strassens(sub_marix_A[1][1], sub_marix_B[1][0])
        prod_array[1][1] = square_matrix_multiply_strassens(sub_marix_A[1][0], sub_marix_B[0][1]) + square_matrix_multiply_strassens(sub_marix_A[1][1], sub_marix_B[1][1])
    return prod_array

#function to multiply matrices using strassens method
def square_matrix_multiply_strassens(A, B):

    """
    Return the product AB of matrix multiplication.
    Assume len(A) is a power of 2
    """

    A = asarray(A)

    B = asarray(B)

    assert A.shape == B.shape

    assert A.shape == A.T.shape

    assert (len(A) & (len(A) -1)) == 0, "A is not a power of 2"

    prod_array = multiply_recursive(A,B)
    S1 = 

   # #==============================================================

# # Calculate the power of a matrix in O(k)
# def power_of_matrix_navie(A, k):
#     """
#     Return A^k.
#     time complexity = O(k)
#     """
#     #TODO

# #==============================================================

# # Calculate the power of a matrix in O(log k)
# def power_of_matrix_divide_and_conquer(A, k):
#     """
#     Return A^k.
#     time complexity = O(log k)
#     """
#     #TODO

# #==============================================================
# def test():

#     assert(find_significant_energy_increase_brute(ENERGY_LEVEL) == (7, 11))
#     assert(find_significant_energy_increase_recursive(ENERGY_LEVEL) == (7, 11))
#     assert(find_significant_energy_increase_iterative(ENERGY_LEVEL) == (7, 11))
#     assert((square_matrix_multiply_strassens([[0, 1], [1, 1]],
#                                              [[0, 1], [1, 1]]) == 
#                                              asarray([[1, 1], [1, 2]])).all())
#     assert((power_of_matrix_navie([[0, 1], [1, 1]], 3) == 
#                                     asarray([[1, 2], [2, 3]])).all())
#     assert((power_of_matrix_divide_and_conquer([[0, 1], [1, 1]], 3) == 
#                                                asarray([[1, 2], [2, 3]])).all())
#     #TODO: Test all of the methods and print results.


# if __name__ == '__main__':

#     test()

# #==============================================================