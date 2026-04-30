class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,j in enumerate(nums):
            if (target-j) in s:
                return [s[target-j], i]
            s[j] = i
