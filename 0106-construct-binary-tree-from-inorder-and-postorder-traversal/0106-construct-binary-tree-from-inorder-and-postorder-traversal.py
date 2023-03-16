# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # print(inorder, postorder)
        if not inorder:
            return None
        mid = postorder[-1]
        node = TreeNode(mid)
        ini = 0
        while inorder[ini] != mid:
            ini += 1
        # if ini == 0:
        #     node.right = self.buildTree(inorder[1:], postorder[:-1])
        #     return node
        # elif ini == len(inorder)-1:
        #     node.left = self.buildTree(inorder[:ini], postorder[:-1])
        #     return node
        # left = inorder[ini-1]
        # poi = 0
        # while postorder[poi] != left:
        #     poi += 1
        node.left = self.buildTree(inorder[:ini], postorder[:ini])
        node.right = self.buildTree(inorder[ini+1:], postorder[ini:-1])
        return node