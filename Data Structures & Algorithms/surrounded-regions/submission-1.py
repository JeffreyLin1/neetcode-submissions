class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        1. iterate over border
        2. if a cell is 0, run dfs and turn EVERY o in its path into an X.
        '''
        n = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        def dfs(r, c):
            if (min(r, c) < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                board[r][c] == 'X' or
                (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in n:
                dfs(r + dr, c + dc)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if c == 0 or r == 0 or c == len(board[0])-1 or r == len(board) -1:
                    dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visit:
                    board[r][c] = 'X'



            

