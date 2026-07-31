class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dp = [0]* len(boxes)
        l, r = 0, 0
        for c in range(1, len(boxes)):
            if boxes[c] == "1":
                r += 1
                dp[0] += c
        if boxes[0] == "1":
            l += 1

        for i in range(1, len(boxes)):
            dp[i] = dp[i-1] + l - r
            if boxes[i] == "1":
                l += 1
                r -= 1
        
        return dp