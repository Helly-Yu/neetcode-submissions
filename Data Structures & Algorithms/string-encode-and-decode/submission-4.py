class Solution:

    def encode(self, strs: List[str]) -> str:
        # time: o(m) space:o(m+n)
        res = []
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # time: o(m) space:o(m+n)
        res = []
        i = 0
        while i < len(s):
            # 1. find the "#"
            j = i
            while s[j]!="#":
                j += 1
            # 2. get the length
            length = int(s[i:j])
            # 3. according to the length, get teh word
            start = j+1
            end = start + length
            res.append(s[start:end])

            # 4. move to the start of the next word
            i = end
        return res
