# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if not root:
                return 0
            good = 0
            if root.val >= m:
                good = 1
            return good + dfs(root.left, max(root.val, m)) + dfs(root.right, max(root.val, m))
        if not root:
            return 0
        return dfs(root, root.val)
        