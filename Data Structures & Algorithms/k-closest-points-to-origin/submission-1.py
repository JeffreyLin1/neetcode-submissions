import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for cord in points:
            distance = math.sqrt((cord[0]**2) + (cord[1]**2))
            heapq.heappush(heap, (distance, cord[0], cord[1]))
        ans = []
        for i in range(k):
            cords = heapq.heappop(heap)
            ans.append([cords[1], cords[2]])
        return ans
