# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node):
            nonlocal ans
            count = (node == p) or (node == q)
            if node.left:
                count += dfs(node.left)
                if ans:
                    return 0
                if count == 2:
                    ans = node
                    return 0
            if node.right:
                count += dfs(node.right)
                if ans:
                    return 0
                if count == 2:
                    ans = node
                    return 0
            return count

        dfs(root)
        return ans