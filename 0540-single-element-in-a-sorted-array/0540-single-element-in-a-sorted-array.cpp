class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int l=0, r=n-1;
        while (l < r) {
            int mid = (l+r)/2;
            int mid2 = mid+1;
            if (nums[mid] != nums[mid2]) {
                if (mid > 0) {
                    if (nums[mid] == nums[mid-1]) {
                        mid--;
                        mid2--;
                    } else return nums[mid];
                } else if (mid2 < n-1) {
                    if (nums[mid2] == nums[mid2+1]) {
                        mid++;
                        mid2++;
                    } else return nums[mid2];
                } else {
                    return -1; // impossible
                }
            }
            // now nums[mid] === nums[mid2]
            if ((mid-l) % 2) {
                r = mid-1;
            } else {
                l = mid2+1;
            }
        }
        return nums[l];
    }
};