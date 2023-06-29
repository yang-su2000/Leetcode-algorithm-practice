# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(node):
            nonlocal ans
            valid = True
            if node.left:
                l = rec(node.left)
                if l == 1001 or l != node.val:
                    valid = False
            if node.right:
                r = rec(node.right)
                if r == 1001 or r != node.val:
                    valid = False
            if valid:
                ans += 1
            return node.val if valid else 1001
        
        if root:
            rec(root)
        return ans