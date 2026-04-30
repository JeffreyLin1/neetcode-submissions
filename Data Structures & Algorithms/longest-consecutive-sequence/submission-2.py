from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for num in nums:
            if num-1 not in numSet:
                i = 1
                while(num+i in numSet):
                    i += 1
                length = max(length, i)
        return length
