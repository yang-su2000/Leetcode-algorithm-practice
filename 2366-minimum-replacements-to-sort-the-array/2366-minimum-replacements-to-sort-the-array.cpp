#define ll long long

class Solution {
public:
    ll minimumReplacement(vector<int>& nums) {
        int n = nums.size();
        stack<int> s;
        ll ans = 0;
        for (int i=n-1; i>=0; i--) {
            if (!s.empty() and nums[i] > s.top()) {
                int val = (nums[i] + s.top() - 1) / s.top();
                ans += val - 1;
                s.push(nums[i] / val);
                // cout << nums[i] << " " << ans << endl;
            } else s.push(nums[i]);
        }
        return ans;
    }
};