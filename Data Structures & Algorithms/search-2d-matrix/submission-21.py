class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0]))-1
        while l <= r:
            m = (l + r) // 2
            print("l, r: ", l, r)
            print("m: ", m)
            print("row: ", m // len(matrix))
            print("col: ", m % len(matrix[0]))
            
            mval = matrix[m // len(matrix[0])][m % len(matrix[0])]
            print("mval: ", mval)
            if target > mval:
                l = m + 1
            elif target < mval:
                r = m - 1
            else:
                return True
        return False