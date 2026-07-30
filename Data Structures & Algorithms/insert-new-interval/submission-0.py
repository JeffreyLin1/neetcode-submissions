class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        binary search the intervals list by start time to find where it should fit
        does it overlap with adjacent intervals? if so merge with the overlapping ones
        '''

        l, r = 0, len(intervals)
        while l < r:
            mid = (l + r)//2
            if intervals[mid][0] >= newInterval[0]:
                r = mid
            else:
                l = mid + 1

        intervals.insert(l, newInterval)

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

