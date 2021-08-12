class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        int high = INT_MIN, right = -1; // right bound of ans subarray
        int low = INT_MAX, left = -1; // left bound of ans subarray
        for (int i = 0; i < n; i++) {
            if (high > nums[i]) { // go forward, if a number is smaller than current max, update right bound (because this number needs to be sorted)
                right = i;
            } else { // if number >= current max, update current max
                high = nums[i];
            }
            if (low < nums[n - i - 1]) { // go backward, if a number is bigger than current min, update left bound (because this number needs to be sorted)
                left = n - i - 1;
            } else { // if number <= current min, update current min
                low = nums[n - i - 1];
            }
        }
        return right == -1 ? 0 : right - left + 1;
    }
};