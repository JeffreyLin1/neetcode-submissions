from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.keys[key]
        l, r = 0, len(vals)
        while l < r:
            m = (l + r) // 2
            if timestamp >= vals[m][1]:
                l = m + 1
            else:
                r = m
        return vals[l-1][0] if l > 0 else ""

