from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        a = defaultdict(list)
        for i, j in edges:
            a[i].append(j)
            a[j].append(i)
        
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            for i in a[node]:
                if i == parent:
                    continue
                if not dfs(node, i):
                    return False
            return True
        return dfs(-1, 0) and len(visited) == n