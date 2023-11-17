class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n-i-1])
        return ans