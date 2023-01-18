class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int csum = 0;
        int msum = nums[0];
        for (int i: nums) {
            csum = max(csum, 0) + i;
            msum = max(msum, csum);
        }
        return msum;
    }
};