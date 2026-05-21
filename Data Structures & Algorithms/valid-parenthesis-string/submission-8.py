class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack
        left = [] # Store indices of '('
        star = [] # Store indices of '*'
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else: # s[i] == ')'
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while left and star:
            if left.pop()>star.pop():
                return False
        
        return len(left) == 0
        
        