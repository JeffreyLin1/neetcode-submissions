class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = []
        cache = {}
        def help(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = cost[i] + min(help(i + 1), help(i + 2))
            return cache[i]
        return min(help(0), help(1))