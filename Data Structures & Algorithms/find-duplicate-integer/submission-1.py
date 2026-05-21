class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 第一阶段：寻找相遇点
        slow = fast = nums[0]
        while True:
            slow = nums[slow]          # 走一步
            fast = nums[nums[fast]]    # 走两步
            if slow == fast:
                break
        
        # 第二阶段：寻找环的入口
        slow = nums[0]                 # slow 回到起点
        while slow != fast:
            slow = nums[slow]          # 都走一步
            fast = nums[fast] 
            print(slow, fast)   
            
        return slow