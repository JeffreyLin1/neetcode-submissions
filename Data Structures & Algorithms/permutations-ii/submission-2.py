class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        nums.sort()
        def backtrack(curr, pick):
            if len(curr) == len(nums):
                perms.append(curr[:])

            for i in range(len(pick)):
                if not pick[i]:
                    if (nums[i-1] == nums[i] and pick[i-1]) or nums[i-1] != nums[i] or i == 0:
                        curr.append(nums[i])
                        pick[i] = True
                        backtrack(curr, pick)
                        pick[i] = False
                        curr.pop()
        backtrack([], [False]*len(nums))
            
        return perms