
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            return sum(int(i)**2 for i in str(number))
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)           # 走一步
            fast = get_next(get_next(fast)) # 走两步
        
        # seen = set()
        # while n!=1 and n not in seen:
        #     seen.add(n)
        #     n = sum(int(i)**2 for i in str(n))
        
        # return n == 1
            
        return fast == 1




            


        