class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def backtrack(curr, picks):
            if len(curr) == len(nums):
                perms.append(curr[:])
                return

            for i in range(len(picks)):
                if not picks[i]:
                    picks[i] = True
                    curr.append(nums[i])
                    backtrack(curr, picks)
                    picks[i] = False
                    curr.pop()
                    
        backtrack([], [False] * len(nums))

        return perms