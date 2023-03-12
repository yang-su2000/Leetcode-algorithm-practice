# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, '__lt__', lambda x, y: x.val < y.val)
        ans = ListNode()
        cur = ans
        h = []
        for node in lists:
            if node:
                heapq.heappush(h, node)
        while len(h) > 0:
            node = heapq.heappop(h)
            cur.next = ListNode(node.val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(h, node)
        return ans.next