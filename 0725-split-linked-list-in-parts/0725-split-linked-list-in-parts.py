# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ls = []
        while head:
            ls.append(head)
            head = head.next
        ans = [None] * k
        i = 0
        count = 0
        while i < len(ls):
            j = i + len(ls) // k + (count < len(ls) % k) - 1
            # print(i, j)
            if i <= j:
                ls[j].next = None
                ans[count] = ls[i]
                i = j + 1
                count += 1
            else:
                break
        return ans