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
        level = 0
        while len(qu)>0:            
            ans.append([])
            for i in range(len(qu)):
                curr = qu.popleft()
                ans[level].append(curr.val)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            level += 1   
        return ans