class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset = []
        subsets = []
        
        def helper(i, curset, subsets):
            if i == len(nums):
                subsets.append(curset[:])
                return
            curset.append(nums[i])
            helper(i + 1, curset, subsets)
            curset.pop()
            helper(i + 1, curset, subsets)
        helper(0, curset, subsets)
        return subsets
        