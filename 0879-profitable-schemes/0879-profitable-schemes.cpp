#define ll long long

class Solution {
public:
    int profitableSchemes(int n, int minp, vector<int>& group, vector<int>& profit) {
        int m = group.size();
        int mod = 1e9+7;
        // dp[i][j][k]: idx i, members j, profit k
        vector<vector<vector<int>>> dp(m+1, vector<vector<int>>(n+1, vector<int>(minp+1)));
        dp[0][0][0] = 1;
        for (int i=0; i<m; i++) {
            int g = group[i];
            int p = profit[i];
            for (int j=0; j<=n; j++) {
                for (int k=0; k<=minp; k++) {
                    (dp[i+1][j][k] += dp[i][j][k]) %= mod;
                    if (j+g <= n) (dp[i+1][j+g][min(minp, k+p)] += dp[i][j][k]) %= mod;
                }
            }
        }
        int ans = 0;
        for (int j=0; j<=n; j++) {
            (ans += dp[m][j][minp]) %= mod;
        }
        return ans;
    }
};