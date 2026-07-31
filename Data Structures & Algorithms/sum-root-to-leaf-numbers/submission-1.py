# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(root, curr):
            if not root:
                return
            curr.append(str(root.val))
            if not root.left and not root.right:
                nums.append("".join(curr))
            else:
                dfs(root.left, curr)
                dfs(root.right, curr)
            curr.pop()

        dfs(root, [])
        ans = 0
        for num in nums:
            ans += int(num)
        return ans




