class StrinCompression:
    def __init__(self):
        pass

    def compress(self, givenString):
        comStr = ""
        count = 0

        for i in range(len(givenString)):
            count +=1 
            if (i+1 >= len(givenString)) or (givenString[i] != givenString[i+1]):
                comStr +=givenString[i] + str(count)
                count = 0
        
        if len(comStr) < len(givenString):
            return comStr
        else:
            return givenString
    
    def optimized(self, givenString):
        count = 0
        strlist = []
        

        for i in range(len(givenString)):
            count += 1
            if i+1 >= len(givenString) or givenString[i] != givenString[i+1]:
                strlist.append(givenString[i] + str(count))
                count = 0

        strCon = ''.join(strlist)
        if len(strCon) < len(givenString) :
            return strCon
        else:
            return givenString


if __name__ == "__main__":
    obj = StrinCompression()

    print(obj.optimized("aabcccccaaa"))

