class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # O(nlogn) all possible d for all len
        ds = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for d in range(1, i):
                if i % d:
                    continue
                ds[i].append(d)
        
        # O(n^3logn) all minimum letter change for substring s[l:r+1]
        dp = [[0] * n for _ in range(n)] 
        for l in range(n):
            for r in range(l, n):
                ss = s[l:r+1]
                minval = inf
                len_ = r - l + 1
                for d in ds[len_]:
                    val = 0
                    for start in range(d):
                        ss2 = ss[start::d]
                        val += sum(int(c != c2) for c, c2 in zip(ss2, ss2[::-1]))
                    minval = min(minval, val)
                dp[l][r] = minval // 2 if minval != inf else inf
        # print(dp)
        
        # O(n^3) minimum letter change for each position with k substrings
        dp2 = [[inf] * (n + 1) for _ in range(k + 1)] 
        dp2[0][0] = 0
        for k_ in range(k):
            for l in range(n + 1):
                if dp2[k_][l] == inf:
                    continue
                for r in range(l + 1, n + 1):
                    dp2[k_+1][r] = min(dp2[k_+1][r], dp2[k_][l] + dp[l][r-1])
        return dp2[k][n]