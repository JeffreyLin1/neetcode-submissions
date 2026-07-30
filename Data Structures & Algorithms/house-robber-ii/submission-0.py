class Solution:
    def rob(self, nums: List[int]) -> int:

        def help(nums):
            if len(nums) < 2:
                return nums[0]
            dp = [nums[0]]
            dp.append(max(nums[0], nums[1]))

            for i in range(2, len(nums)):
                dp.append(max(dp[i-1], dp[i-2] + nums[i]))

            return dp[-1]
        if len(nums) < 2:
            return nums[0]
        return max(help(nums[1:]), help(nums[:-1]))