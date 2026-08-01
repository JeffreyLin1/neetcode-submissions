class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = ""

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack:
                    continue
                else:
                    stack.pop()
            ans += c

        for i in range(len(ans)-1, -1, -1):
            if not stack:
                break
            if ans[i] == '(':
                ans = ans[:i] + ans[i+1:]
                stack.pop()
        return ans


                
        