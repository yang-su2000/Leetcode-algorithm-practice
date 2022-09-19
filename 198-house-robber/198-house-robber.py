class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ls = [0] * n
        nls = [0] * n
        ls[0] = nums[0]
        ls[1] = nums[1]
        nls[1] = nums[0]
        for i in range(2, n):
            ls[i] = nls[i-1] + nums[i]
            nls[i] = max(ls[i-1], nls[i-1])
        return max(ls[-1], nls[-1])
            