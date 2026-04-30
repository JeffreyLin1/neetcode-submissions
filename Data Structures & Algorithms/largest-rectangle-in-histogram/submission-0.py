class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i, h in enumerate(heights):
            maxArea = h
            minHeight = h
            for r in range(i, len(heights)):
                minHeight = min(minHeight, heights[r])
                area = min(minHeight, heights[r]) * (r - i + 1)
                maxArea = max(maxArea, area) 
            for l in range(i, -1, -1):
                minHeight = min(minHeight, heights[l])
                area = minHeight * (i - l + 1)
                maxArea = max(maxArea, area)
            ans = max(ans, maxArea)
        return ans

