# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        # print(ls)
        ls2 = []
        for i in ls:
            while ls2:
                if ls2[-1] < i:
                    ls2.pop()
                else:
                    break
            ls2.append(i)
        # print(ls2)
        dummy = ListNode()
        head2 = dummy
        for i in ls2:
            head2.next = ListNode(i)
            head2 = head2.next
        return dummy.next