class Solution {
public:
    int minDistance(string word1, string word2) {
        if (word1.size() < word2.size()) swap(word1, word2);
        int l1 = word1.size();
        int l2 = word2.size();
        vector<vector<int>> dp(l1 + 1, vector<int>(l2 + 1, 500));
        dp[0][0] = 0;
        for (int i=0; i<=l1; i++) {
            for (int j=0; j<=l2; j++) {
                // cout << dp[i][j] << " ";
                if (i < l1) dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1);
                if (j < l2) dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1);
                if (i < l1 and j < l2) {
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + !(word1[i] == word2[j]));
                }
            }
            // cout << endl;
        }
        return dp[l1][l2];
    }
};