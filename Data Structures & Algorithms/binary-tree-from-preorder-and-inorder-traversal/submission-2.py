# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inord = {j: i for i, j in enumerate(inorder)}
        def build(preL, preR, inL, inR):
            nonlocal inord
            if preL > preR:
                return None
            root = TreeNode(preorder[preL])
            mid = inord[root.val]
            root.left = build(preL + 1, preL + mid - inL, inL, mid - 1)
            root.right = build(preL + 1 + mid - inL, preR, mid + 1, inR)
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)