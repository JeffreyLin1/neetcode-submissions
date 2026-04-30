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
                return 0
            lMax = max(0, dfs(root.left))
            rMax = max(0, dfs(root.right))

            ans = max(ans, root.val + lMax + rMax)
            return root.val + max(lMax, rMax)
        dfs(root)
        return ans
