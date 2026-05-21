class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P: the set of number with a + sign
        # N: the set of number with a - sign
        # SUM(P)+SUM(N) = TOTAL_SUM AND SUM(P)-SUM(N) = TARGET => 2SUM(P)= TOTAL_SUM+TARGET

        total_sum = sum(nums)
        if (total_sum + target) % 2 == 1 or abs(target) > total_sum:
            return 0

        new_target = (total_sum + target) // 2
        dp =[0]*(new_target+1)
        dp[0]=1
        for n in nums:
            for i in range(new_target, n-1, -1):
                dp[i]+=dp[i-n]
                print(i, dp[i])
        return dp[new_target]