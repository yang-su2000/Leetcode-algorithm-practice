# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.rec(root)
        return self.ans
    
    def rec(self, root):
        if not root:
            return 0
        l = self.rec(root.left)
        r = self.rec(root.right)
        self.ans = max(self.ans, l + r)
        return max(l, r) + 1