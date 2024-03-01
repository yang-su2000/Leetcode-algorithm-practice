# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        cur = [root]
        while cur:
            ls = [node.val for node in cur]
            # print(even, ls)
            for x, y in pairwise(ls):
                if x % 2 != even or y % 2 != even or (even and x >= y) or ((not even) and x <= y):
                    return False
            if ls[0] % 2 != even:
                return False
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
            even = not even
        return True