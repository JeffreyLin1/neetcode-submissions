class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate through grid until 1
        # turn into a 0
        # dfs through the 1 but including diagonal edges too
        # dfs: 
        # base cases
        # turn current node into 0
        # island + 1
        ans = 0

        def dfs(r, c):
            if (min(r, c) < 0 or
                r == len(grid) or
                c == len(grid[0]) or
                grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            tempans = 0
            tempans += dfs(r-1, c)
            tempans += dfs(r+1, c)
            tempans += dfs(r, c-1)
            tempans += dfs(r, c+1)
            return tempans + 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = max(ans, dfs(r, c))
        return ans            
