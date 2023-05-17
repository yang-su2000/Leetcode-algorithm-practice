# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ans = 0
        for i in range(len(ls) // 2):
            ans = max(ans, ls[i] + ls[len(ls)-i-1])
        return ans