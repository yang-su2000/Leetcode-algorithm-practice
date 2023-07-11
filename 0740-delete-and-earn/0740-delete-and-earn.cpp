class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int n = nums.size();
        vector<int> v(1e4+1);
        for (int i=0; i<n; i++) v[nums[i]]++;
        vector<int> dp(1e4+1, -1);
        function<int(int)> dfs = [&](int i) {
            if (i < 0 or i > 1e4) return 0;
            if (dp[i] != -1) return dp[i];
            dp[i] = max(dfs(i+1), i * v[i] + dfs(i+2));
            return dp[i];
        };
        return dfs(0);
    }
};