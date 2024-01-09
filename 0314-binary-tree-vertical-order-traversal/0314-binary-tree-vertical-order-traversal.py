# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        cur = [(root, 0)]
        while cur:
            nxt = []
            for node, col in cur:
                if not node:
                    continue
                ans[col].append(node.val)
                nxt.append((node.left, col - 1))
                nxt.append((node.right, col + 1))
            cur = nxt
        return list(v for k, v in sorted(ans.items()))