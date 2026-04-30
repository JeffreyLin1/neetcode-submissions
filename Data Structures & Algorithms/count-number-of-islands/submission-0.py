class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        # iterate through list until we hit a 1
        # recursively call dfs and turn each 1 we hit into a 0
        def dfs(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans
