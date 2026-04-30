class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(c.lower() for c in s if c.isalnum())
        for i in range(len(new)//2):
            if new[i] != new[-1-i]:
                return False
        return True