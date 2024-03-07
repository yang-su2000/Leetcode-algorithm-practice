# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = ListNode(next=head)
        slow = fast
        while fast and slow:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow