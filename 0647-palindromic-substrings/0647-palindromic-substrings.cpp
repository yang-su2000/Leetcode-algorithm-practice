class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n));
        int ans = n;
        for (int i=0; i<n; i++) dp[i][i] = true;
        for (int i=0; i<n-1; i++) {
            if (s[i] == s[i+1]) {
                dp[i][i+1] = true;
                ans++;
            }
        }
        for (int l=3; l<=n; l++) {
            for (int i=0; i<=n-l; i++) {
                int j=i+l-1;
                if (s[i] == s[j] and dp[i+1][j-1]) {
                    dp[i][j] = true;
                    ans++;
                }
            }
        }
        return ans;
    }
};