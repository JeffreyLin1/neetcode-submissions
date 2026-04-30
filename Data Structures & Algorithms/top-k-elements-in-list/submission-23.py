from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = []
        groupedCounts = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            groupedCounts[count].append(num)
        for i in range(len(groupedCounts)-1, 0, -1):
            for j in groupedCounts[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
