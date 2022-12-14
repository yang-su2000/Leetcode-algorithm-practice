class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        prev = max(nums[0], nums[1])
        prev2 = nums[0]
        for i in range(2, n):
            prev, prev2 = max(prev2 + nums[i], prev), prev
        return prev
            