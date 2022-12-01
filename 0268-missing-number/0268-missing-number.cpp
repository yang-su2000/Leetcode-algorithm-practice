class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int has0 = -1;
        for (int i=0; i<n; i++) {
            int val = abs(nums[i]);
            if (val == 0) has0 = i;
            else nums[val-1] *= -1;
        }
        if (has0 == -1) return 0;
        for (int i=0; i<n; i++) {
            if (nums[i] > 0) return i+1;
        }
        return has0+1;
    }
};