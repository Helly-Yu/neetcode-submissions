class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: o(n) space:0(m)
        l = 0
        result = set()
        max_length = 0
        for r in range(len(s)):
            # Continuously shrink the window until the duplicate is removed
            while s[r] in result:
                result.remove(s[l])
                l+=1
            # add the current character
            result.add(s[r])
            # update the max length
            max_length = max(max_length, r-l+1)
        
        return max_length


            




        