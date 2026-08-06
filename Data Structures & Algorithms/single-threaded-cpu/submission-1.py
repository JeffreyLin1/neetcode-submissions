import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # (process time, index, enqueue time)
        t = sorted([(tasks[i][1], i, tasks[i][0]) for i in range(len(tasks))], key = lambda i: i[2])
        ans = []
        heap = []
        time = 0
        i = 0
        while i < len(tasks) or heap:
            if not heap and time < t[i][2]:
                time = t[i][2]
            while i < len(tasks) and t[i][2] <= time:
                heapq.heappush(heap, (t[i][0], t[i][1]))
                i += 1
            
            proc, idx = heapq.heappop(heap)
            ans.append(idx)
            time += proc
        return ans





        
