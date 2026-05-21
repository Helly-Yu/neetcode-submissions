
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)           # 走一步
            fast = self.get_next(self.get_next(fast)) # 走两步
        
        # seen = set()
        # while n!=1 and n not in seen:
        #     seen.add(n)
        #     n = sum(int(i)**2 for i in str(n))
        
        # return n == 1
            
        return fast == 1
    
    def get_next(self, number:int):
        return sum(int(i)**2 for i in str(number))




            


        