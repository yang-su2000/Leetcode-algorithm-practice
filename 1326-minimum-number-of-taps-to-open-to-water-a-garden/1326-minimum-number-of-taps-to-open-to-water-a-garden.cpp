class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        int mval = 1e5;
        vector<int> dp(n + 1, mval);
        dp[0] = 0;
        for (int i=0; i<=n; i++) {
            int val = dp[max(i - ranges[i], 0)];
            for (int j=i-ranges[i]; j<=i+ranges[i]; j++) {
                if (j < 0 or j > n) continue;
                dp[j] = min(dp[j], 1 + val);
            }
            // for (int i=0; i<=n; i++) cout << dp[i] << " ";
            // cout << endl;
        }
        if (dp[n] == mval) return -1;
        return dp[n];
    }
};