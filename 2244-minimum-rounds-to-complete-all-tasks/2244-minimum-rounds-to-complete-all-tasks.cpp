class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> mc;
        for (int &t: tasks) mc[t]++;
        int max_count = 0;
        for (auto &[k, v]: mc) {
            if (v == 1) return -1;
            max_count = max(max_count, v);
        }
        vector<int> dp(max(4, max_count + 1));
        dp[1] = 2e5;
        dp[2] = 1;
        dp[3] = 1;
        for (int i=4; i<dp.size(); i++) {
            dp[i] = min(dp[i-2] + 1, dp[i-3] + 1);
        }
        int ans = 0;
        for (auto &[k, v]: mc) ans += dp[v];
        return ans;
    }
};