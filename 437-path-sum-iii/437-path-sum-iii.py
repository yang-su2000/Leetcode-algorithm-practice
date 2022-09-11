# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.d = defaultdict(int)
        self.rec(root, 0, targetSum)
        return self.ans
    
    def rec(self, root, cur, s):
        if not root:
            return
        cur += root.val
        if cur == s:
            self.ans += 1
        # cur = cur prefix sum, ? = prev prefix sum, want the count for (cur - ? = s)
        # hence ? = cur - s, ? is the consecutive sum for any inner path
        self.ans += self.d[cur - s]
        self.d[cur] += 1
        self.rec(root.left, cur, s)
        self.rec(root.right, cur, s)
        self.d[cur] -= 1
        