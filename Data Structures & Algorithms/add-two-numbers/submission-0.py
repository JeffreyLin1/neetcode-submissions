# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ans = ListNode()

        while l1 or l2:
            if l1:
                ans.val += l1.val
                l1 = l1.next
            if l2:
                ans.val += l2.val
                l2 = l2.next
            if ans.val > 9:
                ans.val = ans.val % 10
                ans.next = ListNode()
                ans = ans.next
                ans.val = 1
            elif l1 or l2:
                ans.next = ListNode()
                ans = ans.next

        return head
        

        




        