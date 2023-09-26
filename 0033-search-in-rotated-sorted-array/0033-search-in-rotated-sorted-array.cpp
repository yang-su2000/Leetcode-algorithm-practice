class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[0] <= target) {
                if (nums[0] <= nums[mid] && nums[mid] < target) l = mid + 1;
                else if (target <= nums[mid]) r = mid;
                else r = mid - 1;
            } else if (target <= nums[n-1]) {
                if (nums[mid] > nums[n-1]) l = mid + 1;
                else if (target <= nums[mid]) r = mid;
                else l = mid + 1;
            } else {
                return -1;
            }
            // cout << l << ", " << mid << ", " << r << endl;
            // break;
        }
        if (nums[l] != target) return -1;
        return l;
    }
};