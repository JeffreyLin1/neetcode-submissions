class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupes = set()
        i = 0
        while i < len(nums):
            if nums[i] in dupes:
                nums.pop(i)
                i -= 1
            else:
                dupes.add(nums[i])
            i += 1
        return len(nums)