# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        qu = deque()
        if root:
            qu.append(root)
        while len(qu)>0:            
            level = []
            for i in range(len(qu)):
                curr = qu.popleft()
                level.append(curr.val)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            if level:
                ans.append(level) 
        return ans