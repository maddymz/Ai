class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        lenNums1 = m - 1
        lenNums2 = n - 1
        mergedEnd = m + n - 1
        
        while lenNums1 >= 0:
            if nums1[lenNums1] > nums2[lenNums2]:
                nums1[mergedEnd] = nums1[lenNums1]
                lenNums1 -= 1
            else:
                nums1[mergedEnd] = nums2[lenNums2]
                lenNums2 -= 1
        
        return nums1


if __name__ == "__main__":

    obj = Solution()

    print(obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3))