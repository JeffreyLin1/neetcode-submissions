class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        curr = intervals[0]
        '''
        intervals=[[1,3],[1,5],[6,7]]
        curr = [6, 7]
        ans = [[1, 3]]
        '''
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= curr[1]:
                if end > curr[1]:
                    curr[1] = end
            elif start > curr[1]:
                ans.append(curr)
                curr = [start, end]

        if not ans or curr != ans[-1]:
            ans.append(curr)
                
        return ans