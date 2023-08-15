# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = [], []
        cur = head
        while cur:
            if cur.val < x:
                l.append(cur.val)
            else:
                r.append(cur.val)
            cur = cur.next
        cur = head
        ls = l + r
        i = 0
        while cur:
            cur.val = ls[i]
            i += 1
            cur = cur.next
        return head