import collections
class Solution:
    def findShortestSubArray(self, nums):
        # find the degree of the array
        freqs = collections.Counter(nums)
        degree = 0
        degree_num = []
        degree = max(freqs.values())
        for key, val in freqs.items():
            if val == degree:
                degree_num.append(key)
    
        # use two pointers to find the minimum interval with the degree
        left = 0
        res = float('inf')
        for num in degree_num:
            right = 0
            temp = degree
            while nums[left] != num:
                left += 1
            right = left + 1
            temp -= 1
            while temp != 0 and right < len(nums):
                if nums[right] == num:
                    temp -= 1
                right += 1
            res = min(res, right - left)
        return res


if __name__ == "__main__":

    arr = [1,2,2,3,1,4,2]
    obj = Solution()
    print(obj.findShortestSubArray(arr))
