#define ll long long

class Solution {
public:
    ll minimumReplacement(vector<int>& nums) {
        int n = nums.size();
        ll ans = 0;
        for (int i=n-2; i>=0; i--) {
            if (nums[i] > nums[i+1]) {
                int val = (nums[i] + nums[i+1] - 1) / nums[i+1];
                ans += val - 1;
                nums[i] /= val;
            }
        }
        return ans;
    }
};