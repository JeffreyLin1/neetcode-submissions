class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixRows = [[] for i in range(len(matrix))]
        for row in range(len(matrix)):
            sum = 0
            for num in range(len(matrix[row])):
                sum += matrix[row][num]
                self.prefixRows[row].append(sum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            if col1 != 0:
                ans += (self.prefixRows[i][col2] - self.prefixRows[i][col1-1])
            else:
                ans += (self.prefixRows[i][col2])
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)