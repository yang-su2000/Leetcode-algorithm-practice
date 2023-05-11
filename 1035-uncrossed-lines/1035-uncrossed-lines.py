class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(n1):
            for j in range(n2):
                v1 = (dp[i-1][j-1] if i and j else 0) + (nums1[i] == nums2[j])
                v2 = (dp[i-1][j] if i else 0)
                v3 = (dp[i][j-1] if j else 0)
                dp[i][j] = max(v1, v2, v3)
        # print(dp)
        return dp[-1][-1]