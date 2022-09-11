# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
    
    def getHeight(self, root):
        if not root:
            return 0
        l = self.getHeight(root.left)
        if l == -1:
            return -1
        r = self.getHeight(root.right)
        if r == -1 or abs(l - r) > 1:
            return -1
        return max(l, r) + 1