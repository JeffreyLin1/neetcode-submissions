class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            if (r - l + 1) % 2 == 0:
                cache[(l, r)] = max(dfs(l + 1, r) + piles[l], dfs(l, r - 1) + piles[r])
            else:
                cache[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            return cache[(l, r)]
            
        total = sum(piles)
        alice = dfs(0, len(piles) - 1) 
        return total - alice < alice