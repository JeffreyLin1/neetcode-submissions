class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        v = set()
        n = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        curr = (0, 0)
        ans = []
        for _ in range(len(matrix) * len(matrix[0])):
            ans.append(matrix[curr[0]][curr[1]])
            v.add(curr)
            dr, dc = n[d]
            newcurr = (curr[0] + dr, curr[1] + dc)
            if not (newcurr not in v and
                newcurr[0] > -1 and newcurr[1] > -1 and 
                newcurr[0] < len(matrix) and 
                newcurr[1] < len(matrix[0])
                ):
                d = (d+1)%4
                dr, dc = n[d]
                newcurr = (curr[0] + dr, curr[1] + dc)
            curr = newcurr

        return ans
