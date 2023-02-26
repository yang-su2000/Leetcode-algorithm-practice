class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        // for (int i: nums) cout << i << " ";
        // cout << endl;
        int n = nums.size();
        int r = n / 2 + (n % 2);
        int l = 0;
        int ans = 0;
        while (r < n) {
            if (nums[l] * 2 <= nums[r]) {
                ans += 2;
                l++;
                r++;
            } else r++;
        }
        return ans;
    }
};