#o(n2)
def strangeSorting(mapping, nums):
    dic = {}
    for i, val in enumerate(mapping):
        dic[str(val)] = str(i)
    
    result = []
    
    for i in nums:
        newstr = ''
        for j in i:
            newstr += dic[j]
        result.append([int(newstr), i])
    
    result = sorted(result, key=lambda x: (x[0]))
    for i in range(len(result)):
        result[i] = result[i][1]
    
    return result

# Driver Code
mapping = [2,1,4,8,6,3,0,9,7,5]
nums = ['12','02','4', '023', '65', '83', '224', '50']
print(strangeSorting(mapping, nums))