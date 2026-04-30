# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        def sametree(p, q):
            if (not p and not q):
                return True
            elif (p and q) and sametree(q.left, p.left) and sametree(q.right, p.right) and p.val == q.val:
                return True
            else:
                return False
        if sametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        else:
            return False
            

        