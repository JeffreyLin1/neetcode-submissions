import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
