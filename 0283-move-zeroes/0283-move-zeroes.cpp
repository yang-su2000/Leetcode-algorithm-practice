class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lo = 0;
        int hi = 0;
        while (hi < nums.size()) {
            if (nums[hi]) nums[lo++] = nums[hi];
            hi++;
        }
        while (lo < nums.size()) nums[lo++] = 0;
    }
};