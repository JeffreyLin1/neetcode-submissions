from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        deg = [0] * n
        for i in range(n):
            for e in adj[i]:
                deg[e] += 1

        q = deque()  
        for i in range(len(deg)):
            if deg[i] <= 1:
                q.append(i)
        rem = n
        while rem > 2:
            rem -= len(q)
            s = len(q)
            for _ in range(s):
                curr = q.popleft()
                for node in adj[curr]:
                    deg[node] -= 1
                    if deg[node] == 1:
                        q.append(node)
                    
        return list(q)

