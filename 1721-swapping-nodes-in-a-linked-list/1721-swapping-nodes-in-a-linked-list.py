# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        b = head
        while k > 1:
            b = b.next
            k -= 1
        swap1 = b
        while b.next:
            a = a.next
            b = b.next
        swap2 = a
        swap1.val, swap2.val = swap2.val, swap1.val
        return head