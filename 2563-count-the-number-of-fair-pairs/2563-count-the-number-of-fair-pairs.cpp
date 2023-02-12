#define ll long long

class Solution {
public:
    ll countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        ll ans = 0;
        for (int i: nums) {
            auto l = lower_bound(nums.begin(), nums.end(), lower - i);
            auto r = upper_bound(nums.begin(), nums.end(), upper - i);
            if (lower <= 2 * i && 2 * i <= upper) ans--;
            ans += r - l;
            // cout << *l << ", " << *r << endl;
        }
        return ans / 2;
    }
};