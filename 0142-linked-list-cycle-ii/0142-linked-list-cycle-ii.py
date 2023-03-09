# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        start = True
        found = False
        while fast and fast.next:
            if fast == slow:
                if start:
                    start = False
                else:
                    found = True
                    break
            fast = fast.next.next
            slow = slow.next
        if not found:
            return None
        # print(fast.val)
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow