class Solution {
public:
    int numTilings(int n) {
        vector<vector<long>> dp(n+1, vector<long>(2)); // 0: used, 1: partial
        if (n == 1) return 1;
        if (n == 2) return 2;
        dp[1][0] = 1;
        dp[1][1] = 0;
        dp[2][0] = 2;
        dp[2][1] = 2;
        for (int i=3; i<=n; i++) {
            dp[i][0] = dp[i-1][1] + dp[i-1][0] + dp[i-2][0];
            dp[i][1] = dp[i-2][0] * 2 + dp[i-1][1];
            dp[i][0] %= (int)(1e9+7);
            dp[i][1] %= (int)(1e9+7);
        }
        return dp[n][0];
    }
};