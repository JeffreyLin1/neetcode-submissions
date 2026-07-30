class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def help(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            best = float('inf')
            if amount in cache:
                return cache[amount]
            for coin in coins:
                amt = help(amount - coin)
                if amt > -1:
                    best = min(best, amt + 1)
            if best != float('inf'):
                cache[amount] = best
            else:
                cache[amount] = -1
            return cache[amount]
        return help(amount)
                

