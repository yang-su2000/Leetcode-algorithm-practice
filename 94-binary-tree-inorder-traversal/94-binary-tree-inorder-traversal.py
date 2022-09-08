# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.rec(root)
        return self.ans
    
    def rec(self, root):
        if not root:
            return
        self.rec(root.left)
        self.ans.append(root.val)
        self.rec(root.right)
            