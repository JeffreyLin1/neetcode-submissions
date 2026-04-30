from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1set = Counter(s1)
        l, r = 0, len(s1)-1
        while r < len(s2):
            windowset = Counter(s2[l:r+1])
            if s1set == windowset:
                return True
            l += 1
            r += 1
        return False
