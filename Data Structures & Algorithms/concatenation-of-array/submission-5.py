import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = copy.copy(nums)
        for i in nums:
            ans.append(i)
        return ans