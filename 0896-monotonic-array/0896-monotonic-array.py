class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sum(i <= j for i, j in pairwise(nums)) == len(nums) - 1 or sum(i >= j for i, j in pairwise(nums)) == len(nums) - 1