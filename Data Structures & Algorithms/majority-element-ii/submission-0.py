from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        c = Counter(nums)
        for i, j in c.items():
            if j > len(nums)//3:
                ans.append(i)
        return ans
