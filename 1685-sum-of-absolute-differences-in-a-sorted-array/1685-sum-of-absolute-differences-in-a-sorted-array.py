class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = sum(nums) - n * nums[0]
        for i in range(1, n):
            ans[i] = ans[i-1] + (i - (n - i)) * (nums[i] - nums[i-1])
        return ans