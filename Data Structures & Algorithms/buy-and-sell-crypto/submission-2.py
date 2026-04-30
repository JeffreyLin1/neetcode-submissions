class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0,1
        while r < len(prices):
            windowProfit = prices[r] - prices[l]
            if windowProfit <= 0:
                l = r
                r = l + 1
            elif windowProfit > 0:
                profit = max(profit, windowProfit)
                r += 1

        return profit