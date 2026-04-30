import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        heapq.heappush(heap, (0, k))
        time = 0
        v = set()
        while heap:
            print(time)
            distance, node = heapq.heappop(heap)
            if node in v:
                continue
            time = max(time, distance)
            v.add(node)
            for n2, d2 in adj[node]:
                if n2 not in v:
                    heapq.heappush(heap, (distance + d2, n2))

        if len(v) != n:
            return -1
        return time
