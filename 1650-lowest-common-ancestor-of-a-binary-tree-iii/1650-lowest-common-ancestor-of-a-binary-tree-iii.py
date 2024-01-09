"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        x, y = p, q
        while x != y:
            x = q if not x.parent else x.parent
            y = p if not y.parent else y.parent
        return x