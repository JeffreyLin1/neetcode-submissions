class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def backtrack(curSet, curSum, i):
            if curSum == target:
                combs.append(curSet[:])
                return
            
            for j in range(i, len(candidates)):
                if curSum + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curSet.append(candidates[j])
                backtrack(curSet, curSum + candidates[j], j+1)
                curSet.pop()
        
        backtrack([], 0, 0)
        return combs
            
            
