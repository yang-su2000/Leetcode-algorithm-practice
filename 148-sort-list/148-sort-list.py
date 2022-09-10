# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find2Head(self, head):
        fast = head
        slow = head
        slower = head
        while fast and fast.next:
            fast = fast.next.next
            slower = slow
            slow = slow.next
        slower.next = None
        return head, slow
    
    def merge2Sorted(self, head1, head2):
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        else:
            cur.next = head2
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head1, head2 = self.find2Head(head)
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge2Sorted(head1, head2)
        