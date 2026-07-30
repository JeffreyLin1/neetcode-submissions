class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1. if the entire arr is desc, reverse and return
        2. reverse search the array for the first instance of a descending order
        3. swap the numbers, then sort everything past that by ascending order
        '''
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
                        break
                tmp = nums[sdx]
                nums[sdx] = nums[i]
                nums[i] = tmp
                break
        if idx == 0:
            nums.sort()
        nums[idx:] = sorted(nums[idx:])
