class URLify:
    def __init__(self):
        pass


    def replaceSpaces(self, arr, tl):
        scount = 0
        for i in range(len(arr)):
            
        for i in range(len(arr)):
            if arr[i] == ' ':
                scount += 1
        
        index = tl + scount * 2

        if tl < len(arr):
            arr[tl] = '\0'

        for j in range(-1,1,len(arr)):
            if arr[j] == ' ':
                arr[index - 1] = '0'
                arr[index -2] = '2'
                arr[index -3] ='%'
                index = index - 3
            else:
                arr[index - 1] = arr[j]
                index -= 1
        return arr


if __name__ == "__main__":

    obj = URLify()

    "Mr John Smith   ".split()

    print(obj.replaceSpaces(, 13))