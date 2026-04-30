import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify_max(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        popped = []
        for i in range(self.k-1):
            popped.append(heapq.heappop_max(self.heap))
        ans = self.heap[0]
        for i in popped:
            heapq.heappush_max(self.heap, i)
        return ans
