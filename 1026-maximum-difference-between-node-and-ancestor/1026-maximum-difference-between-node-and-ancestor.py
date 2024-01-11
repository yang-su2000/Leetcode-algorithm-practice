# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            lo, hi = inf, -inf
            if node.left:
                x, y = dfs(node.left)
                lo = min(lo, x)
                hi = max(hi, y)
            if node.right:
                x, y = dfs(node.right)
                lo = min(lo, x)
                hi = max(hi, y)
            ans = max(ans, node.val - lo, hi - node.val)
            lo = min(lo, node.val)
            hi = max(hi, node.val)
            return lo, hi
        
        dfs(root)
        return ans