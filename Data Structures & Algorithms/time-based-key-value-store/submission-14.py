from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.m[key])
        while l < r:
            mid = (l + r)//2
            vals = self.m[key]
            if vals[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid 
        return vals[l-1][1] if l > 0 else ""

