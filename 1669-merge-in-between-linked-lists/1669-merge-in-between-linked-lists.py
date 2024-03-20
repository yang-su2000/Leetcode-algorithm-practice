# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        before_a = list1
        while a > 1:
            before_a = before_a.next
            a -= 1
            b -= 1
        after_b = before_a
        while b >= 0:
            after_b = after_b.next
            b -= 1
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        before_a.next = list2
        tail2.next = after_b
        return list1
        