class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time: O(2^(t/m)) space:O(t/m)
        res = []
        def dfs(i, curr, total):
            # success: if the total == target
            if total == target:
                res.append(curr.copy())
                return
            
            # fail: 
            if total > target or i >= len(nums):
                return
            
            # decision 1: choose nums[i], and do not move i
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            
            # decision 2: do not use nums[i]
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0,[],0)
        return res
