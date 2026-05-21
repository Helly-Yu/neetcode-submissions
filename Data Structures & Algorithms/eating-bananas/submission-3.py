class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)
        res = k_max

        while k_min <= k_max:
            m = (k_min + k_max)//2
            hours = 0
            for p in piles:
                hours += (p+m-1)//m
            
            if hours <= h:
                res = m
                k_max = m-1
            else:
                k_min = m+1          
        return res

                

        