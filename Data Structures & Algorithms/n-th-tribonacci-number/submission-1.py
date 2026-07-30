class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def help(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            if n in cache:
                return cache[n]
            
            cache[n] = help(n-1) + help(n-2) + help(n-3)
            return cache[n]

        return help(n)

        
