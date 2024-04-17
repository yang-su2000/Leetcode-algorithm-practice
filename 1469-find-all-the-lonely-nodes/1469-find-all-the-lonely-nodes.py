# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node):
            nonlocal ans
            if not (node.left or node.right):
                return
            elif not node.left:
                ans.append(node.right.val)
                dfs(node.right)
            elif not node.right:
                ans.append(node.left.val)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ans