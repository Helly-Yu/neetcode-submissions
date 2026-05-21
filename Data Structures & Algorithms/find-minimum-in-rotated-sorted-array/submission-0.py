class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = nums[0]
        while i <= j:
            if nums[i] < nums[j]:
                res = min(res, nums[i])
            
            m = (i+j)//2
            res = min(res, nums[m])
            print(res)
            print(i,j)
            if nums[i] <= nums[m]:
                i = m + 1
            else:
                j = m -1
        return res
            
        
        