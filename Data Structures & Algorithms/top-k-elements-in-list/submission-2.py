from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time:o(n) space:o(n)
        count = Counter(nums) 
        # bucket[i] store the num happend i times
        bucket = [[] for _ in range(len(nums)+1)]
        print(count.items())

        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        # from high freq to low
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
    

        