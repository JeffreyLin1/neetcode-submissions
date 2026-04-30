from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize queue with all rotten oranges on the grid
        # run bfs across all of them traversing only through oranges
        # turn 1 -> 2
        # run the counter until all reachable oranges are 2
        # run through the matrix one more time to check if there are still any fresh
        # if so return -1
        q = deque()
        n = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in n:
                    fr, fc = r + dr, c + dc
                    if (min(fr, fc) < 0 or
                        fr == len(grid) or
                        fc == len(grid[0]) or
                        grid[fr][fc] == 2 or
                        grid[fr][fc] == 0):
                        continue
                    grid[fr][fc] = 2
                    q.append((fr, fc))
            if q:
                time += 1

        for r in grid:
            for c in r:
                if c == 1:
                    return -1
        
        return time

