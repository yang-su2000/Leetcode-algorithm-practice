class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        multiset<int> s {nums[0]};
        int n = nums.size();
        int ans = nums[0];
        int psum = nums[0];
        for (int i=1; i<n; i++) {
            psum += nums[i];
            ans = max(ans, psum - min(0, *s.begin()));
            s.insert(psum);
        }
        int psum2 = 0;
        for (int i=0; i<n-1; i++) {
            psum += nums[i];
            psum2 += nums[i];
            s.erase(s.lower_bound(psum2));
            ans = max(ans, psum - *s.begin());
        }
        return ans;
    }
};