class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ls = [0] * n
        ls[0] = nums[0]
        ls[1] = max(nums[0], nums[1])
        for i in range(2, n):
            ls[i] = max(ls[i-2] + nums[i], ls[i-1])
        return ls[-1]
            