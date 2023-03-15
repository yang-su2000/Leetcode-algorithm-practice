# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        cur = [root]
        end = False
        while cur:
            nex = []
            for node in cur:
                nex.append(node.left)
                nex.append(node.right)
            cur = []
            for node in nex:
                if not node:
                    end = True
                elif end:
                    return False
                else:
                    cur.append(node)
        return True