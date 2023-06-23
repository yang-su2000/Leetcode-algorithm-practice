# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        s = set()
        cur = [root1]
        while cur:
            node = cur.pop()
            s.add(target - node.val)
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
        cur2 = [root2]
        while cur2:
            node = cur2.pop()
            if node.val in s:
                return True
            if node.left:
                cur2.append(node.left)
            if node.right:
                cur2.append(node.right)
        return False