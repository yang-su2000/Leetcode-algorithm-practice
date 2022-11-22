class Solution {
public:
    int numSquares(int n) {
        vector<int> cands;
        for (int i=1; i*i<=n; i++) {
            cands.emplace_back(i*i);
        }
        vector<int> dp(n+1, n);
        for (int &cand:cands) dp[cand] = 1;
        for (int i=1; i<=n; i++) {
            for (int &cand:cands) {
                if (i-cand>=0 and dp[i-cand]) dp[i] = min(dp[i], dp[i-cand]+1);
            }
        }
        return dp[n];
    }
};