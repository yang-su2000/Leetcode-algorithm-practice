# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.rec(root, set())
        return self.ans
    
    def rec(self, root, s):
        if not root:
            return
        if root.val in s:
            s.remove(root.val)
        else:
            s.add(root.val)
        self.rec(root.left, s)
        self.rec(root.right, s)
        if not root.left and not root.right:
            self.ans += (len(s) <= 1)
        if root.val in s:
            s.remove(root.val)
        else:
            s.add(root.val)