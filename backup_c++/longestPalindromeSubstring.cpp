class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n=s.size();
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = n - 1; i >= 0; i--) {
            char c1 = s[i];
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                char c2 = s[j];
                if (c1 == c2) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        // for (auto &v:dp) {
        //     for (auto &i:v) {
        //         printf("%d ", i);
        //     }
        //     printf("\n");
        // }
        return dp[0][n - 1];
    }
};