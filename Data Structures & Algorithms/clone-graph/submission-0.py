"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        on = {}
        
        def dfs(node):
            if node in on:
                return on[node]
            if not node:
                return None
            nCopy = Node(node.val)
            on[node] = nCopy
            for n in node.neighbors:
                nCopy.neighbors.append(dfs(n))
            return nCopy
        return dfs(node)


