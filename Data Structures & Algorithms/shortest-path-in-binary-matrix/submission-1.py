from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append((0, 0))
        length = 0
        n = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while q:
            length += 1
            for i in range(len(q)):
                r, c = q.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                grid[r][c] = 1
                for dr, dc in n:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == len(grid) or
                        c + dc == len(grid[0]) or
                        grid[r + dr][c + dc] == 1):
                        continue
                    q.append((r + dr, c + dc))      
        return -1
                


                
