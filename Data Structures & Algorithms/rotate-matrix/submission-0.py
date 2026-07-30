class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose matrix
        # reverse every row
        n = len(matrix) - 1

        for i in range(n):
            for j in range(i, n+1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        for row in matrix:
            row[:] = row[::-1]
        

