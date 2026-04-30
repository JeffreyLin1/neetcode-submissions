# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        qu = collections.deque()
        ans = []

        if root:
            qu.append(root)
        while len(qu) > 0:
            l = len(qu)
            for i in range(l):
                curr = qu.popleft()
                if i == l-1:
                    ans.append(curr.val)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        return ans