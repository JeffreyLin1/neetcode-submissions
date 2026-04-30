from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        v = set()
        for i in prerequisites:
            adj[i[0]].append(i[1])
            
        def dfs(course):
            if not adj[course]:
                return True
            if course in v:
                return False
            v.add(course)
            for p in adj[course]:
                if not dfs(p):
                    return False
            adj[course] = []
            v.remove(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            
            

        