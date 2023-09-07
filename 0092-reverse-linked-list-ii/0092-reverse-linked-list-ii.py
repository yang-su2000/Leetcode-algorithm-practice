# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        ls = []
        cur = dummy
        while cur:
            ls.append(cur)
            cur = cur.next
        ls[left].next, ls[left-1].next = ls[right].next, ls[right]
        for i in range(left + 1, right + 1):
            ls[i].next = ls[i-1]
        return dummy.next