from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        prev = 0
        count = defaultdict(int)
        count[0] += 1
        ans = 0
        for i in nums:
            prefix.append(prev + i)
            prev = prev + i
        for i in range(len(prefix)):
            ans += count[prefix[i] - k]
            count[prefix[i]] += 1
        return ans
            