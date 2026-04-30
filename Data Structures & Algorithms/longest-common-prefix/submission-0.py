class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(min(strs, key=len))):
            curr = strs[0][i]
            for word in strs:
                if word[i] != curr:
                    return ans
            ans += curr
        return ans
            


