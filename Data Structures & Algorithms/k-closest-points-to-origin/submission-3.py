class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2) + (y**2)
            heap.append((distance, x, y))
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            cords = heapq.heappop(heap)
            ans.append([cords[1], cords[2]])
        return ans
