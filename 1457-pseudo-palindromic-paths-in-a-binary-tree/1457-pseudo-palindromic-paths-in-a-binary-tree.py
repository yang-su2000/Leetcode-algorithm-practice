# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.rec(root, 0)
        return self.ans
    
    def rec(self, root, i):
        if not root:
            return
        i ^= (1 << root.val)
        self.rec(root.left, i)
        self.rec(root.right, i)
        if not root.left and not root.right:
            self.ans += (i & (i - 1) == 0)
        i ^= (1 << root.val)