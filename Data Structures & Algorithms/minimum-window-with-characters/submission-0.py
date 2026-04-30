from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substrings = []
        for i in range(len(s)):
            l = r = i
            while r < len(s):
                sub = ""
                for j in range(l, r+1):
                    sub += s[j]
                substrings.append(sub)
                r += 1
        ans = ""
        for sub in substrings:
            issub = True
            tset = defaultdict(int)
            for c in t:
                tset[c]+=1
            for c in sub:
                tset[c] -= 1
            for c in tset.values():
                if c > 0:
                    issub = False
            if issub and (ans == "" or len(ans) > len(sub)):
                ans = sub

        return ans

                





            