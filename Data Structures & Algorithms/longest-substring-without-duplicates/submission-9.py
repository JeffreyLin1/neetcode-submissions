class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        dupes = set()
        while r < len(s):
            if s[r] in dupes:
                while s[l] != s[r]:
                    dupes.remove(s[l])
                    l += 1
                l+=1
            else:
                dupes.add(s[r])
            ans = max(ans, r-l+1)
            r +=1
                    
            
        return ans





            


