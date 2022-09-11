# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.rec(root, targetSum)
        return self.ans
    
    def rec(self, root, s):
        if not root:
            return defaultdict(lambda: 0)
        l, r = self.rec(root.left, s), self.rec(root.right, s)
        ans = defaultdict(lambda: 0)
        for k, v in l.items():
            ans[k + root.val] += v
        for k, v in r.items():
            ans[k + root.val] += v
        ans[root.val] += 1
        if s in ans:
            self.ans += ans[s]
        # print(ans.items())
        return ans
        