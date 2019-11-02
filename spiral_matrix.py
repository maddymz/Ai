import math

def checkPrime(num):
    if num <= 1:
        return False
    if num < 3:
        return True

    if num%2 == 0 or num %3 == 0:
        return False
    
    i = 5
    while i*i <= num:
        if num%i ==0 or num %(i+2) ==0:
            return False
        i = i + 6
    return True

def spiralOrder(matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix: return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            res = checkPrime(matrix[r][c])
            if res :
                ans.append(matrix[r][c])
        r1 += 1; r2 -= 1
        c1 += 1; c2 -= 1
    return ans


arr = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(spiralOrder(arr))