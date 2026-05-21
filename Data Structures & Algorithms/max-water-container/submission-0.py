class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        container = 0
        while l < r:
            if heights[l] < heights[r]:
                store = (r-l) * heights[l]
                l+=1
            else:
                store = (r-l) * heights[r]   
                r-=1   

            container = max(container, store)
        
        return container