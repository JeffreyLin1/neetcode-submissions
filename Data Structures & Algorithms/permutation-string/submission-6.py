from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1set = {}
        for c in s1:
            s1set[c] = s1set.get(c, 0) + 1

        l = 0
        winset = {}
        print(s1set)
        for r in range(len(s2)):
            winset[s2[r]] = winset.get(s2[r], 0) + 1
            
            if r-l == len(s1):
                winset[s2[l]] -= 1
                if winset[s2[l]] == 0:
                    winset.pop(s2[l])
                l += 1  
            r += 1
            if s1set == winset: 
                return True
            print(winset)
        return False
