class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        curcomb=[]
        def backtrack(i, curcomb):
            if len(curcomb) == k:
                combs.append(curcomb.copy())
                return
            if i > n:
                return
            
            curcomb.append(i)
            backtrack(i + 1, curcomb)
            curcomb.pop()
            backtrack(i + 1, curcomb)
        backtrack(1, curcomb)
        return combs