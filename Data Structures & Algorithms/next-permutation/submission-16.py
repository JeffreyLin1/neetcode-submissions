class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                idx = i + 1
                sdx = idx
                smallest = nums[idx]
                for j in range(idx, len(nums)):
                    if nums[j] < smallest and nums[j] > nums[i]:
                        sdx = j
                        smallest = nums[j]
                tmp = nums[sdx]
                nums[sdx] = nums[i]
                nums[i] = tmp
                break
        if idx != 0:
            r = len(nums) - 1
            while idx < r:
                t = nums[idx]
                nums[idx] = nums[r]
                nums[r] = t
                idx += 1
                r -= 1
        else:
            nums[:] = reversed(nums)
