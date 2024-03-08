# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = Counter()
        while head:
            c[head.val] += 1
            head = head.next
        cur = ListNode()
        ret = cur
        for count in c.values():
            cur.next = ListNode(count)
            cur = cur.next
        return ret.next