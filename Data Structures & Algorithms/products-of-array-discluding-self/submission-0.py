class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i,j in enumerate(nums):
            prod = 1
            for n,m in enumerate(nums):
                if n == i:
                    continue
                prod *= m
            ans.append(prod)
        return ans