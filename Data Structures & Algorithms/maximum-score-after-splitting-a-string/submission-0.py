class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(c) for c in s]
        right = sum(nums[1:])
        if nums[0] == 0:
            left = 1
        else:
            left = 0
        ans = right + left
        for c in s[1:len(s)-1]:
            n = int(c)
            if n == 0:
                left += 1
            if n == 1:
                right -= 1
            ans = max(ans, left + right)
        return ans