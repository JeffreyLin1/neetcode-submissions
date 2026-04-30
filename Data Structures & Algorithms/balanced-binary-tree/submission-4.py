# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            lheight = dfs(node.left)
            rheight = dfs(node.right)
            if lheight == -1 or rheight == -1:
                return -1
            if abs(lheight - rheight) > 1:
                return -1
            else:
                return 1 + max(lheight, rheight)
        if not root:
            return True
        if dfs(root) < 0:
            return False
        else:
            return True
        
        
        
        
        
        
            