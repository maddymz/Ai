def countSuchNum(l, r, q):
    count = 0
    for i in range(l,r+1):
        l_cmp = str(i * q)
        i_s = str(i)
        flag = True
        for c in i_s:
            if c in l_cmp:
                flag = False
                break
        if flag:
            count+=1
    return count
print(countSuchNum(5, 15, 2))