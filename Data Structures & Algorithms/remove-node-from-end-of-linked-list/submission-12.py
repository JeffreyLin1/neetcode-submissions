# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        leng = 0
        while curr:
            curr = curr.next
            leng += 1
        curr = head
        print(leng)
        print(n)
        for i in range(leng-n):
            prev = curr
            curr = curr.next


        if prev and curr.next:
            prev.next = curr.next
        elif prev:
            prev.next = None
        elif leng-n == 0:
            head = curr.next
        else:
            return None

        return head
        
            