class Solution:
    def rob(self, nums: List[int]) -> int:
        # option a: nums[0:n-1]
        # option b: nums[1:n]
        n = len(nums)
        if n==1:
            return nums[0]
        
        res1 = self.calcu(nums[0:n-1])
        res2 = self.calcu(nums[1:n])
        return max(res1, res2)
    
    def calcu(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
