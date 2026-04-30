class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three buckets - red, white, blue
        # bucket stores indices
        # iterate through buckets and swap(?)

        r = w = b = 0
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                w += 1
            else:
                b += 1
        for i in range(r):
            nums[i] = 0
        for i in range(w):
            nums[r + i] = 1
        for i in range(b):
            nums[r + w + i] = 2
