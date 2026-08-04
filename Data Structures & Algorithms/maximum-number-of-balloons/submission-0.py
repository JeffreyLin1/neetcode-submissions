from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count['l']//2, count['b'], count['o']//2, count['n'], count['a'])