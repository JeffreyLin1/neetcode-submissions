class Solution:
    def climbStairs(self, n: int) -> int:
        def help(n, cache):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = help(n - 1, cache) + help(n-2, cache)
            return cache[n]
        return help(n, {})