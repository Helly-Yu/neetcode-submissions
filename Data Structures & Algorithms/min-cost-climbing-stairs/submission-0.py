class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # start from index 0 or 1
    # step 1 or 2 
    # top floor is the one after the last index
        cost.append(0) 
        #[1,2,3,8,5,7,4,0] i = 5 cost[5]= 7
        for i in range(len(cost)-3, -1, -1):
            # i = 5 cost[5]= 7, cost[6]=4, cost[7]=0, cost[5]= 7
            # i = 4 cost[4]= 5, cost[5]=7, cost[6]=4, cost[4]= 9
            # i = 3 cost[3]= 8, cost[4]= 9, cost[5]=7, cost[3] = 15
            # i = 2 cost[2]=3, cost[3] = 15, cost[4]= 9, cost[2] = 12
            # i = 1 cost[1]=2, cost[2] = 12, cost[3] = 15, cost[1] = 14
            # i = 0 cost[0]=1, cost[1] = 14, cost[2]=12 cost[0]=13
            cost[i] += min(cost[i+1], cost[i+2]) # 1-step or 2
            # 0->2->4->6
        return min(cost[0],cost[1])
        




