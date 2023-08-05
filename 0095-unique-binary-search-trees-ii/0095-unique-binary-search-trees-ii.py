# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def trace(remain):
            if not remain:
                return [None]
            ret = []
            for i in range(len(remain)):
                for l in trace(remain[:i]):
                    for r in trace(remain[i+1:]):
                        node = TreeNode(remain[i])
                        node.left = l
                        node.right = r
                        ret.append(node)
            return ret
        return trace(list(range(1, n + 1)))