class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                take = nums1[i] * nums2[j] + (max(0, dp[i-1][j-1]) if i and j else 0)
                not_take = max(dp[i-1][j] if i else -1e9, dp[i][j-1] if j else -1e9)
                dp[i][j] = max(take, not_take)
        return dp[-1][-1]