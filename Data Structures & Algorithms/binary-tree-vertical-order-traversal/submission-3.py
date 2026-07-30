# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        positions = defaultdict(list)

        q = deque()
        if root:
            q.append((root, 0))
        while q:
            curr = q.popleft()
            positions[curr[1]].append(curr[0].val)
            if curr[0].left:
                q.append((curr[0].left, curr[1] - 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
        ans = []
        if positions:
            for i in range(min(positions), max(positions) + 1):
                if i in positions:
                    ans.append(positions[i])
        return ans 


        
