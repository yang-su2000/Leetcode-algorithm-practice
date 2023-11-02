# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node): # [val, count]
            nonlocal ans
            if not node:
                return 0, 0
            val, count = node.val, 1
            lval, lcount = dfs(node.left)
            rval, rcount = dfs(node.right)
            sval = val + lval + rval
            scount = count + lcount + rcount
            if sval // scount == val:
                ans += 1
            return sval, scount
        dfs(root)
        return ans