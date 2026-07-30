class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(r, c):
            if r == len(grid) or c == len(grid[0]) or grid[r][c] == 0 or min(r, c) < 0:
                return 1
            
            if (r, c) in visit:
                return 0
            
            count = 0
            visit.add((r,c))
            count += dfs(r, c + 1)
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c - 1)

            return count
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = dfs(i, j)
                    return ans
        return ans
        