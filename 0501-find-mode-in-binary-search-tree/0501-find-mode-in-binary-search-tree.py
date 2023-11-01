# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = Counter()
        cur = [root]
        while cur:
            node = cur.pop()
            c[node.val] += 1
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
        cmax = max(c.values())
        return [key for key, value in c.items() if value == cmax]