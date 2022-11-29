class Solution {
public:
    bool isValidPalindrome(string s, int k) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 1));
        for (int l=0, r=l+1; r<n; l++, r++) {
            if (s[l] == s[r]) dp[l][r] = 2;
        }
        for (int i=2; i<n; i++) {
            for (int l=0, r=l+i; r<n; l++, r++) {
                if (s[l] == s[r]) dp[l][r] = max(dp[l][r], dp[l+1][r-1] + 2);
                else dp[l][r] = max(dp[l][r], max(dp[l+1][r], dp[l][r-1]));
            }
        }
        int maxl = 1;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) maxl = max(maxl, dp[i][j]);
        }
        return maxl >= n-k;
    }
};