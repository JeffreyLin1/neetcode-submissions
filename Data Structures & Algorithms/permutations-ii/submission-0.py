class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def backtrack(curr, pick):
            if len(curr) == len(nums):
                for i in perms:
                    if i == curr:
                        return
                perms.append(curr[:])

            for i in range(len(pick)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    backtrack(curr, pick)
                    pick[i] = False
                    curr.pop()
        backtrack([], [False]*len(nums))
            
        return perms