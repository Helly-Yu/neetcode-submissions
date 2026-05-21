import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = int(np.prod(nums[:i]) * np.prod(nums[i+1:]))
        return res
            
        