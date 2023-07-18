class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        v = [0] * (m + 1)
        hi = max(nums)
        for i in nums:
            v[i] += i
        a, b = 0, v[1]
        for i in range(2, hi + 1):
            a, b = b, max(a + v[i], b)
        return b