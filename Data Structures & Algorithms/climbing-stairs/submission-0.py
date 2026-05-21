class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1): # 0,1,2,3,4
            temp = one # set temp as v1
            one = one + two # add two previous values
            two = temp # update v2 to v1
        
        return one
        