# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')
        def dfs(root):
            nonlocal ans
            if not root:
                return
            
            ans = max(ans, self.getMax(root.left) + self.getMax(root.right) + root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
       
    def getMax(self, root):
        if not root:
            return 0
        
        lMax = self.getMax(root.left)
        rMax = self.getMax(root.right)

        return max(0, root.val + max(lMax, rMax))