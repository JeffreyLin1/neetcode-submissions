class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= ans[-1][1]:
                if end > ans[-1][1]:
                    ans[-1][1] = end
            else:
                ans.append([start, end])
                
        return ans