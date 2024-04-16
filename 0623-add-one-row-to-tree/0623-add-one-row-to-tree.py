# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            root = node
        else:
            self.val = val
            self.dfs(root, depth)
        return root
    
    def dfs(self, root, depth):
        if not root:
            return
        if depth == 2:
            l, r = root.left, root.right
            root.left = TreeNode(self.val)
            root.right = TreeNode(self.val)
            root.left.left = l
            root.right.right = r
            return
        else:
            depth -= 1
            self.dfs(root.left, depth)
            self.dfs(root.right, depth)