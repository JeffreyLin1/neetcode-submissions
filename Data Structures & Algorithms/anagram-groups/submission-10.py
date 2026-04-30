from collections import defaultdict
import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            a = [0]*26
            for character in word:
                a[ord(character) - ord("a")] += 1
            answer[tuple(a)].append(word)
        return list(answer.values())


                




