from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        l = r = 0
        tset = defaultdict(int)
        for c in t:
            tset[c] += 1
        freq = defaultdict(int)
        # start with l, r = 0
        # add a character at r to freq dict if frequency is met or below required.
        # if frequency is met, metChars += 1
        # check if metChars is = len(tset.keys())
        # if it is, if ans == "" or if len(ans) is greater than r-l:
        # ans = s[l:r]
        # then move l forward one step until the same thing happens
        # 
        metChars = 0
        while r < len(s):
            char = s[r]
            if char in tset:
                freq[char] += 1
                if freq[char] == tset[char]:
                    metChars += 1
            if metChars == len(tset.keys()):
                while l < r:
                    if s[l] in freq:
                        if freq[s[l]] - 1 < tset[s[l]]:
                            break
                        else:
                            freq[s[l]] -= 1 
                    l += 1
                if ans == "" or len(ans) > r - l + 1:
                    ans = s[l:r+1]
                freq[s[l]] -= 1
                if freq[s[l]] < tset[s[l]]:
                    metChars -= 1
                l += 1
            r += 1
        return ans

                





            