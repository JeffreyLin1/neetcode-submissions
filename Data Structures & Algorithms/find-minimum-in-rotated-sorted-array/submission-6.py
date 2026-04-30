class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r ) // 2
            rm = m + 1
            if len(nums) <3:
                return min(nums)
            if rm == len(nums):
                rm = 0
            if nums[m-1] > nums[m] < nums[rm]:
                return nums[m]
            elif nums[l] > nums[m] or nums[l] < nums[m] < nums[r]:
                r = m-1
            elif nums[r] < nums[l] < nums[m]:
                l = m+1
            elif nums[m] == nums[l] and nums[m] > nums[r]:
                return nums[r]
            



            