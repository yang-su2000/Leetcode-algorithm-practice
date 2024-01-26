# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        s = [root]
        ans = None
        while s:
            node = s.pop()
            if node.val > p.val:
                if not ans or ans.val > node.val:
                    ans = node
                if node.left:
                    s.append(node.left)
            else:
                if node.right:
                    s.append(node.right)
        return ans