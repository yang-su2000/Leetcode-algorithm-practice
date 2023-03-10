# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        cur = self.head
        ret = cur.val
        while cur:
            if random.random() < 1 / scope:
                ret = cur.val
            cur = cur.next
            scope += 1
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()