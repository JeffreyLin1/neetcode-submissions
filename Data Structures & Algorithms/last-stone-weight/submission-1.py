import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            one = heapq.heappop_max(stones)
            two = heapq.heappop_max(stones)
            if one != two:
                heapq.heappush_max(stones, one-two)
        if not stones:
            return 0
        else:
            return stones[0]