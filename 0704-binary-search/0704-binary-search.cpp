class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        int l=0, r=nums.size()-1;
        while (l<r) {
            int mid=(l+r)/2;
            if (nums[mid]==target) return mid;
            if (nums[mid]>target) r=mid-1;
            else l=mid+1;
        }
        return nums[l]==target ? l : -1;
    }
};