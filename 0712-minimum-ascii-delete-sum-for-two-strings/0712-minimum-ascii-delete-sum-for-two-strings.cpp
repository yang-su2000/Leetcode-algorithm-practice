class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        // at dp[i][j] means uses len(s1) == i, len(s2) == j
        vector<vector<int>> dp(n1 + 1, vector<int>(n2 + 1));
        for (int i=1; i<=n1; i++) {
            dp[i][0] = s1[i-1] + dp[i-1][0];
        }
        for (int j=1; j<=n2; j++) {
            dp[0][j] = s2[j-1] + dp[0][j-1];
        }
        for (int i=1; i<=n1; i++) {
            for (int j=1; j<=n2; j++) {
                if (s1[i-1] == s2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = min(s1[i-1] + dp[i-1][j], s2[j-1] + dp[i][j-1]);
                }
                // cout << i << ", " << j << ": " << dp[i][j] << endl;
            }
        }
        return dp[n1][n2];
    }
};