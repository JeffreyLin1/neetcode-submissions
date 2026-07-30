class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)

        for i in range(k, k + maxPts):
            if i <= n:
                dp[i] = 1
        windowSum = sum(dp[k:k + maxPts])
        for i in range(k-1, -1 ,-1):
            dp[i] += windowSum / maxPts
            windowSum += dp[i]
            windowSum -= dp[i + maxPts]

        return dp[0]
        
