# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.ls = []
        while head:
            self.ls.append(head.val)
            head = head.next
        self.l = len(self.ls)

    def getRandom(self) -> int:
        return self.ls[random.randint(0, self.l - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()