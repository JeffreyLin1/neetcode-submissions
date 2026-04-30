from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts, countd = defaultdict(int), defaultdict(int)
        for i, j in zip(s, t):
            counts[i] += 1
            countd[j] += 1
        return counts == countd

        return True
            