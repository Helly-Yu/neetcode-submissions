class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = 1
        minp = 1
        res = max(nums)
        for num in nums:
            temp = maxp*num
            maxp = max(maxp*num, minp*num, num)
            minp = min(temp, minp*num, num)
            res = max(res, maxp)
        return res
