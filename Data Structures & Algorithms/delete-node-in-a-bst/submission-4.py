# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None

        while curr and curr.val != key:
            parent = curr
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
        
        if not curr:
            return root
        
        if curr.left and curr.right:
            curr2 = curr.right
            p2 = curr
            while curr2.left:
                p2 = curr2
                curr2 = curr2.left
            if p2.left == curr2:
                p2.left = curr2.right
            else:
                p2.right = curr2.right
            curr.val = curr2.val
        elif curr.left:
            if not parent:
                root = curr.left
            elif parent.left == curr:
                parent.left = curr.left
            elif parent.right == curr:
                parent.right = curr.left
        elif curr.right:
            if not parent:
                root = curr.right
            elif parent.left == curr:
                parent.left = curr.right
            elif parent.right == curr:
                parent.right = curr.right
        else:
            if parent and parent.right == curr:
                parent.right = None
            elif parent and parent.left == curr:
                parent.left = None
            else:
                return None
        return root



        

            
            