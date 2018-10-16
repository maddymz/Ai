# -*- coding: utf-8 -*-
import numpy as np
from sysconfig import sys
from numpy import asarray

ENERGY_LEVEL = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
# #==============================================================

# #function to calculate array of energy difference


def find_array_energy_difference(array):

    array_diff = []
    for i in range(1, len(array)):
        energy_difference = array[i] - array[i-1]
        array_diff.append(energy_difference)
    return asarray(array_diff)

# # The brute force method to solve first problem

# #function to find the max energy increase


def find_significant_energy_increase_brute(array):

    """
    Return a tuple (i,j) where A[i:j] is the most significant energy increase period.
    time complexity = O(n^2)
    """
    array = find_array_energy_difference(array)  
    energy_change_max_sum = - sys.maxsize - 1
    for i in range(len(array)):
        sum_so_far = 0
        for j in range(i + 1, len(array)):
            sum_so_far += array[j]
            if(sum_so_far > energy_change_max_sum):
                energy_change_max_sum = sum_so_far
                index_low = i
                index_high = j
    return index_low + 1, index_high + 1
# #==============================================================

# # The recursive method to solve first problem

# #function to find the energy increase in cross subarrays


def find_significant_energy_increase_cross(low, high, mid, array):
    left_energy_max_sum = - sys.maxsize - 1
    sum_so_far = 0
    for i in range(mid, low - 1, - 1):
        sum_so_far += array[i]
        if(sum_so_far > left_energy_max_sum):
            left_energy_max_sum = sum_so_far
            max_left = i
    right_energy_max_sum = - sys.maxsize - 1
    sum_so_far = 0
    for j in range(mid + 1, high + 1):
        sum_so_far += array[j]
        if(sum_so_far > right_energy_max_sum):
            right_energy_max_sum = sum_so_far
            max_right = j
    return max_left, max_right + 1, left_energy_max_sum + right_energy_max_sum

def find_significant_energy_increase_recursive(array):
    array = find_array_energy_difference(array)
    return find_significant_energy_increase_recursive_helper(0, len(array) - 1, array)[0:2]

def find_significant_energy_increase_recursive_helper(low, high, array):
    
    """
    Return a tuple (i,j) where A[i:j] is 
    the most significant energy increase period.
    time complexity = O (n logn)
    """
    if(low == high):
        return low, high, array[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_significant_energy_increase_recursive_helper(
            low, mid, array)
        right_low, right_high, right_sum = find_significant_energy_increase_recursive_helper(
            mid + 1, high, array)
        cross_left, cross_right, cross_sum = find_significant_energy_increase_cross(
            low, high, mid, array)
        if(left_sum > right_sum and left_sum > cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum > left_sum and right_sum > cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_left, cross_right, cross_sum         
# #==============================================================

# #The iterative method to solve first problem

# #function to find the max increase


def find_significant_energy_increase_iterative(array):

    """
    Return a tuple (i,j) where A[i:j] is the most significant energy increase period.
    time complexity = O(n)
    """
    array = find_array_energy_difference(array)
    max_increase_sum = 0
    sum_so_far = 0
    for i in range(len(array)):
        if(sum_so_far + array[i] > 0):
            sum_so_far += array[i]
        else:
            sum_so_far = 0
            low_index = i
        if(sum_so_far > max_increase_sum):
            max_increase_sum = sum_so_far
            high_index = i   
    return low_index + 1, high_index + 1

# # variable initialization and function call


array_energy_level = np.asarray(ENERGY_LEVEL)
low, high = find_significant_energy_increase_brute(array_energy_level)
print("Max increase brute force: ({},{})".format(low, high))
low, high = find_significant_energy_increase_recursive(array_energy_level)
print("Max increase recursive: ({},{}) ".format(low, high))
low_index, high_index = find_significant_energy_increase_iterative(array_energy_level)
print("Max increase iterative: ({},{})".format(low_index, high_index))
# #==============================================================
# # The Strassen Algorithm to do the matrix multiplication

# # function to create new matrx


def create_new_matrix(p, q):
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix

# #function to split teh matrices


def split(matrix):
    row, col = matrix.shape
    matrix_one = matrix[:row // 2, :col // 2]
    matrix_two = matrix[:row // 2, col // 2:]
    matrix_three = matrix[row // 2:, :col // 2]
    matrix_four = matrix[row // 2:, col // 2:]
    return matrix_one, matrix_two, matrix_three, matrix_four

# # function to add two matrices


def add_matrix(a, b):
    n = len(a)
    matrix_sum = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix_sum[i][j] = a[i][j] + b[i][j]
    return matrix_sum

# # function to subtract two matrices


def sub_matrix(a, b):
    n = len(a)
    matrix_diff = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix_diff[i][j] = a[i][j] - b[i][j]
    return matrix_diff

# # function to multiply matrices using strassens method


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

    size = len(A)
    if(size == 1):
        return A * B
    else:
        A00, A01, A10, A11 = split(A)
        B00, B01, B10, B11 = split(B)
        M1 = square_matrix_multiply_strassens(
            add_matrix(A00, A11), add_matrix(B00, B11))
        M2 = square_matrix_multiply_strassens(
            add_matrix(A10, A11), B00)
        M3 = square_matrix_multiply_strassens(
            A00, sub_matrix(B01, B11))
        M4 = square_matrix_multiply_strassens(
            A11, sub_matrix(B10, B00))
        M5 = square_matrix_multiply_strassens(
            add_matrix(A00, A01), B11)
        M6 = square_matrix_multiply_strassens(
            sub_matrix(A10, A00), add_matrix(B00, B01))
        M7 = square_matrix_multiply_strassens(
            sub_matrix(A01, A11), add_matrix(B10, B11))
        c11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
        c12 = add_matrix(M3, M5)
        c21 = add_matrix(M2, M4)
        c22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)
        C = create_new_matrix(len(c11) * 2, len(c11) * 2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                C[i][j] = c11[i][j]
                C[i][j+len(c11)] = c12[i][j]
                C[i+len(c11)][j] = c21[i][j]
                C[i+len(c11)][j+len(c11)] = c22[i][j]
        return C
# #==============================================================

# # Calculate the power of a matrix in O(k)


def power_of_matrix_navie(A, k):
    """
    Return A^k.
    time complexity = O(k)
    """
    if(k == 1):
        return A
    product = A
    for i in range(1, k):
        product = square_matrix_multiply_strassens(product, A)
    return product

# #==============================================================

# # Calculate the power of a matrix in O(log k)

# # function using divide and conqure to calculate the product


def power(A, k):
 
    if(k == 0):   # base case                                                                   
        matrix = [[0 for row in range(len(A))] for col in range(len(A))]
        for i in range(len(A)):
            matrix[i, i] = 1         # cereate an identity matrix
        return matrix               # return identity matrix

    if(k == 1):
        return A
    temp = power(A, k // 2)
    if (k % 2 == 0):
        return square_matrix_multiply_strassens(temp, temp)
    else:
        return square_matrix_multiply_strassens(A, square_matrix_multiply_strassens(temp, temp))

# # fucntion to calculate the product using divide and conqure


def power_of_matrix_divide_and_conquer(A, k):
    """
    Return A^k.
    time complexity = O(log k)
    """ 
    product = power(A, k)
    return product

# # variable intialization and function call


A = [[1, 3], [7, 5]]
B = [[6, 8], [4, 2]]
k = 7
product_strassens = square_matrix_multiply_strassens(A, B)
product_naive = power_of_matrix_navie(A, k)
product_divide_n_conqure = power_of_matrix_divide_and_conquer(A, k)
print("Product matrix of matrix using strassens algo: ", product_strassens)
print("Product of matrix using divide and conqure: ", product_divide_n_conqure)
print("Product of matrix using naive approach: ", product_naive)
# #==============================================================


def test():
    assert(find_significant_energy_increase_brute(ENERGY_LEVEL) == (7, 11))
    assert(find_significant_energy_increase_recursive(ENERGY_LEVEL) == (7, 11))
    assert(find_significant_energy_increase_iterative(ENERGY_LEVEL) == (7, 11))
    assert((square_matrix_multiply_strassens([[0, 1], [1, 1]],
                                             [[0, 1], [1, 1]]) ==
                                             asarray([[1, 1], [1, 2]])).all())
    assert((power_of_matrix_navie([[0, 1], [1, 1]], 3) ==
                                    asarray([[1, 2], [2, 3]])).all())
    assert((power_of_matrix_divide_and_conquer([[0, 1], [1, 1]], 3) ==
                                               asarray([[1, 2], [2, 3]])).all())


if __name__ == '__main__':

    test()
# #==============================================================