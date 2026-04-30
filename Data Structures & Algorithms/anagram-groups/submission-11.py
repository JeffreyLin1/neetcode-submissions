from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = defaultdict(list)
        for word in strs:
            freqList = [0] * 26
            for c in word:
                freqList[ord(c)-97] += 1
            freqDict[tuple(freqList)].append(word)

        return list(freqDict.values())


            