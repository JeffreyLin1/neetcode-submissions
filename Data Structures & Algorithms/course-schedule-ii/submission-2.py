class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for i in prerequisites:
            adj[i[0]].append(i[1])
        visiting = set()
        ans = []
        taken = set()
        def dfs(course):
            if course in visiting:
                return None
            
            cOrd = []
            print(course)
            visiting.add(course)
            for pre in adj[course]:
                if pre in taken:
                    continue
                pres = dfs(pre)
                if not pres:
                    return None
                if pres[0] != -1:
                    cOrd.extend(pres)
            adj[course] = []
            visiting.remove(course)
            if course not in taken:
                cOrd.append(course)
                taken.add(course)
            if not cOrd:
                cOrd = [-1]
            return cOrd
        
        for i in range(numCourses):
            prereqs = dfs(i)
            if not prereqs:
                return []
            elif prereqs[0] != -1:
                ans.extend(prereqs)
        return ans
            




