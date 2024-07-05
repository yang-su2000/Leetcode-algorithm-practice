# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ls = []
        cur = 2
        while head.next and head.next.next:
            if head.val < head.next.val and head.next.val > head.next.next.val:
                ls.append(cur)
            elif head.val > head.next.val and head.next.val < head.next.next.val:
                ls.append(cur)
            head = head.next
            cur += 1
        ls.sort()
        # print(ls)
        if len(ls) >= 2:
            ans = [inf, ls[-1] - ls[0]]
            for a, b in pairwise(ls):
                ans[0] = min(ans[0], b - a)
            return ans
        else:
            return [-1, -1]