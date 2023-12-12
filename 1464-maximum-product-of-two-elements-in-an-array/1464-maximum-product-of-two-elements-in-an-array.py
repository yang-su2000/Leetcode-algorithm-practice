class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = sorted(nums)[-2:]
        return (a - 1) * (b - 1)