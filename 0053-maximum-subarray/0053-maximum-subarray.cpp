class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int csum = 0;
        int msum = nums[0];
        for (int i: nums) {
            csum += i;
            msum = max(msum, csum);
            csum = max(csum, 0);
        }
        return msum;
    }
};