class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * n2 for _ in range(n1)]
        for i1 in range(n1):
            for i2 in range(n2):
                if nums1[i1] == nums2[i2]:
                    dp[i1][i2] = 1
                    if i1 and i2:
                        dp[i1][i2] += dp[i1-1][i2-1]
        return max([max(ls) for ls in dp])
                