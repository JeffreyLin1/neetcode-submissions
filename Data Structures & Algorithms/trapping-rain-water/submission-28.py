class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1, len(height)-1):
            left = height[:i]
            right = height[i+1:]
            leftMax = max(left)
            rightMax = max(right)
            
            water = min(leftMax, rightMax) - height[i]
            if water > 0:
                ans += min(leftMax, rightMax) - height[i]

            

        return ans
            

