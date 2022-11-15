class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        int sum = -1;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i=0; i<n and nums[i] < k; i++) {
            int j = lower_bound(nums.begin()+i+1, nums.end(), k-nums[i]) - (nums.begin()+1);
            if (j > i) sum = max(sum, nums[i] + nums[j]);
        }
        return sum;
    }
};