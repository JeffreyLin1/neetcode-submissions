class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            need = target - j
            if need in d:
                return [d[need], i]
            d[j] = i