class Solution {
public:
    int jump(vector<int>& nums) {
        int ans = 0;
        int n = nums.size();
        int l = 0, r = 0;
        while (r < n - 1) {
            int r2 = r;
            for (int i=l; i<=r; i++) {
                r2 = max(r2, min(n - 1, i + nums[i]));
            }
            l = r + 1;
            r = r2;
            ans++;
        }
        return ans;
    }
};