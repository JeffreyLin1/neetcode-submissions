class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m] > x:
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                break
        if arr[m] < x:
            l, r = m, m + 1
        else:
            l, r = m-1, m
        left = []

        for i in range(k):
            if l < 0:
                ans.append(arr[r])
                r += 1
            elif r >= len(arr):
                left.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) > abs(arr[r] - x):
                ans.append(arr[r])
                r += 1
            else:
                left.append(arr[l])
                l -= 1
        ans = left[::-1] + ans
        return ans


            