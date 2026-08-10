# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node):
            if not node:
                return None
            if not node.left:
                return node.val
            return getMin(node.left)
        def dfs(node, t):
            if not node:
                return None
            if node.val > t:
                node.left = dfs(node.left, t)
            elif node.val < t:
                node.right = dfs(node.right, t)
            else:
                if node.left and node.right:
                    node.val = getMin(node.right)
                    node.right = dfs(node.right, node.val)
                elif node.left:
                    return node.left
                elif node.right:
                    return node.right
                else:
                    return None
            return node
        return dfs(root, key)
            
            