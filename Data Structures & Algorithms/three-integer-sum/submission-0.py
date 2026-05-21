class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sort = sorted(nums)
        for i in range(len(sort)):
            if sort[i] > 0:
                break
            elif i>0 and sort[i] == sort[i-1]:
                continue
            
            l = i+1
            r = len(sort)-1
            while l<r:
                s = sort[i]+sort[l]+sort[r]
                if s < 0:
                    l+=1
                elif s>0:
                    r-=1
                elif s == 0:
                    res.append([sort[i], sort[l], sort[r]]) 
                    l += 1
                    r -= 1
                    while l<r and sort[l] ==sort[l-1]:
                        l+=1
        return res
            