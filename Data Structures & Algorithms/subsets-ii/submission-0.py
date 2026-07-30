class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur = []
        sub = []
        nums.sort()

        def backtrack(i, cur):
            if i == len(nums):
                sub.append(cur[:])
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            skip = cur.pop()
            while i < len(nums) and nums[i] == skip:
                i += 1
            backtrack(i, cur)
        
        backtrack(0, cur)
        return sub