# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        removed = True
        if root.left:
            if self.dfs(root.left):
                removed = False
            else:
                root.left = None
        if root.right:
            if self.dfs(root.right):
                removed = False
            else:
                root.right = None
        if root.val == 1:
            removed = False
        return not removed
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.dfs(root):
            root = None
        return root