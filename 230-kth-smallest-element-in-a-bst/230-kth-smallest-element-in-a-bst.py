# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = 0
        self.ans = None
        self.rec(root, k)
        return self.ans
    
    def rec(self, root, k):
        if not root:
            return
        self.rec(root.left, k)
        if self.ans:
            return
        self.k += 1
        if self.k == k:
            self.ans = root.val
            return
        self.rec(root.right, k)