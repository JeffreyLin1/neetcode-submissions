# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        positions = defaultdict(list)

        q = deque()
        mn = 0
        mx = 0
        q.append((root, 0))
        while q:
            curr = q.popleft()
            positions[curr[1]].append(curr[0].val)
            if curr[0].left:
                q.append((curr[0].left, curr[1] - 1))
                mn = min(curr[1]-1, mn)
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
                mx = max(curr[1] + 1, mx)
        ans = [positions[i] for i in range(mn, mx + 1)]
        return ans 


        
