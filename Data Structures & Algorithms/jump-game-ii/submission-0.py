class Solution:
    def jump(self, nums: List[int]) -> int:
        # JUMPS: I+J J<=nums[i] and i+j < len(nums)
        # jumps=0
        # curr_end = 0
        # fartest = 0

        # for i in range(len(nums)-1):
        #     # Update the overall farthest point reachable from current position
        #     fartest = max(fartest, i+nums[i]) # i+j 
        #     print(i,fartest)
        #     # If we've reached the end of the range for our current jump...
        #     if i == curr_end:
        #         jumps+=1
        #         curr_end = fartest
        #         # Optimization: if we can already reach the last index
        #         if curr_end >= len(nums)-1:
        #             break
        
        # return jumps

        res = 0
        l=r=0
        while r<len(nums)-1:
            fartest = 0
            for i in range(l,r+1):
                fartest = max(fartest, i+nums[i]) # i+j
            
            l = r+1
            r = fartest
            res += 1
        
        return res
        



