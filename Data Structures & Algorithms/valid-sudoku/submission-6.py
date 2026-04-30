class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()  
            for num in row:
                if num in rowSet:
                    return False
                if num != ".":
                    rowSet.add(num)
        for col in range(9):
            colSet = set()  
            for row in range(9):
                if board[row][col] in colSet:
                    return False
                if board[row][col] != ".":
                    colSet.add(board[row][col])
        for box in range(9):
            boxSet = set()
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box % 3) * 3 + j
                    if board[row][col] in boxSet:
                        return False
                    if board[row][col] != ".":
                        boxSet.add(board[row][col])

                    

        return True
        



