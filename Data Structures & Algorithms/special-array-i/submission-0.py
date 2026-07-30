class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] % 2 == nums[r] % 2:
                return False
            l += 1
            r += 1
        return True