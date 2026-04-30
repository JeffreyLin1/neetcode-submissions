class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = 1
        for i, num in enumerate(nums):
            ans.append(prefix)
            prefix *= num
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
            