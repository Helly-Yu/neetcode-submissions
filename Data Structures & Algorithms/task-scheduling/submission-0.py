class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # caclulate each task's count
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            # if there is any task
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1 # 取出当前频率最高的任务（注意是负数，+1 相当于绝对值减 1）
                if cnt != 0:
                    q.append([cnt, time+n]) # 如果任务还没做完，计算它的“解禁时间”并入队
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

