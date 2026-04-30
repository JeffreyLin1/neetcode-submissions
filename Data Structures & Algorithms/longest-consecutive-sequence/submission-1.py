from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        length = 0
        for num in nums:
            numSet.add(num)
        for num in nums:
            if num-1 not in numSet:
                con = [num]
                i = 1
                while(num+i in numSet):
                    con.append(num+i)
                    i += 1
                length = max(length, len(con))
        return length
