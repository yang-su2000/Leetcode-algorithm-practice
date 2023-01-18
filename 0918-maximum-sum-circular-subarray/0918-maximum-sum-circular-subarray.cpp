class Solution {
public:
    // which is equal to: find the minimum subarray (could be empty)
    // look up: Kadane's algorithm
    int maxSubarraySumCircular(vector<int>& nums) {
        int cmax = 0;
        int cmin = 0;
        int smax = nums[0];
        int smin = nums[0];
        int sum = 0;
        for (int i: nums) {
            cmax = max(cmax, 0) + i;
            cmin = min(cmin, 0) + i;
            smax = max(smax, cmax);
            smin = min(smin, cmin);
            sum += i;
        }
        return sum == smin ? smax : max(smax, sum - smin);
    }
};