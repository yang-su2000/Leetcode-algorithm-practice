class Solution {
public:
    int minInsertions(string s) {
        int n = s.length();
        int dp[n+1][n];
        memset(dp, 0, sizeof(dp));
        for (int i=0; i<n; i++) dp[1][i] = 0;
        for (int i=0; i<n-1; i++) dp[2][i] = (s[i] != s[i+1]);
        for (int l=3; l<=n; l++) {
            for (int i=0; i<=n-l; i++) {
                int r = i+l-1;
                if (s[i] == s[r]) dp[l][i] = dp[l-2][i+1];
                else dp[l][i] = 1 + min(dp[l-1][i], dp[l-1][i+1]);
                // cout << l << "," << i << ":" << dp[l][i] << endl;
            }
        }
        return dp[n][0];
    }
};