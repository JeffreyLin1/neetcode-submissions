# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dhead = curr = head
        tempprev = None
        n = 1
        while curr:
            if n == k:
                head = curr
            if n % k == 0:
                prev = curr.next
                if tempprev:
                    tempprev.next = curr
                for i in range(k):
                    temp = dhead.next
                    dhead.next = prev
                    prev = dhead
                    dhead = temp
                    if i == 0:
                        tempprev = prev
                curr = dhead

            else:
                curr = curr.next
            n += 1
        return head
