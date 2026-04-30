from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        v = set()
        for c, p in prerequisites:
            adj[c].append(p)
        
        def dfs(c):
            if c in v:
                return False
            if not adj[c]:
                return True
            
            v.add(c)

            for p in adj[c]:
                if not dfs(p):
                    return False
            adj[c] = []
            v.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
            

        