class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int lo = 1, hi = 1;
        while (hi < nums.size()) {
            if (nums[hi] > nums[hi-1]) nums[lo++] = nums[hi];
            hi++;
        }
        return lo;
    }
};