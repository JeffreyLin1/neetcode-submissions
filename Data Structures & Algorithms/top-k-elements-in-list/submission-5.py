from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = defaultdict(int)
        for i in nums:
            occ[i] += 1
        occur = [(-value, key) for key, value in occ.items()]
        yo = []
        for i in occur:
            heapq.heappush(yo, i)
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(yo)[1])
        return answer

