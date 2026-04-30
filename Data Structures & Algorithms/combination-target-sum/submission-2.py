class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.backtrack(0, [], combs, nums, target, 0)
        return combs

    def backtrack(self, i, curComb, combs, nums, target, curSum):
        if i == len(nums) or curSum > target:
            return
        if curSum == target:
            combs.append(curComb[:])
            return

        curComb.append(nums[i])
        self.backtrack(i, curComb, combs, nums, target, curSum + nums[i])
        curComb.pop()
        self.backtrack(i + 1, curComb, combs, nums, target, curSum)
        

