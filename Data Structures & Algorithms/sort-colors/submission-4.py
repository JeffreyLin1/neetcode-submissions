class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # one pointer to traverse through list
        # when encounter a 0, place at the end of our current 0 section
        # when encounter a 2, place at the start of the 2 section
        red, blue = 0, len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                tmp = nums[red]
                nums[red] = 0
                nums[i] = tmp
                red += 1
            elif nums[i] == 2:
                tmp = nums[blue]
                nums[blue] = 2
                nums[i] = tmp
                blue -= 1
                i -= 1
            i += 1
                

            


