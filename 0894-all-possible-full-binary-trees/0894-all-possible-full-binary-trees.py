# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        ret = []
        for i in range(1, n - 1):
            l = self.allPossibleFBT(i)
            r = self.allPossibleFBT(n - 1 - i)
            for lnode in l:
                for rnode in r:
                    node = TreeNode()
                    node.left = lnode
                    node.right = rnode
                    ret.append(node)
        return ret