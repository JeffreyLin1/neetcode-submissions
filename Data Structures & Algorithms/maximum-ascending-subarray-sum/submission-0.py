class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                ans = max(ans, curr)
                curr = 0
            curr += nums[i]
        return max(ans, curr)
