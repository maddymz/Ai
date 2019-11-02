#o(n) time
#o(n) space
def findMaxCommonality(stri):
    count = [0 for _ in range(26)]
    for i in stri:
        count[ord(i) - 97] += 1

    res = 0
    cur = 0
    for i in stri:
        if count[ord(i) - 97] > 1:
            cur += 1
            count[ord(i) - 97] -= 2
        elif count[ord(i) - 97] == 0:
            cur -= 1
        res = max(cur, res)
    return res

print (findMaxCommonality('abcdecdefg'))