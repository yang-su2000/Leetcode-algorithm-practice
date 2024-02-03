class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            j = i
            count = 1
            val = 0
            while j >= 0 and count <= k:
                val = max(val, arr[j])
                dp[i] = max(dp[i], (dp[j-1] if j > 0 else 0) + val * count)
                j -= 1
                count += 1
        # print(dp)
        return dp[-1]