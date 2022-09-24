# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        if not root:
            return self.ans
        self.rec(root, [], 0, targetSum)
        return self.ans
        
    def rec(self, root, ls, s, t):
        ls.append(root.val)
        s += root.val
        if not root.left and not root.right:
            # print(ls, s)
            if s == t:
                self.ans.append(ls.copy())
            ls.pop()
            return
        if root.left:
            self.rec(root.left, ls, s, t)
        if root.right:
            self.rec(root.right, ls, s, t)
        ls.pop()