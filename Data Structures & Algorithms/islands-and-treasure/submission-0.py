from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        n = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        a = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        v = set()
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == inf:
                    grid[r][c] = a
                for dr, dc in n:
                    ar, ac = r + dr, c + dc
                    if (min(ar,ac) < 0 or
                        ar == len(grid) or
                        ac == len(grid[0]) or
                        grid[ar][ac] == -1 or
                        (ar, ac) in v
                        ):
                        continue
                    q.append((ar, ac))
                    v.add((r, c))
            a += 1

                                
                                
                                
        