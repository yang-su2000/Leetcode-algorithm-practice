# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        cur = [(root, 0)]
        while cur:
            node, flag = cur.pop()
            if flag == 0:
                cur.append((node, 1))
                if node.left:
                    cur.append((node.left, 0))
            elif flag == 1:
                cur.append((node, 2))
                if node.right:
                    cur.append((node.right, 0))
            else:
                ans.append(node.val)
        return ans