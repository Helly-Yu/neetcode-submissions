class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time:o(n2) space:o(1)
        res = []
        # sort 
        nums.sort()
        n = len(nums)
        for i in range(n):
            # if the first one is bigger than 0, then there is no way.
            if nums[i] > 0:
                break
            
            # skip the duplicate one
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # initial the double pointers(all at the right of i)
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # skip the duplicate
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
        return res

                    

