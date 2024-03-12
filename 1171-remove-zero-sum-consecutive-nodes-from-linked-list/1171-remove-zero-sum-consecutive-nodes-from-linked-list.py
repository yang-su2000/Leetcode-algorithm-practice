# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = [0]
        while head:
            add = val = head.val
            i = len(cur) - 1
            while val and i:
                val += cur[i]
                i -= 1
            if val == 0:
                cur = cur[:i+1]
            else:
                cur.append(add)
            # print(cur)
            head = head.next
        ans = ListNode()
        node = ans
        for val in cur[1:]:
            node.next = ListNode(val)
            node = node.next
        return ans.next
            