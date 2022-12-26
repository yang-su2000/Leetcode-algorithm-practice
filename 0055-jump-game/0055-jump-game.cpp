class Solution {
public:
    bool canJump(vector<int>& nums) {
        int end = nums[0];
        for (int i=1; i<nums.size(); i++) {
            if (end < i) return false;
            end = max(end, nums[i] + i);
        }
        return true;
    }
};