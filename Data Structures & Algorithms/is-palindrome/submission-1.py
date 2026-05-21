class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time: o(n) space:o(1)
        s = s.lower()
        # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
        l = 0
        r = len(s)-1
        while l < r:
            # 1. make sure l doesn't cross the line
            while l<r and not s[l].isalnum():
                l+=1
            # 2. same to r
            while r>l and not s[r].isalnum():
                r-=1
            
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        
        