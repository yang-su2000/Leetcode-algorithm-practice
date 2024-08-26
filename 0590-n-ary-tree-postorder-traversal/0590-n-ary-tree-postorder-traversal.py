"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ans = []
        cur = [(root, 0)]
        while cur:
            node, idx = cur.pop()
            if idx < len(node.children):
                cur.append((node, idx + 1))
                cur.append((node.children[idx], 0))
            else:
                ans.append(node.val)
        return ans