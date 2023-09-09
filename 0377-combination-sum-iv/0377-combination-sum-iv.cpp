class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target + 1);
        dp[0] = 1;
        for (int i=1; i<=target; i++) {
            for (int val: nums) {
                if (i - val >= 0) dp[i] += dp[i - val];
            }
        }
        return dp[target];
    }
};