# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        midprev = None
        while head and head.next:
            midprev = midprev.next if midprev else head
            head = head.next.next
        mid = midprev.next
        midprev.next = None
        return mid
    
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
        mid = self.findMid(head)
        head = self.sortList(head)
        mid = self.sortList(mid)
        return self.merge2Sorted(head, mid)
        