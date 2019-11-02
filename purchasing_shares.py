def sol(word):
    dic = {'A' : [float('inf')], 'B' : [float('inf')], 'C' : [float('inf')] }
    for i,letter  in enumerate(word):
        if letter in dic:
            dic[letter].append(i)

    for i in dic:
        dic[i].sort()    
    i = 0
    count = 0
    while i < len(word) - 2:
        a = dic['A'][0]
        if a == i :
            dic['A'].pop(0)
        b = dic['B'][0]
        if b == i :
            dic['B'].pop(0)
        c = dic['C'][0]
        if c == i :
            dic['C'].pop(0)

        k = max(a,b,c)
        if k == float('inf'):
            break
        count += len(word) - k
        i += 1
    return count

print( sol('PQACBA'))