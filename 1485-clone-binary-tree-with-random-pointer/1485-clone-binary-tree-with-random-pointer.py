# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        d = {None: None} # origin -> new
        q = [root]
        ls = []
        while q:
            node = q.pop()
            if not node:
                continue
            new_node = NodeCopy(node.val, node.left, node.right, node.random)
            d[node] = new_node
            ls.append(new_node)
            q.append(node.left)
            q.append(node.right)
        for new_node in ls:
            new_node.left = d[new_node.left]
            new_node.right = d[new_node.right]
            new_node.random = d[new_node.random]
        return d[root]