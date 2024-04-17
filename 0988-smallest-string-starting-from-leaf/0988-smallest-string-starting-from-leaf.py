# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        
        def dfs(node, s):
            nonlocal ans
            c = chr(ord('a') + node.val)
            s = c + s
            if not (node.left or node.right):
                ans = min(ans, s) if ans else s
                return
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
            
        dfs(root, '')
        return ans