class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int seen1 = 0;
        int seen2 = 0;
        for (int i: nums) {
            seen1 = (~seen2) & (seen1 ^ i);
            seen2 = (~seen1) & (seen2 ^ i);
        }
        return seen1;
    }
};