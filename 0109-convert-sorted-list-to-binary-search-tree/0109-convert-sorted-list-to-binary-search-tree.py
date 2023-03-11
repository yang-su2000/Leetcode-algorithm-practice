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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.buildBST(ls, 0, len(ls)-1)
    
    def buildBST(self, ls: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(ls[mid])
        node.left = self.buildBST(ls, l, mid-1)
        node.right = self.buildBST(ls, mid+1, r)
        return node