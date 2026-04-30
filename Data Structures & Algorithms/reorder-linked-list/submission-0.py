# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next

        slow.next = None
        prev = None
        while curr !=  None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l1 = head
        while prev != None:
            temp1 = l1.next
            temp2 = prev.next
            l1.next = prev
            prev.next= temp1
            l1 = temp1
            prev = temp2
        

