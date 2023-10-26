class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans = 0
        mod = int(1e9+7)
        arr.sort()
        n = len(arr)
        dp = [0] * n
        A = [[] for _ in range(n)]
        d = {arr[i]: i for i in range(n)}
        for i in range(n):
            for j in range(n):
                val = arr[i] * arr[j]
                if val in d:
                    idx = d[val]
                    A[idx].append((i, j))
        for i in range(n):
            val = 1
            for x, y in A[i]:
                val += dp[x] * dp[y]
            dp[i] = val % mod
            ans += dp[i]
        # print(dp)
        return ans % mod