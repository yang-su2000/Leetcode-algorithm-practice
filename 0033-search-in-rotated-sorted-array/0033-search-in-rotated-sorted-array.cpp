class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, r=nums.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (target < nums[0] && nums[0] < nums[mid]) l = mid+1;
            else if (nums[mid] < nums[0] && nums[0] <= target) r = mid;
            else if (nums[mid] < target) l = mid+1;
            else if (target < nums[mid]) r = mid;
            else return mid;
        }
        return -1;
    }
};