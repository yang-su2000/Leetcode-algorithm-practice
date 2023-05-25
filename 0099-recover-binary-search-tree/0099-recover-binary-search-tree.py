# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        
        ls = inorder(root)
        # print([node.val for node in ls])
        a, b = None, None
        for i in range(len(ls) - 1):
            node, node2 = ls[i], ls[i+1]
            if node.val > node2.val:
                if a is None:
                    a = node
                b = node2
        # print(a.val, b.val)
        a.val, b.val = b.val, a.val