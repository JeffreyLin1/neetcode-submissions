# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastcurr = slowcurr = head
        while fastcurr != None:
            if not fastcurr.next or not fastcurr.next.next:
                return False
            fastcurr = fastcurr.next.next
            slowcurr = slowcurr.next
            if fastcurr == slowcurr:
                return True
        return False