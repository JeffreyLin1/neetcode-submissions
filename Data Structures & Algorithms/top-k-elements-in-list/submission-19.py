from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int) 
        for i in nums:
            mapping[i] += 1
        ans = []
        for i in range(len(nums)+1):
            ans.append([])
        for key, value in mapping.items():
            ans[value].append(key)
        ans2 = []
        for i in range(len(ans)-1, -1, -1):
            for j in ans[i]:
                ans2.append(j)
                if len(ans2) == k:
                    return ans2

        return ans2
        
        

