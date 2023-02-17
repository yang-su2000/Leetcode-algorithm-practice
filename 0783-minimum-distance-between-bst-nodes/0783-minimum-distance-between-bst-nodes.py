# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        q = [root]
        s = set()
        while q:
            node = q.pop()
            if node.val in s:
                return 0
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans = 2e5
        prev = 2e5
        for i in sorted(s):
            ans = min(ans, abs(i - prev))
            prev = i
        return ans