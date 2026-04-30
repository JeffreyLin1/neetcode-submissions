import heapq
from collections import defaultdict
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        ans = 0
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        for task in count:
            heapq.heappush(heap, -count[task])
        wl = deque()
        while heap or wl:
            if wl and wl[0][1] == ans:
                heapq.heappush(heap, wl.popleft()[0])
            if heap:
                task = heapq.heappop(heap)
                if task < -1:
                    wl.append([task+1, ans + n + 1])
            ans += 1
            
        return ans
        
