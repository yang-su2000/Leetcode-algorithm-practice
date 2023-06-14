# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        cur = inf
        
        def preorder(node):
            nonlocal ans, cur
            if node.left:
                preorder(node.left)
            ans = min(ans, abs(node.val - cur))
            cur = node.val
            if node.right:
                preorder(node.right)
        
        preorder(root)
        return ans