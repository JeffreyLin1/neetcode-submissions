"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        if not head:
            return None
        dummy = curr = Node(head.val)
        ncurr = head.next
        hm[head] = curr
        while ncurr:
            curr.next = Node(ncurr.val)
            curr = curr.next
            hm[ncurr] = curr
            ncurr = ncurr.next
        while head:
            if head.random:
                hm[head].random = hm[head.random]
            head = head.next
        return dummy


        return dummy

        
        


