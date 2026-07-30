class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def help(curr, prev):
            if curr >= len(nums):
                return 0
            
            if (curr+1, prev) in cache:
                return cache[(curr+1, prev)]
            ans = help(curr+1, prev)

            if nums[curr] > nums[prev] or prev == -1:
                ans = max(ans, 1 + help(curr+1, curr))
            cache[(curr+1, prev)] = ans
            
            return ans
        return help(0, -1)





            
                