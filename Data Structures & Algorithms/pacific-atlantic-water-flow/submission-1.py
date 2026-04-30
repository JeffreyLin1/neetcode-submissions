from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        tiles = {
            (r, c): [False, False]
            for r in range(len(heights)) 
            for c in range(len(heights[0]))
        }
        v = set()
        p = deque(
            (r, c)
            for r in range(len(heights))
            for c in range(len(heights[0]))
            if r == 0 or c == 0
        )
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while p:
            for i in range(len(p)):
                r, c = p.popleft()
                tiles[(r, c)][0] = True
                v.add((r, c))
                for dr, dc in neighbours:
                    fr = r + dr
                    fc = c + dc
                    if (min(fr, fc) < 0 or
                        fr == len(heights) or
                        fc == len(heights[0]) or
                        (fr, fc) in v or
                        heights[fr][fc] < heights[r][c]):
                        continue
                    
                    v.add((fr,fc))
                    p.append((fr,fc))
        a = deque(
            (r, c)
            for r in range(len(heights))
            for c in range(len(heights[0]))
            if r == len(heights)-1 or c == len(heights[0])-1
        )
        v = set()
        while a:
            for i in range(len(a)):
                r, c = a.popleft()
                tiles[(r, c)][1] = True
                v.add((r, c))
                for dr, dc in neighbours:
                    fr = r + dr
                    fc = c + dc
                    if (min(fr, fc) < 0 or
                        fr == len(heights) or
                        fc == len(heights[0]) or
                        (fr, fc) in v or
                        heights[fr][fc] < heights[r][c]):
                        continue
                    a.append((fr, fc))
        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if tiles[(r, c)] == [True, True]:
                    ans.append([r,c])
        return ans
