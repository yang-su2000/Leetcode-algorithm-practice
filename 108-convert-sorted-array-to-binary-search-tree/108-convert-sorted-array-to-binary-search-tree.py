# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.rec(nums, root, 0, len(nums) - 1)
        return root
    
    def rec(self, nums, root, l, r):
        mid = (l + r) // 2
        root.val = nums[mid]
        if l <= mid - 1:
            root.left = TreeNode()
            self.rec(nums, root.left, l, mid - 1)
        if mid + 1 <= r:
            root.right = TreeNode()
            self.rec(nums, root.right, mid + 1, r)