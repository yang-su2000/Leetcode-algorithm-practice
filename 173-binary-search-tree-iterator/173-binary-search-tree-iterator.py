# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ls = [root]
        while self.ls[-1].left:
            self.ls.append(self.ls[-1].left)

    def next(self) -> int:
        node = self.ls.pop()
        if node.right:
            self.ls.append(node.right)
            while self.ls[-1].left:
                self.ls.append(self.ls[-1].left)
        return node.val

    def hasNext(self) -> bool:
        return self.ls


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()