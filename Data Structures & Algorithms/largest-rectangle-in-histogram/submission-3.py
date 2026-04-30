class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans = 0
        stack = []
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                popped = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, heights[popped] * width)
            stack.append(i)
        
        return ans