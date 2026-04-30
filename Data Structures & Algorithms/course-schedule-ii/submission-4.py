from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in prerequisites:
            adj[i[0]].append(i[1])
        v = set()
        taken = set()
        ans = []
        def dfs(c):
            if c in v:
                return False
            if c in taken:
                return True
            v.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            v.remove(c)
            taken.add(c)
            ans.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        
        return ans
            




