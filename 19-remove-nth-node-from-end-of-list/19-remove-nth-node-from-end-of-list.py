# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = last = dummy
        while n:
            last = last.next
            n -= 1
        while last.next:
            first = first.next
            last = last.next
        first.next = first.next.next
        return dummy.next