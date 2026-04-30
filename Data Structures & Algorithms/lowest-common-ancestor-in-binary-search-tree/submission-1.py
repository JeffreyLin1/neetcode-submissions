# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, q, p)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, q, p)
        else:
            return root
        

