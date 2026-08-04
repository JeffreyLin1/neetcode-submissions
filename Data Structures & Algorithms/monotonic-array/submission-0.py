class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if t == 0:
                    return False
                t = 1
            elif nums[i] < nums[i-1]:
                if t == 1:
                    return False
                t = 0
        return True