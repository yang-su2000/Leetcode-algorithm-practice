# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        cur = [root]
        cand = []
        while cur:
            node = cur.pop()
            if node.val == head.val:
                cand.append(node)
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
        head = head.next
        while head:
            cand2 = []
            for node in cand:
                if node.left and node.left.val == head.val:
                    cand2.append(node.left)
                if node.right and node.right.val == head.val:
                    cand2.append(node.right)
            cand = cand2
            head = head.next
        return cand