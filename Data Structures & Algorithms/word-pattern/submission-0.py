class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p1 = []
        p2 = []
        d1 = {}
        d2 = {}
        arr = s.split(" ")
        if len(arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d1:
                p1[d1[pattern[i]]] += 1
            else:
                d1[pattern[i]] = len(p1)
                p1.append(1)
        for i in range(len(pattern)):
            if arr[i] in d2:
                p2[d2[arr[i]]] += 1
            else:
                d2[arr[i]] = len(p2)
                p2.append(1)
        return p1 == p2

        print(arr)