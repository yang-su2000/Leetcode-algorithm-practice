# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        ls = [0, 0]
        while head.next:
            if head.val != head.next.val and head.val % 2 == 0:
                if head.val > head.next.val:
                    ls[head.val % 2] += 1
                else:
                    ls[head.next.val % 2] += 1
            head = head.next
        if ls[0] == ls[1]:
            return 'Tie'
        elif ls[0] > ls[1]:
            return 'Even'
        else:
            return 'Odd'