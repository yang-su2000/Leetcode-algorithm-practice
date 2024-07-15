# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        for _, child, _ in descriptions:
            nodes[child] = TreeNode(child)
        root = None
        for parent, child, _ in descriptions:
            if parent not in nodes:
                root = parent
                nodes[parent] = TreeNode(parent)
                break
        for parent, child, isLeft in descriptions:
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        return nodes[root]
