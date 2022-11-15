class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        int sum = -1;
        int n = nums.size();
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                int cur = nums[i] + nums[j];
                if (cur > sum and cur < k) {
                    sum = cur;
                }
            }
        }
        return sum;
    }
};