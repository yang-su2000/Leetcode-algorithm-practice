class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        bool less = true;
        for (int i=0; i<nums.size()-1; i++) {
            if (less) {
                if (nums[i] > nums[i+1]) swap(nums[i], nums[i+1]);
            } else {
                if (nums[i] < nums[i+1]) swap(nums[i], nums[i+1]);
            }
            less = !less;
        }
    }
};