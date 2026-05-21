class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if odd, false for sure
        if sum(nums)%2==1:
            return False
        target = sum(nums)//2 
        dp = [False]*(target+1)
        dp[0]=True # dp[i] means if sum == i 
        for num in nums:
            for i in range(target, num-1, -1):
                # if sum can be (i-num), then plus num, sum can be i 
                print(num, i, dp[i-num])
                if dp[i-num]: 
                    dp[i]= True
                

            if dp[target]:
                return True
        
        return dp[target]
        
    