class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for r in range(len(mat)):
            ans += mat[r][r]
            ans += mat[-1-r][r]
        if len(mat) % 2 != 0:
            ans -= mat[len(mat)//2][len(mat)//2]
        return ans