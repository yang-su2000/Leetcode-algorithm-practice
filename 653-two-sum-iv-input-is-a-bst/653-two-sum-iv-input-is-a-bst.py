# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = [root]
        s = set()
        while q:
            node = q.pop()
            if node.val in s:
                return True
            s.add(k - node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False