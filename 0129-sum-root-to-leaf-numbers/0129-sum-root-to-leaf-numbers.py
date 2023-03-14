# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.getd(root)
        return self.ans
        
    def getd(self, node: Optional[TreeNode]) -> Dict[int, int]:
        if node.left or node.right:
            d = defaultdict(int)
            if node.left:
                for depth, count in self.getd(node.left).items():
                    self.ans += 10 ** depth * count * node.val
                    d[depth + 1] += count
            if node.right:
                for depth, count in self.getd(node.right).items():
                    self.ans += 10 ** depth * count * node.val
                    d[depth + 1] += count
            return d
        self.ans += node.val
        return {1: 1} # at depth 0, we have 1 value