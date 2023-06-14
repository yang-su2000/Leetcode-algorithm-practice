# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        
        def getDiff(node):
            nonlocal ans
            l, r = node.val, node.val
            if node.left:
                ll, lr = getDiff(node.left)
                l = ll
                ans = min(ans, abs(node.val - lr))
            if node.right:
                rl, rr = getDiff(node.right)
                r = rr
                ans = min(ans, abs(node.val - rl))
            return l, r
        
        getDiff(root)
        return ans