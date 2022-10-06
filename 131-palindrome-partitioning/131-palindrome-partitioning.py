class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j]: s[i:j+1] palindrome?
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        for l in range(3, n+1):
            i, j = 0, l-1
            while j < n:
                dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                i += 1
                j += 1
        # print(dp)
        self.ans = []
        self.dfs(dp, s, 0, [])
        return self.ans
    
    def dfs(self, dp, s, i, ls):
        if i == len(s):
            if ls:
                self.ans.append(ls)
            return
        for j in range(i, len(s)):
            if dp[i][j]:
                self.dfs(dp, s, j+1, ls + [s[i:j+1]])
        