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
        a, b, lst = None, None, None
        
        def inorder(node):
            nonlocal a, b, lst
            if node.left:
                inorder(node.left)
            if lst and lst.val > node.val:
                b = node
                if not a:
                    a = lst
                else:
                    return
            lst = node
            if node.right:
                inorder(node.right)

        inorder(root)
        # print(a.val, b.val)
        a.val, b.val = b.val, a.val