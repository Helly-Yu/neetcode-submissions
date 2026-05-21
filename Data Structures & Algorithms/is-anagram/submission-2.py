class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m: # O(1)
            return False
        # return sorted(s) == sorted(t)   # time difficulty O(nlogn+mlogm)
        # O(n+m) verion:
        count = [0] * 26
        for char in s: #o(n)
            count[ord(char)-ord('a')]+=1 # ord() to get the ASCII 
            
        for char in t: #o(m)
            count[ord(char)-ord('a')]-=1
        
        for val in count: #o(1)
            if val != 0:
                return False
        
        return True

