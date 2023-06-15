# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cur = [root]
        msum = -inf
        level = 1
        ans = None
        while cur:
            nxt = []
            s = 0
            for node in cur:
                s += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if s > msum:
                msum = s
                ans = level
            cur = nxt
            level += 1
        return ans