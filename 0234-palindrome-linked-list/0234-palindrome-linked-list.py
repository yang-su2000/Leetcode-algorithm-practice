# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        fast, slow = dummy, dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        # print(head2)
        head2 = self.reverseLinkedList(head2)
        # print(head2)
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
        
    def reverseLinkedList(self, head):
        head_prev = None
        while head.next:
            head_next = head.next
            head.next = head_prev
            head_prev = head
            head = head_next
        head.next = head_prev
        return head
            