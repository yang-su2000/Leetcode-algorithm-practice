class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1;
        function<bool(int, int)> same_side = [&](int mid, int target) {
            if (nums[0] <= mid && nums[0] <= target) return true;
            if (nums[0] > mid && nums[0] > target) return true;
            return false;
        };
        while (l <= r) {
            int mid = (l + r) / 2;
            int val;
            if (same_side(nums[mid], target)) val = nums[mid];
            else if (nums[0] <= target) val = INT_MAX;
            else val = INT_MIN;
            if (target == val) return mid;
            else if (target < val) r = mid-1;
            else l = mid+1;
        }
        return -1;
    }
};