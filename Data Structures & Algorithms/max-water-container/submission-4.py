class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i,  num in enumerate(heights):
            for j, num2 in enumerate(heights):
                if i == j:
                    continue
                ans = max(min(num, num2)*abs(j-i), ans)
                print(ans)
        return ans