'''
merge sort 
time complexity: o(nlogn)
space complexity: o(n)
'''

# merge the two sorted halves O(n)
def merge(A, B):
    (C, m, n) = ([],len(A), len(B))
    (i,j) = (0,0)

    while i+j < m+n :
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n: 
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i =+ 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1

# sort the two halves O(logn)
def mergeSort(A, left , right):
    if right -left:
        return A[left:right]
    
    elif right - left > 1 :
        mid = (left + right) // 2

        L = mergeSort(A,left, mid)
        R = mergeSort(A, mid, right)
        return merge(L,R)
    
    return A

a = list(range(1, 1000, 2)) + list(range(0, 1000, 2))

res = mergeSort(a, 0, len(a))
print("sorted lsit : ", res )