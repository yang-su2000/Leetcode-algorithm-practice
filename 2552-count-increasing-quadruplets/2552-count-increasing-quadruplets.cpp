#define ll long long

class Solution {
public:
    ll countQuadruplets(vector<int>& nums) {
        // find all i < j < k < l such that nums[i] < nums[k] < nums[j] < nums[l]
        // in short, find all "ikjl" pattern
        int n = nums.size();
        int i, j, k, l;
        ll lt_k = 0; // number of "ik" pattern
        vector<ll> dp(n); // number of "ikj" pattern
        ll ans = 0; // number of "ikjl" pattern
        for (int idx_1 = 0; idx_1 < n; idx_1++){
            lt_k = 0;
            for (int idx_2 = 0; idx_2 < idx_1; idx_2++){
                if (nums[idx_2] < nums[idx_1]) {
                    // k = idx_1;
                    // i = idx_2;
                    // nums[i] < nums[k]
                    lt_k++;
                    // nums[j] < nums[l] from dp[j] that has all "ikj" pattern
                    // l = idx_1;
                    // j = idx_2;
                    ans += dp[idx_2];
                } else if (nums[idx_1] < nums[idx_2]) {
                    // k = idx_1;
                    // j = idx_2;
                    // nums[k] < nums[j] from lt_k that has all "ik" pattern
                    dp[idx_2] += lt_k;
                }
            }
        }
        return ans; 
    }
};