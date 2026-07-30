from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.m[key]) - 1
        ans = ""
        while l <= r:
            mid = (l + r)//2
            time = self.m[key][mid][0]
            if time > timestamp:
                r = mid - 1
            elif time <= timestamp:
                l = mid + 1
                ans = self.m[key][mid][1]
            else:
                return self.m[key][mid][1]
        
        return ans

