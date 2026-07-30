class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dfs(i, curCap):
            if i >= len(profit):
                return 0
            if (i, curCap) in memo:
                return memo[(i, curCap)]

            memo[(i, curCap)] = dfs(i + 1, curCap)
            newCap = curCap - weight[i]
            if newCap >= 0:
                memo[(i, curCap)] = max(memo[(i, curCap)], dfs(i + 1, newCap) + profit[i])

            return memo[(i, curCap)]
        
        return dfs(0, capacity)

