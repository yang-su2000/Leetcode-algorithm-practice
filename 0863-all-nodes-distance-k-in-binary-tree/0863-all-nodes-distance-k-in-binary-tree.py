# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ls = [[] for _ in range(501)]
        cur = [root]
        while cur:
            node = cur.pop()
            if node.left:
                ls[node.val].append(node.left.val)
                ls[node.left.val].append(node.val)
                cur.append(node.left)
            if node.right:
                ls[node.val].append(node.right.val)
                ls[node.right.val].append(node.val)
                cur.append(node.right)
        # print(ls)
        cur = [(target.val, -1)]
        while k:
            nxt = []
            for node, parent in cur:
                for child in ls[node]:
                    if child != parent:
                        nxt.append((child, node))
            cur = nxt
            k -= 1
        return [node for node, _ in cur]