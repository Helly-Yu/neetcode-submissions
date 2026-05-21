class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountS, CountT={},{}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            CountS[a] = 1 + CountS.get(a,0)
            CountT[b] = 1+ CountT.get(b,0)
        return CountS == CountT
