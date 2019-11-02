#time complexity: o(n**2)
#space o(n) -- creates an extra dict
def twoSumLessThanK(A, K):
    count = 0
    dict = {}
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            s = A[i] + A[j]
            if i < j and s < K :
                dict[s] = (i,j)
                count +=1
    if count > 0:
        return max(dict.keys())
    else:
        return -1

res = twoSumLessThanK([34,23,1,24,75,33,54,8], 60)
print(res)


# o(nlogn)
def twoSumLessThanKOptimized(A, K):     
    max_sum=-1
    A.sort()
    l, r= 0, len(A)-1
    
    while l<r:
        total=A[l]+A[r]
        if total<K:
            max_sum=max(max_sum, total)
            l+=1
        else:
            r-=1
    return max_sum