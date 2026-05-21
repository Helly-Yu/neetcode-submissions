class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print("encode:", res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print("j:",j)
            length = int(s[i:j]) # get the length of s in str
            print("length:", length)
            i = j + 1
            print("i",i)
            j = i + length
            print("j:",j)
            res.append(s[i:j])
            i = j

        return res