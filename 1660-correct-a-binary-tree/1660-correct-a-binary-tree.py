# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        cur = set([root])
        while cur:
            nxt = set()
            for node in cur:
                if node.left:
                    nxt.add(node.left)
                if node.right:
                    nxt.add(node.right)
            for node in cur:
                if node.left and node.left.right in nxt:
                    nxt.remove(node.left)
                    node.left = None
                if node.right and node.right.right in nxt:
                    nxt.remove(node.right)
                    node.right = None
            cur = nxt
        return root