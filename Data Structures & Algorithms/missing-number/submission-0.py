class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = [0,2]
        # len(nums) = 2, range = [0,2], [0,1,2]
        # XOR: ^ 
        res = 0
        for i in range(len(nums)):
            optimal = i # at most (len-1)
            fact = nums[i] 
            res += (optimal-fact)

        return res + len(nums)


        