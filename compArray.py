class Solution:
    def compress(self, chars):
        count = 0
        concList = []
        for i in range(len(chars)):
            count += 1
            if i+1 >= len(chars) or chars[i] != chars[i+1]:
                concList.append(chars[i])
                concList.append(count)
                count = 0
            
        if len(concList) < len(chars):
            return len(concList), concList
        else:
            return len(chars)



if __name__ == "__main__":

    obj = Solution()

    print(obj.compress(["a","a","b","b","c","c","c"]))