class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.backtrack(0, [], combs, nums, target, 0)
        return combs

    def backtrack(self, i, curComb, combs, nums, target, curSum):
        if curSum == target:
            combs.append(curComb[:])
            return

        for j in range(i, len(nums)):
            if curSum + nums[j] > target:
                continue
            curComb.append(nums[j])
            self.backtrack(j, curComb, combs, nums, target, curSum + nums[j])
            curComb.pop()
        
                
        

