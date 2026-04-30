from collections import defaultdict
import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = []
        nodupe = []
        for i in strs:
            counts = defaultdict(int)
            for j in i:
                counts[j] += 1
            dicts.append(counts)
        ans = []

        for dic in dicts: # iterate over all dicts 
            if dic not in nodupe: 
                # this means we have not yet made an inner list of this anagram yet
                
                a = []
                for index, word in enumerate(dicts):
                    if word == dic:
                        a.append(strs[index]) # append the corresponding word
                ans.append(a)
                nodupe.append(dic)
        




        return ans
                




