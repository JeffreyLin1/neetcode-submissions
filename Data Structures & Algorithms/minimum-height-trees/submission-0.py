from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for node, nxt in edges:
            adj[node].append(nxt)
            adj[nxt].append(node)
        v = set()
        def dfs(root):
            if root in v or root not in adj or not adj[root]:
                return 0
            
            v.add(root)
            height = 1 + dfs(adj[root][0])
            for i in range(1, len(adj[root])):
                height = max(height, dfs(adj[root][i]) + 1)
            return height
        heights = defaultdict(list)
        mh = float('inf')
        for i in range(n):
            v = set()
            height = dfs(i)
            if height <= mh:
                mh = height
                heights[mh].append(i)
        return heights[mh]
