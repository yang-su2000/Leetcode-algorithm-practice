# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        p = {}
        start_node = None
        cur = [(root, None)]
        while cur:
            node, parent = cur.pop()
            p[node] = parent
            if node.val == start:
                start_node = node
            if node.left:
                cur.append((node.left, node))
            if node.right:
                cur.append((node.right, node))
        time = 0
        cur2 = [start_node]
        vis = set([start_node])
        while True:
            nxt = []
            for node in cur2:
                for child in [p[node], node.left, node.right]:
                    if child and child not in vis:
                        nxt.append(child)
                        vis.add(child)
            cur2 = nxt
            if not cur2:
                break
            time += 1
        return time