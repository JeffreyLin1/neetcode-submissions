from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        ans = 0
        l = 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            maxfreq = max(freq.values())
            if r-l+1 - maxfreq > k:
                while r-l+1 - maxfreq > k:
                    freq[s[l]] -= 1
                    l += 1
                    
            else:
                ans = max(r-l+1,ans)
        return ans



            
