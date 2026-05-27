class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # time:o(n) space:o(m)
        if len(t) > len(s):
            return ""

        first = defaultdict(int)
        second = defaultdict(int)
        
        # record the characters in t
        for char in t:
            second[char] += 1
        
        # 'have' is how many unique characters currently meet the required frequency
        have = 0 
        # 'need' is the number of UNIQUE characters we need to match
        need = len(second)

        # To keep track of the smallest window found: [left_index, right_index]
        res, res_len = [-1, -1], len(s)+1

        l = 0 
        for r in range(len(s)):
            char = s[r]

            if char in second:
                first[char] += 1
                # if equal freq
                if first[char] == second[char]:
                    have += 1
            
            # While the current window is valid
            while have == need:
                # Update our result if this window is smaller than our current best
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res = [l, r]
                # shrink the window from the left to find a smaller valid window 
                left_char = s[l]
                if left_char in second:
                    first[left_char]-=1
                    # If removing this character drops us below the required frequency, our window is no longer valid
                    if first[left_char] < second[left_char]:
                        have -= 1
                # move the left pointer
                l += 1
        
        l, r = res
        return s[l:r+1]

                





            
            

            
            
            

