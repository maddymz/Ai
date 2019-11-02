##o(n)space
#o(n3)
def solution(arr, rank):
    rankArr = [None for i in range(rank)]
    for i in range(len(arr)):
        rankArr = updateRanks(arr[i], rankArr,i)
    print(rankArr)
    return rankArr

def updateRanks(current,rankArr,idx):
    total = sum(current)
    for i in range(len(rankArr)-1,-1,-1):
        if rankArr[i] is None or total > rankArr[i][0]:
            rankArr = shiftAndUpdate(rankArr, current , i,idx)
            break
    return rankArr

def shiftAndUpdate(arr, num, idx, res):
    for i in range(idx + 1):
        if i == idx:
            arr[i] = [sum(num),num, res]
        else:
            arr[i] = arr[i+1]
    return arr

arr = [[80, 96, 81, 77 ],
[78, 71, 93, 75 ],
[71, 98, 70, 95 ],
[80, 96, 89, 77]]

print(solution(arr, 3))