class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]]) # max_f 是一个“标杆”：它记录了窗口曾达到过的“最高效率”。不需要变小：因为即使变小了，计算出来的窗口长度也会变小，对求 max 没有任何贡献。
            if (r - l + 1)-maxf > k:
                count[s[l]]-=1
                l+=1

            res = max(r-l+1, res)

        return res
        

        