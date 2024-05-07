# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        node = None
        add = 0
        for val in ls[::-1]:
            val2 = val * 2 + add
            node = ListNode(val2 % 10, node)
            add = val2 // 10
        if add:
            node = ListNode(add, node)
        return node
        