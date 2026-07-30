class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def help(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(help(i+1), help(i+2) + nums[i])

            return cache[i]
        return help(0)
