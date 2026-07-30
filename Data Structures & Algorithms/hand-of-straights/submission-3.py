from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        hand.sort()
        
        for i, c in enumerate(hand):
            if freq[c] == 0:
                continue
            for j in range(c, c + groupSize):
                if j not in freq or freq[j] == 0:
                    return False
                freq[j] -= 1
        
        return True
