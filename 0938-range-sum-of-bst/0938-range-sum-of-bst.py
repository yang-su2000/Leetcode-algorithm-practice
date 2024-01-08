# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if low <= node.val <= high:
                ans += node.val
            if node.left and low <= node.val:
                dfs(node.left)
            if node.right and node.val <= high:
                dfs(node.right)
                
        dfs(root)
        return ans