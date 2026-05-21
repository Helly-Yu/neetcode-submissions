class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int) # 如果发现新键，默认值设为 int (也就是 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        for num in nums:
            hashmap[num]+=1
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        
        res = []
        # 从后往前遍历桶（频率从高到低）
        for i in range(len(buckets)-1, 0 , -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        