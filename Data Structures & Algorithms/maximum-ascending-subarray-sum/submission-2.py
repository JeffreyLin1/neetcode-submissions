class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = 0
            curr += nums[i]
            ans = max(ans, curr)
        return max(ans, curr)
