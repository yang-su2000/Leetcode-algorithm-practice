# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            s2 = []
            sub = []
            for node in s:
                sub.append(node.val)
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            s = s2
            ans.append(sub)
        return ans