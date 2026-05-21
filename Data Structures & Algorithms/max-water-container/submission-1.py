class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # time:o(n) space:o(1)
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            min_height = min(heights[l], heights[r])
            container = min_height * (r-l)
            res = max(res, container)
            # move the shorter one
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res

            

        